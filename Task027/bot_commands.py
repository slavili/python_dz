from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from controller import *

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    result = """
/help - путеводитель по боту
/getAllAbonents - вывод на экран всех абонентов с телефонами
/getAllAbonents Фамилия - вывод всех абонентов с указанной фамилией
/addAbonent Фамилия Имя - добавление нового абонента(id генерируется автоматически, по принципу max+1)
/addPhone idАбонента НомерТелефона - добавление номера телефона сотрудника(idАбонента необходимо посмотреть с помощью предыдущих комманд)
    """
    await update.message.reply_text(result)

async def get_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text;
    msg = msg.split()
    if len(msg)>1:
        result = printAllAbonents(str(msg[1]));
    else:
        result = printAllAbonents();
    await update.message.reply_text(f'{result}')

async def addAbonent_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text;
    msg = msg.split()
    addAbonent(msg[1], msg[2])
    result = printAbonentsWithoutPhones()
    await update.message.reply_text(f'{result}')

async def addPhone_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text;
    msg = msg.split()
    if VerificationIdAbonent(int(msg[1])):
        addPhone(msg[1], msg[2])
        result = searchAbonentsById(msg[1]);
    else:
        result = f'Абонента с идентификатором {msg[1]} не существует!'

    await update.message.reply_text(f'{result}')