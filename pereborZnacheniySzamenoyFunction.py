def emoji_aa(text):
	splitWords = text.split(' ')
	output = ""
	
	emojiDist = {
		":)": "😀",
		":(": "🙁"
	}
	
	for word in splitWords:
		output += emojiDist.get(word,word) + " "
	return(output)
