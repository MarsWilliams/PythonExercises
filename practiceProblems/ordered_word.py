def ordered_word(word):
	l = len(word)
	for i in range(l):
		next = i + 1
		temp = word[next]
		if word[i] < temp:
			if i + 1 < l:
				continue
		else:
			return False
		return true


	

def crypto_words(word):
    l = len(word)
    crypto_pairs = []
    pair = ["", 1]
    for i in range(l):
        pair[0] = word[i]
        nextword = i + 1
        temp = word[next]
        if word[i] == temp:
        	pair[1] += 1
        	if (i + 1) < l:
        		continue
        	else:
			    crypto_pairs.append(pair)
			    pair[1] = 1
			else:
			crypto_pairs.append(pair)
	return crypto_pair

if __name__ == "__main__":
	ordered_word("zmaap")