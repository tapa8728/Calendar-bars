import calendar, json

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
		dic[key]["female"] = {}
		dic[key]["male"] ={}

		dic[key]["female"]["no"] = 0
		dic[key]["female"]["yes"] = 0
		dic[key]["female"]["numyes"] = 0
		dic[key]["female"]["total"] = 0

		dic[key]["male"]["no"] = 0
		dic[key]["male"]["yes"] = 0
		dic[key]["male"]["numyes"] = 0
		dic[key]["male"]["total"] = 0
		if gender == "male":
			if had == "No":
				dic[key]["male"]["no"] = dic[key]["male"]["no"] + 1
			elif had == "Yes":
				dic[key]["male"]["yes"] = dic[key]["male"]["yes"] + 1
				dic[key]["male"]["numyes"] = dic[key]["male"]["numyes"] + int(num)
			dic[key]["male"]["total"] = dic[key]["male"]["total"] + 1
		elif gender == "female":
			if had == "No":
				dic[key]["female"]["no"] = dic[key]["female"]["no"] + 1
			elif had == "Yes":
				dic[key]["female"]["yes"] = dic[key]["female"]["yes"] + 1
				dic[key]["female"]["numyes"] = dic[key]["female"]["numyes"] + int(num)
			dic[key]["female"]["total"] = dic[key]["female"]["total"] + 1
			
	else:
		if gender == "male":
			if had == "No":
				dic[key]["male"]["no"] = dic[key]["male"]["no"] + 1
			elif had == "Yes":
				dic[key]["male"]["yes"] = dic[key]["male"]["yes"] + 1
				dic[key]["male"]["numyes"] = dic[key]["male"]["numyes"] + int(num)
			dic[key]["male"]["total"] = dic[key]["male"]["total"] + 1
		elif gender == "female":
			if had == "No":
				dic[key]["female"]["no"] = dic[key]["female"]["no"] + 1
			elif had == "Yes":
				dic[key]["female"]["yes"] = dic[key]["female"]["yes"] + 1
				dic[key]["female"]["numyes"] = dic[key]["female"]["numyes"] + int(num)
			dic[key]["female"]["total"] = dic[key]["female"]["total"] + 1

	if dic[key]["female"]["total"] == 10:
		break

print dic
with open('drinking.json', 'w') as outfile:
    json.dump(dic, outfile)