from src.server.tgbot_app.my_stuff.responses.common_response import CommonResponse
from telepot.namedtuple import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
import telepot
import dotenv
bot = telepot.Bot(dotenv.dotenv_values('.env')['TOKEN'])


class MergePdfResponse(CommonResponse):

    # used when pdf is sent
    def response_with_reply_keyboard_when_pdf_is_sent_creation(self, chat_id):
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Завершити сеанс")],
                [KeyboardButton(text="Продовжити об'єднання 📂")]
            ],
            resize_keyboard=True)
        bot.sendMessage(chat_id, "Що робити далі?", reply_markup=keyboard)

    # used when opening merge pdf session
    def response_with_reply_keyboard_when_opening_merge_session(self, chat_id):
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Об'єднати pdf 📂")],
                [KeyboardButton(text="Відмінити об'єднання pdf ❌")]
            ],
            resize_keyboard=True)
        bot.sendMessage(chat_id,
                        "Сеанс об'єднання pdf відкритий.\n\n"
                        "1) Надішліть pdf-файли, які б хотіли об'єднати в один.\n"
                        "2) Коли готові створювати pdf, натисність кнопку "
                        "'Створити pdf'", reply_markup=keyboard)

    # used when opening session
    def response_with_reply_keyboard_when_waiting_pdfs_state_2(self, chat_id):
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Об'єднати pdf 📂")],
                [KeyboardButton(text="Відмінити об'єднання pdf ❌")]
            ],
            resize_keyboard=True)
        bot.sendMessage(chat_id, "Надішліть хоча б один pdf!", reply_markup=keyboard)

    def response_with_reply_keyboard_when_received_pdfs(self, chat_id):
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Автоматична назва 📂"), KeyboardButton(text="Моя назва 📂")],
                [KeyboardButton(text="Відмінити об'єднання pdf ❌")]
            ],
            resize_keyboard=True)
        bot.sendMessage(chat_id, "Як назвати pdf?", reply_markup=keyboard)

    # used when merge session was continued
    def response_with_reply_keyboard_when_merge_session_was_continued(self, chat_id):
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Об'єднати pdf 📂")],
                [KeyboardButton(text="Відмінити об'єднання pdf ❌")]
            ],
            resize_keyboard=True)
        bot.sendMessage(chat_id, "Сеанс об'єднання pdf продовжено. Надішліть фото.", reply_markup=keyboard)

    # used when pdf is sent
    def response_with_reply_keyboard_when_pdf_is_sent_merge(self, chat_id):
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Завершити сеанс")],
                [KeyboardButton(text="Продовжити об'єднання 📂")]
            ],
            resize_keyboard=True)
        bot.sendMessage(chat_id, "Що робити далі?", reply_markup=keyboard)