import time
import grovepi

class Moves(object):

    def __init__(self):
        self.pir_sensor = 8 
        grovepi.pinMode(self.pir_sensor,"INPUT")

    def detect(self):
        det = False
        while True:
            try:
                # Sense motion, usually human, within the target range
                if grovepi.digitalRead(self.pir_sensor):
                    print 'motion detected'
                    det = True
                else:
                    print '-'

                # if your hold time is less than this, you might not see as many detections
                time.sleep(.8)

            except IOError:
                print "Error"
        return det