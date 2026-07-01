import re
import json
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    ContextTypes, filters
)

# === Settings ===
ATTENDANCE_FILE = "attendance.json"
ADMIN_USER_ID = "the_one_who_conquered"  # Replace with your actual Telegram ID

# === File Storage ===
def load_attendance():
    try:
        with open(ATTENDANCE_FILE, "r") as f:
            return set(json.load(f))
    except FileNotFoundError:
        return set()

def save_attendance(attendance_set):
    with open(ATTENDANCE_FILE, "w") as f:
        json.dump(list(attendance_set), f)

attendance_list = load_attendance()

# === Commands ===

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to the CSC Attendance Bot!\n\n"
        "Use /attendance to mark your attendance.\n"
        "Admin can use /view_attendance or /reset_attendance."
    )

async def attendance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Please enter your matric number (e.g., 240591123):")
    context.user_data["awaiting_attendance"] = True

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    user_data = context.user_data

    if user_data.get("awaiting_attendance"):
        pattern = r"^240591\d{3}$"
        if not re.match(pattern, text):
            await update.message.reply_text("❌ Invalid matric number format. Try: 240591123")
            return

        if text in attendance_list:
            await update.message.reply_text("✅ Attendance already marked.")
        else:
            attendance_list.add(text)
            save_attendance(attendance_list)
            await update.message.reply_text("✅ Your attendance has been marked!")

        user_data["awaiting_attendance"] = False
    else:
        await update.message.reply_text("❓ Please use /attendance to begin.")

async def view_attendance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_USER_ID:
        await update.message.reply_text("🚫 You are not authorized to view attendance.")
        return

    if not attendance_list:
        await update.message.reply_text("📋 Attendance list is currently empty.")
    else:
        entries = "\n".join(sorted(attendance_list))
        await update.message.reply_text(f"📋 Attendance List:\n{entries}")

async def reset_attendance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_USER_ID:
        await update.message.reply_text("🚫 You are not authorized to reset attendance.")
        return

    attendance_list.clear()
    save_attendance(attendance_list)
    await update.message.reply_text("✅ Attendance list has been cleared.")

# === Main Bot Setup ===
def main():
    bot_token = "7718408832:AAGlkAWcfLQJbuNnwa8xHUbKD4TmfhMfrZE"
    app = ApplicationBuilder().token(bot_token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("attendance", attendance))
    app.add_handler(CommandHandler("view_attendance", view_attendance))
    app.add_handler(CommandHandler("reset_attendance", reset_attendance))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
