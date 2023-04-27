import random as rd

NAMES = open('names.txt', 'r')  #Open contents that consists of Names from names.txt
for line in NAMES:
    num = rd.uniform(1,5)       #Generate numbers for GWA
    num = "%.2f"%num            #Generate numbers for GWA
    GWA_NAMES = open('GWA_and_NAME.txt', 'a')
    GWA_NAMES.write(num), GWA_NAMES.write(" "), GWA_NAMES.write(line) #Append contents from names.txt and random GWA.
    

