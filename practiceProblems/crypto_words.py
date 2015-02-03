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
        else:
            crypto_pairs.append(pair)
        pair[1] = 1
	return crypto_pair

if __name__ == "__main__":
	ordered_word("zmaap")