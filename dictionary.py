import json

data = json.load(open("data.json"))

print(type(data))

def translate(word):
	return data[word]

word = input("Enter Word: ")

print(translate(word))



#print(data)

