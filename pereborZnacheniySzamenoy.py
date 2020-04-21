user_input = input(">")
splitWords = user_input.split(' ')
output = ""

emojiDist = {
	":)": "😀",
	":(": "🙁"
}

for word in splitWords:
	output += emojiDist.get(word,word) + " "

print(output)

