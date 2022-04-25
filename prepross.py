import json
f = open('yelp_academic_dataset_user.json')
lines = f.readlines()
data = []
for line in lines:
    data.append(json.loads(line))
print(len(data))