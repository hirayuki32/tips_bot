import json
import os
from pathlib import Path


def _touch_tips_if_not_exist(tips_path):
    """
    If it is the first time that you to mamage tips,
    create a new json named by channel_id
    """
    is_exists = os.path.exists(tips_path.format(tips_path))
    if is_exists:
        return
    with open(tips_path, "w") as tips_file:
        tips_file.write("{}")


def update_tips(channel_id, tip_number, tip):
    """
    Parameters
    ----------
    channel_id : str
    tip_number : integer
    tip : str
    """
    tips_path = "tips/{}.json".format(channel_id)
    _touch_tips_if_not_exist(tips_path)

    with open(tips_path, "r") as tips_file:
        tips_json = json.load(tips_file)

    tips_json[tip_number] = tip  # set tip

    with open(tips_path, "w") as tips_file:
        json.dump(tips_json, tips_file, ensure_ascii=False)


def read_tips(channel_id):
    """
    Parameters
    ----------
    channel_id : str
    """
    tips_path = "tips/{}.json".format(channel_id)
    is_exists = os.path.exists(tips_path.format(tips_path))
    if not is_exists:
        return "まだtipsはありません。"

    with open(tips_path, "r") as tips_file:
        tips_json = json.load(tips_file)
    tips = json.dumps(tips_json, ensure_ascii=False, indent=2, sort_keys=True)
    return tips
