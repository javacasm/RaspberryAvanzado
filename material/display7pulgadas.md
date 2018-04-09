# Pantalla 7"

Vamos a ver cómo conectar una pantalla externa de 7"

![7" display](https://www.waveshare.com/img/devkit/LCD/7inch-HDMI-LCD-C/7inch-HDMI-LCD-C-4.jpg)

## Preparación

Siempre que vamos a modificar temas que afectan a la visualización, lo mejor es preparnos para poder hacer cambios en remoto (por si en algún momento deja de función la visualización)

Para ello activamos al menos el acceso ssh (algo que en cualquier caso siempre es útil) y mejor si activamos el VNC

Si vamos a alimentar la pantalla desde la Raspberry debemos comprobar que la alimentación es suficiente. Estas pantallas suelen consumir casi 1A

## Cambios

Modificamos el fichero /boot/config.txt


    # set current over USB to 1.2A
    max_usb_current=1

    # overscan to adjust image position
    overscan_left=0
    overscan_right=0
    overscan_top=0
    overscan_bottom=0

    # HDMI config
    hdmi_drive=1
    hdmi_ignore_edid=0xa5000080
    hdmi_group=2
    hdmi_mode=87

    # 1024x600 display
    hdmi_cvt=1024 600 60 3 0 0 0


##  Pantallas pequeñas

[Mini Pal Display](https://learn.adafruit.com/using-a-mini-pal-ntsc-display-with-a-raspberry-pi?view=all)

[Test Mini Pal Display](https://learn.adafruit.com/using-a-mini-pal-ntsc-display-with-a-raspberry-pi/configure-and-test)

## Referencias

[Foro](https://www.raspberrypi.org/forums/viewtopic.php?t=163810)

[foro 2](https://www.raspberrypi.org/forums/viewtopic.php?t=121263)

[Foro 3](https://www.raspberrypi.org/forums/viewtopic.php?t=120793)

[Resolución de problemas con el teclado](https://www.raspberrypi.org/documentation/hardware/display/troubleshooting.md)
