from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters
from ollama import chat, ChatResponse

async def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text("Welcome! I am your dsss bot. How can I help you today?")

async def process(update: Update, context: CallbackContext) -> None:
    """Process the user message."""
    user_message = update.message.text
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    response: ChatResponse = chat(
            model="llama3.2",
            messages=[{"role": "user", "content": user_message}],
        )
    await update.message.reply_text(response.message.content)

def main() -> None:
    """Start the bot."""
    API_TOKEN = "7709226654:AAGJroInVpvhOdqIhDHlBYiW1bWBqy29yts"

    application = Application.builder().token(API_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process))

    application.run_polling()

if __name__ == "__main__":
    main()
