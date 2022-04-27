import json
from collections import defaultdict
import statistics
import csv
def readfile(filename):
    f = open(filename)
    lines = f.readlines()
    data = []
    for line in lines:
        data.append(json.loads(line))
    return data
user = readfile("testset_user_@_CA.json")
review = readfile("testset_review_@_CA.json")
business = readfile("testset_business_@_CA.json")
thumbUp = defaultdict(int)
sums = defaultdict(list)
counts = defaultdict(int)
means = defaultdict(float)
stds = defaultdict(float)
id2Name = defaultdict(str)
thumbDown = defaultdict(int)
reviewCount = defaultdict(int)
rating = defaultdict(float)
for i in business:
    id2Name[i["business_id"]] = i["name"]
    reviewCount[i["business_id"]] = i["review_count"]
    rating[i["business_id"]] = i["stars"]
for i in review:
    sums[i["user_id"]].append(i["stars"])
    ##counts[i["user_id"]] += 1
for i in user:
    means[i["user_id"]] = statistics.mean(sums[i["user_id"]])
    stds[i["user_id"]] = statistics.pstdev(sums[i["user_id"]])
for i in review:
    if i["stars"] > means[i["user_id"]] + stds[i["user_id"]]:
        thumbUp[i["business_id"]] += 1
    if i["stars"] < means[i["user_id"]] - stds[i["user_id"]]:
        thumbDown[i["business_id"]] += 1
with open('test.csv', 'w') as f:
    for key in id2Name.keys():
        f.write("%s;%d;%d;%d;%f\n"%(id2Name[key],thumbUp[key],thumbDown[key],reviewCount[key],rating[key]))