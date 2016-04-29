#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (linuxfish@domob.cn)
#########################################################################
# Created Time: 2016-04-29 07:38:02
# File Name: server.py
# Description: server side
#########################################################################

from gevent.server import StreamServer
from gevent import socket

from utils import send, receive


def handle_echo(socket, address):
    expression = receive(socket, 'request')
    print 'Got one task from client: %s' % expression
    result = calculate(expression)
    send(socket, result, 'response')
    socket.close()

def calculate(e):
    ops = []
    vals = []
    for c in e:
        if c == '(':
            pass
        elif c == '+':
            ops.append(c)
        elif c == '-':
            ops.append(c)
        elif c == '*':
            ops.append(c)
        elif c == '/':
            ops.append(c)
        elif c == ')':
            op = ops.pop()
            v = vals.pop()
            if op == '+':
                v = vals.pop() + v
            elif op == '-':
                v = vals.pop() - v
            elif op == '*':
                v = vals.pop() * v
            elif op == '/':
                v = vals.pop() / v;
            vals.append(v)
        else:
            vals.append(int(c))
    return vals.pop()


server = StreamServer(('127.0.0.1', 12000), handle_echo)
server.serve_forever()
