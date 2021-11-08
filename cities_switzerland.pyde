import csv

citiesData = None

def setup():
    global citiesData
    size(900, 600)
    citiesFileHandle = open("cities.csv")
    citiesData = list(csv.DictReader(citiesFileHandle))
    strokeWeight(0.1)
    stroke(255)
    
def draw():
    background(0, 26, 51)
    xoffset = map(mouseX, 0, width, -width*5.5, -width*5.2)
    print xoffset
    translate(xoffset, -1400)
    scale(12)
    
    for row in citiesData:
        lat = float(row["lat"])
        lng = float(row["lng"])
        setXY(lat, lng)

def setXY(lat, lng):
    x = map(lng, -180, 180, 0, width)
    y = map(lat, 90, -90, 0, height)
    point(x,y)
