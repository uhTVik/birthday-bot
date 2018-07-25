import json
import time
import util

with open("config.json") as f:
    config = json.load(f)

def ping(bot, update, args):
    update.message.reply_text("Response!")

def add_admin(bot, update, args):
    if update.message.from_user.username in config["admins"]:
        with open("config.json") as f:
            db = json.load(f)
        db["admins"].append(args[0])
        with open(config["db"], "w") as f:
            json.dump(db, f)
        update.message.reply_text("Successfully added {} to admins!".format(args[0]))


def add(bot, update, args):
    if update.message.from_user.username in config["admins"]:
        with open(config["db"]) as f:
            db = json.load(f)
        if util.invalid(args):
            update.message.reply_text(
                "Invalid arguments =( We use the following format: '/add @ivanov_ivan Ivan Ivanov 1111.11.11" )
        else:
            db.append(args)
            with open(config["db"], "w") as f:
                json.dump(db, f)
            update.message.reply_text("Successfully added {}! The birthday is recognized as {}".format(args[0], args[1]))

def notify(bot, update, args):
    waiting_time  =15 #in seconds
    while True:
        with open(config["db"]) as f:
            db = json.load(f)
        str_db = ""
        for name, data in db:
            str_db =  str_db + name + ": " + data + "\n"
        bot.sendMessage(chat_id='@cromtuschannel', text=str_db)
        time.sleep(waiting_time)

#def listen(bot, update, args):


index = {
    "ping": ping,
    "add": add,
    "add_admin": add_admin,
    "notify": notify,
    #"listen": listen
}

