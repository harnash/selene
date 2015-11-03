# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
import string


def rand_str(length, chars=string.ascii_uppercase + string.digits):
    """
    Utility function which generate random string from a given character list

    Args:
        length (int): length of the generated string
        chars (list): list of characters to generate string from

    Returns:
        string: randomly generated string
    """
    return ''.join(random.choice(chars) for _ in range(length))
