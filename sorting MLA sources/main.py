import os
import csv


files = [f for f in os.listdir('.') if os.path.isfile(f)]
csv_files_folder = []


for f in files:
    if(f[-4:len(f)] == ".csv"):
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
with open(file) as csv_file:
    csv_reader = csv_reader(csv_file, delimiter = '\t')
    line_count = 0
    

"""
    Alternative to get number from input

    NOTE: this code is purelly to avoid typos and missclicks, however givving a higher/different number than requested will still return an error

    for word in choice:
        if(word.isdigit()):
            choice = word

"""