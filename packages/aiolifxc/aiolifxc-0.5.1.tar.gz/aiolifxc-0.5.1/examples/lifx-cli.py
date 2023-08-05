#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#
# This application is an example on how to use aiolifx 
# 
# Copyright (c) 2016 François Wautier
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
import asyncio as aio
import aiolifx as alix
from functools import partial

from aiolifx.aiolifx import DeviceOffline

UDP_BROADCAST_PORT = 56700

#Simple bulb control frpm console
class bulbs():
    """ A simple class with a register and  unregister methods
    """
    def __init__(self):
        self.bulbs=[]
        self.boi=None #bulb of interest
        
    def register(self,bulb):
        loop = aio.get_event_loop()
        loop.create_task(bulb.get_metadata(loop=loop))
        self.bulbs.append(bulb)

    def unregister(self,bulb):
        idx=0
        for x in list([ y.mac_addr for y in self.bulbs]):
            if x == bulb.mac_addr:
                del(self.bulbs[idx])
                break
            idx+=1


def readin():
    """Reading from stdin and displaying menu"""

    selection = sys.stdin.readline().strip("\n")
    loop = aio.get_event_loop()
    loop.create_task(readin_process(selection))


async def readin_process(selection):
    MyBulbs.bulbs.sort(key=lambda x: x.label or x.mac_addr)
    lov=[ x for x in selection.split(" ") if x != ""]
    if lov:
        if MyBulbs.boi:
            #try:
            if True:
                if int(lov[0]) == 0:
                    MyBulbs.boi=None
                elif int(lov[0]) == 1:
                    if len(lov) >1:
                        try:
                            await MyBulbs.boi.set_power(lov[1].lower() in ["1","on","true"])
                            MyBulbs.boi = None
                        except DeviceOffline:
                            print("Error: Device is offline")
                    else:
                        print("Error: For power you must indicate on or off\n")
                elif int(lov[0]) == 2:
                    if len(lov) >2:
                        try:
                            await MyBulbs.boi.set_color([58275,0,
                                    int(round((float(lov[1])*65365.0)/100.0)),
                                    int(round(float(lov[2])))])
                            
                            MyBulbs.boi=None
                        except DeviceOffline:
                            print("Error: Device is offline")
                        except (IndexError, ValueError):
                            print("Error: For white brightness (0-100) and temperature (2500-9000) must be numbers.\n")
                    else:
                        print("Error: For white you must indicate brightness (0-100) and temperature (2500-9000)\n")
                elif int(lov[0]) == 3:
                    if len(lov) >3:
                        try:
                            await MyBulbs.boi.set_color([int(round((float(lov[1])*65535.0)/360.0)),
                                    int(round((float(lov[2])*65535.0)/100.0)),
                                    int(round((float(lov[3])*65535.0)/100.0)),3500])
                            MyBulbs.boi=None
                        except DeviceOffline:
                            print("Error: Device is offline")
                        except (IndexError, ValueError):
                            print("Error: For colour hue (0-360), saturation (0-100) and brightness (0-100)) must be numbers.\n")
                    else:
                        print("Error: For colour you must indicate hue (0-360), saturation (0-100) and brightness (0-100))\n")
                        
                elif int(lov[0]) == 4: 
                    print(MyBulbs.boi.device_characteristics_str("    "))
                    print(MyBulbs.boi.device_product_str("    "))
                    MyBulbs.boi=None
                elif int(lov[0]) == 5: 
                    print(MyBulbs.boi.device_firmware_str("   "))
                    MyBulbs.boi=None
                elif int(lov[0]) == 6: 
                    resp = await MyBulbs.boi.get_wifiinfo()
                    print(MyBulbs.boi.device_radio_str(resp))
                    MyBulbs.boi=None
                elif int(lov[0]) == 7: 
                    resp = await MyBulbs.boi.get_hostinfo()
                    print(MyBulbs.boi.device_time_str(resp))
                    MyBulbs.boi=None
                elif int(lov[0]) == 8: 
                    if len(lov) >3:
                        try:
                            print ( "Sending {}".format([int(round((float(lov[1])*65535.0)/360.0)),
                                    int(round((float(lov[2])*65535.0)/100.0)),
                                    int(round((float(lov[3])*65535.0)/100.0)),3500]))
                            await MyBulbs.boi.set_waveform({"color":[int(round((float(lov[1])*65535.0)/360.0)),
                                                               int(round((float(lov[2])*65535.0)/100.0)),
                                                               int(round((float(lov[3])*65535.0)/100.0)),
                                                               3500],
                                                      "transient":1, "period":100, "cycles":30,
                                                      "duty_cycle":0,"waveform":0})
                            MyBulbs.boi=None
                        except DeviceOffline:
                            print("Error: Device is offline")
                        except (IndexError, ValueError):
                            print("Error: For pulse hue (0-360), saturation (0-100) and brightness (0-100)) must be numbers.\n")
                    else:
                        print("Error: For pulse you must indicate hue (0-360), saturation (0-100) and brightness (0-100))\n")
            #except:
                #print ("\nError: Selection must be a number.\n")  
        else:
            try:
                if int(lov[0]) > 0:
                    if int(lov[0]) <=len(MyBulbs.bulbs):
                        MyBulbs.boi=MyBulbs.bulbs[int(lov[0])-1]
                    else:
                        print("\nError: Not a valid selection.\n")
            
            except:
                print ("\nError: Selection must be a number.\n")
        
    if MyBulbs.boi:
        print("Select Function for {}:".format(MyBulbs.boi.label))
        print("\t[1]\tPower (0 or 1)")
        print("\t[2]\tWhite (Brigthness Temperature)")
        print("\t[3]\tColour (Hue Saturation Value)")
        print("\t[4]\tInfo")
        print("\t[5]\tFirmware")
        print("\t[6]\tWifi")
        print("\t[7]\tUptime")
        print("\t[8]\tPulse")
        print("")
        print("\t[0]\tBack to bulb selection")
    else:
        idx=1
        print("Select Bulb:")
        for x in MyBulbs.bulbs:
            print("\t[{}]\t{}".format(idx,x.label or x.mac_addr))
            idx+=1
    print("")
    print("Your choice: ", end='',flush=True)
  


MyBulbs= bulbs()
loop = aio.get_event_loop()
coro = loop.create_datagram_endpoint(
            partial(alix.LifxDiscovery,loop, MyBulbs), local_addr=('0.0.0.0', UDP_BROADCAST_PORT))
try:
    loop.add_reader(sys.stdin,readin)
    server = loop.create_task(coro)
    print("Hit \"Enter\" to start")
    print("Use Ctrl-C to quit")
    loop.run_forever()
except:
    pass
finally:
    server.cancel()
    loop.remove_reader(sys.stdin)
    loop.close()