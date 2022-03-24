# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/Flare_Robot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID =  16575130 # integer value, dont use ""
    API_HASH = " a3da19f8b34b5916e151d06b792f7798"
    TOKEN = " 5287424511:AAHViuto-wpB3yhSjbHla12-CpYDN1aXcrA"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 5053846242 # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "Asta_Silva_02"
    DB_URI = postgresql://nygjqrud:zMvTtzR7NbbOui7397UqYZ4knZXMxnsu@castor.db.elephantsql.com/nygjqrud # use your db
    SUPPORT_CHAT = "Marin_Support"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001671750109 
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001671750109 
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = " postgres://zksjznbd:E9c7y6cwnpGQdQkTGB2q05nzsLinffbt@jelani.db.elephantsql.com/zksjznbd"  # needed for any database modules # its "URI" and not "URL" as herok and similar ones only accept it as such
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "tA5nqHFn9gjAKqnawhsuw0so9_z1BJ4uog4fB65h2r_L68rWHqqKT63ofObVBgmR"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = "CAACAgUAAxkBAAIDf2IY_5yQsaQrIl82_Dh-IeZNdJFpAALKAgACCHoxVdWKVeuiIreCIwQ"  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "4K5NXNGAJW9RP21Y"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "1WNTS9XB1BRV"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
