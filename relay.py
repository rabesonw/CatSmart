import time
import grovepi

class Relay(object):
    # Connect the Grove Relay to digital port D4
    # SIG,NC,VCC,GND

    def __init__(self):
        self.relay = 4
        grovepi.pinMode(self.relay,"OUTPUT")

    def relay(self):
        while True:
            try:
                if True:
                    grovepi.digitalWrite(self.relay,1)
                else:
                    grovepi.digitalWrite(self.relay,0)
                    time.sleep(.05)
            except KeyboardInterrupt:
                grovepi.digitalWrite(self.relay,0)
                break
            except IOError:
                print "Error"

    def on(self):
        try:
            grovepi.digitalWrite(self.relay, 1)
            print("Relay on")
        except KeyboardInterrupt:
            grovepi.digitalWrite(self.relay,0)
            # break
        except IOError:
            print "Error"

    def off(self):
        try:
            grovepi.digitalWrite(self.relay, 0)
            print("Relay off")
        except KeyboardInterrupt:
            grovepi.digitalWrite(self.relay,0)
            # break
        except IOError:
            print "Error"