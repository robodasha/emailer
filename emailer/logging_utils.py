"""
Utilities for logging
"""

import math

__author__ = 'robodasha'
__email__ = 'damirah@live.com'


def how_often(total, update_freq=100):
    """
    :param total: how many items in total have to be processed
    :param update_freq: default is 100, that is -- update every 1%
    :return: number denoting after how many items should progress be updated
    """
    return math.ceil(total / update_freq)


def get_progress(processed, total):
    """
    Based on how many items were processed and how many items are there in total
    return string representing progress (e.g. "Progress: 54%")
    :param processed: number of already processed items
    :param total: total number of items to be processed
    :return: string with current progress
    """
    progress = processed / total * 100
    return "Progress: %.2f%%" % round(progress, 2)
