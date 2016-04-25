import calendar

f  = open("drinking_answers.txt", "r")
lines  = f.readlines()

for each in lines[1:]:
	m = each.split(",")
	gfgid = m[0]
	year = m[1]
	month= calendar.month_abbr[int(m[2])]
	day = m[3]
	had = m[4]
	num = m[5].replace("\n", "")
	key = year + month + day;
	print "key is ", key
	print "year:",year,"month:", month, "day:",day,"had?:", had," #",num
	break