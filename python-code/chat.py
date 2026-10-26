import random as rand

def token(string):
	txt = string.lower().split(" ")
	out = []
	for i in txt:
		if i == "hello" or i == "hi" :
			out.append(1)
		elif i == "bye" or i == "goodbye" or i == "good bye" :
			out.append(2)
		elif i == "how" or i == "what" or i == "when" or i == "why" or i == "where":
			out.append(3)
		elif i == "you" or i == "bot" or i == "your" or i == "yourself":
			out.append(4)
		elif i == "me" or i == "i" or i == "myself":
			out.append(5)
		elif i == "good" or i == "great" or i == "ok" or i == "okay":
			out.append(6)
		elif i == "bad" or i == "horrible":
			out.append(7)
		else :
			out.append(0)
	return(out)

wordList = [
	[""],
	["Hi.", "Hello.", "How are You?"],
	["See you later.", "Goodbye.", "Comeback soon."]
]

#WIP WIP take list of words into list of what responces needed then generate responces WIP WIP
def condense(array):
	txt = array
	out = []
	for i in txt:
		out.append(wordList[int(i)][rand.randint(0,len(wordList[int(i)]))])
	print("".join(out))

isChatting = True

print("Hello, I am ChatterBot")

while isChatting == True:

	condense(token(input()))

