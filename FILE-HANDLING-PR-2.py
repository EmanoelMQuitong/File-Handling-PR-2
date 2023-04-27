#TASK: P-2 (25 points). Write a Python program that read a file containing the name of 20 students together with their GWA. The program will outputs the name of the student who got the highest GWA (including the GWA).

#Write a Python program that read a file containing the name of 20 students together with their GWA.

#The program will outputs the name of the student who got the highest GWA (including the GWA).

#Generate numbers for GWA
import random as rd
def gwa(num):
    for i in range(20):
        num = rd.uniform(1.00,5.00)
        print("%.2f" % num)
    return num
