from time import ticks_ms
from machine import UART


def hexlify(data: bytes, sep: str = "") -> str:
    hexs = []
    for i in data:
        part = hex(i)[2:]
        if len(part) == 1:
            part = "0" + part
        hexs.append(part)
    return sep.join(hexs)


RETURN_CODES = (
    "OK",
    "AT_BUSY_ERROR",
    "AT_NO_NETWORK_JOINED",
    "AT_PARAM_ERROR",
    "AT_ERROR"
)


class RAK3172:

    def __init__(self, uart: UART, debug: bool = False) -> None:
        self.uart = uart
        self.debug = debug

    def command(self, command: str):
        """Stuur een commando naar de RF Module en wacht op een return code"""
        # Prepare variables
        command = command + "\r\n"
        return_data = list()

        # Send command
        self._send_line(command)

        # Read until we receive a valid return code
        while True:
            line = self._read_line()
            if line == None:
                continue
            if self.debug:
                print(f"<<< {line}")
            # If we received a return code then stop
            if line in RETURN_CODES:
                return (return_data, line)
            if line.startswith("+EVT"):
                continue
            # Otherwise append the received data to our responses
            return_data.append(line)

    def verbind(self, dev_eui: str, join_eui: str, app_key: str) -> bool:
        self.command("AT+DR=5")
        self.command("AT+ADR=1")
        # Zet de DEVEUI variabele op de RF Module
        _, status = self.command("AT+DEVEUI=" + dev_eui)
        if not status is "OK":
            return False
        # Zet de APPEUI variabele op de RF Module
        _, status = self.command("AT+APPEUI=" + join_eui)
        if not status is "OK":
            return False
        # Zet de APPKEY variabele op de RF Module
        _, status = self.command("AT+APPKEY=" + app_key)
        if not status is "OK":
            return False
        # Geef het commando om een verbinding te gaan maken
        _, status = self.command("AT+JOIN=1:0:10:8")
        if not status is "OK":
            return False
        # Wacht op het "JOINED" event
        evt = self._wait_for_event()
        if not evt is "JOINED":
            return False
        return True

    def zend(self, msg):
        data = hexlify(str(msg).encode())
        _, status = self.command(f"AT+SEND=1:{data}")

    def _wait_for_event(self, timeout=10000):
        start = ticks_ms()
        while ticks_ms() - start < timeout:
            data = self._read_line()
            if data is None:
                continue
            if not data.startswith("+EVT"):
                continue
            return data[len("+EVT:"):]

    def _read_line(self, timeout=500):
        """Ontvang een bericht via UART"""
        start = ticks_ms()
        msg = ""
        # Dit blijft oneindig herhalen, maar in de functie hebben we manieren om eruit te komen
        while True:
            # Als er meer dan <timeout> milliseconden voorbij zijn, returnen we None (niks)
            if ticks_ms() - start > timeout:
                return None
            # Lees 1 byte
            data = self.uart.read(1)
            # Als de data "None" (niks) is dan slaan we alles over en gaan we terug naar de "while True"
            if data == None:
                continue
            # Als we hier zijn dat moet er data zijn dus dat voegen we toe aan het bericht
            msg = msg + data.decode("utf-8")
            # Nu even kijken of het bericht eindigt op \r\n
            if msg.endswith("\r\n"):
                # Nu halen we alle extra enters en spaties weg
                msg = msg.strip()
                # En als er iets over blijft returnen we dat
                if msg != "":
                    return msg

    def _send_line(self, data: str):
        """Stuur een bericht naar de RF module"""
        if self.debug:
            print(">>> " + data)
        self.uart.write(str.encode(data + "\r\n"))


# while read_line() != None:
#   pass

# # Commando's hier
# response, code = send_command("AT+DEVEUI=?")
# print(f"[{code}] DEVEUI: {response}")

# response, code = send_command("AT+NWM=1")
# print(f"[{code}] AT+NWM: {response}")

# response, code = send_command("AT+NJM=1")
# print(f"[{code}] AT+NJM: {response}")

# response, code = send_command("AT+CLASS=A")
# print(f"[{code}] AT+CLASS: {response}")

# response, code = send_command("AT+BAND=4")
# print(f"[{code}] AT+BAND: {response}")

# response, code = send_command("AT+DEVEUI=70B3D57ED0049AAB")
# print(f"[{code}] AT+DEVEUI: {response}")
# response, code = send_command("AT+APPEUI=0000000000000000")
# print(f"[{code}] AT+APPEUI: {response}")
# response, code = send_command("AT+APPKEY=1D7A8E7408DF809B5E86FB2C342759DC")
# print(f"[{code}] AT+APPKEY: {response}")

# response, code = send_command("AT+JOIN=1:0:10:8")
# print(f"[{code}] JOIN: {response}")
