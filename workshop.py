from utime import sleep, ticks_ms
from machine import UART, Pin
from rak3172 import RAK3172
from sps30 import SPS30


def main():
  rf_verbinding = UART(0, baudrate=9600)
  sensor_verbinding = UART(1, tx=Pin(4), rx=Pin(5), baudrate=115200)

  rf = RAK3172(rf_verbinding)
  sensor = SPS30(sensor_verbinding)

  print("Serie nummer: " + sensor.serie_nummer())

  print("Verbinding maken")
  if not rf.verbind("70B3D57ED0049AAB", "0000000000000000", "1D7A8E7408DF809B5E86FB2C342759DC"):
    print("Niet verbonden...")
  print("Verbonden!")

  laatste_zending = 0
  while True:
    sleep(1)
    sensor.start()
    meting = sensor.meting()
    if meting is None:
      print("Meting gefaald!")
      continue
    print(f"Meting PM2.5: {meting[1]}")
    if ticks_ms() - laatste_zending > 20000:
      laatste_zending = ticks_ms()
      rf.zend(str(meting[1]))


main()
