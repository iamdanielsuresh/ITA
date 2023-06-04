#!/usr/bin/env python3

def to_seconds(hours,minutes,seconds):
	return hours*3600 + minutes*60+seconds
print("Welcome to time converter")
cont= "y"
while(cont.lower() == "y"):
	hours = int(input("Enter the number of hours : "))
	minutes = int(input("Enter seconds : " ))
	seconds = int(input("Enter the numbwe of seconds : "))
	
	print("Thats  {} seconds". format(to_seconds(hours,minutes,seconds)))
	print()
	cont = input("Do you want to continue ?[y/n] ")
print("Good bie")

