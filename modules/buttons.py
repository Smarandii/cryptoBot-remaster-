from modules.content import BotContent


class Buttons:
    def __init__(self, types):
        self.types = types
        self.REQUISITES_CONFIRM_KEYBOARD = self.keyboard_maker(2, ['⚒ Изменить реквизиты', '👌 Всё верно'],
                                                          ['edit_requisites', 'requisites_correct'])
        self.RETURN_MONEY = self.one_button_keyboard(text='Вывести деньги со счёта', callback_line='return_money')
        self.RETURN_MONEY_CONFIRM_KEYBOARD = self.keyboard_maker(2, ['👌 Всё верно', '🚫 Отменить заявку'],
                                                            ['return_confirmed', 'cancel_return'])
        self.REPLENISH_CONFIRM_KEYBOARD = self.keyboard_maker(2, ['👌 Всё верно', '🚫 Отменить заявку'],
                                                         ['replenish_confirmed', 'cancel_replenish'])
        self.REPLENISH_INSTEAD_REPLENISH = self.keyboard_maker(3, ['🚫 Отменить завявку и пополнить баланс',
                                                              '🕐 Не удалять заявку',
                                                              '❌ Просто отменить'],
                                                          ['replenish_instead', 'user_confirmed_payment',
                                                           'cancel_replenish_anyway'])
        self.CANCEL_REPLENISH_INSTEAD_REPLENISH = self.keyboard_maker(2, [
                                                                   '🕐 Не удалять заявку',
                                                                   '❌ Просто отменить'],
                                                               ['user_confirmed_payment',
                                                                'cancel_replenish_anyway'])
        self.REPLENISH_INSTEAD_RETURN = self.keyboard_maker(3, ['🚫 Отменить завявку и пополнить баланс', '🕐 Не удалять заявку',
                                                      '❌ Просто отменить'],
                                                  ['replenish_instead', 'user_confirmed_payment_replenish',
                                                   'cancel_return_anyway'])
        self.REPLENISH_INSTEAD_TRADE = self.keyboard_maker(3, ['🚫 Отменить завявку и пополнить баланс', '🕐 Не удалять заявку',
                                                     '❌ Просто отменить'],
                                                 ['replenish_instead', 'user_confirmed_payment_replenish', 'cancel_trade_anyway'])
        self.REPLENISH_BALANCE = self.one_button_keyboard(text="Пополнить баланс", callback_line='replenish_balance')
        self.REPLENISH_BALANCE_FROM_NEW_MSG = self.one_button_keyboard(text="Пополнить баланс",
                                                             callback_line='replenish_balance_nwmsg')
        self.CANCEL_ORDER = self.one_button_keyboard(text="🚫 Отменить заявку", callback_line='cancel_trade')
        self.CANCEL_HELP_RQ = self.one_button_keyboard(text="🚫 Удалить вопрос", callback_line='cancel_help_request')
        self.CANCEL_REPLENISH = self.one_button_keyboard(text='🚫 Отменить заявку', callback_line='cancel_replenish')
        self.CANCEL_RETURN = self.one_button_keyboard(text='🚫 Отменить заявку', callback_line='cancel_return')
        self.SHOW_OR_CANCEL_TRADE_ORDER = self.keyboard_maker(2, ['🚫 Отменить заявку', '❓ Показать заявку'],
                                                    ['cancel_trade', 'show_trade'])
        self.SHOW_OR_CANCEL_REPLENISH_ORDER = self.keyboard_maker(2, ['🚫 Отменить заявку', '❓ Показать заявку'],
                                                        ['cancel_replenish', 'show_replenish'])
        self.SHOW_OR_CANCEL_HELP_ORDER = self.keyboard_maker(2, ['🚫 Удалить вопрос', '❓ Показать вопрос'],
                                                   ['cancel_help_request', 'show_help_request'])
        self.SHOW_OR_CANCEL_RETURN_ORDER = self.keyboard_maker(2, ['🚫 Отменить заявку', '❓ Показать заявку'],
                                                     ['cancel_return', 'show_return'])
        self.WALLET_CONFIRM_KEYBOARD = self.keyboard_maker(2, ['⚒ Изменить кошелёк', '👌 Всё верно'],
                                                 ['edit_wallet', 'wallet_correct'])
        self.PURCHASE_CONFIRM_KEYBOARD = self.keyboard_maker(2, ['👌 Оплатил', '🚫 Отменить заявку'],
                                                   ['user_confirmed_payment', 'cancel_trade'])
        self.PURCHASE_CONFIRM_REPLENISH_KEYBOARD = self.keyboard_maker(2, ['👌 Оплатил', '🚫 Отменить заявку'],
                                                             ['user_confirmed_payment_replenish', 'cancel_replenish'])
        self.BALANCE_PAY_CONFIRM_REPLENISH_KEYBOARD = self.keyboard_maker(2, ['👌 Оплатить', '🚫 Отменить заявку'],
                                                      ['user_confirmed_blnc_replenish', 'cancel_replenish'])
        self.BALANCE_PAY_CONFIRM_KEYBOARD = self.keyboard_maker(2, ['👌 Оплатить', '🚫 Отменить заявку'],
                                                                ['user_confirmed_blnc', 'cancel_trade'])

        self.PAYMENT_METHODS = self.keyboard_maker(4, ['Сбербанк', 'Яндекс.Деньги', 'AdvCash', 'Списать деньги с баланса'],
                                         ['pay_sber', 'pay_yandex', 'pay_advcash', 'pay_balance'])
        self.CANCEL = types.InlineKeyboardButton(text='🚫 Отменить заявку', callback_data='cancel_trade')
        self.PAYMENT_METHODS.add(self.CANCEL)

        self.REPLENISH_METHODS = self.keyboard_maker(4, ['Сбербанк', 'Яндекс.Деньги', 'AdvCash', '🚫 Отменить заявку'],
                                           ['pay_sber_replenish', 'pay_yandex_replenish', 'pay_advcash_replenish', 'cancel_replenish'])

        self.REQUEST_PRIORITIES = self.keyboard_maker(3, ['Обычная', 'Повышенная (+80р.)', "Максимальная (+230р.)"],
                                            ['priority_usl', 'priority_adv', 'priority_max'])

    def one_button_keyboard(self, text, callback_line, url=None):
        keyboard = self.types.InlineKeyboardMarkup(row_width=1)
        button = self.types.InlineKeyboardButton(text=text, callback_data=callback_line, url=url)
        keyboard.add(button)
        return keyboard

    def keyboard_maker(self, number_of_buttons: int, text_for_each_button: list, callback_data: list):
        keyboard = self.types.InlineKeyboardMarkup()
        if number_of_buttons > 1:
            butt1 = self.types.InlineKeyboardButton(text=text_for_each_button[0], callback_data=callback_data[0])
            keyboard.add(butt1)
        if number_of_buttons >= 2:
            butt2 = self.types.InlineKeyboardButton(text=text_for_each_button[1], callback_data=callback_data[1])
            keyboard.add(butt2)
        if number_of_buttons >= 3:
            butt3 = self.types.InlineKeyboardButton(text=text_for_each_button[2], callback_data=callback_data[2])
            keyboard.add(butt3)
        if number_of_buttons >= 4:
            butt4 = self.types.InlineKeyboardButton(text=text_for_each_button[3], callback_data=callback_data[3])
            keyboard.add(butt4)
        return keyboard


