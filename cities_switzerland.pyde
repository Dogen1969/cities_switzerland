import csv

# Variable zur Sammlung der Koordinaten wird erstellt
citiesData = None

# Variable für Schrift wird erstellt
font = None

# Funktion zeichnet insgesamt 1256 Punkte(Städte)
# Funktion verwendet die Daten der citiesData-Variable
def setXY(lat, lng):
    x = map(lng, -180, 180, 0, width)
    y = map(lat, 90, -90, 0, height)
    point(x,y)

# Daten werden in setup() geladen
def setup():
    global citiesData, font
    size(900, 600)
    # Schrift wird importiert
    font = createFont("Roboto-Regular.ttf", 32)
    
    # Mit der Python Funktion open() erhalten wir Zugang zur CSV-Datei
    citiesFileHandle = open("cities.csv")
    
    # Das csv.DictReader Objekt gibt für jede Zeile ein Dictionary aus. Damit bekommen wir einen einfacheren Zugang zu den Daten.
    # Die Funktion list() liest alle Zeile auf einmal und speichert die Daten in der Variable "citiesData".
    citiesData = list(csv.DictReader(citiesFileHandle))
    strokeWeight(0.05)
    stroke(255, 0, 0)


def draw():
    background(0, 26, 51)
    
    # Überschrift
    textSize(32)
    text("1.256 Swiss Cities", width/2, height/4)
    
    pushMatrix()
    xoffset = map(mouseX, 0, width, -9100, -8900)
    
    # Mit translate() verschieben wir den Nullpunkt des Rasters
    translate(xoffset, -2600)
         
    # Mit scale() vergrössern wir die Darstellung der Daten
    scale(20)
    
    # Die Daten werden Reihe für Reihe mit der for-Schlaufe auf den Bildschirm gezeichnet.
    for row in citiesData:
        lat = float(row["lat"])
        lng = float(row["lng"])
        setXY(lat, lng)
    popMatrix()

    
