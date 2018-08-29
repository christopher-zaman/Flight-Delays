import csv
import matplotlib.pyplot as plt

class Flight:
    orig = ""
    dest = ""
    depDelay = 0
    arrDelay = 0
    dist = 0

# open file
file = open("airline_delays.csv")

# create a csv reader object from the file
rows = csv.reader(file)

# skip the first row -- the column headers
next(rows)

flights = []

# go through each row in the file
for col in rows:
    
    if col[0] == "" or col[1] == "" or col[2] == ""  or col[3] == "" or col[4] == "":  
        continue;
        
    f = Flight()    
    f.orig = col[0] 
    f.dest = col[1]
    f.depDelay = int(col[2])
    f.arrDelay= int(col[3])
    f.dist = int(col[4])

    flights.append(f)

def GetAirportList(flights):
    airportList = []

    for f in flights:
        if f.orig not in airportList:
            airportList.append(f.orig)
    
    return airportList


def OnTimeRecord(airport, flights):
    ontimeCount = 0    
    totalCount = 0    

    for f in flights:
        if f.orig == airport:
            totalCount = totalCount + 1
            if f.depDelay == 0:
                ontimeCount = ontimeCount + 1
    
    percentOnTime = ontimeCount / float(totalCount)
    
    return percentOnTime

def DelaysByAirport(flights):
    airport = input("What is the airport code? ")

    percentOnTime = OnTimeRecord(airport, flights)
    percentDelayed = 1.0 - percentOnTime
    
    print("Ontime : " + str(percentOnTime * 100))
    print("Delayed: " + str(percentDelayed * 100))
    
    
def BestAndWorst(flights):
    airports = GetAirportList(flights)
    
    bestRec = 0.0
    bestRecAirport = "UKNOWN"
    
    worstRec = 1.1
    worstRecAirport = "UKNOWN"
    
    for airport in airports:
        percentageOnTime = OnTimeRecord(airport, flights)
        if percentageOnTime > bestRec:
            bestRec = percentageOnTime
            bestRecAirport = airport
        
        if percentageOnTime < worstRec:
            worstRec = percentageOnTime
            worstRecAirport = airport
        
    print ("Best airport is " + bestRecAirport + " " + str(bestRec))    
    print ("Worst airport is " + worstRecAirport + " " + str(worstRec))    
    
def OnTimeDistCorr(flights):
    return 0

while True:
    print("")
    print("Welcome to AirDelay 1.0")    
    print("=======================")    
    print("1- Delays By Airport")    
    print("2- Best and Worst Airports")    
    print("3- Ontime/Distance Correlation")    
    print("0- Exit")
    choice = int(input("What do you want to do (0-3)? "))
    
    if choice == 1:
        DelaysByAirport(flights)
    elif choice == 2:
        BestAndWorst(flights)
    elif choice == 3:
        OnTimeDistCorr(flights)
    elif choice == 0:
        break
                
        
    
    
    








