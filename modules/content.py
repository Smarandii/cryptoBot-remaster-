
class BotContent:
    BOT_TAG = 'crypto_bot_bot_bot'

    # STATUSES
    BASE_STATUS = 'Серебрянный'
    MEDIUM_STATUS = 'Золотой'
    ADVANCED_STATUS = 'Платиновый'

    # SPECIAL USERS FILES
    ADMINS_LIST = 'admins.txt'
    OPERATORS_LIST = 'operators.txt'

    # GROUP & CHANNEL ID'S
    GROUP_ID = "-498679897"
    CHANNEL_ID = "-1001461384160"

    # SUGGESTION URLS
    URLS = {'group': 'https://t.me/joinchat/JihjtQ9PzjsJBH2Uw2NxFg',
            'channel': 'https://t.me/joinchat/AAAAAFca8-DX0MYpg3nfNA'}

    # SPECIAL INFO FOR BOT
    BASE_REQUEST_NUM = 1000
    REFERAL_PERCENT = 0.003
    RETURN_PERCENT = 0.9
    PERCENTS = {'under_5k_f': {'Bitcoin': 0.12,
                               'LiteCoin': 0.10,
                               'Ethereum': 0.11,
                               'Bitcoin Cash': 0.11,
                               'ExmoRUB': 0.10
                               },
                'from_5k_to_10k_f': {'Bitcoin': 0.11,
                                     'LiteCoin': 0.09,
                                     'Ethereum': 0.11,
                                     'Bitcoin Cash': 0.11,
                                     'ExmoRUB': 0.09
                                     },
                'above_10k_f': {'Bitcoin': 0.10,
                                'LiteCoin': 0.08,
                                'Ethereum': 0.10,
                                'Bitcoin Cash': 0.10,
                                'ExmoRUB': 0.085
                                },
                'under_2k': {
                            'Bitcoin': 0.13,
                            'LiteCoin': 0.11,
                            'Ethereum': 0.12,
                            'Bitcoin Cash': 0.12,
                            'ExmoRUB': 0.10
                             },
                'from_2k_to_5k': {
                            'Bitcoin': 0.12,
                            'LiteCoin': 0.11,
                            'Ethereum': 0.11,
                            'Bitcoin Cash': 0.12,
                            'ExmoRUB': 0.10
                                 },
                'from_5k_to_10k': {
                            'Bitcoin': 0.115,
                            'LiteCoin': 0.105,
                            'Ethereum': 0.105,
                            'Bitcoin Cash': 0.115,
                            'ExmoRUB': 0.095
                                 },
                'above_10k': {
                    'Bitcoin': 0.11,
                    'LiteCoin': 0.10,
                    'Ethereum': 0.10,
                    'Bitcoin Cash': 0.11,
                    'ExmoRUB': 0.09
                             },
                }
    DISCOUNTS = {'Серебрянный': 0,
                 'Золотой': 0.005,
                 'Платиновый': 0.01}
    EXAMPLE = {'ExmoRUB': '1000',
               'Bitcoin': '0.001456 BTC\nили\n1000 RUB',
               'Ethereum': '0.001432',
               'Bitcoin Cash': '0.001687',
               'LiteCoin': '0.00987 LTC\nили\n1000 RUB'}

    SBER_REQUISITES = "sbersbersbersbersbersber"
    YANDEX_REQUISITES = "yayayayayayayayayayaya"
    ADVCASH_REQUISITES = "advadvadvadvadvadvadv"
    TO_ACHIEVE_MEDIUM_STATUS = 40
    TO_ACHIEVE_ADVANCED_STATUS = 100
    MIN_VALUE_FOR_RETURN = 150

    ADV_COMMISSION_PRICE = 80
    MAX_COMMISSION_PRICE = 230

    COMMISSION = {
        'priority_usl': 0,
        'priority_adv': ADV_COMMISSION_PRICE,
        'priority_max': MAX_COMMISSION_PRICE
    }

    REQUISITES = {
        'pay_sber': SBER_REQUISITES,
        'pay_yandex': YANDEX_REQUISITES,
        'pay_advcash': ADVCASH_REQUISITES,
    }

    BITCOIN_WALLET_EXAMPLE = '3GncF7muEw1oayeuH33rxahdmtHSWoj4tw'
    LITCOIN_WALLET_EXAMPLE = 'MDwCMAofN9K4U8e9EPMzs57Asams2AFBen'
    ETHEREUM_WALLET_EXAMPLE = '0x2Fe62eae2fB629808C94E55AF69fB373FD959980'
    BITCOINCASH_WALLET_EXAMPLE = '3GncF7muEw1oayeuH33rxahdmtHSWoj4tw'

    MESSAGES = {
        'channel_suggest': "❓ Ещё не подписаны на наш канал и не в групповом чате?\n"
                           "📈 А зря! Всем подписавшимся - более выгодный процент обмена.",
        'partnership': '👥 👥 0.3% от суммы выданной валюты\n🤝 Приглашено пользователей: {}\n💰 Заработано: {} руб.\n'
                       '💳 Доступно на вывод: {} руб.\n* для вывода обращайтесь в тех. поддержку\n➖➖➖➖➖➖➖➖\n'
                       '🔗 Ваша партнерская ссылка:\n{}',
        'choose_crypto': '⬇️ Выберите криптовалюту',
        'replenish_balance': "На данный момент ваш баланс: {} руб.\n",
        'current_balance': "Вы {} пользователь!\nНа данный момент ваш баланс: {} руб.\n",
        'menu_arrow': "⬇️Меню",
        'personal_cabinet': 'Личный кабинет',
        'start_trade_rq': '💰Введи нужную сумму в RUB или в {}\n'
                          'Например: {}',
        'where_return': 'Выберите куда возвращать деньги',
        'return_failure': 'Не удалось отправить заявку.\nНа вашем счёте недостаточно средств.\n'
                          'Доступно для вывода: {} руб.\n'
                          'Минимальная сумма вывода: {}\n',
        'return_available': "Сумма доступная на вывод: {}\n"
                            "💰 Отправьте сумму в рублях, которую вы хотите вывести"
                            "Минимальная сумма вывода: {}\n",
        'confirm_return_requisites': 'Деньги с вашего баланса будут отправлены сюда:\n'
                                     '{}',
        'confirm_user_question': "⏰ Ответ на ваш вопрос будет в чате с ботом, ожидайте!",
        'confirm_user_replenish': "Пополнение баланса на сумму: {} ₽",
        'unacceptable_value': 'Недопустимое значение, попробуйте снова',
        'choose_payment_method': 'Выберите способ оплаты!',
        'promotion_message': 'Это ваша {} заявка, она будет беспроцентной!',
        'confirm_user_wallet': 'После оплаты, криптоваллюта будет отправлена на этот кошелёк:\n{}',
        'unacceptable_wallet': '🙅‍♂️ Такого кошелька не существует! Попробуйте ещё раз.',
        'choose_commission': 'Выберите желаемую комиссию',
        'message_from_operator_notification': 'Вам написал сотрудник тех. поддержки: {}',
        'message_sent_notification': 'Сообщение отправлено!',
        'question_answered_notification': 'На ваш вопрос ответили!\nОтвет: {}\nВопрос автоматически закрыт',
        'wait_for_operator_answer': "Отправьте ответ на вопрос следующим сообщением!",
        'question_deleted': 'Вопрос был удалён!',
        'request_deleted': 'Заявка была удалена!',
        'request_cancelled_by_operator': '✅ Заявка была отменена!\nОтправить сообщение пользователю:',
        'notify_user': '✅ Отправить сообщение пользователю:',
        'balance_cut': 'Деньги списаны',
        'balance_cut_notification': 'С вашего счёта списали {}!',
        'user_have_low_balance': 'У пользователя не достаточно денег',
        'user_not_found': 'Данный пользователь не пользуется ботом',
        'client_balance_replenished': 'Деньги были зачислены на счёт пользователя',
        'balance_replenished': '{} руб. было зачислено на ваш баланс',
        'input_requisites_next': 'Введите реквизиты следующим сообщением!',
        'wait_after_return': 'Осталось только подождать! Бот уже отправляет вам деньги',
        'already_have_request': 'У вас уже есть заявка, желаете её отменить?',
        'request_in_progress': 'Ваша заявка обрабатывается!',
        'request_not_found': 'Заявка не найдена :(',
        'requests_not_found': 'Заявки не найдены :(',
        'trade_cancel_warning': 'Если вы уже перевели деньги по указанным реквизитам, то они зачислятся на ваш баланс.'
                          'Вы уверены, что хотите отменить заявку?',
        'request_cancelled': '✅ Заявка была отменена!',
        'return_cancel_warning': 'Деньги уже были списаны с вашего баланса! '
                         'Подождите пока бот отправит их на указанные реквизиты.'
                         'Если вы отмените заявку, то платёж может потеряться! Вы уверены, что хотите отменить заявку?',
        'priority_usl': 'Комиссия установлена! Ваша заявка будет обработана как только '
                            'бот освободится от обработки заявок с более высокими комиссиями.\n'
                            'Выберите способ оплаты!',
        'priority_adv': 'Комиссия установлена! Ваша заявка будет обработана как только '
                          'бот освободится от обработки заявок с максимальными комиссиями.\n'
                          'Выберите способ оплаты!',
        'priority_max': 'Комиссия установлена! Ваша заявка будет обработана в самое ближайшее время.\n'
                          'Выберите способ оплаты!',
        'edit_wallet': 'Введите новый кошелёк следующим сообщением!',
        'wallet_correct': 'Выберите желаемую комиссию сети!',
        'input_replenish_amount': "💰 Отправьте сумму в рублях, на которую вы хотите пополнить ваш баланс",
        'replenish_confirm': "Пополнение баланса на сумму: {} ₽\n"
                             "Не отменяйте заявку, если передумали пополнять баланс!\n"
                             "(Ваш платёж потеряется)\n"
                             "Вы всегда сможете вывести деньги с баланса бота.",
        'request_processing': 'Отлично! Ваша завяка обрабатывается. Уникальный номер заявки: {}',
        'requisites_for_payment': 'Реквизиты для оплаты: {}\n{}',
        'pay_balance': 'Деньги спишутся c вашего баланса в боте: {}\n',
        'balance_is_too_low': 'На вашем счёте недостаточно средств.\n'
                              'Ваш баланс: {} руб.\n'
                              'Выберите другой способ оплаты:',




        'confirm_user_balance_unreplenish': 'Вы уверены, что хотите списать с баланса этого пользователя '
                                            '{} сумму {}?',
        'confirm_user_balance_replenish': 'Вы уверены, что хотите пополнить баланс этого пользователя?\n'
                                          '{} на сумму {}?',
        'confirm_send_answer': 'Вы уверены, что хотите отправить этот ответ пользователю?\n{}',
        'confirm_send_message': 'Вы уверены, что хотите отправить это сообщение пользователю?\n{}',
        'send_message_to_user': "Отправьте персональный идентификатор "
                                "пользователя и ваше сообщение следующим сообщением!\n"
                                "Вот так:\n"
                                "id message",
        'user_balance_unreplenish': "Отправьте персональный идентификатор "
                                    "пользователя и сумму снятия следующим сообщением!\n"
                                    "Вот так:\n"
                                    "id amount",
        'user_balance_replenish': "Отправьте персональный идентификатор "
                                  "пользователя и сумму пополнения следующим сообщением!\n"
                                  "Вот так:\n"
                                  "id amount",
        'delete_admin': 'Админ успешно удалён!',
        'delete_operator': 'Оператор успешно удалён!',
        'new_operator': 'Новый оператор успешно добавлен!',
        'new_admin': 'Новый админ успешно добавлен!',
        'request_exist_warning': 'У вас уже есть заявка, желаете её отменить?'
    }

    def get_price_from_request(self, request):
        price = request.comment.split(': ')[1]
        return float(price)

    def change_request_comment_price(self, request, amount: float):
        price = self.get_price_from_request(request)
        price = round(price + amount, 2)
        if amount == 0:
            request.comment = request.comment + ' Обычная комиссия'
        if amount == self.ADV_COMMISSION_PRICE:
            request.comment = request.comment.split(': ')[0] + f': {price} Комиссия повышенная'
        if amount == self.MAX_COMMISSION_PRICE:
            request.comment = request.comment.split(': ')[0] + f': {price} Комиссия максимальная'
        return request.comment

    def get_fee(self, request):
        fee = request.comment.split(": ")[1]
        return round(float(fee) * self.REFERAL_PERCENT, 2)

    def get_status_discount(self, user):
        return self.DISCOUNTS[user.status]

    def get_user_price(self, curr_price, user, trade_value, key):
        user_price = float(curr_price) * float(trade_value)
        discount = self.get_status_discount(user)
        promotion = None
        if (user.quantity_of_trades + 1) % 10 == 0 and 1 < user_price < 3000:
            promotion = True
            percent = 1
        elif user.is_follower is True:
            if 1 <= user_price <= 5000:
                percent = self.PERCENTS['under_5k_f'][key]
            elif 5000 < user_price < 10000:
                percent = self.PERCENTS['from_5k_to_10k_f'][key]
            elif 10000 <= user_price:
                percent = self.PERCENTS['above_10k_f'][key]
            else:
                return 'price is too low'
        else:  # if user is not follower
            if 1 <= user_price <= 2000:
                percent = self.PERCENTS['under_2k'][key]
            elif 2000 < user_price < 5000:
                percent = self.PERCENTS['from_2k_to_5k'][key]
            elif 5000 <= user_price < 10000:
                percent = self.PERCENTS['from_5k_to_10k'][key]
            elif 10000 <= user_price:
                percent = self.PERCENTS['above_10k'][key]
            else:
                return 'price is too low'
        user_curr = float(curr_price) + float(curr_price) * percent
        user_price = user_curr * float(trade_value)
        if key == "EXMOCoin":
            user_price -= 5
        return round(user_price, 2) - user_price * discount, user_curr, promotion

    def get_admins_list(self) -> list:
        admins = []
        with open(self.ADMINS_LIST, 'r') as f:
            for admin in f:
                admins.append(admin[:-1:])
        return admins

    def get_operators_list(self) -> list:
        operators = []
        with open(self.ADMINS_LIST, 'r') as f:
            for operator in f:
                operators.append(operator[:-1:])
        return operators

    def add_admin(self, new_admin_id: str):
        new_admin_id = str(new_admin_id)
        with open(self.ADMINS_LIST, 'a') as f:
            f.write(new_admin_id + "\n")

    def add_operator(self, new_operator_id: str):
        new_operator_id = str(new_operator_id)
        with open(self.OPERATORS_LIST, 'a') as f:
            f.write(new_operator_id + "\n")

    def delete_operator(self, operator_id):
        operator_id = str(operator_id)
        operators = self.get_admins_list()
        with open(self.OPERATORS_LIST, 'w') as f:
            for operator in operators:
                if operator != operator_id:
                    continue
                else:
                    f.write(operator + "\n")

    def delete_admin(self, admin_id):
        admin_id = str(admin_id)
        admins = self.get_admins_list()
        with open(self.ADMINS_LIST, 'w') as f:
            for admin in admins:
                if admin != admin_id:
                    continue
                else:
                    f.write(admin_id + "\n")

    def get_prepayment_message(self, user_curr, trade_value, user_price, key) -> str:
        messages = {'Bitcoin': f"Курс: {user_curr} руб.\n"
                               f"Покупка {trade_value} {key}\n"
                               f"К оплате: {user_price} руб.\n"
                               f"Следующим сообщением отправьте нам ваш криптокошелёк.\n"
                               f"Пример: {self.BITCOIN_WALLET_EXAMPLE}",
                    'LiteCoin': f"Курс: {user_curr} руб.\n"
                                f"Покупка {trade_value} {key}\n"
                                f"К оплате: {user_price} руб.\n"
                                f"Следующим сообщением отправьте нам ваш криптокошелёк.\n"
                                f"Пример: {self.LITCOIN_WALLET_EXAMPLE}",
                    'ExmoRUB': f"Курс: {user_curr} руб.\n"
                               f"Покупка {trade_value} {key}\n"
                               f"К оплате: {user_price} руб.\n",
                    'Ethereum': f"Курс: {user_curr} руб.\n"
                                f"Покупка {trade_value} {key}\n"
                                f"К оплате: {user_price} руб.\n"
                                f"Следующим сообщением отправьте нам ваш криптокошелёк.\n"
                                f"Пример: {self.ETHEREUM_WALLET_EXAMPLE}",
                    'Bitcoin Cash': f"Курс: {user_curr} руб.\n"
                                    f"Покупка {trade_value} {key}\n"
                                    f"К оплате: {user_price} руб.\n"
                                    f"Следующим сообщением отправьте нам ваш криптокошелёк.\n"
                                    f"Пример: {self.BITCOINCASH_WALLET_EXAMPLE}",
                    }
        return messages[key]
