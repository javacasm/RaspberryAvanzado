import time
import I2C_LCD_driver
mylcd = I2C_LCD_driver.lcd()

while True:
    mylcd.lcd_display_string(u"TEXTO PARPADEANTE")
    mylcd.backlight(1)
    time.sleep(1)
    mylcd.lcd_clear()
    mylcd.backlight(0)
    time.sleep(1)
