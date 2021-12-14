import time
from ustruct import unpack
from utime import sleep
from machine import UART, Pin


def hexlify(data: bytes, sep: str = "") -> str:
  hexs = []
  for i in data:
    part = hex(i)[2:]
    if len(part) == 1:
      part = "0" + part
    hexs.append(part)
  return sep.join(hexs)


def stuff(data: bytes) -> bytes:
  unstuffed = bytearray(data)
  stuffed = bytearray()
  ix = 0
  while ix < len(unstuffed):
    b = unstuffed[ix]
    ix += 1
    # if the current byte is one that has to be stuffed, then replace it
    if b == 0x7E:
      stuffed += bytearray([0x7D, 0x5E])
    elif b == 0x7D:
      stuffed += bytearray([0x7D, 0x5D])
    elif b == 0x11:
      stuffed += bytearray([0x7D, 0x31])
    elif b == 0x13:
      stuffed += bytearray([0x7D, 0x33])
    else:
      stuffed.append(b)
  return stuffed


def unstuff(data: bytes) -> bytes:
  stuffed = bytearray(data)
  unstuffed = bytearray()
  ix = 0
  while ix < len(stuffed)-1:
    b = stuffed[ix]
    n = stuffed[ix+1]
    # Is there a "stuffed" indicator
    if b != 0x7D:
      unstuffed.append(b)
      ix += 1
      continue
    # Determine what the original "unstuffed" byte is
    if n == 0x5E:
      unstuffed.append(0x7E)
    elif n == 0x5D:
      unstuffed.append(0x7D)
    elif n == 0x31:
      unstuffed.append(0x11)
    elif n == 0x33:
      unstuffed.append(0x13)
    # We processed the current byte (stuffed indicator) and the next byte
    # so add 2 to the ix
    ix += 2
  return unstuffed


class Frame:
  cmd: int = 0
  data: bytes = b''
  state: int = 0

  def __init__(self, cmd: int = 0, data: bytes = b'') -> None:
    self.cmd = cmd
    self.data = data

  @staticmethod
  def Decode(raw: bytes):
    frame = Frame()
    pretty = unstuff(raw)
    # Addr is pretty[0]
    frame.cmd = pretty[1]
    frame.state = pretty[2]
    l = pretty[3]
    if l > 0:
      frame.data = pretty[4:l+4]
    return frame

  def Encode(self) -> bytes:
    # Build frame
    raw = bytearray([0x00, self.cmd, len(self.data)]) + stuff(self.data)
    return raw

  @staticmethod
  def Read(uart: UART, timeout=200):
    start = time.ticks_ms()
    data = bytearray()
    # Get start of frame
    while True:
      if time.ticks_ms() - start > timeout:
        return None
      SoF = uart.read(1)
      if SoF != None and SoF[0] == 0x7E:
        break
    # read rest
    while True:
      if time.ticks_ms() - start > timeout:
        return None
      # Read a byte
      section = uart.read(1)
      if section == None:
        continue
      if section[0] == 0x7E:
        break
      data.append(section[0])

    # unstuff
    return Frame.Decode(data)

  def Write(self, uart: UART):
    buf = b'\x7E' + self.Encode() + bytes([self.checksum()]) + b'\x7E'
    uart.write(buf)

  def checksum(self) -> int:
    data = self.Encode()
    value = 0
    for i in data:
      value += i
    return (value & 0xff) ^ 0xff

  def __str__(self) -> str:
    return f"Frame(cmd={hex(self.cmd)}, data={hexlify(self.data)}, state={hex(self.state)}, chk={hex(self.checksum())})"


keys = ['MassPM1', 'MassPM2.5', 'MassPM4', 'MassPM10', 'CountPM0.5',
        'CountPM1', 'CountPM2.5', 'CountPM4', 'CountPM10', 'TypSize']


class SPS30:

  def __init__(self, uart: UART, debug: bool = False) -> None:
    self.uart = uart
    self.debug = debug
    self.active = False

  def send_command(self, cmd: int, data: bytes = b''):
    f = Frame(cmd, data)
    f.Write(self.uart)
    if self.debug:
      print("--> " + str(f))
    rec = Frame.Read(self.uart)
    if self.debug:
      print("<-- " + str(rec))
    return rec

  def start(self):
    if self.active:
      return
    frame = self.send_command(0x00, b'\x01\x03')
    self.active = True

  def stop(self):
    frame = self.send_command(0x01)
    self.active = False

  def meting(self):
    if not self.active:
      return None
    # Vraag meetresultaten
    frame = self.send_command(0x03)
    if frame is None:
      return None
    return self._frameToMeasurements(frame)

  def serie_nummer(self):
    frame = self.send_command(0xD0, b'\x03')
    if frame is None:
      return ""
    return frame.data.decode()

  def _frameToMeasurements(self, f: Frame):
    if len(f.data) < 40:
      return None
    values = unpack('!ffffffffff', f.data)
    return list(values)
