from utils.message import message

def init(update, context):
    bot = context.bot
    msg = "Ciao io sono {}\nsono stato creato da @squirrelnetwork\nSe vuoi vedere i miei sorgenti digita: /source\nPer funzionare basta digitare <code>/search terminediricercachevuoi</code>\nESEMPIO: <code>/search android</code>".format("@"+bot.username)
    message(update, context, msg)