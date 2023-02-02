from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *
# name of bot: test_bot_for_python
# username: SlaviliBot
app = ApplicationBuilder().token("6120987249:AAH135fxVudWeWVmJ_dnTWgOat30vIpbiA4").build()

app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("getAllAbonents", get_command))
app.add_handler(CommandHandler("addAbonent", addAbonent_command))
app.add_handler(CommandHandler("addPhone", addPhone_command))
print('Server has being started')
app.run_polling()