from machine import UART, Pin

blue = UART (1,9600)
led = Pin(25, Pin.OUT)

while True:
	msg = blue.readline()
	if "on" in msg:
		led.value(1)
		blue.write("Led encendido\r\n")
	elif "off" in msg:
		led.value(0)
		blue.write("Led apagado\r\n")
	else:
		blue.write("Comando desconocido\r\n")
