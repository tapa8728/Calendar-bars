import calendar

f  = open("drinking_answers.txt", "r")
lines  = f.readlines()
dic ={} #key: date; value
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
	if key not in dic:
		dic[key] = {}
		dic[key]["no"] = 0
		dic[key]["yes"] = 0
		dic[key]["numyes"] = 0
		dic[key]["total"] = 0
		if had == "No":
			dic[key]["no"] = dic[key]["no"] + 1
		elif had == "Yes":
			dic[key]["yes"] = dic[key]["yes"] + 1
			dic[key]["numyes"] = dic[key]["numyes"] + num
		dic[key]["total"] = dic[key]["total"] + 1
	break

print dic