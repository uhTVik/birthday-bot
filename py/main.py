import collections
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def echo(bot, update):
    update.message.reply_text(update.message.text)

def command(bot, update, args):
    update.message.reply_text('Parsed args: ' + (','.join(args)))
    update.message.reply_text('You are {}, by the way'.format(update.effective_user.username))
    update.message.reply_sticker('CAADAgADGAIAAmkSAAJWHyklsyrFUQI')

def main():
    try:
        updater = Updater(open('token').read().strip())
    except:
        print('Ask cromtus for the token ;)')
        return
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("command", command, pass_args=True))

    # # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
