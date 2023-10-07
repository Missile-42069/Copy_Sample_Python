#! /usr/bin/python3

x = input("input a number: ")

number = int(x)
if number <= 1000:
	print("now we will make this as the limit of the list \n")
	number += 1
	
	number_list = []
	odd_number_list = []
	even_number_list = []

	for i in range(0,number):
		number_list.append(i)
	for j in range(1,number,2):
		odd_number_list.append(j)
	for k in range(0,number,2):
		even_number_list.append(k)

	print("this is the list of the numbers from 0 to the number you provided: \n")
	print(number_list,"\n")
	print("this is the list of odd numbers in the range you provided: \n ")
	print(odd_number_list,'\n')
	print("this is the number of even numbers in the range you provided: \n")
	print(even_number_list,'\n')
else:
	print("The number is too large, I fear I cannot display it")
