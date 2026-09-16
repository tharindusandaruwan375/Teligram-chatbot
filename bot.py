from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"  # BotFather ගෙන් ලැබුණු Token එක

# 1. ඔයාගේ User ID එක (මෙන්න මෙතැනට ඔයාගේ ID එක දැම්මා)
OWNER_ID = 7600273207  

# 2. Access එක සල්ලි දීලා ගත්ත අයගේ User IDs (පස්සේ සල්ලි දෙන අයගේ IDs මෙතනට එකතු කරන්න)
ALLOWED_USERS = []

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    # Owner (ඔයා) හෝ Access Buy කරපු අයදැයි Check කිරීම
    if user_id == OWNER_ID or user_id in ALLOWED_USERS:
        await update.message.reply_text("✅ සාදරයෙන් පිළිගන්නවා! ඔයාට Bot ගේ සියලුම සේවාවන් නොමිලේ පාවිච්චි කරන්න පුළුවන්.")
    else:
        # වෙන කෙනෙක් ආවොත් යන Message එක
        await update.message.reply_text(
            "❌ කණගාටුයි! ඔයාට මේ Bot පාවිච්චි කරන්න Access නැත.\n\n"
            "💳 මේ Bot පාවිච්චි කිරීමට Premium Access ලබාගැනීමට Owner ව සම්බන්ධ කරගන්න: @KingX_OFFIAL"
        )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    # Access නැති අය එවන Messages වලට Response නොදී Block කිරීම
    if user_id != OWNER_ID and user_id not in ALLOWED_USERS:
        await update.message.reply_text("⛔ කරුණාකර Access ලබාගැනීමට Buy කරන්න.")
        return

    # Access තියෙන අයට විතරක් Bot වැඩ කරයි
    user_text = update.message.text
    await update.message.reply_text(f"🤖 Bot Response: {user_text}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    
    print("Bot is running securely for KingX...")
    app.run_polling()
