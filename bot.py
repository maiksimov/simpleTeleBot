from misc import *
import telebot
import time
import sys

bot = telebot.TeleBot(BOT_TOKEN)


def send_message_by_channel_name(message):
    result = bot.send_message(CHANNEL_NAME, message)
    time.sleep(1)
    return result


def send_message_by_chat_id(id, message):
    result = bot.send_message(chat_id=id, text=message)
    time.sleep(1)
    return result


def main():
    message = sys.argv[1] if len(sys.argv) > 1 else "test message"
    bot.config['api_key'] = BOT_TOKEN
    print(send_message_by_chat_id(CHAT_ID, message))


if __name__ == '__main__':
    main()
