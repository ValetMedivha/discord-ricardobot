import json

with open('data.json') as infile:
	data = json.load(infile)
rating = []
for user in data["dicks"]:
	rating.append([user, data["dicks"][user][0]])

rating.sort(key=lambda x: x[1], reverse=True)

print(rating)