from misc import *
import telebot
import time

URL = 'https://api.telegram.org/bot' + BOT_TOKEN + '/'

bot = telebot.TeleBot(BOT_TOKEN)


def send_message_by_channel_name(message):
    result = bot.send_message(chat_id=CHAT_ID, text=message)
    time.sleep(1)
    return result


def send_message_by_chat_id(id, message):
    result = bot.send_message(chat_id=id, text=message)
    time.sleep(1)
    return result


def main():
    print(send_message_by_chat_id(CHAT_ID, 'test Message from local'))


if __name__ == '__main__':
    main()
