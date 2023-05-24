from telepot import Bot
import dotenv

dotenv.load_dotenv()

token = dotenv.dotenv_values('.env')['TOKEN']
url = dotenv.dotenv_values('.env')['URL']

bot = Bot(token)

bot.setWebhook(url)
# bot.deleteWebhook()