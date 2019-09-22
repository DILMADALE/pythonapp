import json

data = json.load(open("data.json"))

print(type(data))

def translate(word):
	if word in data:
		return data[word]
	else:
		return "This is not a correct word, please check the word again"

word = input("Enter Word: ")

print(translate(word))



#print(data)

