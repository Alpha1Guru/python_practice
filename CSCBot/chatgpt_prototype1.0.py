from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import re

# Dummy DB
attendance_list = {"240591245"}
student_db = {"240591245"}

# Define command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to the CSC Assistant Bot!\n"
        "Please choose an option:\n"
        "1. /attendance - Mark Attendance\n"
        "2. /register - Register for Semester\n"
        "3. /pay - Pay for Math101 Workbook"
    )

async def attendance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Please enter your matric number to mark attendance:")

    return

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    if re.match(r"240591\d{3}", text):
        if text in attendance_list:
            await update.message.reply_text("Your attendance is already recorded.")
        else:
            attendance_list.add(text)
            await update.message.reply_text("Your attendance has been marked.")
    else:
        await update.message.reply_text("Invalid matric number format. Try again.")

# Set up the bot
def main():
    bot_token = "7718408832:AAGlkAWcfLQJbuNnwa8xHUbKD4TmfhMfrZE"
    app = ApplicationBuilder().token(bot_token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("attendance", attendance))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
