#Code made by: u/TheSparkyNator. V 1.1 of Brawl Stars Draft
import random
ABI = int(0)
c = int(0)
l = int(0)
s = int(0)
brawlers = ["None"]
addbackin = ["None"]
maps = ["Skull Creek", "Scorched Stone", "Rockwall Brawl", "Feast or Famine", "Thousand Lakes", "Royal Runway",  "Double Trouble", "Flying Fantasies", "Dune Drift", "Stormy Plains", "Passage", "Hot Point", "Erratic Blocks", "Eye of the Storm"]
addbackin.remove("None")
brawlers.remove("None")
for i in range(2):
    brawlers.append("Shelly")
for i in range(5):
    brawlers.append("Poco")
    brawlers.append("El Primo")
    brawlers.append("Barley")
    #brawlers.append("Rosa")
runcount = int(input("How many Brawlers per player? "))
players = int(input("How many players? "))
includelegends = input("Include Legendaries? Y/N ")
includemyths = input("Include Mythics? Y/N ")
includeepics = input("Include Epics? Y/N ")
includesrs = input("Include Super Rares? Y/N ")
includetroads = input("Include Trophy Road Brawlers (excluding Shelly)? Y/N ")
if includelegends == "Y" or includelegends == "y":
    print(" ")
    brawlers.append("Crow")
    brawlers.append("Spike")
    brawlers.append("Leon")
else:
    pass
if includemyths == "Y" or includemyths == "y":
    for i in range(2):
        brawlers.append("Mortis")
        brawlers.append("Tara")
        brawlers.append("Gene")
else:
    pass
if includeepics == "Y" or includeepics == "y":
    for i in range(3):
        brawlers.append("Piper")
        brawlers.append("Pam")
        brawlers.append("Frank")
else:
    pass
if includesrs == "Y" or includesrs == "y":
    for i in range(4):
        brawlers.append("Rico")
        brawlers.append("Penny")
        brawlers.append("Darryl")
        brawlers.append("Carl")
else:
    pass
if includetroads == "Y" or includetroads == "y":
    for i in range(2):
        brawlers.append("Nita")
        brawlers.append("Colt")
        brawlers.append("Bull")
        brawlers.append("Jessie")
        brawlers.append("Brock")
        brawlers.append("Dynamike")
        brawlers.append("Bo")
else:
    pass
map = random.choice(maps)
print(map)
print(" ")
for i in range(players):
    banned = input("Who do you want to ban? ")
    if banned == "Shelly" or banned == "Nita" or banned == "Colt" or banned == "Bull" or banned == "Jessie" or banned == "Brock" or banned == "Dynamike" or banned == "Bo":
        for i in range(2):
            brawlers.remove(banned)
    if banned == "Poco" or banned == "Barley" or banned == "El Primo" or banned == "Rosa":
        for i in range(5):
            brawlers.remove(banned)
    if banned == "Rico" or banned == "Darryl" or banned == "Penny" or banned == "Carl":
        for i in range(4):
            brawlers.remove(banned)
    if banned == "Piper" or banned == "Pam" or banned == "Frank":
        for i in range(3):
            brawlers.remove(banned)
    if banned == "Mortis" or banned == "Tara" or banned == "Gene":
        for i in range(2):
            brawlers.remove(banned)
    if banned == "Crow" or banned == "Spike" or banned == "Leon":
        brawlers.remove(banned)
    else:
        pass
for i in range(players):
    for i in range(runcount):
        global brawlerdrafted
        brawlerdrafted = random.choice(brawlers)
        print(brawlerdrafted)
        if brawlerdrafted == "Shelly" or brawlerdrafted == "Nita" or brawlerdrafted == "Colt" or brawlerdrafted == "Bull" or brawlerdrafted == "Jessie" or brawlerdrafted == "Brock" or brawlerdrafted == "Dynamike" or brawlerdrafted == "Bo":
            ABI = brawlers.count(brawlerdrafted)
            for i in range(ABI):
                brawlers.remove(brawlerdrafted)
            importante = ABI - 1
            for i in range(importante):
                addbackin.append(brawlerdrafted)
        if brawlerdrafted == "Barley" or brawlerdrafted == "Poco" or brawlerdrafted == "El Primo" or brawlerdrafted == "Rosa":
            ABI = brawlers.count(brawlerdrafted)
            for i in range(ABI):
                brawlers.remove(brawlerdrafted)
            importante = ABI - 1
            for i in range(importante):
                addbackin.append(brawlerdrafted)
        if brawlerdrafted == "Rico" or brawlerdrafted == "Penny" or brawlerdrafted == "Darryl" or brawlerdrafted == "Carl":
            ABI = brawlers.count(brawlerdrafted)
            for i in range(ABI):
                brawlers.remove(brawlerdrafted)
            importante = ABI - 1
            for i in range(importante):
                addbackin.append(brawlerdrafted)
        if brawlerdrafted == "Piper" or brawlerdrafted == "Pam" or brawlerdrafted == "Frank":
            ABI = brawlers.count(brawlerdrafted)
            for i in range(ABI):
                brawlers.remove(brawlerdrafted)
            importante = ABI - 1
            for i in range(importante):
                addbackin.append(brawlerdrafted)
        if brawlerdrafted == "Mortis" or brawlerdrafted == "Tara" or brawlerdrafted == "Gene":
            ABI = brawlers.count(brawlerdrafted)
            for i in range(ABI):
                brawlers.remove(brawlerdrafted)
            importante = ABI - 1
            for i in range(importante):
                addbackin.append(brawlerdrafted)
        if brawlerdrafted == "Crow" or brawlerdrafted == "Spike" or brawlerdrafted == "Leon":
            ABI = brawlers.count(brawlerdrafted)
            if brawlerdrafted == "Crow":
                s = brawlers.count("Spike")
                for i in range(s):
                    brawlers.remove("Spike")
                    addbackin.append("Spike")
                l = brawlers.count("Leon")
                for i in range(l):
                    brawlers.remove("Leon")
                    addbackin.append("Leon")
            elif brawlerdrafted == "Spike":
                c = brawlers.count("Crow")
                for i in range(c):
                    brawlers.remove("Crow")
                    addbackin.append("Crow")
                l = brawlers.count("Leon")
                for i in range(l):
                    brawlers.remove("Leon")
                    addbackin.append("Leon")
            elif brawlerdrafted == "Leon":
                c = brawlers.count("Crow")
                for i in range(c):
                    brawlers.remove("Crow")
                    addbackin.append("Crow")
                s = brawlers.count("Spike")
                for i in range(s):
                    brawlers.remove("Spike")
                    addbackin.append("Spike")
            brawlers.remove(brawlerdrafted)
            importante = ABI - 1
            for i in range(importante):
                addbackin.append(brawlerdrafted)
    print("-------")
    brawlers.extend(addbackin)
    addbackin.clear()