#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (linuxfish@domob.cn)
#########################################################################
# Created Time: 2016-04-29 17:10:41
# File Name: utils.py
# Description: helper functions
#########################################################################

import struct

import calculator_pb2

def send(socket, data, send_type):
    data_type = None
    if send_type == 'request':
        data_type = calculator_pb2.Request()
        data_type.expression = data
    elif send_type == 'response':
        data_type = calculator_pb2.Response()
        data_type.val = data
    serial_data = data_type.SerializeToString()
    socket.send(struct.pack("H", len(serial_data)))
    socket.send(serial_data)

def receive(socket, res_type):
    data_type = None
    data_to_read = struct.unpack("H", socket.recv(2))[0]
    serial_data = socket.recv(data_to_read)
    if serial_data:
        if res_type == 'request':
            data_type = calculator_pb2.Request()
            data_type.ParseFromString(serial_data)
            return data_type.expression
        elif res_type == 'response':
            data_type = calculator_pb2.Response()
            data_type.ParseFromString(serial_data)
            return data_type.val
