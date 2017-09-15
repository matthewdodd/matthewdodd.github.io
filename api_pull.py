import sys
from opencage.geocoder import OpenCageGeocode

key = '<insert key here>'
geocoder = OpenCageGeocode(key)
infilepath = 'places_2.txt'
o = open('out.txt', 'w')

try: 
  with open(infilepath,'r') as f:
    for line in f:
      address = line.strip()
      query = address;
      result = geocoder.geocode(query)

      if result and len(result):
        longitude = result[0]['geometry']['lng']
        latitude  = result[0]["geometry"]["lat"]
        z = "%f;%f;%s" % (latitude, longitude, query)
        print z
        print >> o.write(z)
      else:
        sys.stderr.write("not found: %s\n" % query)
  o.close()
except IOError:
  print("Error: File does not appear to exist.")