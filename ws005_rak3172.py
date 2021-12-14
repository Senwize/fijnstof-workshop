from machine import UART
# Gebruik ook de RAK3172 functionaliteit
from rak3172 import RAK3172

# We gebruiken de standaarden UART0 pinnen en configuratie
# dat is pin 0 en 1 met een baudrate van 9600
verbinding = UART(0)
# Maak een object dat de RAK3172 module representeert
# dit object beheerd de communicatie naar de module en
# helpt om met handige functies zoals "verbind" en "zend"
radio = RAK3172(verbinding)

print("Verbinding maken")
successful = radio.verbind("70B3D57ED0049AAB", "0000000000000000",
                       "1D7A8E7408DF809B5E86FB2C342759DC")
if not successful:
  print("Verbinding niet gelukt!")
else:
  print("Verbinding gelukt!")
  radio.zend("Hallo wereld!")
