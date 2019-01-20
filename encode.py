# convert normal Python code into "Pythonic" code!
import sys


def to_base_n(num, base):
	convertedNums = []
	while num:
		convertedNums.append(num % base)
		num //= base
	# fix digits to order desc
	convertedNums.reverse()
	return convertedNums


def encode_to_underlines(programmingCodes):
	# instance name (1st letter of chain)
	nameChains = ['_']
	for char in programmingCodes:
		# express ascii code of char as base 4 number
		charNumbers = to_base_n(ord(char), base=4)
		# length of chain expresses base 4 number
		# ex: 104 = 1 * 4**3 + 2 * 4**2 + 2 * 4 ** 1 + 0 * 4**0 -> ____.___.___._()
		methodNames = '.'.join(['_' * (n + 1) for n in charNumbers]) + '()'
		nameChains.append(methodNames)
	return '.'.join(nameChains)

if __name__ == '__main__':
	fileName = sys.argv[1]
	with open(fileName, 'r', encoding='utf-8') as f:
		codes = f.read()
	print(encode_to_underlines(codes))