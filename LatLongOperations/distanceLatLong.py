import geopy.distance

def getDistance(lat1, long1, lat2, long2):
  return geopy.distance.distance((lat1, long1), (lat2, long2)).km

print(getDistance(18.485727604082577,73.80228928075138,18.46922613027476,73.80325967648821))