#!/usr/bin/env python
"""

Copyright (c) 2009  Kevin Dunglas <dunglas@gmail.com>
"""

import os
import sys

sys.path.append(os.path.join(sys.path[0], '..', 'twittytwister'))
sys.path.append('twittytwister')

from twisted.internet import reactor

import twitter
from oauth import oauth

def gotUser(u):
    print "Got a user: %s" % u

consumer = oauth.OAuthConsumer(sys.argv[1], sys.argv[2])
token = oauth.OAuthToken(sys.argv[3], sys.argv[4])

twitter.Twitter(consumer=consumer, token=token).show_user(sys.argv[5]).addCallback(
    gotUser).addBoth(lambda x: reactor.stop())

reactor.run()