class CryptoMenu:
    MENU_BUTTONS = {
                    'btc': 'Bitcoin(BTC)',
                    'ltc': 'LiteCoin(LTC)',
                    'exmo': 'ExmoRUB',
                    'eth': 'Ethereum(ETH)',
                    'bch': 'Bitcoin Cash(BCH)',
                    'main_menu': 'Главное меню'
                    }

    def __init__(self, types):
        self.types = types

    def get_menu_markup(self):
        markup = self.types.ReplyKeyboardMarkup()
        currency_btn_btc = self.types.KeyboardButton(self.MENU_BUTTONS['btc'])
        currency_btn_ltc = self.types.KeyboardButton(self.MENU_BUTTONS['ltc'])
        currency_btn_exmo = self.types.KeyboardButton(self.MENU_BUTTONS['exmo'])
        currency_btn_eth = self.types.KeyboardButton(self.MENU_BUTTONS['eth'])
        currency_btn_bch = self.types.KeyboardButton(self.MENU_BUTTONS['bch'])
        back_btn = self.types.KeyboardButton(self.MENU_BUTTONS['main_menu'])

        markup.row(currency_btn_btc, currency_btn_exmo)
        markup.row(currency_btn_ltc, currency_btn_eth, currency_btn_bch)
        markup.row(back_btn)
        return markup

    def sent_by_menu(self, text):
        if text in self.MENU_BUTTONS.values():
            return True
        return False


