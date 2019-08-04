import random
import math
import csv

centers = [
  {
    "lat": 18.464815,
    "long": 73.796439
  },
  {
    "lat": 18.507762,
    "long": 73.798775
  },
  {
    "lat": 18.52517,
    "long": 73.779009
  },
  {
    "lat": 18.56792,
    "long": 73.770989
  },
  {
    "lat": 18.556043,
    "long": 73.812341
  },
  {
    "lat": 18.683466,
    "long": 73.731081
  },
  {
    "lat": 18.665461,
    "long": 73.808566
  },
  {
    "lat": 18.565205,
    "long": 73.911494
  },
  {
    "lat": 18.529224,
    "long": 73.860415
  },
  {
    "lat": 18.435227,
    "long": 73.889246
  },
  {
    "lat": 18.50861,
    "long": 73.934341
  },
  {
    "lat": 18.635565,
    "long": 73.843959
  },
  {
    "lat": 18.606168,
    "long": 73.874991
  },
  {
    "lat": 18.599301,
    "long": 73.927049
  },
  {
    "lat": 18.59913,
    "long": 73.737242
  }
]

societies = [15,28]
societiesId = []

with open("societies_latlong.csv", mode='w') as csvFile:
    csvFileWriter = csv.writer(csvFile, delimiter=',')
    csvFileWriter.writerow(["society_id", "lat", "long", "area"])

def readSocieties():
  with open("societies_of_selected_society.csv") as csvFile:
    csvFileRead = csv.reader(csvFile)
    for row in csvFileRead:
      societiesId.append(int(row[0]))

def generateLatLong(lat, lon, radius, societies, societiesCovered, pod):
  radius = (radius*1000)/111300
  with open("societies_latlong.csv", mode='a+') as csvFile:
    csvFileWriter = csv.writer(csvFile, delimiter=',')
    for i in range(societies):
      randomU = random.random()
      randomV = random.random()
      w = radius * math.sqrt(randomU)
      t = 2 * math.pi * randomV
      x = w * math.cos(t)
      y1 = w * math.sin(t)
      x1 = x / math.cos(lat)
      newLat = lat + y1
      newLong = lon + x1
      csvFileWriter.writerow([societiesId[societiesCovered], newLat, newLong, pod])
      societiesCovered += 1
      if societiesCovered == (len(societiesId)):
        break
  return societiesCovered


readSocieties()

societiesCovered = 0
for i in range(len(centers)):
  location = centers[i]
  societiesCovered = generateLatLong(location["lat"], location["long"], 2.5, random.randrange(societies[0], societies[1]), societiesCovered, i)
  if societiesCovered == len(societiesId):
    break

