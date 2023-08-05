#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#
# This application is an example on how to use aioblescan 
# 
# Copyright (c) 2017 François Wautier
#
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies
# or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR 
# IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE
import sys
import asyncio
import argparse
import aioblescan as aiobs

parser = argparse.ArgumentParser(description="Track BLE advertised packets")
parser.add_argument("-e", "--eddy", action='store_true', default=False,
                    help="Look specificaly for Eddystone messages.")
parser.add_argument("-r","--ruuvi", action='store_true', default=False,
                    help="Look only for Ruuvi tag Weather station messages")
try:
    opts = parser.parse_args()
except Exception as e:
    parser.error("Error: " + str(e))
    sys.exit()

def my_process(data):
    global opts

    ev=aiobs.HCI_Event()
    xx=ev.decode(data)
    if opts.eddy:
        xx=aiobs.EddyStone(ev)
        if xx:
            print("Google Beacon {}".format(xx))
    elif opts.ruuvi:
        xx=aiobs.RuuviWeather(ev)
        if xx:
            print("Weather info {}".format(xx))
    else:
        ev.show(0)
    
try:
    mydev=int(sys.argv[1])
except:
    mydev=0


event_loop = asyncio.get_event_loop()

#First create and configure a raw socket
mysocket = aiobs.create_bt_socket(mydev)

#create a connection with the raw socket
fac=event_loop.create_connection(aiobs.BLEScanRequester,sock=mysocket)
#Start it
conn,btctrl = event_loop.run_until_complete(fac)
#Attach your processing 
btctrl.process=my_process
#Probe
btctrl.request()
try:
    # event_loop.run_until_complete(coro)
    event_loop.run_forever()
except KeyboardInterrupt:
    print('keyboard interrupt')
finally:
    print('closing event loop')
    conn.close()
    event_loop.close()
