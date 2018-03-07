#!/usr/bin/env python

import smbus
import time
import curses

# 2014-08-26 PCF8591-x.py

# Connect Pi 3V3 - VCC, Ground - Ground, SDA - SDA, SCL - SCL.

# ./PCF8591-x.py

bus = smbus.SMBus(1)

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

aout = 0

stdscr.addstr(10, 0, "Brightness")
stdscr.addstr(12, 0, "Temperature")
stdscr.addstr(14, 0, "AOUT->AIN2")
stdscr.addstr(16, 0, "Resistor")

stdscr.nodelay(1)

try:

   while True:

      for a in range(0,4):
         aout = aout + 1
         bus.write_byte_data(0x48,0x40 | ((a+1) & 0x03), aout)
         v = bus.read_byte(0x48)
         hashes = v / 4
         spaces = 64 - hashes
         stdscr.addstr(10+a*2, 12, str(v) + ' ')
         stdscr.addstr(10+a*2, 16, '#' * hashes + ' ' * spaces )

      stdscr.refresh()
      time.sleep(0.04)

      c = stdscr.getch()

      if c != curses.ERR:
         break

except:
   pass

curses.nocbreak()
curses.echo()
curses.endwin()
