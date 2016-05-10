from __future__ import division
import datetime, time
from datetime import date, timedelta
import calendar, json, operator
from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

f  = open("drinking_answers.txt", "r")
year_list = []		#keep track of the number of years
lines  = f.readlines()
dic ={} #key: date; value
for each in lines[1:]:
	m = each.split(",")
	gfgid = m[0]
	gender = m[1]
	year = m[3]
	month= m[4]   # calendar.month_abbr[int(m[4])]
	day = m[5]
	had = m[6]
	num = m[7].replace("\n", "")
	# subtract -1 from the date specified
	dt = datetime.date(int(year), int(month), int(day))
	ndt = dt - timedelta(days=1)
	day,  month, year = ndt.day, ndt.month, ndt.year
	if year not in year_list:
		year_list.append(year)
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

	# if dic[key]["female"]["total"] == 20:
	# 	break

'''Generic code for generating JSONs for every year for timeseries graph'''
for eachYear in year_list: 	#[2015, 2016, 2017 ..]
	thisYear = []
	# Special case of year 2015
	if eachYear == 2015:
		start_date = datetime.date(eachYear, 4, 1) #1st April 2015
	else:
		start_date = datetime.date(eachYear, 1, 1) #1st January XYZ
	end_date = datetime.date(eachYear, 12, 31) #31st December XYZ
	# Iterate over the dictionary to extract the data for that particular year
	for k,v in dic.iteritems():
		d = {} #empty dictionary
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
			thisYear.append(d)
		else:
			pass
	# Append blank values to the future days. Done to align the maps efficiently
	if eachYear == 2015:
		# Add blank values from 1st jan to start_date
		for single_date in daterange(date(2015, 1, 1), date(2015, 4, 1)):
			d ={}
			d["date"] = str(single_date)
			d["weekday"] = single_date.strftime("%A")
			d["male"] = 0
			d["female"] = 0
			thisYear.append(d)
	else:
		# Add blank values from tomorrow to end_date
		tomorrow_date = datetime.date.today() + datetime.timedelta(days=1)
		for single_date in daterange(tomorrow_date, end_date):
			d={}
			d["date"] = str(single_date)
			d["weekday"] = single_date.strftime("%A")
			d["male"] = 0
			d["female"] = 0
			thisYear.append(d)
	# Convert the list into JSON file for that year
	thisYear.sort(key=operator.itemgetter('date'))
	fname = "timeseries_"+str(eachYear)+ ".json"
	with open("data/"+fname, 'w') as write:
		json.dump(thisYear, write)
	print  eachYear," has been dumped"
	write.close()
 
