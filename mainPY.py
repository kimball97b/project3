#old runFIRST.py file here
import requests

url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
r = requests.get(url, allow_redirects=True)

open('local_copy.log', 'wb').write(r.content)
#old runFIRST.py file here



with open("local_copy.log") as infile:
    data = infile.readlines()

#count = data.count("GET")  didnt work but could be useful

#initialize lists
GETlist = []
GET_list = []
GET1995 = []


# this loop is to include all requests with "GET" 724413
count = 0

for line in data:
    if "GET" in line:
        count += 1
        GETlist.append(line)

#print (count) # prints how many requests there are with "GET"



# this loop is to include all requests with "GET " 724411
count = 0

for line in data:
    if "GET " in line:
        count += 1
        GET_list.append(line)

print ("The amount of requests out in for the entirety of the log file: ", count) # prints how many requests there are with "GET "



#print ("\"GET")  making sure "GET is serachable in file. update: Didnt need that.

#searching "GET" and "GET " is coming up with two different answers. Adding some more code to find out why.

#result = []

#for line in GETlist:
#    if line not in GET_list:
#        result.append(line)

#print (result)



# this loop is to include all requests with "GET " and "1995"
count = 0

for line in data:
    if "GET "and"1995" in line:
        count += 1
        GET1995.append(line)

print ("The amount of requests put in for the year 1995: ",count) # prints how many requests there are with "GET " and "1995"
