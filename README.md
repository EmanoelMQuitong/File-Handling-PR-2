# GWA and Names Ranker

<b>Write a Python program that read a file containing the name of 20 students together with their GWA. The program will outputs the name of the student who got the highest GWA (including the GWA).</b>

###

# Program Sequence
+ Create a variable that will serve as list. Leave it blank.
+ Read text file that contains GWA and Names 
+ Sort the contents of the text file.
+ Write the sorted contents based on GWA to a new text file.
+ Write the GWA and names of the desired position from 1 to 20.

###

# Guide
<b>
 Create a variable that will serve as list. Leave it blank.</b>


  ```GWA_NAMES
  GWA_NAMES = list()
  ```
  
<b>
 Read text file that contains GWA and Names </b>


  + Use the variable with a blank list for listing the contents from the file source.
  
  + 'Variable' + '.append()' allows the add the contents of the variable to the opened file.
  
  + '.line strip()' removes unecessary space and additional line of the list.
 
 
  ```
  filename = 'GWA_and_NAME.txt'
    with open(filename) as fn:
      for line in fn:
        GWA_NAMES.append(line.strip())
  ```
  
  
  <b>
 Sort the contents of the text file.</b>

  + 'variable'+'.sort()' enables to sort the contents of the variable/list.
  
  
  ```
  GWA_NAMES.sort()
  ```
  
  
  <b>
 Write the sorted contents based on GWA to a new text file.</b>

  + 'with open('.txt', 'a','r', or 'w' )' + 'as' + 'variable' allows the programmer to open a text file and declare as a variable at the same time.

    + 'a' is used for append function.
    + 'r' is used to read the file.
    + 'w' is used to overwrite the contents of the file.

  + This loop allows the user to create new file called 'GWAnNames_sorted.txt' and write the contents from the previous process per line.


  + '\n' is added to create a new line for the next information to be written.



  ```
  new_file = 'GWAnNames_sorted.txt'
    with open(new_file, 'w') as fs:
      for line in GWA_NAMES:
        fs.write(line + '\n')
  ```
  
  
  <b>
 Write the GWA and names of the desired position from 1 to 20.</b>

  + An input is required to continue the process.(You can immediately declare the input variable as 1 to find the student with highest GWA. However, i made it this way   to be an interactive type of program.)

  
  + 'lines = file.readlines()' allows the user to read the contents per line from the text file.
  
  + 'line = lines[GWA_position - 1]' is used because when listing, it always starts with 0.
  
  
  ```
  GWA_position = int(input("Which GWA position do you desire to find out? "))
  file = open('GWAnNames_sorted.txt', 'r')
  lines = file.readlines()
  line = lines[GWA_position - 1]
  file.close()
  print(line)
  ```
 
