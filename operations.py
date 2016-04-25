import calendar

f  = open("drinking_answers.txt", "r")
lines  = f.readlines()
dic ={} #key: date; value
for each in lines[1:]:
	m = each.split(",")
	gfgid = m[0]
	gender = m[1]
	year = m[3]
	month= calendar.month_abbr[int(m[4])]
	day = m[5]
	had = m[6]
	num = m[7].replace("\n", "")
	key = year + month + day;
	print "key is ", key
	print "gender:",gender,"year:",year,"month:", month, "day:",day,"had?:", had," #",num
	if key not in dic:
		dic[key] = {}
		dic[key]["gender"] = "null"
		dic[key]["no"] = 0
		dic[key]["yes"] = 0
		dic[key]["numyes"] = 0
		dic[key]["total"] = 0
		if had == "No":
			dic[key]["no"] = dic[key]["no"] + 1
		elif had == "Yes":
			dic[key]["yes"] = dic[key]["yes"] + 1
			dic[key]["numyes"] = dic[key]["numyes"] + int(num)
		dic[key]["total"] = dic[key]["total"] + 1
		dic[key]["gender"] = gender
	else:
		if had == "No":
			dic[key]["no"] = dic[key]["no"] + 1
		elif had == "Yes":
			dic[key]["yes"] = dic[key]["yes"] + 1
			dic[key]["numyes"] = dic[key]["numyes"] + int(num)
		dic[key]["total"] = dic[key]["total"] + 1
		dic[key]["gender"] = gender
	if dic[key]["total"] == 10:
		break

print dic