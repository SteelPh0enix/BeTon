#!/usr/bin/python3
import time
from BeTon import BeTon
from Elements.Light import Light

if __name__ == "__main__":
	try:
		bot = BeTon(37, 35, 38, 40, 6.3)
		bot.setupRadar(33, 36)
		
		l = Light(11)
		l.blink(5)
		
		while True:
			bot.automove(True)
	except KeyboardInterrupt:
		bot.stop()
