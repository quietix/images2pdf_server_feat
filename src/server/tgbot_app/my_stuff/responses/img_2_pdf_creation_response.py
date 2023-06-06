from src.server.tgbot_app.my_stuff.responses.common_response import CommonResponse
from telepot.namedtuple import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
import telepot
import dotenv
bot = telepot.Bot(dotenv.dotenv_values('.env')['TOKEN'])


class Img2PdfCreationResponse(CommonResponse):

    # used when opening session
    def response_with_reply_keyboard_when_waiting_photos(self, chat_id):
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Створити pdf 🖼")],
                [KeyboardButton(text="Відмінити створення pdf ❌")]
            ],
            resize_keyboard=True)
        bot.sendMessage(chat_id,
                        "Сеанс створення pdf відкритий.\n\n1) Надішліть фото.\n2) Коли готові створювати pdf, натисність кнопку "
                        "'Створити pdf'", reply_markup=keyboard)

    # used when opening session
    def response_with_reply_keyboard_when_waiting_photos_state_2(self, chat_id):
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Створити pdf 🖼")],
                [KeyboardButton(text="Відмінити створення pdf ❌")]
            ],
            resize_keyboard=True)
        bot.sendMessage(chat_id, "Надішліть хоча б одне фото!", reply_markup=keyboard)

    # used when user want to start creating (figuratively event is called <when received photo>, but it's not obvious)
    def response_with_reply_keyboard_when_received_photos(self, chat_id):
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Автоматична назва 🖼"), KeyboardButton(text="Моя назва 🖼")],
                [KeyboardButton(text="Відмінити створення pdf ❌")]
            ],
            resize_keyboard=True)
        bot.sendMessage(chat_id, "Як назвати pdf?", reply_markup=keyboard)

    # used when creation session was continued
    def response_with_reply_keyboard_when_creation_session_was_continued(self, chat_id):
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Створити pdf 🖼")],
                [KeyboardButton(text="Відмінити створення pdf ❌")]
            ],
            resize_keyboard=True)
        bot.sendMessage(chat_id, "Сеанс створення pdf продовжено. Надішліть фото.", reply_markup=keyboard)

    # used when pdf is sent
    def response_with_reply_keyboard_when_pdf_is_sent_creation(self, chat_id):
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Завершити сеанс")],
                [KeyboardButton(text="Продовжити створення 🖼")]
            ],
            resize_keyboard=True)
        bot.sendMessage(chat_id, "Що робити далі?", reply_markup=keyboard)