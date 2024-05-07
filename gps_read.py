import microstacknode.hardware.gps.l80gps

gps = microstacknode.hardware.gps.l80gps.L80GPS()

while True:
  data = gps.get_gpgga()
  print('lat: ',data['latitude'])
  print('lon: ', data['longitude'])
  print('alt: ', data['altitude'])
  print('utc: ', data['utc'])
  print('-----------------')
  time.sleep(2)
