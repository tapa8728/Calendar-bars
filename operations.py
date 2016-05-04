from __future__ import division
import datetime, time
from datetime import date, timedelta
import calendar, json, operator



f  = open("drinking_answers.txt", "r")
lines  = f.readlines()
dic ={} #key: date; value
for each in lines[1:]:
	m = each.split(",")
	gfgid = m[0]
	gender = m[1]
	year = m[3]
	month= m[4]   #calendar.month_abbr[int(m[4])]
	day = m[5]
	had = m[6]
	num = m[7].replace("\n", "")
	# subtract -1 from the date specified
	dt = datetime.date(int(year), int(month), int(day))
	ndt = dt - timedelta(days=1)
	day,  month, year = ndt.day, ndt.month, ndt.year
	key = str(year) +"-"+ "%02d" % month +"-"+ "%02d" % day;
	# print "key is ", key
	# print "gender:",gender,"year:",year,"month:", month, "day:",day,"had?:", had," #",num
	if key not in dic:
		dic[key] = {}
		dic[key]["female"] = {}
		dic[key]["male"] ={}
		dic[key]["day"] = day
		dic[key]["month"] = month
		dic[key]["year"] = year

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
				dic[key]["male"]["no"]+= 1
			elif had == "Yes":
				dic[key]["male"]["yes"] += 1
				dic[key]["male"]["numyes"]+= int(num)
			dic[key]["male"]["total"]+= 1
		elif gender == "female":
			if had == "No":
				dic[key]["female"]["no"] += 1
			elif had == "Yes":
				dic[key]["female"]["yes"]+= 1
				dic[key]["female"]["numyes"]+= int(num)
			dic[key]["female"]["total"]+= 1

	else:
		if gender == "male":
			if had == "No":
				dic[key]["male"]["no"]+= 1
			elif had == "Yes":
				dic[key]["male"]["yes"]+= 1
				dic[key]["male"]["numyes"]+= int(num)
			dic[key]["male"]["total"] += 1
		elif gender == "female":
			if had == "No":
				dic[key]["female"]["no"]+= 1
			elif had == "Yes":
				dic[key]["female"]["yes"]+= 1
				dic[key]["female"]["numyes"]+= int(num)
			dic[key]["female"]["total"]+= 1

	# if dic[key]["female"]["total"] == 5:
	# 	exit()

#print dic
# with open('drinking.json', 'w') as outfile:
#     json.dump(dic, outfile)

# list of dictionaries
# drinkinglist =[]
# for k,v in dic.iteritems():
# 	d = {}
# 	if v["month"] == "Oct": #for October
# 		d["day"] = int(v["day"])
# 		d["male"] = round(v["male"]["numyes"]/v["male"]["total"], 2)
# 		d["female"] = round(v["female"]["numyes"]/v["female"]["total"], 2)
# 		drinkinglist.append(d)

# drinkinglist.sort(key=operator.itemgetter('day'))
# with open('Oct_drinking.json', 'w') as outfile2:
#     json.dump(drinkinglist, outfile2)

'''For timeseries graph'''
timeseries2015 =[]
start_date = datetime.date(2015, 4,1)	#1st Jan 2015
curr_date = datetime.today()
end_date = datetime.date(2015, 12,31)	#31st Dec 2015
for k,v in dic.iteritems():
	d = {} #empty dictionary
	# print "key :: ", k
	# print "value ::", v
	ans = datetime.date(int(v['year']), int(v['month']), int(v['day']))
	if ans >= start_date and ans <= curr_date :
		d["date"] = k
		d["weekday"] = ans.strftime("%A")
		if v["male"]["total"] == 0:
			d["male"] = 0
		else:
			d["male"] = round(v["male"]["numyes"]/float(v["male"]["total"]), 2)
		if v["female"]["total"] == 0:
			d["female"] = 0
		else:
			d["female"] = round(v["female"]["numyes"]/float(v["female"]["total"]), 2)
		timeseries2015.append(d)
	else if ans > curr_date and ans <= end_date:
		
		pass

timeseries2016 =[]
start_date = datetime.date(2016, 1,1)	#1st Jan 2015
end_date = datetime.date(2016, 12,31)	#31st Dec 2015
for k,v in dic.iteritems():
	d = {} #empty dictionary
	# print "key :: ", k
	# print "value ::", v
	ans = datetime.date(int(v['year']), int(v['month']), int(v['day']))
	if ans >= start_date and ans <= end_date :
		d["date"] = k
		d["weekday"] = ans.strftime("%A")
		if v["male"]["total"] == 0:
			d["male"] = 0
		else:
			d["male"] = round(v["male"]["numyes"]/float(v["male"]["total"]), 2)
		if v["female"]["total"] == 0:
			d["female"] = 0
		else:
			d["female"] = round(v["female"]["numyes"]/float(v["female"]["total"]), 2)
		timeseries2016.append(d)
	else:
		pass
# print timeseries_list


timeseries2015.sort(key=operator.itemgetter('date'))
with open('timeseries_2015.json', 'w') as outfile3:
    json.dump(timeseries2015, outfile3)
print "2015 dumped"
timeseries2016.sort(key=operator.itemgetter('date'))
with open('timeseries_2016.json', 'w') as outfile4:
    json.dump(timeseries2016, outfile4)
print "2016 dumped"
