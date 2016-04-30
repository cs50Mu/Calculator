#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (linuxfish@domob.cn)
#########################################################################
# Created Time: 2016-04-29 08:07:39
# File Name: client.py
# Description: client side
#########################################################################

import sys
from gevent import socket

from utils import send, receive


class Client(object):
    def __init__(self, message):
        self.address = ('127.0.0.1', 12000)
        self.message = message.strip()
        self.socket = socket.socket(type=socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect(self.address)

    def run(self):
        print 'connecting...'
        self.connect()
        print 'sending messages...'
        send(self.socket, self.message, 'request')
        res = receive(self.socket, 'response')
        print res

if __name__ == '__main__':
    req = sys.argv[1]
    client = Client(req)
    client.run()
