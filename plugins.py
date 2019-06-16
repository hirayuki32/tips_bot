from slackbot.bot import respond_to
from slackbot.bot import listen_to
from functions.tips_manager import update_tip, read_tips, delete_tip
import re


@respond_to('learn tip(\d*) (.*)')
def learn_tip(message, tip_number, tip_msg):
    channel_id = message.body["channel"]
    update_tip(channel_id, tip_number, tip_msg)
    message.reply('I learned tips{} as {}'.format(tip_number, tip_msg))


@respond_to('show tips')
def show_tips(message):
    channel_id = message.body["channel"]
    tips = read_tips(channel_id)
    message.reply(tips, in_thread=True)


@respond_to('delete tip(\d*)')
def forget_tip(message, tip_number):
    channel_id = message.body["channel"]
    deleted_tip = delete_tip(channel_id, tip_number)
    if deleted_tip is None:
        message.reply('No tip was found for the number.')
        return
    message.reply('I deleted tip{}: {}'.format(tip_number, deleted_tip))
