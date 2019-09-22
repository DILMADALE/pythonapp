import json
from difflib import get_close_matches

data = json.load(open("data.json"))

print(type(data))

def translate(word):
	word = word.lower()
	if word in data:
		return data[word]
	elif get_close_matches(word, data.keys(), cutoff=0.8):
		replaceword = get_close_matches(word, data.keys(), cutoff=0.8)[0]
		print("Were you thinking about following word: ", replaceword)
		return data[replaceword]
	else:
		return "This is not a correct word, please check the word again"
		


word = input("Enter Word: ")

print(translate(word))



#print(data)

