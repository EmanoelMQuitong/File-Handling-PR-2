#TASK: P-2 (25 points). Write a Python program that read a file containing the name of 20 students together with their GWA. The program will outputs the name of the student who got the highest GWA (including the GWA).

#Write a Python program that read a file containing the name of 20 students together with their GWA.

#The program will outputs the name of the student who got the highest GWA (including the GWA).
GWA_NAMES = list()

#read GWA_and_NAME.txt
filename = 'GWA_and_NAME.txt'
with open(filename) as fn:
    for line in fn:
        GWA_NAMES.append(line.strip())


BLUE = '\033[94m'
DARKCYAN = '\033[36m'
PURPLE = '\033[95m'
GREEN = '\033[92m'
BOLD = '\033[1m'
END = '\033[0m'
#Sort
GWA_NAMES.sort()
print('\n')
print(DARKCYAN +BOLD +"The following names and numbers are the sorted names and General weigthed average with respect to their class performance." + END )
print('\n')
print(GWA_NAMES)
print('\n')

#Write Sorted contents based on GWA
fn2 = 'GWAnNames_sorted.txt'
with open(fn2, 'w') as fs:
    for inp in GWA_NAMES:
        fs.write(inp + '\n')

#Write the GWA and Name with the highest GWA
GWA_position = int(input(GREEN + BOLD + "Which GWA position do you desire to find out? "+ END))
file = open('GWAnNames_sorted.txt', 'r')
lines = file.readlines()
line = lines[GWA_position - 1]
file.close()
print("The student on the"+ PURPLE + BOLD , GWA_position, END + " position is "+ PURPLE + BOLD + line + END)
print(PURPLE +BOLD +"CONGRATULATIONS!!!" + END )

