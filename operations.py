import operation

f  = open("drinking_answers.txt", "r")
lines  = f.readlines()

for each in lines[1:]:
	m = each.split(",")
	print m
	break