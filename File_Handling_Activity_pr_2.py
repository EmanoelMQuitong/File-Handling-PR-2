#TASK: P-2 (25 points). Write a Python program that read a file containing the name of 20 students together with their GWA. The program will outputs the name of the student who got the highest GWA (including the GWA).

#Write a Python program that read a file containing the name of 20 students together with their GWA.

#The program will outputs the name of the student who got the highest GWA (including the GWA).
GWA_NAMES = list()

#read GWA_and_NAME.txt
filename = 'GWA_and_NAME.txt'
with open(filename) as fn:
    for line in fn:
        GWA_NAMES.append(line)

#Sort
GWA_NAMES.sort()
print(GWA_NAMES)
#Write Sorted contents based on GWA

#Write the GWA and Name with the highest GWA