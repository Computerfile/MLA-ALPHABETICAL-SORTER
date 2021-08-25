from os import listdir
from os.path import isfile, join
import csv

PATH = '.\sorting MLA sources'

files = [f for f in listdir(PATH) if isfile(join(PATH, f))]

csv_files_folder = []
print(f"{files}")

for f in files:
    print(f"{f[-4:len(f)]}")
    if(f[-4:len(f)] == '.csv'):
        csv_files_folder.append(f)

if(len(csv_files_folder) > 1):
    print("please choose a number for the correct csv file\n")
    for i in csv_files_folder:
        print(f'{str(csv_files_folder.index(i))}) {i} \n')

    choice = input("\n") 
    file = [int(word) for word in choice if word.isdigit()]

    if(len(file) > 1):
        print("More than 1 number detected please retry input")
        exit()
    
    file = csv_files_folder[file[0]]

else:
    file = csv_files_folder[0]


print(f'{file}')

#This section is incomplete check documentation for csv
with open(join(PATH, file), newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = '\t')
    line_count = 0
    for row in csv_reader:
        print(f'{row}\t')    

exit()

"""

    Alternative to get number from input

    NOTE: this code is purelly to avoid typos and missclicks, however givving a higher/different number than requested will still return an error

    for word in choice:
        if(word.isdigit()):
            choice = word

"""