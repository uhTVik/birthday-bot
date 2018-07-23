from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import listeners

def main():
    try:
        updater = Updater(open('token').read().strip())
    except:
        print('Ask cromtus for the token ;)')
        return
    dp = updater.dispatcher

    for command, handler in listeners.index.items():
        dp.add_handler(CommandHandler(command, handler, pass_args=True))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
