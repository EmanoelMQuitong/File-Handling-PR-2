#TASK: P-2 (25 points). Write a Python program that read a file containing the name of 20 students together with their GWA. The program will outputs the name of the student who got the highest GWA (including the GWA).

#Write a Python program that read a file containing the name of 20 students together with their GWA.

#The program will outputs the name of the student who got the highest GWA (including the GWA).
GWA_NAMES = list()

#read GWA_and_NAME.txt
filename = 'GWA_and_NAME.txt'
with open(filename) as fn:
    for line in fn:
        GWA_NAMES.append(line.strip())

#Sort
GWA_NAMES.sort()
print('\n')
print("The following names and numbers are the sorted names and General weigthed average with respect to their class performance.")
print('\n')
print(GWA_NAMES)
print('\n')

#Write Sorted contents based on GWA
fn2 = 'GWAnNames_sorted.txt'
with open(fn2, 'w') as fs:
    for inp in GWA_NAMES:
        fs.write(inp + '\n')

#Write the GWA and Name with the highest GWA
GWA_position = int(input("Which GWA position do you desire to find out? "))
file = open('GWAnNames_sorted.txt', 'r')
lines = file.readlines()
line = lines[GWA_position - 1]
file.close()
print(line)