# -*- coding: utf-8 -*-
from slackbot_settings import API_TOKE
from slacker import Slacker

slack = Slacker(API_TOKE)

slack.chat.post_message("#project-飲み会", "今日はさっさと帰って飲みに行こう！",
                        as_user=True)
