# =============================================
# -------- Programa para chip PCF8591  --------
# ---------------------------------------------
# - (c) J.C.G.P. - DIVERTEKA / Webtronika 2013
# =============================================

#!/usr/bin/python
import curses
import smbus
import time

# - Carga de modulo para I2C  -----------------------------------
miADC = smbus.SMBus(1)

# - Rutina de lectura del valor ADC -----------------------------
#   X = canal a leer (1 a 4)
# ---------------------------------------------------------------
def leeINPUT(X):
	# Configuro registro de control para lectura de canal X
	miADC.write_byte_data(0x48, (0x40 + X),X)
	time.sleep(0.2)
	lectura = miADC.read_byte(0x48) # read A/D
	return lectura
# ---------------------------------------------------------------
# ###############################################################
# - PROGRAMA PRINCIPAL --- Usa curses para salida a pantalla ----
# ###############################################################
# ---------------------------------------------------------------
stdscr = curses.initscr()
curses.cbreak()
curses.start_color()
curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
hsize = curses.COLS
vsize = curses.LINES
curses.curs_set(0)
curses.noecho
stdscr.border(0)
stdscr.keypad(1)
stdscr.nodelay(1)
try:
	stdscr.bkgd(curses.color_pair(1))
	while True:  # Rutina principal del programa
		char = stdscr.getch()
		if (char == 81 or char == 113): # Tecla Q/q
			break
		else:
			an1 = leeINPUT(1)
			an2 = leeINPUT(2)
			an3 = leeINPUT(3)
			an4 = leeINPUT(4)
			stdscr.addstr(vsize/6, (hsize/2)-18,"Lecturas analogicas con chip PCF8591")
			nON = an1 / 10
			nOFF = 25 - nON
			stdscr.addstr((vsize/5)+3, (hsize/2)- 28,"Entrada AIN0 (Luz   = " + str(an1).rjust(3) +')  ' +'=' * nON + ' ' * nOFF)
			nON = an2 / 10
			nOFF = 25 - nON
			stdscr.addstr((vsize/5)+5, (hsize/2)- 28,"Entrada AIN1 (Temp. = " + str(an2).rjust(3) +')  ' +'=' * nON + ' ' * nOFF)
			nON = an3 / 10
			nOFF = 25 - nON
			stdscr.addstr((vsize/5)+7, (hsize/2)- 28,"Entrada AIN2 (Libre = " + str(an3).rjust(3) +')  ' +'=' * nON + ' ' * nOFF)
			nON = an4 / 10
			nOFF = 25 - nON
			stdscr.addstr((vsize/5)+9, (hsize/2)- 28,"Entrada AIN3 (Poten.= " + str(an4).rjust(3) +')  ' +'=' * nON + ' ' * nOFF)
			stdscr.addstr(vsize-4, (hsize/2)- 18," Pulsa [Q] para salir")
			stdscr.refresh()
finally:
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()
    curses.endwin()
