import sqlite3
from sqlite3 import Error

from modules.functions import get_user_from_db, get_request_from_db, request_time_is_done
from modules.models import User, Request


class DataBase:
    def __init__(self, db_file='database.db'):
        self.db_file = db_file
        self.create_connection()
        self.c = self._get_connection()
        self.cursor = self.c.cursor()
        self.create_tables()
        self.check_requests_shell_life()

    def _get_connection(self) -> sqlite3.connect:
        c = sqlite3.connect(self.db_file)
        return c

    def create_connection(self):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

    def create_tables(self):
        with self.c:
            self.c.execute('''CREATE TABLE IF NOT EXISTS users
                         (id integer PRIMARY KEY, telegram_id text, balance bigint, status text, 
                         is_follower int, invited_by text, q_of_trades bigint, earned_from_partnership bigint)''')
            self.c.execute('''CREATE TABLE IF NOT EXISTS requests
                                 (id integer PRIMARY KEY, telegram_id text, status text, 
                                 type text, when_created text, comment text, wallet text)''')
            self.c.commit()

    def get_request_by_telegram_id(self, telegram_id: int, rq_type='trade', status='any') -> Request or None:
        telegram_id = int(telegram_id)
        requests = self.get_all_requests()
        if status == 'any':
            for request in requests:
                if request.telegram_id == telegram_id \
                        and rq_type in request.type \
                        and request.status != "user_confirmed" \
                        and request.status != 'user_payed':
                    return request
            else:
                return None
        else:
            for request in requests:
                if request.telegram_id == telegram_id and rq_type in request.type:

                    return request
        return None

    def get_all_requests(self) -> list:
        requests_from_db = self.select_column_from_db('*', 'requests')
        requests = []
        for request in requests_from_db:
            requests.append(get_request_from_db(request))
        return requests

    def get_request_by_id(self, rq_id: int):
        rq_id = int(rq_id)
        requests = self.get_all_requests()
        for request in requests:
            if request.db_id == rq_id:
                return request
        return None

    def add_request_to_db(self, request):
        request = get_request_from_db(request)
        if not self.request_in_db(request):
            self.insert_request_in_db(request)
            print(request, 'added', request.type)
            return self.get_request_by_telegram_id(telegram_id=request.telegram_id, rq_type=request.type)

    def insert_request_in_db(self, request):
        sql = f''' INSERT INTO requests(telegram_id, status, type, when_created, comment, wallet)
                                                         VALUES(?,?,?,?,?,?) '''
        self.cursor.execute(sql, request.database_list())
        self.c.commit()

    def top_up_user_balance(self, user: User, amount: (int or float)):
        user.balance = float(user.balance) + float(amount)
        self.update_user_in_db(user)

    def user_in_db(self, telegram_id):
        return self.get_user_by_telegram_id(telegram_id) is not None

    def get_status_message(self, call):
        call_data, request_id, client_id, status = call.split(" ")
        if status in ["no_payment", 'close_request']:
            self.delete_request_from_db(request_id)
        status_msgs = {'payment_s': 'Платёж подтверждён!',
                       'crypto_sent': 'Криптовалюта отправлена!',
                       'replenish_s': 'Баланс пополнен!',
                       'not_enough': 'Было отправленно недостаточно средств!',
                       'no_payment': "Не удалось найти ваш платёж!",
                       'close_request': 'Заявка закрыта!'}
        message = status_msgs[status]
        return client_id, message

    def update_user_in_db(self, user):
        cursor = self.c.cursor()
        cursor.execute(f'UPDATE users SET id = ?, telegram_id = ?, balance = ?, status = ?, '
                       f'is_follower = ?, invited_by = ?, '
                       f'q_of_trades = ?, earned_from_partnership = ? WHERE telegram_id = {user.telegram_id}',
                       user.update_database_list())
        self.c.commit()
        print(self.get_user_by_telegram_id(user.telegram_id), 'usr updated')

    def update_request_in_db(self, request: Request):
        with self.c:
            self.cursor.execute(f'UPDATE requests SET id = ?, telegram_id = ?, status = ?, type = ?, '
                                f'when_created = ?, comment = ?, wallet = ? '
                                f'WHERE id = {request.db_id}', request.update_database_list())
            self.c.commit()
        print(self.get_request_by_id(request.db_id), 'rq updated')

    def get_requests(self, user: User):
        trade_request = self.get_request_by_telegram_id(user.telegram_id)
        help_request = self.get_request_by_telegram_id(user.telegram_id, rq_type='help_request')
        replenish_request = self.get_request_by_telegram_id(user.telegram_id, rq_type='replenish')
        service_request = self.get_request_by_telegram_id(user.telegram_id, rq_type='service_request')
        return_request = self.get_request_by_telegram_id(user.telegram_id, rq_type='return')
        return trade_request, help_request, replenish_request, service_request, return_request

    def delete_request_from_db(self, request_id: int):
        with self.c:
            self.cursor.execute(f'DELETE FROM requests WHERE id = {request_id}')
            self.c.commit()

    def print_all_requests(self):
        requests = self.get_all_requests()
        for request in requests:
            print(request)

    def print_all_users(self):
        users = self.get_all_users()
        for user in users:
            print(user)

    def check_requests_shell_life(self):
        requests = self.get_all_requests()
        for request in requests:
            if request_time_is_done(request.when_created) and request.type != 'help_request' \
                    and request.status != 'user_confirmed' \
                    and request.status != 'T: user_payed':
                self.delete_request_from_db(request.db_id)

    def select_column_from_db(self, column, table):
        with self.c:
            cursor = self.c.cursor()
            cursor.execute(f"SELECT {column} FROM {table}")
            result = cursor.fetchall()
        return result

    def add_new_user_to_db(self, user_id, follow_status=0, invited_by=0):
        user = User(telegram_id=user_id, is_follower=follow_status, invited_by=invited_by)
        telegram_ids_from_db = self.select_column_from_db('telegram_id', 'users')
        if telegram_ids_from_db is None or self.get_user_by_telegram_id(user.telegram_id) is None:
            self.insert_user_in_db(user)
            return user

        else:
            user = self.get_user_by_telegram_id(user.telegram_id)
            return user

    def insert_user_in_db(self, user):
        sql = f'INSERT INTO users(telegram_id, balance, status, is_follower, invited_by, ' \
              f'q_of_trades, earned_from_partnership) VALUES(?,?,?,?,?,?,?)'
        self.cursor.execute(sql, user.database_list())
        self.c.commit()

    def get_all_users(self):
        users_from_db = self.select_column_from_db('*', 'users')
        users = []
        for user in users_from_db:
            user = get_user_from_db(user)
            users.append(user)
        return users

    def get_all_unprocessed_requests_in_list(self) -> list:
        requests = self.get_all_requests()
        unprocessed_requests = []
        for request in requests:
            if request.status == "user_confirmed" or request.status == 'user_payed':
                unprocessed_requests.append(request)
        return unprocessed_requests

    def get_user_by_telegram_id(self, telegram_id: int) -> User or None:
        telegram_id = int(telegram_id)
        users = self.get_all_users()
        for user in users:
            if user.telegram_id == telegram_id:
                return user
        return None

    def get_number_of_invitations(self, telegram_id):
        self.cursor.execute(f"SELECT * FROM users WHERE invited_by = ({telegram_id})")
        res = self.cursor.fetchall()
        number = len(res)
        return number

    def pay_inviter(self, telegram_id, fee):
        # TODO
        user = self.get_user_by_telegram_id(telegram_id)
        if user.invited_by != 0:
            inviter = self.get_user_by_telegram_id(user.invited_by)
            inviter.earned_from_partnership = inviter.earned_from_partnership + fee  # earned from partnership increased
            inviter.balance = inviter.balance + fee  # balance increased
            self.update_user_in_db(inviter)

    def request_in_db(self, request):
        return self.get_request_by_telegram_id(telegram_id=request.telegram_id,
                                               rq_type=request.type,
                                               status=request.status) is not None


if __name__ == '__main__':
    database = DataBase()
    database.print_all_users()
    print('_' * 100)
    database.print_all_requests()
    print('_' * 100)
