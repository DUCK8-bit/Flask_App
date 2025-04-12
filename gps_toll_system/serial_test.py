import serial

data = serial.Serial(
                  'COM5',
                  baudrate = 9600,
                  parity=serial.PARITY_NONE,
                  stopbits=serial.STOPBITS_ONE,
                  bytesize=serial.EIGHTBITS,                  
                  timeout=1
                  )

def getdata():
    lat = None
    long = None
    print('Start........')
    while True:
        d = data.readline()
        d = d.decode('utf-8', 'ignore')
        d = d.strip()
        print('data', d)
        if d:
            if 'Lat' in d:
                lat = float(d.replace('Lat:', ''))
            
            if 'Long' in d:
                long = float(d.replace('Long:', ''))
            
            if lat and long:
                break
    return lat, long
