import dotenv
import telepot
from telepot.namedtuple import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

bot = telepot.Bot(dotenv.dotenv_values('.env')['TOKEN'])


class Response:
    @staticmethod
    def send_message(chat_id, text):
        bot.sendMessage(chat_id, text)

    @staticmethod
    def delete_reply_keyboard(chat_id, text):
        bot.sendMessage(chat_id, text, reply_markup=ReplyKeyboardRemove())

    @staticmethod
    # used when opening session
    def response_with_reply_keyboard_when_waiting_photos(chat_id):
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Створити pdf")],
                [KeyboardButton(text="Відмінити створення pdf")]
            ],
            resize_keyboard=True)
        bot.sendMessage(chat_id,
                        "Сеанс створення pdf відкритий.\n\n1) Надішліть фото.\n2) Коли готові створювати pdf натисність кнопку "
                        "'Створити pdf'", reply_markup=keyboard)

    @staticmethod
    # used when opening session
    def response_with_reply_keyboard_when_waiting_photos_state_2(chat_id):
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Створити pdf")],
                [KeyboardButton(text="Відмінити створення pdf")]
            ],
            resize_keyboard=True)
        bot.sendMessage(chat_id, "Надішліть хоча б одне фото!", reply_markup=keyboard)

    @staticmethod
    # used when user want to start creating (figuratively event is called <when received photo>, but it's not obvious)
    def response_with_reply_keyboard_when_received_photos(chat_id):
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Автоматична назва"), KeyboardButton(text="Моя назва")],
                [KeyboardButton(text="Відмінити створення pdf")]
            ],
            resize_keyboard=True)
        bot.sendMessage(chat_id, "Як назвати pdf?", reply_markup=keyboard)

    @staticmethod
    # used when pdf is sent
    def response_with_reply_keyboard_when_pdf_is_sent(chat_id):
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Завершити сеанс")],
                [KeyboardButton(text="Продовжити створення")]
            ],
            resize_keyboard=True)
        bot.sendMessage(chat_id, "Що робити далі?", reply_markup=keyboard)

    @staticmethod
    # used when session was continued
    def response_with_reply_keyboard_when_session_was_continued(chat_id):
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Створити pdf")],
                [KeyboardButton(text="Відмінити створення pdf")]
            ],
            resize_keyboard=True)
        bot.sendMessage(chat_id, "Сеанс створення pdf продовжено. Надішліть фото.", reply_markup=keyboard)