class PersonalMenu:
    MENU_BUTTONS = {
        'replenish': 'Пополнить баланс бота',
        'show_balance': 'Показать баланс',
        'main_menu': 'Главное меню'
    }

    def __init__(self, types):
        self.types = types

    def get_menu_markup(self):
        markup = self.types.ReplyKeyboardMarkup()
        replenish_btn = self.types.KeyboardButton(self.MENU_BUTTONS['replenish'])
        blnc_btn = self.types.KeyboardButton(self.MENU_BUTTONS['show_balance'])
        back_btn = self.types.KeyboardButton(self.MENU_BUTTONS['main_menu'])
        markup.row(replenish_btn, blnc_btn)
        markup.row(back_btn)
        return markup

    def sent_by_menu(self, text):
        if text in self.MENU_BUTTONS.values():
            return True
        return False


class UserMenu:
    MENU_BUTTONS = {'buy': 'Купить криптовалюту',
                    'personal_cabinet': 'Личный кабинет',
                    'help': 'Помощь 🆘',
                    'partnership': 'Партнёрка 👥'
                    }

    def __init__(self, types):
        self.types = types

    def get_menu_markup(self):
        markup = self.types.ReplyKeyboardMarkup()
        trade_btn = self.types.KeyboardButton(self.MENU_BUTTONS['buy'])
        help_btn = self.types.KeyboardButton(self.MENU_BUTTONS['help'])
        personal_menu_btn = self.types.KeyboardButton(self.MENU_BUTTONS['personal_cabinet'])
        partnership_btn = self.types.KeyboardButton(self.MENU_BUTTONS['partnership'])

        markup.row(trade_btn, help_btn)
        markup.row(partnership_btn, personal_menu_btn)
        return markup

    def suggestion_menu(self):
        keyboard = self.types.InlineKeyboardMarkup(row_width=1)
        group_btn = self.types.InlineKeyboardButton(text="Наш групповой чат 💬", url=BotContent.URLS['group'])
        channel_btn = self.types.InlineKeyboardButton(text="Наш канал 📢", url=BotContent.URLS['channel'])
        keyboard.add(group_btn, channel_btn)
        return keyboard

    def sent_by_menu(self, text):
        if text in self.MENU_BUTTONS.values():
            return True
        return False


class OperatorMenu:
    MENU_BUTTONS = {'show_n_a_requests': 'Показать заявки, требующие обработки',
                    'replenish_user': 'Пополнить баланс пользователя',
                    'cut_user_balance': 'Списать с баланса пользователя',
                    'send_message_to_user': 'Отправить сообщение пользователю',
                    'main_menu': 'Пользовательское меню',
                    }

    def __init__(self, types):
        self.types = types

    def get_menu_markup(self):
        markup = self.types.ReplyKeyboardMarkup()
        replenish_user = self.types.KeyboardButton(self.MENU_BUTTONS['replenish_user'])
        show_n_a_requests = self.types.KeyboardButton(self.MENU_BUTTONS['show_n_a_requests'])
        cut_user_balance = self.types.KeyboardButton(self.MENU_BUTTONS['cut_user_balance'])
        message_to_user = self.types.KeyboardButton(self.MENU_BUTTONS['send_message_to_user'])
        back_btn = self.types.KeyboardButton(self.MENU_BUTTONS['main_menu'])
        markup.row(replenish_user, show_n_a_requests)
        markup.row(cut_user_balance, message_to_user)
        markup.row(back_btn)
        return markup

    def sent_by_menu(self, text):
        if text in self.MENU_BUTTONS.values():
            return True
        return False


class AdminMenu:
    MENU_BUTTONS = {
                    'addadmin': "Добавить админа",
                    'deladmin': "Удалить админа",
                    'addoper': 'Добавить оператора',
                    'deloper': 'Удалить оператора',
                    'save_database': 'Сохранить базу данных'
                    }

    def __init__(self, types):
        self.types = types

    def get_menu_markup(self):
        markup = self.types.ReplyKeyboardMarkup()
        r_request = self.types.KeyboardButton(self.MENU_BUTTONS['addadmin'])
        n_a_requests = self.types.KeyboardButton(self.MENU_BUTTONS['deladmin'])
        d_request = self.types.KeyboardButton(self.MENU_BUTTONS['addoper'])
        h_request = self.types.KeyboardButton(self.MENU_BUTTONS['deloper'])
        save_database = self.types.KeyboardButton(self.MENU_BUTTONS['save_database'])
        markup.row(r_request, n_a_requests)
        markup.row(d_request, h_request)
        markup.row(save_database)
        return markup

    def sent_by_menu(self, text):
        if text in self.MENU_BUTTONS.values():
            return True
        return False
