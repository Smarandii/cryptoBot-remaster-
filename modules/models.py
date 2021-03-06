from modules.content import BotContent


class Request:
    def __init__(self, db_id=0, telegram_id=None, status=None, rq_type=None, when_created=None, comment=None,
                 wallet=None):

        self.db_id = int(db_id)
        self.telegram_id = int(telegram_id)
        self.status = status
        self.type = rq_type
        self.when_created = when_created
        self.comment = comment
        self.wallet = wallet
        self.key = None
        self.curr_price = None

    def database_list(self) -> list:
        return [self.telegram_id, self.status, self.type,
                self.when_created, self.comment, self.wallet]

    def update_database_list(self) -> list:
        return [self.db_id, str(self.telegram_id), self.status, self.type,
                self.when_created, self.comment, self.wallet]

    def __str__(self):
        return '{},{},{},{},{},{},{}'.format(self.db_id,
                                             self.telegram_id,
                                             self.status,
                                             self.type,
                                             self.when_created,
                                             self.comment,
                                             self.wallet)

    def get_key_and_curr_price(self):
        if 'Bitcoin Cash' not in self.type:
            operation_type, key, curr_price = self.type.split(" ")
        else:
            operation_type, key, _, curr_price = self.type.split(" ")
        self.key = key
        self.curr_price = curr_price


class User:
    def __init__(self, db_id=0, telegram_id=None,
                 balance=0, status=BotContent.BASE_STATUS,
                 is_follower=None, invited_by=0,
                 quantity_of_trades=0, earned_from_partnership=0):
        self.db_id = int(db_id)
        self.telegram_id = int(telegram_id)
        self.balance = float(balance)
        self.status = status
        self.is_follower = is_follower
        self.invited_by = int(invited_by)
        self.quantity_of_trades = int(quantity_of_trades)
        self.earned_from_partnership = float(earned_from_partnership)
        self.partnership_link = None
        self.is_admin = False
        self.is_operator = False
        self.return_request = None
        self.service_request = None
        self.replenish_request = None
        self.help_request = None
        self.trade_request = None

    def update_database_list(self) -> list:
        return [self.db_id, str(self.telegram_id), self.balance, self.status, self.is_follower,
                self.invited_by, self.quantity_of_trades, self.earned_from_partnership]

    def database_list(self) -> list:
        return [self.telegram_id, self.balance, self.status, self.is_follower,
                self.invited_by, self.quantity_of_trades, self.earned_from_partnership]

    def __str__(self):
        return '{},{},{},{},{},{},{},{}'.format(self.db_id,
                                                self.telegram_id,
                                                self.balance,
                                                self.status,
                                                self.is_follower,
                                                self.invited_by,
                                                self.quantity_of_trades,
                                                self.earned_from_partnership)

    def pull_requests(self, trade_request=None, help_request=None, replenish_request=None, service_request=None,
                      return_request=None):
        self.trade_request = trade_request
        self.help_request = help_request
        self.replenish_request = replenish_request
        self.service_request = service_request
        self.return_request = return_request

    def all_requests_is_none(self):
        return self.trade_request is None and self.replenish_request is None and self.help_request is None and self.service_request is \
               None and self.return_request is None


class Value:
    def __init__(self, value, v_type=None):
        self.value = float(value)
        self.type = v_type

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.value == other

    def __ne__(self, other):
        return self.value != other

    def __lt__(self, other):
        return self.value < other

    def __le__(self, other):
        return self.value <= other

    def __gt__(self, other):
        return self.value > other

    def __ge__(self, other):
        return self.value >= other

    def __float__(self):
        return self.value


class MessageParser:
    def __init__(self, msg):
        self.user_message = msg
        pass

    def replenish_value_is_acceptable(self):
        return 0 < self.get_value_from_message()

    def trade_value_is_acceptable(self, key):
        trade_value = self.get_value_from_message()
        if trade_value.type.lower() == key.lower():
            if key == "ExmoRUB":
                return 5 < trade_value <= 100000
            if key == 'Bitcoin':
                return 0 < trade_value <= 0.02
            if key == 'Ethereum':
                return 0 < trade_value <= 0.02
            if key == 'Bitcoin Cash':
                return 0 < trade_value <= 0.02
            if key == 'LiteCoin':
                return 0 < trade_value <= 0.02
        else:
            if key == "ExmoRUB":
                return 0 < trade_value <= 100000
            if key == 'Bitcoin':
                return 0 < trade_value <= 50000
            if key == 'Ethereum':
                return 0 < trade_value <= 50000
            if key == 'Bitcoin Cash':
                return 0 < trade_value <= 50000
            if key == 'LiteCoin':
                return 0 < trade_value <= 50000

    def get_message(self, words):
        m = ''
        for w in words:
            m += w + " "
        return m

    def get_receiver_id_and_message(self):
        words = self.user_message.text.split(" ")
        client_id = words.pop(0)
        message = self.get_message(words)
        return client_id, message

    def get_value_from_message(self) -> Value:
        if not self.user_message.text.isalpha() and " " in self.user_message.text:
            value_type = self.user_message.text.split()[1]
            value = self.user_message.text.split()[0]
            if ',' in self.user_message.text:
                return Value(v_type=value_type, value=value.replace(',', '.'))
            else:
                return Value(v_type=value_type, value=value)
        return Value(value=self.user_message.text, v_type='None')

    def get_command_value(self):
        command, command_value = self.user_message.text.split(" ")
        return command_value

    def get_invitation(self):
        who_invited = 0
        try:
            command, who_invited = self.user_message.text.split(" ")
            who_invited = int(who_invited, 16)
        except Exception:
            pass
        return who_invited


class CallParser:
    def __init__(self, call=None):
        if call is not None:
            print(call)
            self.data = call.data
            self.message = call.message
            self.from_user = call.from_user
        else:
            self.data = None
            self.message = None
            self.from_user = None























