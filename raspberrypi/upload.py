import serial
from datetime import datetime

import httplib2
import sys

from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials


def main(argv):
    port = "/dev/ttyACM0"
    serialFromArduino = serial.Serial(port, 9600)
    serialFromArduino.flushInput()

    with open('privatekey.p12', 'rb') as f:
        key = f.read()

    credentials = SignedJwtAssertionCredentials(
        '618992491847@developer.gserviceaccount.com',
        key,
        scope='https://www.googleapis.com/auth/fusiontables')

    http = httplib2.Http()
    http = credentials.authorize(http)

    service = build("fusiontables", "v1", http=http)

    while True:
        if (serialFromArduino.inWaiting() > 0):
            sensorvalue = serialFromArduino.readline()
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            request = service.query()\
                .sql(sql="INSERT INTO "
                     "19U4FNVX7eHvq6Icah7izGEZwJzZ8ofupZNutb0M "
                     "(Date, Light) VALUES ('"+now+"', "+str(sensorvalue)+")")
            request.execute()

            line = now+'\t'+sensorvalue
            print(line)

if __name__ == '__main__':
    main(sys.argv)
