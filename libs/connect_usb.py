from threading import Thread
from time import sleep
import requests
import serial

usb_ports = ('/dev/ttyUSB0', '/dev/ttyUSB1')


class usb(Thread):
    def __init__(self):
        super().__init__()

    def run(self, lodge_memeber=None):
        while 1:

            index = 0
            for usb in usb_ports:
                try:
                    arduino = serial.Serial(usb, 9600)
                    print('Connected to arduio at ' + usb)
                    while 1:
                        try:

                            lodge_memeber = []

                            while index < 4:
                                index = index + 1
                                output = arduino.readlines(1)

                                result = str(output[0])[2:-3]
                                lodge_memeber.append(result)

                            index = 0

                            name = lodge_memeber[1].strip() + ' ' + lodge_memeber[2].strip()

                            requests.post("http://localhost:8080/webhook",
                                          data={'membernumber': lodge_memeber[0].strip(),
                                                'name': name, 'lodge': lodge_memeber[3]})

                            [i for i in lodge_memeber if i != 2]

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
