def checkplace(place):
	import csv
	import sys

	#input number you want to search
	# number = "petta"

	#read csv, and split on "," the line
	csv_file = csv.reader(open('metro.csv', "r"), delimiter=",")
	# print(csv_file)
	lati=""
	longi=""
	#loop through the csv list
	for row in csv_file:
		# print(row[0])
	    #if current rows 2nd value is equal to input, print that row
	    if place.lower() == row[0].lower():
	         print (row)
	         lati=row[1]
	         longi=row[2]
	return lati,longi