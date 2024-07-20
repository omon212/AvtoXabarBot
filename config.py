from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
WORK_DIRECTORY = env.str("WORK_DIRECTORY")
API_ID = env.int("API_ID")
API_HASH = env.str("API_HASH")
IP = env.str("ip")
