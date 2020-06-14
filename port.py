#!/bin/usr/env python

import subprocess


print """\033[1m
                        }-----{+} Coded By Roshan Mavale {+}-----{
                 }--------{+}  Email = rpmavale@gmail.com {+}--------{
                       }-----{+} Contact = 9028360800  {+}-----{
  }-----{+} This Script Can Forward Port With SSH Serveo.net Service  {+}-----{
"""

local_ip = raw_input("Enter Your Local IP > ")
port = raw_input("Enter Port Number > ")

subprocess.call("ssh -R" + port + ":" + local_ip + ":" + port + " serveo.net", shell=True)

