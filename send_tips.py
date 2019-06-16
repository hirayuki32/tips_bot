# -*- coding: utf-8 -*-
from slackbot_settings import API_TOKEN
from functions.tips_manager import choose_randomly_from_tips
from slacker import Slacker

slack = Slacker(API_TOKEN)


def get_channel_id_from_name(channel_name):
    channel_id = None  # default
    raw_data = slack.channels.list().body
    channels_info = raw_data["channels"]
    for channel_info in channels_info:
        if channel_name == channel_info["name"]:
            channel_id = channel_info["id"]
            break
    return channel_id


def send_tip(channel_name):
    channel_id = get_channel_id_from_name(channel_name)
    tip = choose_randomly_from_tips(channel_id)
    slack.chat.post_message(channel_name, tip,
                            as_user=True)

send_tip()
