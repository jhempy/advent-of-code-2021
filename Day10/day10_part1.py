# day10_part1.

import re
import math


def createCompletionString(bad):
	fix = ''
	fixes = {
		'(': ')',
		'[': ']',
		'{': '}',
		'<': '>'
	}
	for b in bad[::-1]:
		fix = fix + fixes[b]
	return fix

def calculateIncompleteScore(bad):
	scores = []
	values = {
		')': 1,
		']': 2,
		'}': 3,
		'>': 4
	}
	for b in bad:
		if (firstIllegal(b) == ''): # no illegals found
			comp = createCompletionString(b)
			score = 0
			for c in comp:
				score = score * 5
				score = score + values[c]
			scores.append(score)
	in_order = sorted(scores)
	print(in_order)
	print(len(in_order))
	print(int(len(in_order)/2))
	middle = in_order[int(len(in_order)/2)]
	return middle


def firstIllegal(line):
	first = '' 
	illegals = [ ')', ']', '}', '>' ]
	for c in line[::-1]:
		if c in illegals:
			first = c
	return first

def calculateIllegalScore(bad):
	total = 0
	values = {
		')': 3,
		']': 57,
		'}': 1197,
		'>': 25137
	}
	for b in bad:
		i = firstIllegal(b)
		if i in values:
			total += values[i]
		# print(b, total)
	return total

def removeAllPairs(line):
	last = line
	current = removePairs(last)
	while current != last:
		last = current
		current = removePairs(last)
	return current;

def removePairs(line):
	pairs = [ '\(\)', '\[\]', '\{\}', '\<\>' ]
	blank = ''
	for p in pairs:
		line = re.sub(p, blank, line)	
	return line

def parse_input_file(file):
	lines = []
	f = open(file, "r")
	for l in f:
		lines.append(l.strip())
	f.close()
	return(lines)

def main(file):
	# Setup
	lines = parse_input_file(file)
	
	# Check
	bad = []
	for l in lines:
		sketchy = removeAllPairs(l)
		if sketchy != '':
			bad.append(sketchy)
	# print(bad)
	
	# Calculate results

	illegal = calculateIllegalScore(bad)
	print(f'Illegal score is {illegal}')
	print('---------------------------------')

	incomplete = calculateIncompleteScore(bad)
	print(f'Incomplete score is {incomplete}')

	print("Done!")


main('input.txt')
