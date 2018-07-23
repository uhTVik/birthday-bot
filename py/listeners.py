import json


with open("config.json") as f:
    config = json.load(f)

def ping(bot, update, args):
    update.message.reply_text("Response!")

def add(bot, update, args):
    
    if update.message.from_user.username in config["admins"]:
        print("test")
        with open(config["db"]) as f:
            db = json.load(f)
        db.append(args)
        with open(config["db"], "w") as f:
            json.dump(db, f)
        update.message.reply_text("Successfully added {}! The birthday is recognized as {}".format(args[0], args[1]))

index = {
    "ping": ping,
    "add": add
}
