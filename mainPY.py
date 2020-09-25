#old runFIRST.py file here
import requests
import datetime
import calendar
url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
r = requests.get(url, allow_redirects=True)
open('local_copy.log', 'wb').write(r.content)
#old runFIRST.py file here

with open("local_copy.log") as infile:
    data = infile.readlines()

# this loop is to include all requests with " [" 724411
count = 0
thylist = [] #the list of every log in the file
for line in data:
    if " [" in line:
        count += 1
        thylist.append(line)
print ("The amount of requests put in for the entirety of the log file: ", count) # prints how ma$

# this loop is to include all requests with " [" and "1995"
count = 0
GET1995 = []
for line in data:
    if " ["and"1995" in line:
        count += 1
        GET1995.append(line)
print ("The amount of requests put in for the year 1995: ",count) # prints how many requests ther$

#selecting only the date in each item in thylist
DOWlist = [] #the list only conatining the dates of the logs
for item in thylist:
    start = item.find(" [") +2
    end = start + 11
    dates = (item[start:end])
    DOWlist.append(dates)
#print (DOWlist)

#counting total logs Mons through Suns
weekbig = [0,0,0,0,0,0,0] #teh list adding every log per day ex; weekbig[0] = 234587
for item in DOWlist:
    idgit = '1234567890'
    if item[0] not in idgit:
        continue
    born = datetime.datetime.strptime(item,'%d/%b/%Y').weekday()
    weekbig[born] += 1
#print (weekbig)

#edit DOWlist to eliminate duplicate items
singular = [] # list of dates but no duplicates
for item in DOWlist:
    if item not in singular:
        singular.append(item)
#print (singular)

#counting how many Mons thorugh Suns in between start and end date
startdate = datetime.datetime.strptime(DOWlist[0],'%d/%b/%Y')
enddate = datetime.datetime.strptime(DOWlist[-1],'%d/%b/%Y')
week = [0,0,0,0,0,0,0] # the list of how many weeks between oct24/1994 and oct11/1995. adding how$
for item in singular:
    day = datetime.datetime.strptime(item,'%d/%b/%Y').weekday()
    week[day] += 1
    #print (day)
#print (week)

#dividing to find average per day and printing results
day = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"] # this list is obv$
for indx in range(len(week)):
    print ("Average of",(day[indx]),(weekbig[indx]/week[indx]))

#putting all mondays dates in a list using start/end dates from earlier
MONdates = [] # has date of every MOnday between start/end date
datecount = startdate
while datecount < enddate:
    MONdates.append(datecount)
    datecount = datecount + datetime.timedelta(days=7)
#print (MONdates)

#counting all logs per week
logPweek = [] # has counts of logs per week
for mon in MONdates:
    count = 0
    for dow in DOWlist:
        if datetime.datetime.strptime(dow,'%d/%b/%Y') >= mon and datetime.datetime.strptime(dow,'$
            count += 1
        if datetime.datetime.strptime(dow,'%d/%b/%Y') >= mon+datetime.timedelta(days=7):
            break
    logPweek.append(count)
#print (logPweek)

#printing each weeks data
for index in range(len(logPweek)):
    print ("Requests in week",MONdates[index].strftime("%d/%b/%Y"),":",logPweek[index])

monthdate = [] # has date of every first of the month between start/end date
datecount = startdate
while datecount < enddate:
    datecount = datecount.replace(day=1)
    monthdate.append(datecount)
    datecount = datecount + datetime.timedelta(days=32)
#print (monthdate)

#counting all logs per week
logPmonth = [] # has counts of logs per month
for index in range(len(monthdate)):
    count = 0
    tempend = monthdate[index] + datetime.timedelta(days=32)
    for dow in DOWlist:
        if datetime.datetime.strptime(dow,'%d/%b/%Y') >= monthdate[index] and datetime.datetime.s$
            count += 1
        if datetime.datetime.strptime(dow,'%d/%b/%Y') >= tempend.replace(day=1):
            break
    logPmonth.append(count)
#print (logPmonth)

#printing each monts data
for index in range(len(logPmonth)):
    print ("Requests in Month",monthdate[index].strftime("%b/%Y"),":",logPmonth[index])

#puts status codes in a list
numcode = [] #is list of all status codes
for item in thylist:
    if '" ' in item:
        start = item.find('" ') +2
    else:
        start = item.find("index.html")+11
    nums = (item[start:])
    if nums[0] not in idgit:   #dound line of log with ' " ' so these extra if statements before $
        if len(nums) > 12:
            nums = nums[10:]
        else:
            continue
    numcode.append(nums)
#print (numcode)

#counts all 4xx and 3xx requsts and calculates average
hugenum = len(thylist)
count4xx = count3xx = 0
float(count4xx)
float(count3xx)
for code in numcode:
    if code[0] == '4':
        count4xx += 1.0
    if code[0] == '3':
        count3xx += 1.0
c4 = ((count4xx/hugenum)*100)
c3 = ((count3xx/hugenum)*100)
print ("Percentage of requests were unsuccessful: %.2f" % round(c4,2))
print ("Percentage of requests were redirected elsewhere: %.2f" % round(c3,2))

#puts files in a list
files = [] #puts all files into list
GGfiles = [] #filters out 6 bad files
for item in thylist:
    start = item.find('] "')+3
    end = item.find('" ')
    ONE = (item[start:end])
    files.append(ONE)
for item in files:
    if "GET" in item or "get" in item:
        ggONE = (item[4:])
        GGfiles.append(ggONE)
    elif "HEAD" in item or "POST" in item:
        ggONE = (item[5:])
        GGfiles.append(ggONE)
    elif len(item) > 6:
        GGfiles.append(item)

#making dictionary to keep track of what files are requested (key) and how many times they are re$
filecount = {}
for item in GGfiles:
    if item in filecount:
        filecount[item] += 1
    else:
        filecount[item] = 1

#printing pairs in dicitonary
filemost = max(filecount, key=filecount.get)
fileleast = min(filecount, key=filecount.get)
print ("The most requested file", filemost)
print ("The least requested file", fileleast)
