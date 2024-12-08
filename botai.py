from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import openai

# Set up OpenAI API key
openai.api_key = "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"

# Define a function to handle messages
def handle_message(update, context):
    user_message = update.message.text
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )
    bot_reply = response["choices"][0]["message"]["content"]
    update.message.reply_text(bot_reply)

# Start the bot
def main():
    # Replace '7953171345:AAFRLn4ML2u07HtcmC3aW5e_LuRcKLk5h_c' with your token from BotFather
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN", use_context=True)
    dp = updater.dispatcher

    # Add handlers
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()