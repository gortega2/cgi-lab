#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import cgi
import cgitb
import time
cgitb.enable()
import templates
class FollowingTheTAsInstructionsError(Exception):
    def __init__(self):
        Exception.__init__(self, (
            "You must edit secret.py to change the username, password, "
            "and to delete this error!"
        ))

# Delete this line:
#raise FollowingTheTAsInstructionsError

# Edit the following two lines:
username = "ping"
password = "pong"

