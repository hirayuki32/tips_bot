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
        tips_data = json.load(tips_file)

    tips_data[tip_number] = tip
    print(tips_data)

    with open(tips_path, "w") as tips_file:
        json.dump(tips_data, tips_file, ensure_ascii=False)
