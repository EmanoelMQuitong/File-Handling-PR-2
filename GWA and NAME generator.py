#TASK: P-2 (25 points). Write a Python program that read a file containing the name of 20 students together with their GWA. The program will outputs the name of the student who got the highest GWA (including the GWA).

#Write a Python program that read a file containing the name of 20 students together with their GWA.

#The program will outputs the name of the student who got the highest GWA (including the GWA).

#Generate numbers for GWA
import random as rd

NAMES = open('names.txt', 'r')
for line in NAMES:
    num = rd.uniform(1,5) 
    num = "%.2f"%num
    GWA_NAMES = open('GWA_and_NAME.txt', 'a')
    GWA_NAMES.write(num), GWA_NAMES.write(" "), GWA_NAMES.write(line)
    

