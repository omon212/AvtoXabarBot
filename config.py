from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
WORK_DIRECTORY = env.str("WORK_DIRECTORY")
IP = env.str("ip")
