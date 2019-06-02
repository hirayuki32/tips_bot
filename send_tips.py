# -*- coding: utf-8 -*-
from conf import BOT_API_TOKE
from slacker import Slacker

slack = Slacker(BOT_API_TOKE)

slack.chat.post_message("#project-飲み会", "今日はさっさと帰って飲みに行こう！",
                        as_user=True)
