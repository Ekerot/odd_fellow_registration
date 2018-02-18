import re
from time import sleep
from .has_numbers import has_numbers
import serial
from .write_to_goole_sheet import getresult

usb_ports = ('/dev/ttyACM0', '/dev/ttyACM1')


def start_usb():
    index = 2
    while 1:
        for usb in usb_ports:
            try:
                arduino = serial.Serial(usb, 9600)
                print('Connected to arduio at ' + usb)
                while 1:
                    try:
                        output = arduino.readlines(1)

                        print(output)

                        result = str(output[0])[2:-3]

                        flag = has_numbers(result)

                        if flag:
                            number = re.findall("\d+", str(result))
                            name = result.replace(str(number[0]), '')
                            getresult(number[0], name, index)

                            index = index + 1

                    except KeyboardInterrupt:
                        exit()
                    except serial.SerialException:
                        print('Lost connection. Trying to reconnect...')
                        break
                    except IOError:
                        print('IOError...')
                        pass
            except serial.SerialException:
                print('Arduino not found at ' + usb)
                pass
        sleep(10)