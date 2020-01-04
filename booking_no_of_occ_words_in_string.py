'''
https://www.careercup.com/question?id=5730652642082816

Given a stream of characters (e.g. acacabcatghhellomvnsdb) and a list of words (e.g. ["aca","cat","hello","world"] ) 

find and display count of each and every word once the stream ends.(Like : "aca" : 2 , "cat" : 1 , "hello" : 1 , "world" : 0 ).

Solution by litcode
'''

from collections import defaultdict

def getWordsCount(stream, words):
	map_char_positions = defaultdict(set)
	for index,char in enumerate(stream):
		map_char_positions[char].add(index)

	map_word_count = {}
	stream_length = len(stream)-1
	for word in words:
		first_char = word[0]
		if first_char in map_char_positions:
			positions   = map_char_positions[first_char]
			length_word = len(word)
			count=0
			for position in positions:
				if stream[position:position+length_word] == word and position+length_word-1<=stream_length:
					count+=1
			map_word_count[word]=count
		else:
			map_word_count[word] = 0
	return map_word_count


if __name__ == "__main__":
	print(getWordsCount("acacabcatghhellomvnsdb", ["aca","cat","hello","world"]))