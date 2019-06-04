from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re


@respond_to('learn tips(.*) (.*)')
def learn_tip(message, tip_number, tip_msg):
    message.reply('I learned tips{} as {}'.format(tip_number, tip_msg))
