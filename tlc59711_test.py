import board
import busio
import digitalio
import adafruit_tlc59711
spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI)
tlc59711 = adafruit_tlc59711.TLC59711(spi)

tlc59711[3] = (65535, 0, 0)

tlc59711[3] = (0, 32767, 32767)

tlc59711.r3 = 65535

tlc59711.red_brightness = 63

