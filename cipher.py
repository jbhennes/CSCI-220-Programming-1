"""
cipher.py

Classical cryptography with Python.

The ciphers programmed here were taken from the ciphers described in the
classical cryptography section of Wikipedia. The historical details in the
documentation is cribbed straight from those same Wikipedia articles. The
programming was done by Craig "Ichabod" O'Brien, and is released under the
same terms as the Wikipedia content (Creative Commons Attribution ShareAlike
License).

Classes:
CipherFunction: The base class for cipher functions. (object)
ADFGX: Encipher the text using a WWI German cipher. (CipherFunction)
Affine: Encipher using a mathematical substitution cipher. (CipherFunction)
Atbash: Encipher text using an ancient Hebrew cipher. (CipherFunction)
AutoACA: Encode using a hobby autokey cipher (CipherFunction)
Bifid: Encode using a French digraphic substitution cipher. (CipherFunction)
Book: Encipher a text word by word with a long text file. (CipherFunction)
Caesar: Encode using an ancient Roman substitution cipher. (CipherFunction)
Chinese: Encode using a simple transposition cipher. (CipherFunction)
Columnar: Encipher using a keyed transposition cipher. (CipherFunction)
Delastelle: Encipher using a cubic table. (CipherFunction)
Dvorak: Encode the text with a keyboard derived substitution. (CipherFunction)
FourSquare: Encode with a digraphic substitution. (CipherFunction)
Morse: Encipher the text using a radio code. (CipherFunction)
Mutating: Encipher the text using a mutating substitution. (CipherFunction)
Chao: Encode using a hard to break mutating cipher. (Mutating)
Sequence: Encode using an early Italian polyalphabetic cipher. (Mutating)
Vinegere: Encode using a French polyalphabetic cipher. (Mutating)
Nihilist: Encode using a 19th century Russion cipher. (CipherFunction)
Number: Encipher using the first cipher every kid learns. (CipherFunction)
OneTimePad: Encode using a theoretically unbreakable cipher. (CipherFunction)
Playfair: Encode with an English digraphic substitution. (CipherFunction)
Polybius: Encipher the text using an ancient Greek cipher. (CipherFunction)
RailFence: Encode text using a diagonal transposition cipher. (CipherFunction)
Reflexive: Encode the text using a reflexive substitution. (CipherFunction)
Scytale: Encode the text using the simplest machine cipher. (Columnar)
Solitaire: Encode the text using a deck of cards. (CipherFunction)
Straddling: Encode using a Russian substitution cipher. (CipherFunction)
Substitution: Encode the text using a basic substitution. (CipherFunction)
Keyword: Encode the text using a keyword alphabet. (Substitution)
Trifid: Encode the text with a trigraphic cipher. (CipherFunction)

Cipher Functions:
adfgx: Encipher the text using a WWI German cipher. (str)
affine: Encipher using a mathematical substitution cipher. (str)
atbash: Encipher text using an ancient Hebrew cipher. (str)
auto_aca: Encode using a hobby autokey cipher (str)
bifid: Encode using a French digraphic substitution cipher. (str)
book: Encipher a text word by word with a long text file. (str)
caesar: Encode using an ancient Roman substitution cipher. (str)
chao: Encode using a hard to break mutating cipher. (str)
chinese: Encode using a simple transposition cipher. (str)
columnar: Encipher using a simple transposition cipher. (str)
delastelle: Encipher using a cubic table. (str)
dvorak: Encode the text using a keyboard derived substitution. (str)
four_square: Encode the text with a digraphic substitution. (str)
keyword: Encode the text using a keyword alphabet. (str)
morse: Encipher the text using a radio code. (str)
mutating: Encipher the text using a mutating substitution. (str)
nihilist: Encode using a 19th century Russion revolutionary cipher. (str)
number: Encipher using the first cipher every kid learns. (str)
one_time_pad: Encode using a theoretically unbreakable cipher. (str)
playfair: Encode the text with an English digraphic substitution. (str)
polybius: Encipher the text using an ancient Greek cipher. (str)
rail_fence: Encode text using a diagonal transposition cipher. (str)
reflexive: Encode the text using a reflexive substitution. (str)
sequence: Encode using an early Italian polyalphabetic cipher. (str)
scytale: Encode the text using the simplest of machine ciphers. (str)
solitaire: Encode the text using a deck of cards. (str)
straddling: Encode the text using a Russian substitution cipher. (str)
substitution: Encode the text using a basic substitution cipher. (str)
keyword: Encode the text using a keyword alphabet. (str)
trifid: Encode the text with a trigraphic cipher. (str)
vinegere: Encode using a French polyalphabetic cipher. (str)

Other Functions:
mutate_chao: Mutating alphabet for the Chaocipher. (str, str)
mutate_sequence: Mutating alphabet for Bellaso sequence ciphers. (str, str)
mutate_shift: Mutating alphabet that shifts the cipher alphabet (str, str)
mutate_vinegere: Mutating alphabet for the Vinegere cipher. (str, str)
pad: Pad plain text to fit a certain number of columns. (str)
full_test: Run a test of all subclasses of CipherFunction. (dict)
"""
from __future__ import print_function

# imports
from difflib import SequenceMatcher
import random
import string

class CipherFunction(object):
	"""
	The parent class for all cipher functions in the module.
	
	The class provides some starndardized code for all cipher functions, 
	including the book keyword. Decoding is assumed to be done in the encode
	method, but a decode method is available if decoding is significantly
	different than encoding.
	
	Methods:
	change_defaults: Change the defaults for the function call. (None)
	decipher: Decipher the cipher text. (str)
	encipher: Encipher the plain text. (str)
	get_book: Return the code book used by the cipher. (dict)
	set_test: Set the default test for the cipher. (None)
	test: Test encoding and decoding a phrase. (tuple)
	
	Overridden Methods:
	__call__
	"""

	def __init__(self):
		"""
		__init__(self)
		Set up the function call defaults.
		
		This is done in initialization rather than as a class attribute to allow
		for piecemeal overriding by sub-classes.
		"""
		self.defaults = {'alphabet': string.ascii_uppercase, 'book': False, 'case': False, 
			'combines': ['IJ'], 'decode': False, 'deletes': '',
			'indexes': '12345', 'irregular': False, 'key': 'PHLEGM', 'n': 3, 'padding': 'QXJZ'}
		self.change_defaults()
		self.set_test()

	def __call__(self, text, **kwargs):
		"""
		__call__(self, text, **kwargs)
		Mediates function calls between enciphering and deciphering.
		
		This also provides standardized handling of the book parameter. The types
		for the paramters are the types generally used, but specific sub-classes
		may use other types. For example, the Hill sub-class takes matrices as 
		keys. See the specific sub-class for details.
		
		Standard CipherFunction parameters are:
		alphabet: The alphabet(s) used by the cipher. (str or list of str)
		book: A flag for returning the code book instead of the cipher text. (bool)
		decode: A flag for decoding instead of encoding. (bool)
		indexes: The characters used for rows/columns. (str or list of int)
		key: The key(s) used by the cipher. (str or list of str)
		n: The numeric value(s) used by the cipher. (int or list of int)
		
		Parameters:
		text: The plain or cipher text. (str)
		**kwargs: Any keyword arguments. (dict)
		"""
		neokwargs = self.defaults.copy()
		neokwargs.update(kwargs)
		if neokwargs['book']:
			return self.get_book(**neokwargs)
		else:
			return self.encode(text, **neokwargs)
	
	def change_defaults(self, **kwargs):
		"""
		change_defaults(self, **kwargs)
		Change the defaults for the function call. (None)
		
		Parameters:
		**kwargs: The new defaults (dict)
		"""
		self.defaults.update(kwargs)
		
	def decode(self, text, **kwargs):
		"""
		decode(self, text, **kwargs)
		Decipher the cipher text. (str)
		
		Parameters:
		text: the cipher text. (str)
		**kwargs: cipher specific parameters. (dict)
		"""
		kwargs['decode'] = True
		return self.encode(text, **kwargs)
	
	def encode(self, text, **kwargs):
		"""
		encode(self, text, **kwargs)
		Encipher the plain text. (str)
		
		Parameters:
		text: the plain text. (str)
		**kwargs: cipher specific parameters. (dict)
		"""
		return ''
		
	def get_book(self, **kwargs):
		"""
		get_book(self, **kwargs)
		Give a dictionary of string translations for the cipher. (dict of str: str)
		
		Parameters:
		**kwargs: cipher specific parameters. (dict)
		"""
		return {}
		
	def set_test(self, plain = '', cipher = '', **kwargs):
		"""
		set_test(self, plain = '', cipher = '', **kwargs)
		Set the default test for the cipher. (None)
		
		Parameters:
		plain: The plain text to encipher. (str)
		cipher: What the cipher text should be. (str)
		"""
		self.test_plain = plain
		self.test_cipher = cipher
		self.test_kwargs = kwargs
	
	def test(self, text = '', verbose = 1, **kwargs):
		"""
		test(self, text = '', verbose = 1, **kwargs)
		Test encoding and decoding a phrase. (str, str, float)
		
		The return value is the cipher text, the decoded cipher text, and the
		difflib match ration between the plain text and the decoded cipher text.
		
		Note that this doesn't really test wheter the encoding was done correctly,
		just whether the function can correctly decode what it encodes. Checking
		the encoding requires examining the output manually.
		
		Parameters:
		text: The plain text. (str)
		verbose: How much of the results to print. (int)
		"""
		# set up the parameters
		if text:
			test_cipher = ''
		else:
			text = self.test_plain
			test_cipher = self.test_cipher
			kwargs = self.test_kwargs
		neokwargs = self.defaults.copy()
		neokwargs.update(kwargs)
		# encipher the plain text
		cipher = self.__call__(text, **neokwargs)
		if verbose:
			print('CIPHER:', cipher)
		# test the cipher text if possible
		if test_cipher:
			cipher_match = SequenceMatcher(a = cipher, b = test_cipher).ratio()
			if verbose:
				print('CIPHER RATIO:', cipher_match)
		else:
			cipher_match = -1
		# decipher the cipher text
		neokwargs['decode'] = True
		plain = self.__call__(cipher, **neokwargs)
		if verbose:
			print('PLAIN:', plain)
		# test against the original text
		if neokwargs['case']:
			match = SequenceMatcher(a = text, b = plain, isjunk = lambda x: x in ' .')
		else:
			match = SequenceMatcher(a = text.upper(), b = plain.upper(), isjunk = lambda x: x in ' .')
		if verbose:
			print('RATIO:', match.ratio())
		return (cipher, cipher_match, plain, match.ratio())

class ADFGX(CipherFunction):
	"""
	adfgx(self, text, **kwargs)
	Encipher the text using a WWI German cipher. (str)
	
	ADFGX and its successor ADFGVX were designed by Fritz Nebel for use by the
	German army during World War I. It uses of Polybius square with a columnar
	transpositon to fractionate the message. The name comes from the letters 
	used for indexes in the Polybius square. They were chosen because they are
	easy to distinguish when using Morse code to transmit.
	
	Paramaters:
	text: The text to encode or decode. (str)
	indexes: The indexes for the Polybius square. (str)
	alphabet: The alphabet for the Polybius square. (str)
	key: The key for the columnar transposition. (str)
	"""
	
	def change_defaults(self):
		"""
		change_defaults(self)
		Set the cipher specific defaults. (None)
		"""
		self.defaults['indexes'] = 'ADFGX'
		self.defaults['combines'] = ['IJ']
		self.defaults['alphabet'] = string.ascii_uppercase.replace('J', '')
	
	def encode(self, text, **kwargs):
		"""
		encode(self, text, **kwargs)
		Encode/decode the text. (str)
		
		This just uses the Polybius square and the columnar transposition in
		order (or reverse order for decoding.
		
		Paramaters:
		text: The text to encode or decode. (str)
		indexes: The indexes for the Polybius square. (str)
		alphabet: The alphabet for the Polybius square. (str)
		key: The key for the columnar transposition. (str)
		"""
		# check for decoding
		if kwargs['decode']:
			text = columnar(text, **kwargs)
			# clean out odd padding
			if len(text) % 2:
				text = text[:-1]
			text = polybius(text, **kwargs)
		else:
			kwargs['padding'] = kwargs['indexes']
			text = polybius(text, **kwargs)
			text = columnar(text, **kwargs)
		return text
	
	def get_book(self, **kwargs):
		"""
		get_book(self, **kwargs)
		Get the code book for the cipher. (dict of str: str)
		
		This returns the Polybius square codebook, even though it is only part
		of the whole cipher.
		
		Paramaters:
		indexes: The indexes for the Polybius square. (str)
		alphabet: The alphabet for the Polybius square. (str)
		"""
		return polybius.get_book(**kwargs)
		
	def set_test(self):
		"""
		set_test(self)
		Set up the default test for the cipher. (None)
		"""
		self.test_plain = 'attack at once'
		self.test_cipher = 'FAXDFADDDGDGFFFAFAXXAFAFX'
		self.test_kwargs = {'key': 'CARGO', 'alphabet': 'BTALPDHOZKQFVSNGICUXMREWY', 'padding': 'XGFDA'}

class Affine(CipherFunction):
	"""
	affine(self, text, **kwargs)
	Encipher using a mathematical substitution cipher. (str)
	
	The Affine cipher replace a character at index x with the character at index
	ax + b mod m, where m is the length of the alphabet. Note that a must be
	coprime with m in order for the message to be decipherable. 
	
	The Affine cipher is a general case of many other simple substitution 
	ciphers. The Caesar cipher is a subset of the Affine cipher where a = 1. 
	The Atbash cipher is the Affine cipher with a = b = m - 1.
	
	Parameters:
	text: The plain or cipher text. (str)
	n: the parameters of the function (a, b). (int, int)
	"""
	
	def change_defaults(self):
		"""
		change_defaults(self)
		Set the cipher specific defaults (None)
		"""
		self.defaults['n'] = (5, 8)
		self.defaults['case'] = True
	
	def decode(self, text, **kwargs):
		"""
		decode(self, text, **kwargs)
		Decode the cipher text (str)
		
		Parameters:
		text: the cipher text. (str)
		n: the parameters of the function (a, b). (int, int)
		"""
		# get the reverse book
		book = self.get_book(**kwargs)
		# decipher the cipher text
		return ''.join([book.get(char, char) for char in text])
	
	def encode(self, text, **kwargs):
		"""
		encode(self, text, **kwargs)
		Encode the plain text (str)
		
		Parameters:
		text: the plain text. (str)
		n: the parameters of the function (a, b). (int, int)
		"""
		# check for case insensitivity
		if not kwargs['case']:
			text = text.upper()
		# check for decoding
		if kwargs['decode']:
			return self.decode(text, **kwargs)
		# get the book and enchipher the plain text
		book = self.get_book(**kwargs)
		return ''.join([book.get(char, char) for char in text])
		
	def get_book(self, **kwargs):
		"""
		get_book(self, **kwargs)
		Get the book. (dict of str: str)
		
		I over complicated this. Since in the end Affine is a simple 
		substitution cipher, to decipher you just need to get the enciphering
		book and reverse it.
		
		Parameters:
		n: the parameters of the function (a, b). (int, int)
		"""
		# get parameters
		a, b = kwargs['n']
		m = len(kwargs['alphabet'])
		# get the modular multiplicative inverse for deciphering
		if kwargs['decode']:
			for x in range(1, m):
				if (a * x) % m == 1:
					break
			else:
				raise ValueError("The 'a' parameter must be coprime with the length of the alphabet.")
			a = x
		# generate the book
		book = {}
		alphabet = kwargs['alphabet']
		for char_index in range(m):
			if kwargs['decode']:
				# reverse formula for deciphering
				book[alphabet[char_index]] = alphabet[(a * (char_index - b)) % m]
			else:
				book[alphabet[char_index]] = alphabet[(char_index * a + b) % m]
			# check for case sensitivity
			if kwargs['case']:
				book[alphabet[char_index].lower()] = book[alphabet[char_index]].lower()
		return book
		
	def set_test(self):
		"""
		set_test(self)
		Set the default test for the cipher. (None)
		"""
		self.test_plain = 'Affine cipher'
		self.test_cipher = 'Ihhwvc swfrcp'
		self.test_kwargs = {'n': (5, 8), 'case': True}

# function instance
affine = Affine()

class Atbash(CipherFunction):
	"""
	atbash(self, text, **kwargs)
	Encipher text using an ancient Hebrew cipher. (str)
	
	The Atbash cipher was originally used on the Hebrew alphabet, and gets its 
	name from the first two substitutions (aleph for tav and beth for shin). In
	English you might call it Azby. It is a simple substitution done by 
	reversing the alphabet. The first letter is replaced with the last letter,
	the second letter with the next to last letter, and so on.
	
	Enciphering and deciphering in Atbash use the same book, so the decode
	parameter is not necessary.
	
	Parameters:
	text: The plain or cipher text. (str)
	alphabets: Alternative alphabets to use for encipherment. (list of str)
	"""
	
	def change_defaults(self):
		"""
		change_defaults(self)
		Set the cipher specific defaults. (None)
		"""
		self.defaults['case'] = True
	
	def encode(self, text, **kwargs):
		"""
		encode(self, text, **kwargs)
		Encode/decode the text. (str)
		
		Parameters:
		text: The text to encode or decode. (str)
		alphabet: The alphabet to use for the encoding/decoding. (str)
		"""
		kwargs['alphabet'] = [kwargs['alphabet'], kwargs['alphabet'][::-1]]
		return substitution(text, **kwargs)
		
	def get_book(self, **kwargs):
		"""
		get_book(self, **kwargs)
		Get the book for the cipher.
		"""
		kwargs['alphabet'] = [kwargs['alphabet'], kwargs['alphabet'][::-1]]
		return substitution.get_book(**kwargs)
		
# function instance
atbash = Atbash()

class AutoACA(CipherFunction):
	"""
	auto_aca(self, text, **kwargs)
	Encode using a hobby autokey cipher (str)
	
	AutoACA is an autokey cipher based on the Vinegere cipher that was used 
	by the American Cryptological Assocation (a hobby group), it was
	suggested by Vinegere himself. However, Vinegere's starting keys were 
	only one character long.
	
	Parameters:
	text: The text to encode. (str)
	key: The key to start the autokey. (str)
	"""
	
	def change_defaults(self):
		"""
		change_defaults(self)
		Set the cipher specific defaults. (None)
		"""
		self.defaults['mutation'] = mutate_vinegere
	
	def encode(self, text, **kwargs):
		"""
		encode(self, text, **kwargs)
		Encode the text using a mutating substitution cipher. (str)
	
		Parameters:
		alphabet: The starting plain and cipher alphabets. (str)
		mutation: The function to mutate the alphabets with. (str)
		"""
		# adjust the alphabet for a mutating cipher
		index = kwargs['alphabet'].index(kwargs['key'][0])
		cipher = kwargs['alphabet'][index:] + kwargs['alphabet'][:index]
		plain = kwargs['alphabet']
		# check for case insensitivity
		if not kwargs['case']:
			text = text.upper()
		out_text = ''
		# do the encoding/decoding
		for char in text:
			# standard 
			if char in plain:
				if kwargs['decode']:
					out_text += plain[cipher.index(char)]
					kwargs['key'] += out_text[-1]
				else:
					out_text += cipher[plain.index(char)]
					kwargs['key'] += char
			# case sensitive
			elif kwargs['case'] and char.upper() in plain:
				if kwargs['decode']:
					out_text += plain[cipher.index(char.upper())].lower()
					kwargs['key'] += out_text[-1].upper()
				else:
					out_text += cipher[plain.index(char.upper())].lower()
					kwargs['key'] += char.upper()
				print(kwargs['key'])
			# irrelevant characters
			else:
				out_text += char
			# mutate
			plain, cipher = kwargs['mutation'](plain, cipher, char,
				out_text, **kwargs)
		return out_text
		
# function instance made later

class Bifid(CipherFunction):
	"""
	bifid(self, text, **kwargs)
	Encode using a French digraphic substitution cipher. (str)
	
	Bifid was invented by Felix Delastelle around the turn of the 20th
	century. It encodes with a Polybius square, transposes the cipher
	text, and then decodes with the same Polybius square. This results
	in each cipher text character being dependent on two plain text
	characters.
	
	Parameters:
	text: The text to encode. (str)
	alphabet: The alphabet for the Polybius square. (str)
	"""
	
	def change_defaults(self):
		"""
		change_defaults(self)
		Set the cipher specific defaults. (None)
		"""
		self.defaults['alphabet'] = string.ascii_uppercase.replace('J', '')
	
	def decode(self, text, **kwargs):
		"""
		decode(self, text, **kwargs)
		Decode the cipher text. (str)
		
		Parameters:
		text: The text to decode. (str)
		alphabet: The alphabet for the Polybius square. (str)
		"""
		# encode with polybius to get the coordinates
		kwargs['decode'] = False
		coordinates = polybius(text, **kwargs)
		# interleave the coordinates
		plain_len = len(coordinates) // 2
		coordinates = ''.join(a + b for a, b in zip(coordinates[:plain_len], coordinates[plain_len:]))
		# decode with polybius to get the plain text
		kwargs['decode'] = True
		return polybius(coordinates, **kwargs)
	
	def encode(self, text, **kwargs):
		"""
		encode(self, text, **kwargs)
		Encode the plain text. (str)
		
		Parameters:
		text: The text to encode. (str)
		alphabet: The alphabet for the Polybius square. (str)
		"""
		# check for bifid decoding
		if kwargs['decode']:
			return self.decode(text, **kwargs)
		# encode with polybius to get the coordinates
		coordinates = polybius(text, **kwargs)
		# split out the row and column coordinates
		coordinates = coordinates[0::2] + coordinates[1::2]
		# decode with polybius to get the cipher text
		kwargs['decode'] = True
		return polybius(coordinates, **kwargs)
		
	def set_test(self):
		"""
		set_test(self)
		Set the default test for this cipher. (None)
		"""
		self.test_plain = 'Flee at once'
		self.test_cipher = 'UAEOLWRINS'
		self.test_kwargs = {'alphabet': 'BGWKZQPNDSIOAXEFCLUMTHYVR'}
		
# function instance
bifid = Bifid()
		
class Book(CipherFunction):
	"""
	book(self, text, **kwargs)
	Encipher a text word by word with a long text file. (str)
	
	The standard book cipher uses the page, line, and word as a three number
	key for each word. Since electronic files don't have pages, virtual pages
	are made out of every n lines.
		
	The combines parameter is a single word, such as 'the'. If it is 
	repeated ('the the') that is an indicator that a word is about to be
	spelled out using other words. This is done for words that are not
	in the book. When the combines word is doubled again it indicates
	that the spelling is done.
	
	Paramters:
	key: A path to the file with the words. (str)
	n: The length of the virtual pages. (int)
	"""
	
	def change_defaults(self):
		"""
		change_defaults(self)
		Set the cipher specific defaults. (None)
		"""
		key = r'C:\Users\ichabod801\Documents\Alpha Docs\Python\cipher\AV_txt\AV1611Bible.txt'
		self.defaults['key'] = key
		self.defaults['n'] = 100
		self.defaults['combines'] = 'ABEL'
	
	def decode(self, text, **kwargs):
		"""
		decode(self, text, **kwargs)
		Decipher the plain text. (str)
		
		Parameters:
		text: the plain text. (str)
		key: A path to the file with the words. (str)
		n: The length of the virtual pages. (int)
		combines: A word to double to indicate spelling. (str)
		"""
		book = self.get_book(**kwargs)
		# get the encoded words
		numeric = [int(word) for word in text.split()]
		raw_plain = [book[tuple(numeric[start:(start + 3)])] for start in range(0, len(numeric), 3)]
		# translate spelled words
		spell_flag = [kwargs['combines'].upper(), kwargs['combines'].upper()]
		plain = []
		spelling = False
		while raw_plain:
			# check for spell flags
			if raw_plain[:2] == spell_flag:
				if not spelling:
					plain.append('')
				spelling = not spelling
				raw_plain.pop(0)
				raw_plain.pop(0)
			# extract spelling
			elif spelling:
				plain[-1] += raw_plain.pop(0)[0]
			# or extract whole words
			else:
				plain.append(raw_plain.pop(0))
		return ' '.join(plain)
	
	def encode(self, text, **kwargs):
		"""
		encode(self, text, **kwargs)
		Encipher the plain text. (str)
		
		Parameters:
		text: the plain text. (str)
		key: A path to the file with the words. (str)
		n: The length of the virtual pages. (int)
		combines: A word to double to indicate spelling. (str)
		"""
		# set up the encoding
		if kwargs['case']:
			kwargs['alphabet'] = kwargs['alphabet'] + kwargs['alphabet'].lower()
			kwargs['combines'] = kwargs['combines'].lower()
		else:
			text = text.upper()
		if kwargs['decode']:
			return self.decode(text, **kwargs)
		book = self.get_book(**kwargs)
		cipher = []
		for word in text.split():
			# trim out excess characters
			word = ''.join([char for char in word if char in kwargs['alphabet']])
			if word in book:
				# translate words in the book
				cipher.extend(random.choice(book[word]))
			else:
				# spell other words using the spell flag
				cipher.extend(random.choice(book[kwargs['combines']]))
				cipher.extend(random.choice(book[kwargs['combines']]))
				for char in word:
					keys = [key for key in book.keys() if key.startswith(char)]
					if keys:
						cipher.extend(random.choice(book[random.choice(keys)]))
				# close spell flag
				cipher.extend(random.choice(book[kwargs['combines']]))
				cipher.extend(random.choice(book[kwargs['combines']]))
		return ' '.join([str(x) for x in cipher])
	
	def get_book(self, **kwargs):
		"""
		get_book(self, **kwargs)
		Make a translation dict out of a large text file. (dict)
		
		The dict is words keyed to a list of tuples. Tuples are chosen randomly
		from the lists during encoding. Pages, lines, and word are zero indexed.
		
		Parameters:
		key: A path to the file with the words. (str)
		n: The length of the virtual pages. (int)
		"""
		book = {}
		# set up position tracking
		page_index = 0
		line_index = 0
		for line in open(kwargs['key']):
			for word_index, word in enumerate(line.strip().split()):
				if not kwargs['case']:
					word = word.upper()
				# trim out punctuation
				word = ''.join([char for char in word if char in kwargs['alphabet']])
				# put in book in the correct order for encoding or decoding
				if kwargs['decode']:
					book[(page_index, line_index, word_index)] = word
				else:
					if word not in book:
						book[word] = [(page_index, line_index, word_index)]
					else:
						book[word].append((page_index, line_index, word_index))
			# update the position tracking
			line_index += 1
			# make virtual pages
			if line_index == kwargs['n']:
				line_index = 0
				page_index += 1
		return book
		
# function instance
book = Book()

class Caesar(CipherFunction):
	"""
	caesar(self, text, **kwargs)
	Encode using an ancient Roman substitution cipher. (str)
	
	According to the historian Suentonius, Julius Caesar used this cipher with
	n = 3 to communicate with his generals. It is simply a shift of the 
	alphabet so that each letter is coded with the nth following letter.
	
	Parameters:
	text: The text to encode/decode. (str)
	n: The number of letters to shift. (str)
	"""
	
	def encode(self, text, **kwargs):
		"""
		encode(self, text, **kwargs)
		Encode the plain text. (str)
		
		Parameters:
		text: The text to encode/decode. (str)
		n: The number of letters to shift. (str)
		"""
		cipher_alphabet = kwargs['alphabet'][kwargs['n']:] + kwargs['alphabet'][:kwargs['n']]
		kwargs['alphabet'] = [kwargs['alphabet'], cipher_alphabet]
		return substitution(text, **kwargs)
		
	def get_book(self, **kwargs):
		"""
		get_book(self, **kwargs)
		Get the encryption book for the cipher (dict)
		
		Parameters:
		n: The number of letters to shift. (str)
		"""
		cipher_alphabet = kwargs['alphabet'][kwargs['n']:] + kwargs['alphabet'][:kwargs['n']]
		kwargs['alphabet'] = [kwargs['alphabet'], cipher_alphabet]
		return substitution.get_book(**kwargs)
	
	def set_test(self):
		"""
		set_test(self)
		Set the default test for the cipher. (None)
		"""
		self.test_plain = 'The quick brown fox jumps over the lazy dog.'
		self.test_cipher = 'WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ.'
		self.test_kwargs = {}
		
# function instance
casear = Caesar()
	
class Chinese(CipherFunction):
	"""
	chinese(self, text, **kwargs)
	Encipher using a simple transposition cipher. (str)
	
	This is mentioned on Wikepedia, but nothing about it is explained there, 
	and it doesn't show up in the obvious web searches. It's probably a 
	children's cipher known to the author of the Wikipedia article. The idea
	is to write the message alternating down and up, right to left; and then
	read it out left to right, top to bottom.
	
	Case sensitive encoding includes all spaces and punctuation.
	
	Parameters:
	text: The text to encipher or decipher. (str)
	n: The height of the rows to write. (int)
	"""
	
	def change_defaults(self):
		"""
		change_defaults(self)
		Set the cipher specific defaults. (None)
		"""
		self.defaults['case'] = True

	def decode(self, text, **kwargs):
		"""
		decode(self, text, **kwargs)
		Decode the cipher text. (str)
		
		Parameters:
		text: The text to encipher or decipher. (str)
		n: The height of the rows to write. (int)
		"""
		# extract the rows and columns
		row_len = len(text) // kwargs['n']
		rows = [text[(row_len * start):(row_len * start + row_len)] for start in range(kwargs['n'])]
		columns = [''.join(column) for column in zip(*rows)]
		# undo the reversals
		columns.reverse()
		columns = [column[::((-1) ** column_index)] for column_index, column in enumerate(columns)]
		return ''.join(columns)

	def encode(self, text, **kwargs):
		"""
		encode(self, text, **kwargs)
		Encode the plain text. (str)
		
		Parameters:
		text: The text to encipher or decipher. (str)
		n: The height of the rows to write. (int)
		"""
		# check for decoing
		if kwargs['decode']:
			return self.decode(text, **kwargs)
		# check for case insensitivity
		if not kwargs['case']:
			text = text.upper()
			text = ''.join([char for char in text if char in kwargs['alphabet']])
		# put the text in columns
		text = pad(text, kwargs['n'])
		columns = [text[start:(start + kwargs['n'])] for start in range(0, len(text), kwargs['n'])]
		# reverse every other vertical and all horizontals
		columns = [column[::((-1) ** column_index)] for column_index, column in enumerate(columns)]
		columns.reverse()
		return ''.join([''.join([column[row] for column in columns]) for row in range(kwargs['n'])])
		
	def set_test(self):
		"""
		set_test(self)
		Set the default test for the cipher. (None)
		"""
		self.test_plain = 'THEDOGRANFAR'
		self.test_cipher = 'RRGTAAOHFNDE'
		self.test_kwargs = {}
		
# function instance
chinese = Chinese()

class Columnar(CipherFunction):
	"""
	columnar(self, text, **kwargs)
	Encipher using a keyed transposition cipher. (str)
	
	The columnar cipher is a transposition cipher that puts the text into 
	columns and then rearranges those columns. The order of rearrangement is
	determined by sorting the key. If the key is 'PYHTON', the third ('H')
	column will become the first column and the second ('Y') column will
	become the last column. Duplicate characters are taken out of the key
	before determining the order of the columns.
	
	The key is assumed to be a string, but can be any sortable itterable. If
	the key has multiple copies of the same character, the alphabet must be
	in sort order to correctly clean the key.
	
	Parameters:
	key: A key that will determine the sort order. (str)
	alphabet: The alphabet for cleaning keys. (str)
	padding: Letters to pad out the columns. (str)
	irregular: A flag for irregular enciphering, with no padding. (bool)
	"""
		
	def clean_key(self, key, alphabet):
		"""
		clean_key(self, key, alphabet)
		Clean the key to allow a unique sorting. (str)
		
		Parameters:
		key: The key for the cipher. (str)
		alphabet: The alphabet for adjusting duplicate characters. (str)
		"""
		clean = ''
		for char in key:
			# shift duplicate characters up in the sort order
			while char in clean:
				char = alphabet[alphabet.index(char) + 1]
			clean += char
		return clean
		
	def decode(self, text, **kwargs):
		"""
		decode(self, text, **kwargs)
		Decode the cipher text. (str)
		
		Parameters:
		text: The cipher text. (str)
		key: The key that will determine the sort order. (str)
		"""
		# clean up the key
		raw_key = self.clean_key(kwargs['key'], kwargs['alphabet'])
		# get the decode order
		key = ''.join(sorted(raw_key))
		order = [list(key).index(char) for char in raw_key]
		# reorder the colums
		num_columns = len(key)
		column_len = len(text) // num_columns
		if len(text) % num_columns:
			column_len += 1
		# check for variable length columns
		if kwargs['irregular']:
			# determine the column sizes
			long_columns = len(text) % num_columns
			column_size = len(text) // num_columns
			column_sizes = [[column_size, column_size + 1][index < long_columns] for index in order]
			# extract the columns
			start = 0
			columns = []
			for size in column_sizes:
				columns.append(text[start:(start + size)])
				start += size
				# pad short columns (removed in return statement with [:len(text)]
				if size == column_size:
					columns[-1] += ' '
		else:
			columns = [text[start:(start + column_len)] for start in range(0, len(text), column_len)]
		transposed = [columns[order[n]] for n in range(num_columns)]
		# return the rows
		return ''.join([''.join(row) for row in zip(*transposed)])[:len(text)]

	def encode(self, text, **kwargs):
		"""
		encode(self, text, **kwargs)
		Encipher or decipher the text. (str)
			
		Parameters:
		text: the plain text. (str)
		key: A key that will determine the sort order. (str)
		"""
		if kwargs['decode']:
			return self.decode(text, **kwargs)
		# clean up the key
		key = self.clean_key(kwargs['key'], kwargs['alphabet'])
		# determine the sort order
		order = [list(key).index(char) for char in sorted(key)]
		# handle case insensitivity
		if not kwargs['case']:
			text = text.upper()
			text = ''.join([char for char in text if char in kwargs['alphabet']])
		# get the columns
		num_columns = len(key)
		if not kwargs['irregular']:
			text = pad(text, num_columns, kwargs['padding'])
		columns = [text[column_index::num_columns] for column_index in range(num_columns)]
		# reorder the columns.
		transposed = [columns[order[n]] for n in range(num_columns)]
		return ''.join(transposed)
		
	def set_test(self):
		"""
		set_test(self)
		Set the default test for the cipher. (None)
		"""
		self.test_plain = 'We are discovered, flee at once.'
		self.test_cipher = 'EVLNEACDTKESEAQROFOJDEECUWIREE'
		self.test_kwargs = {'padding': 'QKJEU', 'key': 'ZEBRAS'}

# function instance
columnar = Columnar()

class Delastelle(CipherFunction):
	"""
	delastelle(self, text, **kwargs)
	Encode using a cubic table. (str)
	
	The Delastelle cube was created by Felix Delastelle as an extension of the
	Polybius square into three dimensions. It was not meant to be used by 
	iteself, but rather as part of the Trifid cipher. It is separated here to
	allow it to be used as a building block in other ciphers.
	
	Parameters:
	alphabet: The alphabet to use to fill the cube. (str)
	indexes: The characters identifying the rows/columns/levels. (str)
	combines: Letters to combine into the same cell. (list of str)
	deletes: letters to delete from the alphabet and plain text. (str)
	"""
	
	def change_defaults(self):
		"""
		change_defaults(self)
		Set the cipher specific defaults. (None)
		"""
		self.defaults['alphabet'] += '.'
		self.defaults['indexes'] = '123'
		
	def decode(self, text, **kwargs):
		"""
		decode(self, text, **kwargs)
		Decode the cipher text. (str)
		
		Parameters:
		text: The cipher text. (str)
		alphabet: The alphabet to use to fill the cube. (str)
		indexes: The characters identifying the rows/columns/levels. (str)
		combines: Letters to combine into the same cell. (list of str)
		deletes: letters to delete from the alphabet and plain text. (str)
		"""
		# get the translation
		book = self.get_book(**kwargs)
		# scan the cipher text
		triple = ''
		plain = ''
		for char in text:
			# gather triples
			if char in kwargs['indexes']:
				triple += char
				# decode triples
				if len(triple) == 3:
					plain += book[triple]
					triple = ''
		return plain
		
	def encode(self, text, **kwargs):
		"""
		encode(self, text, **kwargs)
		Encode the plain text. (str)
		
		Parameters:
		text: The plain text. (str)
		alphabet: The alphabet to use to fill the cube. (str)
		indexes: The characters identifying the rows/columns/levels. (str)
		combines: Letters to combine into the same cell. (list of str)
		deletes: letters to delete from the alphabet and plain text. (str)
		"""
		if kwargs['decode']:
			return self.decode(text, **kwargs)
		book = self.get_book(**kwargs)
		if not kwargs['case']:
			text = text.upper()
		return ''.join([book.get(char, '') for char in text])
	
	def get_book(self, **kwargs):
		"""
		get_book(self, **kwargs)
		Get the translation book for the cipher. (dict)
		
		Parameters:
		alphabet: The alphabet to use to fill the cube. (str)
		indexes: The characters identifying the rows/columns/levels. (str)
		combines: Letters to combine into the same cell. (list of str)
		deletes: letters to delete from the alphabet and plain text. (str)
		"""
		book = {}
		size = len(kwargs['indexes'])
		# loop through the three dimensions
		for r, row in enumerate(kwargs['indexes']):
			for c, column in enumerate(kwargs['indexes']):
				for v, level in enumerate(kwargs['indexes']):
					# calculate the letter for that location
					book[kwargs['alphabet'][v * size ** 2  + r * size + c]] = level + column + row
		# reverse book if decoding
		if kwargs['decode']:
			book = {value: key for key, value in book.items()}
		# handle lower case for encoding
		elif kwargs['case']:
			for char in book:
				book[char.lower()] = book[char]
		return book
		
# function instance
delastelle = Delastelle()

class Dvorak(CipherFunction):
	"""
	dvorak(self, text, **kwargs)
	Encode the text using a keyboard derived substitution. (str)
	
	This is a simple substitution using the standard QWERTY keyboard layout
	against the various Dvorak keyboard layouts (original, left, and right).
	Added to those is keyboard layout where the letters are layed out in
	alphabetical order.
	
	There are different variations of the Dvorak cipher, depending on the
	way you are typing and the layout you are typing on. These are analagous
	to the plain text and the cipher text. The key parameter determines which
	layouts are used with two letters, the first being for the plain text and
	the second for the cipher text. The letters for each layout are:
	
		A: Alphabetic layout (ABCDE...)
		D: Original Dvorak layout (PYFGC...)
		L: Left hand Dvorak layout (PFMLJ...)
		R: Right hand Dvorak layout (JLMFP...)
		Q: Standard QWERTY layout (QWERT...)
		
	If the key is lower case, only the letters are encoded (in the order they 
	appear on the keyboard). If the key is upper case, all symbols are translated
	(based on the keys they share). See dvorak.alphabets for details.
	
	Parameters:
	text: The text to encode/decode. (str)
	key: Two letters representing the alphabets to be used. (str)
	"""
	
	def change_defaults(self):
		"""
		change_defaults(self)
		Set the cipher specific defaults. (None)
		
		This also sets the alphabets for the different keyboards.
		"""
		self.defaults['key'] = 'DQ'
		self.alphabets = {}
		self.alphabets['a'] = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		self.alphabets['d'] = 'PYFGCRLAOEUIDHTNSQJKXBMWVZ'
		self.alphabets['l'] = 'PFMLJQBYURSOKCDTHEAZXGVWNI'
		self.alphabets['r'] = 'JLMFPQORSUYBZAEHTDCKXINWVG'
		self.alphabets['q'] = 'QWERTYUIOPASDFGHJKLZXCVBNM'
		self.alphabets['A'] = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
		self.alphabets['A'] += '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '
		self.alphabets['D'] = '`1234567890[]\',.pyfgcrl/=\\aoeuidhtns-;qjkxbmwvz '
		self.alphabets['D'] += '~!@#$%^&*(){}"<>PYFGCRL?+|AOEUIDHTNS_:QJKXBMWVZ'
		self.alphabets['L'] = '`[]/pfmlj4321;qbyurso.65=\\-kcdtheaz87\'xgvwni,09 ' 
		self.alphabets['L'] += '~{}?PFMLJ$#@!:QBUYRSO>^%+|_KCDTHEAZ*&"xgvwni<)('
		self.alphabets['R'] = '`1234jlmfp/[]56q.orsuyb;=\\78zaehtdck-90x,inwvg\' '
		self.alphabets['R'] += '~!@#$JLMFP?{}%^Q>ORSUYB:+|&*ZAEHTDCK_()X<INWVG"'
		self.alphabets['Q'] = '`1234567890-=qwertyuiop[]\\asdfghjkl;\'zxcvbnm,./ '
		self.alphabets['Q'] += '~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'
		
	def encode(self, text, **kwargs):
		"""
		encode(self, text, **kwargs)
		Encode the plain text. (str)
		
		This can't be done using the substitution function, because case needs
		to be handled differently.
		
		Parameters:
		text: The text to encode/decode. (str)
		key: Two letters representing the alphabets to be used. (str)
		"""
		kwargs['alphabet'] = [self.alphabets[kwargs['key'][0]], self.alphabets[kwargs['key'][1]]]
		kwargs['case'] = kwargs['key'].islower()
		book = self.get_book(**kwargs)
		return ''.join([book.get(char, char) for char in text])

	def get_book(self, **kwargs):
		"""
		get_book(self, **kwargs)
		Get the book for the supplied alphabets. (dict)
	
		Parameters:
		text: The text to encode/decode. (str)
		alphabet: The plain and cipher alphabets. (list of str)
		"""
		if kwargs['decode']:
			book = {cipher: plain for plain, cipher in zip(*kwargs['alphabet'])}
		else:
			book = {plain: cipher for plain, cipher in zip(*kwargs['alphabet'])}
		return book
		
class FourSquare(CipherFunction):
	"""
	four_square(self, text, **kwargs)
	Encode the text using a digraphic cipher. (str)
	
	The alphabet parameter should have four alphabets for the four squares.
	
	So you encode ABABABAB getting AaBbAaBbAaBb. Then you decode AbBaAbBa.
	Rather than trying to do some fancy application of Polybius, I think I
	should just keep the building of a code book.
	
	Parameters:
	text: The text to encode/decode. (str)
	alphabet: The alphabets for the Polybius squares. (list of str)
	"""
	
	square_names = ['UL', 'UR', 'LL', 'LR']
	no_q = 'ABCDEFGHIJKLMNOPRSTUVWXYZ'
	
	def change_defaults(self):
		"""
		change_defaults(self)
		Set the cipher specific defaults. (None)
		"""
		self.defaults['alphabet'] = [self.no_q] * 4
		self.defaults['combines'] = [[], [], [], []]
		self.defaults['deletes'] = 'Q'
	
	def encode(self, text, **kwargs):
		"""
		encode(self, text, **kwargs)
		Encode the plain text. (str)
		
		Parameters:
		text: The plain text. (str)
		alphabet: Four sets of alphabets for the four squares. (list of list of int)
		combines: Four sets of combined letters for the squares. (list of list of str)
		deletes: Characters to remove from alphabets and plain text. (list of str)
		"""
		# prep the incoming text
		for char in kwargs['deletes']:
			text = text.replace(char, '')
		if not kwargs['case']:
			text = text.upper()
		# get the four code books
		four_books = self.get_book(**kwargs)
		first = ''
		mid = ''
		cipher = ''
		for char in text:
			if first:
				# encode when you have two characters
				if char in four_books['UL']:
					coord1 = four_books['UL'][first]
					coord2 = four_books['LR'][char]
					cipher += four_books['UR'][(coord1[0], coord2[1])]
					cipher += mid
					cipher += four_books['LL'][(coord2[0], coord1[1])]
					mid = ''
					first = ''
				# save intervening characters
				else:
					mid += char
			else:
				# store initial characteres
				if char in four_books['UL']:
					first = char
				else:
					cipher += char
		# clean up any hanging characters
		if first:
			coord1 = four_books['UL'][first]
			coord2 = four_books['LR'][random.choice(list(four_books['LR'].keys()))]
			cipher += four_books['UR'][(coord1[0], coord2[1])]
			cipher += mid
			cipher += four_books['LL'][(coord2[0], coord1[1])]
		else:
			cipher += mid
		return cipher
	
	def get_book(self, **kwargs):
		"""
		get_book(self, **kwargs)
		Get the four squares for the alphabets. (dict)
		
		This returns a dictionary of four dictionaries, rather than the usual
		single dictionary. Each dictionary is letters keyed to tuples, but two
		of them are reversed, depending on the value of the decode 
		parameter.
		
		If the four alphabets provided are not the same length, the results may not
		be what you expected. All alphabets should also fit in a square.
		
		Parameters:
		alphabet: Four sets of alphabets for the four squares. (list of list of str)
		combines: Four sets of combined letters for the squares. (list of list of str)
		deletes: Characters to remove from alphabets and plain text. (list of str)
		"""
		# generate the square dictionaries
		four_books = {}
		for square_index, alphabet in enumerate(kwargs['alphabet']):
			book = {}
			# clean up alphabets
			for bad in kwargs['deletes']:
				alphabet = alphabet.replace(bad, '')
			# associate letters with coordinates
			size = int(len(alphabet) ** 0.5)
			for row in range(size):
				for col in range(size):
					book[alphabet[row * size + col]] = (row, col)
					if kwargs['case']:
						book[alphabet[row * size + col].lower()] = (row, col) 
			for pair in kwargs['combines'][square_index]:
				book[pair[1]] = book[pair[0]]
			four_books[self.square_names[square_index]] = book
		# reverse appropriate books
		if kwargs['decode']:
			four_books['UL'] = {value: key for key, value in four_books['UL'].items()}
			four_books['LR'] = {value: key for key, value in four_books['LR'].items()}
			four_books['UL'], four_books['UR'] = four_books['UR'], four_books['UL']
			four_books['LL'], four_books['LR'] = four_books['LR'], four_books['LL']
		else:
			four_books['UR'] = {value: key for key, value in four_books['UR'].items()}
			four_books['LL'] = {value: key for key, value in four_books['LL'].items()}
		return four_books
		
# function instance
four_square = FourSquare()
					
class Morse(CipherFunction):
	"""
	morse(self, text, **kwargs)
	Encipher the text using a radio code. (str)
	
	Morse code isn't really cryptography, classical or otherwise, but it was
	in heavy use during WWI and influenced some of the codes used then, and
	it can be used for fractionation.
	
	Besides, it's cool, so shut up about it.
	
	Parameters:
	text: the plain text (str)
	dot_dash: Alternate symbols to use for the dot and dash (str)
	"""
	
	def __init__(self):
		"""
		__init__(self)
		Set up the code book. (None)
		"""
		super(Morse, self).__init__()
		self.book = {'A': '*-', 'B': '-***', 'C': '-*-*', 'D': '-**', 'E': '*', 'F': '**-*', 'G': '--*',
			'H': '****', 'I': '**', 'J': '*---', 'K': '-*-', 'L': '*-**', 'M': '--', 'N': '-*',
			'O': '---', 'P': '*--*', 'Q': '--*-', 'R': '*-*', 'S': '***', 'T': '-', 'U': '**-',
			'V': '***-', 'W': '*--', 'X': '-**-', 'Y': '-*--', 'Z': '--**', '1': '*----', '2': '**---',
			'3': '***--', '4': '****-', '5': '*****', '6': '-****', '7': '--***', '8': '---**',
			'9': '----*', '0': '-----', ' ': '   ', '.': '*-*-*-', ',': '--**--',
			'?': '**--**', "'": '*----*', '!': '-*-*--', '/': '-**-*', '(': '-*--*', ')': '-*--*-',
			'&': '*-***', ':': '---***', ';': '-*-*-*', '=': '-***-', '+': '*-*-*', '-': '-****-',
			'_': '**--*-', '"': '*-**-*', '$': '***-**-', '@': '*--*-*', '<space/>': '<space/>'}
		for char in string.ascii_lowercase:
			self.book[char] = self.book[char.upper()]
			
	def change_defaults(self):
		"""
		change_defaults(self)
		set the cipher specific defaults. (None)
		"""
		self.defaults['dot_dash'] = ''
			
	def decode(self, text, **kwargs):
		"""
		decode(self, text, **kwargs)
		Decode the cipher text. (str)
		
		Parameters:
		text: The cipher text. (str)
		dot_dash: Alternate symbols to use for the dot and dash (str)
		"""
		book = {value: key for key, value in self.book.items()}
		text = text.replace('   ', ' <space/> ')
		if kwargs['dot_dash']:
			text = text.replace(kwargs['dot_dash'][0], '*')
			text = text.replace(kwargs['dot_dash'][1], '-')
		plain = ''.join([book.get(word, '') for word in text.split()])
		return plain.replace('<space/>', ' ')
	
	def encode(self, text, **kwargs):
		"""
		encode(self, text, **kwargs)
		Encode the plain text
		
		Parameters:
		text: the plain text (str)
		dot_dash: Alternate symbols to use for the dot and dash (str)
		"""
		if kwargs['decode']:
			return self.decode(text, **kwargs)
		cipher = ' '.join([self.book.get(char, '') for char in text])
		if kwargs['dot_dash']:
			cipher = cipher.replace('*', kwargs['dot_dash'][0])
			cipher = cipher.replace('-', kwargs['dot_dash'][1])
		return cipher
	
	def get_book(self, **kwargs):
		"""
		get_book(self, **kwargs)
		Return the Morse code book. (dict)
		"""
		# check for symbol translation
		if kwargs['dot_dash']:
			book = {key: value.replace('*', kwargs['dot_dash'][0]).replace('-', kwargs['dot_dash'][1])
				for key, value in self.book}
		else:
			book = self.book.copy()
		# check for decoding
		if kwargs['decode']:
			book = {value: key for key, value in book}
		return book

# function instance
morse = Morse()

class Mutating(CipherFunction):
	"""
	mutating(self, text, **kwargs)
	Encipher the text using a mutating substitution. (str)
	
	Parameters:
	alphabet: The starting plain and cipher alphabets. (str)
	mutation: The function to mutate the alphabets with. (str)
	"""
	
	def change_defaults(self):
		"""
		change_defaults(self)
		Set the cipher specific defaults. (None)
		"""
		self.defaults['mutation'] = mutate_shift
		self.defaults['alphabet'] = [string.ascii_uppercase, string.ascii_uppercase]
	
	def encode(self, text, **kwargs):
		"""
		encode(self, text, **kwargs)
		Encode the text using a mutating substitution cipher. (str)
	
		Parameters:
		alphabet: The starting plain and cipher alphabets. (str)
		mutation: The function to mutate the alphabets with. (str)
		"""
		# get the alphabets
		plain, cipher = kwargs['alphabet']
		# check for case insensitivity
		if not kwargs['case']:
			text = text.upper()
		cipher_text, plain_text = '', ''
		# do the encoding/decoding
		for char in text:
			# standard 
			if char in plain:
				if kwargs['decode']:
					plain_text += plain[cipher.index(char)]
					cipher_text += char
				else:
					cipher_text += cipher[plain.index(char)]
					plain_text += char
			# case sensitive
			elif kwargs['case'] and char.upper() in plain:
				if kwargs['decode']:
					plain_text += plain[cipher.index(char.upper())].lower()
					cipher_text += char
				else:
					cipher_text += cipher[plain.index(char.upper())].lower()
					plain_text += char
			# irrelevant characters
			else:
				cipher_text += char
				plain_text += char
			# mutate
			plain, cipher = kwargs['mutation'](plain, cipher, plain_text,
				cipher_text, **kwargs)
		return [cipher_text, plain_text][kwargs['decode']]
		
def mutate_bellaso(plain, cipher, plain_text, cipher_text, **kwargs):
	"""
	mutate_bellaso(plain, cipher, plain_text, cipher_text, **kwargs)
	Mutating alphabet for Bellaso autokey ciphers. (str, str)
	
	Parameters:
	plain: Plain text alphabet. (str)
	cipher: Cipher text alphabet. (str)
	plain_text: The plain text so far. (str)
	cipher_text: The cipher text so far. (str)
	"""
	middle = len(cipher) // 2
	char = plain_text[-1]
	if char in plain or (kwargs['case'] and char.upper() in plain):
		# shift alphabet
		cipher = cipher[1:middle] + cipher[0] + cipher[-1] + cipher[middle:-1]
		# check for reset of alphabet
		check = cipher.index(plain[0])
		if check - middle == kwargs['n']:
			cipher = plain[middle:] + plain[:middle]
	else:
		# switch point in sequence
		last_word = plain_text.split()[-1].upper()
		while last_word[0] not in plain:
			last_word = last_word[1:]
		seq_index = plain.index(last_word[0]) % kwargs['n']
		shift_point = middle + seq_index
		cipher = plain[shift_point:] + plain[middle:shift_point] + plain[:middle]
	return plain, cipher
		
def mutate_chao(plain, cipher, plain_text, cipher_text, **kwargs):
	"""
	mutate_chao(plain, cipher, plain_text, cipher_text, **kwargs)
	Mutating alphabet for the Chaocipher. (str, str)
	
	Parameters:
	plain: Plain text alphabet. (str)
	cipher: Cipher text alphabet. (str)
	plain_text: The plain text so far. (str)
	cipher_text: The cipher text so far. (str)
	"""
	zenith = 0
	nadir = len(plain) // 2 + 1
	cipher_char = cipher_text[-1]
	char = plain_text[-1]
	if char in plain:
		# permute the cipher alphabet
		start = cipher.index(cipher_char)
		cipher = cipher[start:] + cipher[:start]
		cipher = cipher[0] + cipher[2:nadir] + cipher[1] + cipher[nadir:]
		# permute the plain alphabet
		start = plain.index(char) + 1
		plain = plain[start:] + plain[:start]
		plain = plain[:2] + plain[3:nadir] + plain[2] + plain[nadir:]
	return plain, cipher
		
def mutate_sequence(plain, cipher, plain_text, cipher_text, **kwargs):
	"""
	mutate_sequence(plain, cipher, plain_text, cipher_text, **kwargs)
	Mutating alphabet for Bellaso sequence ciphers. (str, str)
	
	Bellaso suggested reflexive alphabets where the secon half of the alphabet
	is shifted each encoding, but after a limited number of times 
	(kwargs['n']) it shifts back to the start of the sequence.
	
	Parameters:
	plain: Plain text alphabet. (str)
	cipher: Cipher text alphabet. (str)
	plain_text: The plain text so far. (str)
	cipher_text: The cipher text so far. (str)
	"""
	char = plain_text[-1]
	if char in plain or (kwargs['case'] and char.upper() in plain):
		middle = len(cipher) // 2
		if len(cipher) % 2:
			raise ValueError('Sequence alphabets must have an even length')
		# shift alphabet
		cipher = cipher[1:middle] + cipher[0] + cipher[-1] + cipher[middle:-1]
		# check for reset of alphabet
		check = cipher.index(plain[0])
		if check - middle == kwargs['n']:
			cipher = plain[middle:] + plain[:middle]
	return plain, cipher

def mutate_shift(plain, cipher, plain_text, cipher_text, **kwargs):
	"""
	mutate_shift(plain, cipher, plain_text, cipher_text, **kwargs)
	Mutating alphabet that shifts the cipher alphabet each character (str, str)
	
	The alphabet is shifted kwargs['n'] characters. It works best if n is
	coprime with the length of the alphabet.
	
	Parameters:
	plain: Plain text alphabet. (str)
	cipher: Cipher text alphabet. (str)
	plain_text: The plain text so far. (str)
	cipher_text: The cipher text so far. (str)
	"""
	char = plain_text[-1]
	# check for actual encoding
	if char in plain or (kwargs['case'] and char.upper() in plain):
		# shift the alphabet
		cipher = cipher[kwargs['n']:] + cipher[:kwargs['n']]
	return plain, cipher
	
def mutate_vinegere(plain, cipher, plain_text, cipher_text, **kwargs):
	"""
	mutate_vinegere(plain, cipher, plain_text, cipher_text, **kwargs)
	Mutating alphabet for the Vinegere cipher. (str, str)
	
	Parameters:
	plain: Plain text alphabet. (str)
	cipher: Cipher text alphabet. (str)
	plain_text: The plain text so far. (str)
	cipher_text: The cipher text so far. (str)
	"""
	# find where you are in the key
	if kwargs['case']:
		index = len([char for char in cipher_text if char.upper() in cipher.upper()])
	else:
		index = len([char for char in cipher_text if char in cipher])
	index = index % len(kwargs['key'])
	# switch the alphabet
	start = plain.index(kwargs['key'][index])
	return plain, plain[start:] + plain[:start]

# function instance
mutating = Mutating()

class AutoBellaso(Mutating):
	"""
	auto_bellaso(self, text, **kwargs)
	Encode using an early Italian autokey cipher. (str)
	
	Bellaso used his sequence alphabets for an autokey cipher, resetting the
	sequence each word based on the first character of the previous word.
	
	text: The text to encode. (str)
	n: The number of sequence alphabets to use. (int)
	"""
	
	def change_defaults(self):
		"""
		Set the cipher specific defaults. (None)
		"""
		self.defaults['mutation'] = mutate_bellaso
		cipher = string.ascii_uppercase[13:] + string.ascii_uppercase[:13]
		self.defaults['alphabet'] = [string.ascii_uppercase, cipher]
		self.defaults['n'] = 5
		
# function instance
auto_bellaso = AutoBellaso()

class Chao(Mutating):
	"""
	chao(self, text, **kwargs)
	Encode using a hard to break mutating cipher. (str)
	
	The Chaocipher was invented by John F. Byrne in 1918. It remained unbroken
	until the details of the cipher were revealed in 2010, but it was never 
	used by the US military because Byrne did not release enough examples for
	it to be evaluated.
	
	Parameters:
	text: The text to encode. (str)
	alphabet: The plain and cipher alphabets ([str, str])
	"""

	def change_defaults(self):
		"""
		change_defaults(self)
		Set the cipher specific defaults. (None)
		"""
		self.defaults['mutation'] = mutate_chao
		self.defaults['alphabet'] = [string.ascii_uppercase, string.ascii_uppercase]
		
	def set_test(self):
		"""
		set_test(self)
		Set the default test for the cipher. (None)
		"""
		self.test_plain = 'WELL DONE IS BETTER THAN WELL SAID.'
		self.test_cipher = 'OAHQ HCNY NX TSZJRR HJBY HQKS OUJY.'
		self.test_kwargs = {'alphabet': ['PTLNBQDEOYSFAVZKGJRIHWXUMC', 'HXUCZVAMDSLKPEFJRIGTWOBNYQ']}

# function instance
chao = Chao()

class Sequence(Mutating):
	"""
	sequence(self, text, **kwargs)
	Encode using an early Italian polyalphabetic cipher. (str)
	
	This was an invention of Giancarmo Bellaso, and was used with additions
	in his Autokey cipher. It starts with a reflexive alphabet made by 
	placing the first half of the alphabet over the second half. Then it
	creates n reflexive alphabets by shifting the bottom half one step n
	times.
	
	Parameters:
	alphabet: The alphabet for the initial reflexive alphabet. (str)
	n: The number of shifts/alphabets to use. (int)
	"""
	
	def change_defaults(self):
		"""
		change_defaults(self)
		Set the cipher specific defaults. (None)
		"""
		self.defaults['mutation'] = mutate_sequence
		self.defaults['n'] = 5
		plain = string.ascii_uppercase
		cipher = plain[13:] + plain[:13]
		self.defaults['alphabet'] = [plain, cipher]
		
# function instance
sequence = Sequence()

class Vinegere(Mutating):
	"""
	vinegere(self, text, **kwargs)
	Encode using a French polyalphabetic cipher. (str)
	
	The Vinegere cipher uses a tabular recta of every possible Caesar alphabet
	and encodes each letter with using a sequence of alphabets determined by
	the keyword. It was actually first described by Giovan Bellaso, but has 
	been generally misattributed to Vinegere. This cipher can also handle 
	running key and one time pad ciphers by using a longer key parameter for
	the running key or one time pad.
	
	Parameters:
	text: The text to encode. (str)
	alphabet: The alphabet to use for the tabula recta. (str)
	key: A key phrase for rotating through the alphabets. (str)
	"""
	
	def __call__(self, text, **kwargs):
		"""
		__call__(self, text, **kwargs)
		Encode using a French polyalphabetic cipher. (str)
		
		The Vinegere cipher uses a tabular recta of every possible Caesar alphabet
		and encodes each letter with using a sequence of alphabets determined by
		the keyword.
		
		Parameters:
		text: The text to encode. (str)
		alphabet: The alphabet to use for the tabula recta. (str)
		key: A key phrase for rotating through the alphabets. (str)
		"""
		# adjust the alphabet for a mutating cipher
		index = kwargs['alphabet'].index(kwargs['key'][0])
		cipher = kwargs['alphabet'][index:] + kwargs['alphabet'][:index]
		kwargs['alphabet'] = [kwargs['alphabet'], cipher]
		# call with the mutating alphabet
		return super(Vinegere, self).__call__(text, **kwargs)
	
	def change_defaults(self):
		"""
		change_defaults(self)
		Set the cipher specific defaults. (None)
		"""
		self.defaults['mutation'] = mutate_vinegere
	
	def set_test(self):
		"""
		set_test(self)
		Set the default test for the cipher. (None)
		"""
		self.test_cipher = 'LXFOPVEFRNHR'
		self.test_plain = 'ATTACKATDAWN'
		self.test_kwargs = {'key': 'LEMON'}
		
# function instances
auto_aca = AutoACA()
vinegere = Vinegere()

class Nihilist(CipherFunction):
	"""
	nihilist(self, text, **kwargs)
	Encode using a 19th century Russion revolutionary cipher. (str)
	
	This cipher was used by Russian anarchists fighting against the czars, and
	it influenced codes used by Russians for 170 years. It uses a polybius 
	square and a further modular key. Although the original did not use modular 
	addition, I included it as an option to make it more secure.
	
	Parameters:
	text: the text to be encoded. (str)
	alphabet: The alphabet for the polybius square. (str)
	deletes: Characters to delete from the text and the alphabet. (str)
	combines: Characters to combine into one cell (list of str)
	key: The key to encode and add to the initial encoding. (str)
	modular: A flag for using modular addition. (str)
	"""
	
	def change_defaults(self):
		"""
		change_defaults(self)
		Set the cipher specific defaults. (None)
		"""
		self.defaults['modular'] = True
		self.defaults['alphabet'] = string.ascii_uppercase.replace('J', '')
		
	def decode(self, text, **kwargs):
		"""
		decode(self, text, **kwargs)
		Decode using a 19th century Russion revolutionary cipher. (str)
		
		Parameters:
		text: the text to be encoded. (str)
		alphabet: The alphabet for the polybius square. (str)
		deletes: Characters to delete from the text and the alphabet. (str)
		combines: Characters to combine into one cell (list of str)
		key: The key to encode and add to the initial encoding. (str)
		modular: A flag for using modular addition. (str)
		"""
		# get the key as numbers
		kwargs['decode'] = False
		polybius_key = polybius(kwargs['key'], **kwargs)
		kwargs['decode'] = True
		# convert the cipher text
		cipher_ints = [int(word) for word in text.split()]
		# convert and lengthen the key
		numeric_key = [int(polybius_key[index:(index + 2)]) for index in range(0, len(polybius_key), 2)]
		numeric_key *= len(cipher_ints) // len(cipher_ints) + len(cipher_ints)
		# use the key
		plain_ints = [cipher - key for cipher, key in zip(cipher_ints, numeric_key)]
		if kwargs['modular']:
			modulus = int(len(kwargs['alphabet']) ** 0.5) * 11
			plain_ints = [num % modulus for num in plain_ints]
		# return the decoded text
		return polybius(''.join([str(num) for num in plain_ints]), **kwargs)
		
	def encode(self, text, **kwargs):
		"""
		encode(self, text, **kwargs)
		Encode using a 19th century Russion revolutionary cipher. (str)
		
		Parameters:
		text: the text to be encoded. (str)
		alphabet: The alphabet for the polybius square. (str)
		deletes: Characters to delete from the text and the alphabet. (str)
		combines: Characters to combine into one cell (list of str)
		key: The key to encode and add to the initial encoding. (str)
		modular: A flag for using modular addition. (str)
		"""
		# check for decoding
		if kwargs['decode']:
			return self.decode(text, **kwargs)
		# encode the key and text
		polybius_text = polybius(text, **kwargs)
		polybius_key = polybius(kwargs['key'], **kwargs)
		# convert to numbers
		numeric_text = [int(polybius_text[index:(index + 2)]) for index in range(0, len(polybius_text), 2)]
		numeric_key = [int(polybius_key[index:(index + 2)]) for index in range(0, len(polybius_key), 2)]
		numeric_key *= len(numeric_text) // len(numeric_key) + len(numeric_key)
		# add the key to the encoded text
		cipher_ints = [poly + key for poly, key in zip(numeric_text, numeric_key)]
		if kwargs['modular']:
			modulus = int(len(kwargs['alphabet']) ** 0.5) * 11
			cipher_ints = [num % modulus for num in cipher_ints]
		# return as a string
		return ' '.join([str(num) for num in cipher_ints])
	
	def set_test(self):
		"""
		set_test(self)
		Set the default test for the cipher. (None)
		"""
		self.test_plain = 'DYNAMITE WINTER PALACE'
		self.test_cipher = '37 106 62 36 67 47 86 26 104 53 62 77 27 55 57 66 55 36 54 27'
		self.test_kwargs = {'alphabet': 'ZEBRASCDFGHIKLMNOPQTUVWXY', 'deletes': 'J', 'modular': False}
		self.test_kwargs['key'] = 'RUSSIAN'
		
# function instance
nihilist = Nihilist()

class Number(CipherFunction):
	"""
	number(self, text, **kwargs)
	Encipher using the first cipher every kid learns. (str)

	Parameters:
	text: the plain text. (str)
	"""
	
	def decode(self, text, **kwargs):
		"""
		decode(self, text, **kwargs)
		Decode the cipher text (str)
		
		Parameters:
		text: the cipher text. (str)
		"""
		book = self.get_book(**kwargs)
		plain = []
		# decode by word
		for word in text.split():
			plain.append(''.join([book[number] for number in word.split('-')]))
		return ' '.join(plain)
	
	def encode(self, text, **kwargs):
		"""
		decode(self, text, **kwargs)
		Encode the plain text. (str)
		
		Parameters:
		text: the plain text. (str)
		"""
		# check for decoding
		if kwargs['decode']:
			return self.decode(text, **kwargs)
		if not kwargs['case']:
			text = text.upper()
		book = self.get_book(**kwargs)
		cipher = []
		# encode by word
		for word in text.split():
			cipher.append('-'.join([book[char] for char in word if char in book]))
		return ' '.join(cipher)
		
	def get_book(self, **kwargs):
		"""
		get_book(self, **kwargs)
		Get the translation book for the cipher. (dict)
		"""
		book = {}
		for index, letter in enumerate(kwargs['alphabet']):
			# fill book based on decode parameter
			if kwargs['decode']:
				book[str(index + 1)] = letter
			else:
				book[letter] = str(index + 1)
		return book
		
# function instance
number = Number()

class Polybius(CipherFunction):
	"""
	polybius(self, text, **kwargs)
	Encipher the text using an ancient Greek cipher. (str)
	
	Polybius didn't make this for hiding information. He made this to make it
	easier to signal messages by reducing the number of symbols that needed
	to be transmitted. However, by assigning each plain text charact to two
	cipher text characters, it allows mixing up the characters (fractionating)
	to disguise frequencies. For this reason it is used in several other
	ciphers, such as ADFGX and Bifid.
	
	Parameters:
	alphabet: The alphabet to fill the square with. (str)
	indexes: The labels for the rows and columns. (str)
	combines: Pairs of letters to fill the same cell. (list of str)
	deletes: Letters to remove from the plain text and alphabet. (str)
	"""
	
	def change_defaults(self):
		"""
		change_defaults(self)
		Set the cipher specific defaults. (None)
		"""
		self.defaults['alphabet'] = string.ascii_uppercase.replace('J', '')
	
	def decode(self, text, **kwargs):
		"""
		decode(self, text, **kwargs)
		Decode the cipher text using a reversed book. (str)
		
		Parameters:
		text: The cipher text. (str)
		indexes: The letters to use for rows/columns of the polybius square. (str)
		alphabet: The alphabet order to use when filling the polybius square. (str)
		combines: Any letters to combine in one cell of the square. (list of str)
		deletes: Letters to remove from the plain text and alphabet. (str)
		"""
		# get the book
		book = self.get_book(**kwargs)
		# reverse it
		for pair in kwargs['combines']:
			del book[pair[1]]
		book = {value: key for key, value in book.items()}
		# prep the text
		text = ''.join([char for char in text if char in kwargs['indexes']])
		text = [text[char_index:(char_index + 2)] for char_index in range(0, len(text), 2)]
		# decipher
		return ''.join([book[pair] for pair in text])
		
	def encode(self, text, **kwargs):
		"""
		encode(self, text, **kwargs)
		Encode the plain text
		
		Parameters:
		text: The cipher text. (str)
		indexes: The letters to use for rows/columns of the polybius square. (str)
		alphabet: The alphabet order to use when filling the polybius square. (str)
		combines: Any letters to combine in one cell of the square. (list of str)
		"""
		if kwargs['decode']:
			return self.decode(text, **kwargs)
		for char in kwargs['deletes']:
			text = text.replace(char, '')
		book = self.get_book(**kwargs)
		return ''.join([book.get(char, '') for char in text.upper()])
		
	def get_book(self, **kwargs):
		"""
		get_book(self, **kwargs)
		Geneate a Polybius Square book for the settings given. (dict)
		
		Parameters:
		indexes: The letters to use for rows/columns of the polybius square. (str)
		alphabet: The alphabet order to use when filling the polybius square. (str)
		combines: Any letters to combine in one cell of the square. (list of str)
		deletes: Letters to remove from the plain text and alphabet. (str)
		"""
		# clean up the alphabet
		alphabet = kwargs['alphabet']
		for char in kwargs['deletes']:
			alphabet = alphabet.replace(char, '')
		# check the width
		width = len(kwargs['indexes'])
		if len(alphabet) != width ** 2:
			raise ValueError('Polybius alphabets must fill the square exactly.')
		# create the book, looping through throught the rows/columns and applying to the alphabet
		book = {}
		for index1, char1 in enumerate(kwargs['indexes']):
			for index2, char2 in enumerate(kwargs['indexes']):
				book[alphabet[index1 + index2 * width]] = char2 + char1
		# account for combined cells
		for pair in kwargs['combines']:
			book[pair[1]] = book[pair[0]]
		# check for case sensitivty
		if kwargs['case']:
			for key, value in book.items():
				book[key.lower()] = value
		return book
		
# function instance
polybius = Polybius()

class RailFence(CipherFunction):
	"""
	rail_fence(self, text, **kwargs)
	Encode text using a diagonal transposition cipher. (str)
	
	Characters are written into a grid diagonally back (SE) and forth (NE), 
	with the cipher text read off in rows. Case sensitive encodings include
	punctuation and spaces.
	
	Parameters:
	n: The height of the rail fence. (int)
	"""
	
	def decode(self, text, **kwargs):
		"""
		decode(self, text, **kwargs)
		Decode the cipher text. (str)
		
		This one took me a while, mainly figuring out the rail (row) lengths based
		on the length of the text and the number of rows. There's probably a 
		simpler mathematical formula for it.
		
		Parameters:
		n: The height of the rail fence. (int)
		"""
		# split out the rails
		# get smallest full rail lengths that contain the message
		full_len = kwargs['n']
		short_rail = 1
		long_rail = 1
		while full_len <= len(text):
			full_len += kwargs['n'] * 2 - 2
			short_rail += 1
			long_rail += 2
		rail_lens = [short_rail] + [long_rail] * (kwargs['n'] - 2) + [short_rail]
		# trim the rail lengths back to fit the message exactly
		for rail_index in range(min(full_len - len(text), kwargs['n'])):
			rail_lens[kwargs['n'] - rail_index - 1] -= 1
		rail_index = 1
		while sum(rail_lens) > len(text):
			rail_lens[rail_index] -= 1
			rail_index += 1
		# split out the rails
		rails = []
		start = 0
		for length in rail_lens:
			rails.append(text[start:(start + length)])
			start += length
		# set up the rails loop
		plain = ''
		rail_index = 0
		rail_mode = 1
		# loop through the rails bleeding off characters
		for dummy in range(len(text)):
			plain += rails[rail_index][0]
			rails[rail_index] = rails[rail_index][1:]
			rail_index += rail_mode
			if rail_index in (-1, kwargs['n']):
				rail_mode *= -1
				rail_index += rail_mode * 2
		return plain
	
	def encode(self, text, **kwargs):
		"""
		encode(self, text, **kwargs)
		Encode the plain text. (str)
		
		Parameters:
		n: The height of the rail fence. (int)
		"""
		if kwargs['decode']:
			return self.decode(text, **kwargs)
		# handle case insensitivity
		if not kwargs['case']:
			text = ''.join([char for char in text.upper() if char in kwargs['alphabet']])
		# set up character loop
		rails = [''] * kwargs['n']
		rail_index = 0
		rail_mode = 1
		# loop through characters assigning to rails
		for char in text:
			rails[rail_index] += char
			rail_index += rail_mode
			if rail_index in (-1, kwargs['n']):
				rail_mode *= -1
				rail_index += rail_mode * 2
		# return joined rails
		return ''.join(rails)
	
	def set_test(self):
		"""
		set_test(self)
		Set the known test for the cipher.
		"""
		self.test_plain = 'We are discovered, flee at once.'
		self.test_cipher = 'WECRLTEERDSOEEFEAOCAIVDEN'
		self.test_kwargs = {}
		
# function instance
rail_fence = RailFence()

class Reflexive(CipherFunction):
	"""
	reflexive(self, text, **kwargs)
	Encode the text using a reflexive substitution. (str)
	
	A reflexive substitution maps the first half of the alphabet on to the 
	second half of the alphabet. This makes encoding and decoding the same
	process. With the English alphabet (the default) this is known as ROT13, 
	and is popular on some internet forums.
	
	Parameters:
	text: The text to encode/decode. (str)
	alphabet: The alphabet to reflect. (str)
	"""
	
	def encode(self, text, **kwargs):
		"""
		encode(self, text, **kwargs)
		Encode the text using a reflexive substitution. (str)
		
		Parameters:
		text: The text to encode/decode. (str)
		alphabet: The alphabet to reflect. (str)
		"""
		# check for valid input
		if len(kwargs['alphabet']) % 2:
			raise ValueError('Reflexive alphabets must have an even length.')
		# generate reflection
		split = len(kwargs['alphabet']) // 2
		cipher = kwargs['alphabet'][split:] + kwargs['alphabet'][:split]
		kwargs['alphabet'] = [kwargs['alphabet'], cipher]
		# encode with substitution
		return substitution(text, **kwargs)
	
	def get_book(self, **kwargs):
		"""
		get_book(self, **kwargs)
		Get the code book for a reflexive substitution. (dict)
		
		Parameters:
		alphabet: The alphabet to reflect. (str)
		"""
		# check for valid input
		if len(kwargs['alphabet']) % 2:
			raise ValueError('Reflexive alphabets must have an even length.')
		# generate reflection
		split = len(kwargs['alphabet']) // 2
		cipher = kwargs['alphabet'][split:] + kwargs['alphabet'][:split]
		kwargs['alphabet'] = [kwargs['alphabet'], cipher]
		# encode with substitution
		return substitution.get_book(**kwargs)
		
# function instance
reflexive = Reflexive()

class OneTimePad(CipherFunction):
	"""
	one_time_pad(self, text, **kwargs)
	Encode using a theoretically unbreakable cipher. (str)
	
	The one time pad is theoretically unbreakable, but can be broken if there
	are patterns in the pad or if the pad is compromised.
	
	This cipher function can also be used for the running key cipher, but that
	is less secure due to potential patterns in the running key.
	
	This cipher function defaults to being case sensitive. Using this cipher
	as case insensitive with a case sensitive alphabet will cause errors in
	the encoding and decoding.
	
	Parameters:
	text: The text to encode. (str)
	key: The one time pad. (str)
	alphabet: The alphabet for combining the key and the text. (str)
	"""
	
	def change_defaults(self):
		"""
		change_defaults(self)
		Set the cipher specific defaults. (None)
		"""
		self.defaults['key'] = '<jkk"Rd@]|K?\\kIxd&2V.&lf2dN)"-2cQRkTIq51[U9$/oPB}G2DTo"WLE?2orbE~]'
		self.defaults['key'] += 'Tp+()I;t}r6JPJ;#\\<!o4ApWhunEsBjO[(9"]T"$(J'
		self.defaults['alphabet'] = string.printable[:-5]
		self.defaults['case'] = True
		
	def encode(self, text, **kwargs):
		"""
		encode(self, text, **kwargs)
		Encode or decode the text. (str)
		
		Parameters:
		text: The text to encode/decode. (str)
		key: The one time pad. (str)
		alphabet: The alphabet for combining the key and the text. (str)
		"""
		# clean up the text
		if not kwargs['case']:
			text = text.upper()
		text = ''.join([char for char in text if char in kwargs['alphabet']])
		# check pad length
		if len(kwargs['key']) < len(text):
			raise ValueError('The one time pad must be at least as long as the text.')
		# prep the loop
		cipher = ''
		divisor = len(kwargs['alphabet'])
		# translate each character
		for plain, pad in zip(text, kwargs['key']):
			plain_index = kwargs['alphabet'].index(plain)
			pad_index = kwargs['alphabet'].index(pad)
			# check for decoding
			if kwargs['decode']:
				cipher += kwargs['alphabet'][(plain_index - pad_index) % divisor]
			else:
				cipher += kwargs['alphabet'][(plain_index + pad_index) % divisor]
		return cipher

# function instance
one_time_pad = OneTimePad()

class Playfair(CipherFunction):
	"""
	Playfair(self, text, **kwargs)
	Encode the text with an English digraphic substitution. (str)
	
	This cipher was invented by Charles Wheatstone in 1854, but bears the name
	of Lord Playfair due to his work in promoting the cipher. It was used by
	the British and Australians for concealing short term tactical secrets.
	Even if the enemy could decipher the message, the information was usually
	out of date before they could.
	
	Encode on Polybius square with pairs of letters. If two letters are the 
	same, replace the second with an X or Q and continue. If they are on the
	same row, replace with the characters to their left. If they are on the
	came column, replace with the characters below. If they make a rectangle,
	replace with the characters on the same row but on the other corner of the
	rectangle.
	"""
	
	def change_defaults(self):
		"""
		change_defaults(self)
		Set the cipher specific defaults. (None)
		"""
		self.defaults['double'] = 'X'
	
	def encode(self, text, **kwargs):
		"""
		encode(self, text, **kwargs)
		Encode the plain text. (str)
		
		Parameters:
		text: The plain text. (str)
		alphabet: The alphabet for the polybius square. (str)
		combines: The combined letters for the square. (list of str)
		deletes: Characters to remove from alphabet and plain text. (str)
		double: The character to substitute for repeated characters. (str)
		"""
		# prep the incoming text
		for char in kwargs['deletes']:
			text = text.replace(char, '')
		if not kwargs['case']:
			text = text.upper()
		# get the code books
		book = self.get_book(**kwargs)
		debook = {value: key for key, value in book.items()}
		# prep the coding loop
		size = int(len(kwargs['alphabet']) ** 0.5)
		shift = [1, -1][kwargs['decode']]
		first = ''
		mid = ''
		cipher = ''
		for char in text:
			if first:
				# encode when you have two characters
				if char in book:
					coord1 = book[first]
					if char == first:
						coord2 = book[kwargs['double']]
					else:
						coord2 = book[char]
					if coord1[0] == coord2[0]:
						coord1 = ((coord1[0] + shift) % size, coord1[1])
						coord2 = ((coord2[0] + shift) % size, coord2[1])
					elif coord1[1] == coord2[1]:
						coord1 = (coord1[0], (coord1[1] + shift) % size)
						coord2 = (coord2[0], (coord2[1] + shift) % size)
					else:
						temp = coord1[1]
						coord1 = coord1[0], coord2[1]
						coord2 = coord2[0], temp
					cipher += debook[coord1]
					cipher += mid
					cipher += debook[coord2]
					mid = ''
					first = ''
				# save intervening characters
				else:
					mid += char
			else:
				# store initial characteres
				if char in book:
					first = char
				else:
					cipher += char
		# clean up any hanging characters
		if first:
			coord1 = book[first]
			coord2 = book[kwargs['double']]
			if coord1[0] == coord2[0]:
				coord1 = ((coord1[0] + shift) % size, coord1[1])
				coord2 = ((coord2[0] + shift) % size, coord2[1])
			elif coord1[1] == coord2[1]:
				coord1 = (coord1[0], (coord1[1] + shift) % size)
				coord2 = (coord2[0], (coord2[1] + shift) % size)
			else:
				coord1, coor2 = (coord1[0], coord2[1]), (coord2[0], coord1[1])
			cipher += book[coord1]
			cipher += mid
			cipher += book[coord2]
		else:
			cipher += mid
		# clean up deletes
		if kwargs['decode']:
			for pair in kwargs['combines']:
				cipher = cipher.replace(pair[1], pair[0])
		return cipher
	
	def get_book(self, **kwargs):
		"""
		get_book(self, **kwargs)
		Get the translation book for the cipher. (dict)
		"""
		book = {}
		alphabet = kwargs['alphabet']
		# clean up alphabets
		for bad in kwargs['deletes']:
			alphabet = alphabet.replace(bad, '')
		for pair in kwargs['combines']:
			alphabet = alphabet.replace(pair[1], '')
		# associate letters with coordinates
		size = int(len(alphabet) ** 0.5)
		for row in range(size):
			for col in range(size):
				book[alphabet[row * size + col]] = (row, col)
				if kwargs['case']:
					book[alphabet[row * size + col].lower()] = (row, col) 
		for pair in kwargs['combines']:
			book[pair[1]] = book[pair[0]]
		return book
		
# function instance
playfair = Playfair()

class Scytale(Columnar):
	"""
	scytale(self, text, **kwargs)
	Encode the text using the simplest of machine ciphers. (str)
	
	text: The text to encode/decode. (str)
	n: The diameter of the scytale in characters. (int)
	"""
	
	def change_defaults(self):
		"""
		change_defaults(self)
		Set the cipher specific defaults. (None)
		"""
		# base them on columnar defaults
		super(Scytale, self).change_defaults()
		self.defaults['n'] = 3
	
	def __call__(self, text, **kwargs):
		"""
		 __call__(self, text, **kwargs)
		Handle encoding/decoding requests. (str)
		
		This mainly modifies the paramters so a columnar cipher can be used.
		I'm not sure this was the right way to do it, but it works.
		
		text: The text to encode/decode. (str)
		n: The diameter of the scytale in characters. (int)
		"""
		# do some of the standard call handling.
		neokwargs = self.defaults.copy()
		neokwargs.update(kwargs)
		if not neokwargs['case']:
			text = ''.join([char for char in text.upper() if char in neokwargs['alphabet']])
		# calculate the number of columns for the give row height
		neokwargs['n'] = len(text) // neokwargs['n']
		if len(text) % neokwargs['n']:
			neokwargs['n'] += 1
		# generate an unmixing key for the number of columns
		neokwargs['key'] = string.ascii_uppercase[:neokwargs['n']]
		return super(Scytale, self).__call__(text, **neokwargs)
	
	def set_test(self):
		"""
		set_test(self)
		Set the default test for the cipher.
		"""
		self.test_plain = 'Help me I am under attack.'
		self.test_cipher = 'HENTEIDTLAEAPMRCMUAK'
		self.test_kwargs = {'n': 4}
		
# function instance
scytale = Scytale()

class Solitaire(CipherFunction):
	"""
	solitaire(self, text, **kwargs)
	Encode the text using a deck of cards. (str)
	
	This was invented by Bruce Schneier for Neil Stephenson to use in the 
	book Cryptonomicon, where it was called Pontifex. It uses a deck of cards
	to create a keystream for modular encryption. Paul Crowley has discovered 
	problems with the cipher, that show it to be less secure than is claimed 
	in the book. But his analysis appears to hinge on an incorrect 
	interpretation of the algorithm.
	
	The key is a deck of cards with an A joker and a B joker. It can be a list
	of integers or a list of strings. Integer values are 1-52 for Ace through
	King in bridge suit order (clubs, diamonds, hearts, spades). As strings
	card ranks are A23456789TJQK, suits are CDHS, and the jokers are XA and 
	XB. So the dead man's hand is AC, AS, 8C, 8S, QC.
	
	Parameters:
	text: The text to encode. (str)
	key: A deck of cards with two jokers. (list of str or list of int)
	"""
	
	def card_str(self, card):
		"""
		card_str(self, card)
		Convert a card in integer form to string form. (int)
		
		This is to aid in creating copies of keyed decks.
		
		Parameters:
		card: An integer representing a card. (int)
		"""
		if card > 52:
			return ['XA', 'XB'][card - 53]
		card = 'A23456789TJQK'[(card - 1) % 13]
		return card + 'CDHS'[(card - 1) // 13]
	
	def card_int(self, card):
		"""
		card_int(self, card)
		Convert a card in string form to integer form. (int)
		
		As strings card ranks are A23456789TJQK, suits are CDHS, and the 
		jokers are XA and XB. So the dead man's hand is AC, AS, 8C, 8S, QC.
		
		Parameters:
		card: A playing card as two characters. (str)
		"""
		if card[0] == 'X':
			return 53 + card[1] == 'B'
		return ' A23456789TJQK'.index(card[0]) + 13 * 'CDHS'.index(card[1])
	
	def encode(self, text, **kwargs):
		"""
		encode(self, text, **kwargs)
		Encode the text using a deck of cards. (str)
		
		Parameters:
		text: The text to encode. (str)
		key: A deck of cards with two jokers. (list of str or list of int)
		"""
		# prep the text
		text = [char for char in text.upper() if char in kwargs['alphabet']]
		# prep the deck
		if isinstance(kwargs['key'], str):
			deck = self.keyed_deck(kwargs['key'][:])
		elif isinstance(kwargs['key'][0], str):
			deck = [self.card_int(card) for card in kwargs['key'][:]]
		else:
			deck = kwargs['key'][:]
		# encode the text
		cipher_text = ''
		for char in text:
			repeat = True
			while repeat:
				# do the base mutation
				deck = self.mutation_base(deck)
				# find key
				count = min(deck[0], 53)
				key = deck[count]
				# loop if key is a joker
				repeat = key > 51
			# check for decoding
			if kwargs['decode']:
				key_index = (kwargs['alphabet'].index(char) - (key  % 26)) % 26
			else:
				key_index = (kwargs['alphabet'].index(char) + (key  % 26)) % 26
			cipher_text += kwargs['alphabet'][key_index]
		return cipher_text
		
	def keyed_deck(self, key, **kwargs):
		"""
		keyed_deck(self, key, **kwargs)
		Create a keysteam deck using a key word. (list of int)
		
		Bruce Schneier recommends at least a 64-80 character string for this
		method of creating a deck keystream.
		
		Parameters:
		key: A key word or phrase for keying the deck. (str)
		as_string: A flag for returning the deck in string form. (bool)
		"""
		alphabet = kwargs.get('alphabet', self.defaults['alphabet'])
		as_string = kwargs.get('as_string', False)
		deck = list(range(1, 55))
		# prep the text
		key = [char for char in key.upper() if char in alphabet]
		for char in key:
			# do the base mutation
			deck = self.mutation_base(deck)
			# count cut based on key
			index = alphabet.index(char) + 1
			deck = deck[index:-1] + deck[:index] + deck[-1:]
		if as_string:
			deck = [self.card_str(card) for card in deck]
		return deck
	
	def mutation_base(self, deck):
		"""
		mutation_base(self, deck)
		The main part of the keystream mutation. (list of int)
		
		This part is common to both the encryption/decryption of the deck and 
		creating a keyed deck based on a pass phrase.
		
		Parameters:
		deck: The keystream (card deck) to be mutated. (list of int)
		"""
		# move A joker
		joker_a = deck.index(53)
		deck.pop(joker_a)
		if joker_a == 53:
			deck.insert(1, 53)
		else:
			deck.insert(joker_a + 1, 53)
		# move B joker
		joker_b = deck.index(54)
		deck.pop(joker_b)
		if joker_b > 51:
			deck.insert(joker_b - 51, 54)
		else:
			deck.insert(joker_b + 2, 54)
		# triple cut
		joker1 = deck.index(53)
		joker2 = deck.index(54)
		if joker2 < joker1:
			joker1, joker2 = joker2, joker1
		joker2 += 1
		deck = deck[joker2:] + deck[joker1:joker2] + deck[:joker1]
		# count cut
		count = min(deck[-1], 53)
		deck = deck[count:-1] + deck[:count] + deck[-1:]
		return deck
		
	def set_test(self):
		"""
		set_test(self)
		Set the default test for the cipher. (None)
		
		Alternate test with keyed deck:	
		self.test_plain = 'AAAAAAAAAA'
		self.test_cipher = 'EXKYIZSGEH'
		self.test_kwargs = {'key': list(range(1, 55))}
		"""
		self.test_plain = 'SOLITAIREX'
		self.test_cipher = 'KIRAKSFJAN'
		self.test_kwargs = {'key': 'CRYPTONOMICON'}
		
# function instance
solitaire = Solitaire()
pontifex = Solitaire()

class Straddling(CipherFunction):
	"""
	straddling(self, text, **kwargs)
	Encode the text using a Russian substitution cipher. (str)
	
	A straddling checkerboard is a way of encoding text to numbers with
	fractionation and data compression. It uses one digit numbers for the
	most common letters, but leaves two digits to be the tens digit for the
	less common letters. This also helps disguise frequencies. The straddling
	checkerboard was part of the VIC cipher used by the Russian spy Reino
	Hayhanen in the 1950s.
	
	Note that the alphabet must contain two spaces, and must be 30 characters
	long.
	
	Parameters:
	text: The text to encode/decode. (str)
	alphabet: The alphabet for the straddling checkerboard. (str)
	"""
	
	def change_defaults(self):
		"""
		change_defaults(self)
		Set the cipher specific defaults.
		"""
		self.defaults['alphabet'] = 'A SIN TOERBCDFGHJKLMPQUVWXYZ. '
	
	def decode(self, text, **kwargs):
		"""
		decode(self, text, **kwargs)
		Decode the cipher text. (str)
	
		Parameters:
		text: The text to encode/decode. (str)
		alphabet: The plain and cipher alphabets. (list of str)
		"""
		# get the deciphering book
		book = self.get_book(**kwargs)
		# determine the row indexes
		first_blank = kwargs['alphabet'].index(' ')
		next_blank = kwargs['alphabet'].index(' ', first_blank + 1)
		extras = str(first_blank) + str(next_blank)
		# set up the decode loop
		previous_char = ''
		plain = ''
		# loop through characters
		for char in text:
			# check for row indexes
			if char in extras and not previous_char:
				previous_char = char
			else:
				# decode one or two characters as appropriate
				plain += book[previous_char + char]
				previous_char = ''
		return plain

	def encode(self, text, **kwargs):
		"""
		encode(self, text, **kwargs)
		Encode the plain text. (str)
	
		Parameters:
		text: The text to encode/decode. (str)
		alphabet: The plain and cipher alphabets. (list of str)
		"""
		# check for decoding
		if kwargs['decode']:
			return self.decode(text, **kwargs)
		# encoding is simple substitution
		book = self.get_book(**kwargs)
		if not kwargs['case']:
			text = text.upper()
		return ''.join([book.get(char, '') for char in text])
		
	def get_book(self, **kwargs):
		"""
		get_book(self, **kwargs)
		Return the code book for the cipher.
		
		Parameters:
		alphabet: The alphabet for the straddling checkerboard. (str)
		"""
		book = {}
		extras = ''
		for char_index, char in enumerate(kwargs['alphabet']):
			# get first row, storing row indexes
			if char_index < 10:
				if char == ' ':
					extras += str(char_index)
				else:
					book[char] = str(char_index)
			# get second and third rows
			elif char_index < 20:
				book[char] = extras[0] + str(char_index - 10)
			elif char_index < 30:
				book[char] = extras[1] + str(char_index - 20)
		# reverse for decoding
		if kwargs['decode']:
			book = {value: key for key, value in book.items()}
		return book
	
	def set_test(self):
		"""
		set_test(self)
		Set the cipher specific tests.
		"""
		self.test_plain = 'ATTACK AT DAWN'
		self.test_cipher = '3113212731223655'
		self.test_kwargs = {'alphabet': 'ET AON RISBCDFGHJKLMPQ/UVWXYZ.'}
		
# function instance
straddling = Straddling()

class Substitution(CipherFunction):
	"""
	substitution(self, text, **kwargs)
	Encode the text using a basic substitution cipher. (str)
	
	Parameters:
	text: The text to encode/decode. (str)
	alphabet: The plain and cipher alphabets. (list of str)
	"""

	def change_defaults(self):
		"""
		change_defaults(self)
		Set the cipher specific defaults. (None)
		
		The second alphabet reverses pairs of letters that are adjacent in the 
		frequency list, doing consonants and vowels separately. The idea is to
		make the cipher text somewhat pronounceable.
		"""
		plain = string.ascii_uppercase
		cipher = 'EPLRAGFSOXVCWTIBZDHNYKMJUQ'
		self.defaults['alphabet'] = [plain, cipher]

	def encode(self, text, **kwargs):
		"""
		encode(self, text, **kwargs)
		Encode the plain text. (str)
	
		Parameters:
		text: The text to encode/decode. (str)
		alphabet: The plain and cipher alphabets. (list of str)
		"""
		book = self.get_book(**kwargs)
		if not kwargs['case']:
			text = text.upper()
		return ''.join([book.get(char, char) for char in text])

	def get_book(self, **kwargs):
		"""
		get_book(self, **kwargs)
		Get the book for the supplied alphabets.
	
		Parameters:
		text: The text to encode/decode. (str)
		alphabet: The plain and cipher alphabets. (list of str)
		"""
		book = {}
		for plain, cipher in zip(*kwargs['alphabet']):
			book[plain] = cipher
			if kwargs['case']:
				book[plain.lower()] = cipher.lower()
		if kwargs['decode']:
			book = {value: key for key, value in book.items()}
		return book
	
# function instance
substitution = Substitution()

class Keyword(Substitution):
	"""
	keyword(self, text, **kwargs)
	Encode the text using a keyword alphabet. (str)
	
	Keyword creates a simple substitution alphabet from the unique letters in
	the key (in the order they appear) followed by the letters not in the key
	(in alphabetic order).
	
	To get just the alphabet (as they are often used in other ciphers), use 
	substitution.get_alphabet().
	
	Parameters:
	key: The keyword to start the alphabet. (str)
	alphabet: The alphabet to add to the keyword. (str)
	"""
	
	def change_defaults(self):
		"""
		change_defaults(self)
		Set the cipher specific defaults.
		"""
		super(Keyword, self).change_defaults()
		self.defaults['alphabet'] = string.ascii_uppercase
	
	def get_alphabet(self, **kwargs):
		"""
		get_alphabet(self, **kwargs)
		Get the alphabet based on the key.
		
		Parameters:
		key: The keyword to start the alphabet. (str)
		alphabet: The alphabet to add to the keyword. (str)
		"""
		# double check defaults for external usage
		keyed_alpha = kwargs.get('key', self.defaults['key'])
		plain_alpha = kwargs.get('alphabet', self.defaults['alphabet'])
		# clean up the key
		keyed_alpha = [char for index, char in enumerate(keyed_alpha) if char not in kwargs['key'][:index]]
		# add the rest of the alphabet
		keyed_alpha += [char for char in kwargs['alphabet'] if char not in keyed_alpha]
		return ''.join(keyed_alpha)
	
	def get_book(self, **kwargs):
		"""
		get_book(self, **kwargs)
		Get the code book for the keyed alphabet.
		
		Parameters:
		key: The keyword to start the alphabet. (str)
		alphabet: The alphabet to add to the keyword. (str)
		"""
		# get the alphabet
		cipher = self.get_alphabet(**kwargs)
		# treat as substitution on keyed alphabet
		kwargs['alphabet'] = [kwargs['alphabet'], cipher]
		return super(Keyword, self).get_book(**kwargs)
		
# function instance
keyword = Keyword()

class Trifid(CipherFunction):
	"""
	trifid(self, text, **kwargs)
	Encode the text with a trigraphic cipher. (str)
	
	Trifid (unrelated to Day of the Trifids) was invented in 1901 by Felix
	Delastelle, who also created Bifid and Four Square. It is similar to Bifid,
	but in Trifid each cipher text character is dependent on three plain text
	characters rather than two as in Bifid.
	
	Parameters:
	text: The text to encode. (str)
	alphabet: The alphabet to fill the Delastelle cube. (str)
	"""
	
	def change_defaults(self):
		"""
		change_defaults(self)
		Set the cipher specific defaults.
		"""
		self.defaults['alphabet'] += '.'
		self.defaults['indexes'] = '123'
	
	def decode(self, text, **kwargs):
		"""
		decode(self, text, **kwargs)
		Decode the cipher text. (str)
		
		Parameters:
		text: The text to decode. (str)
		alphabet: The alphabet for the Delastelle cube. (str)
		"""
		# encode with cube to get the coordinates
		kwargs['decode'] = False
		coordinates = delastelle(text, **kwargs)
		# interleave the coordinates
		plain_len = len(coordinates) // 3
		first = coordinates[:plain_len]
		second = coordinates[plain_len:(-plain_len)]
		third = coordinates[-plain_len:]
		coordinates = ''.join(a + b + c for a, b, c in zip(first, second, third))
		# decode with polybius to get the plain text
		kwargs['decode'] = True
		return delastelle(coordinates, **kwargs)
	
	def encode(self, text, **kwargs):
		"""
		encode(self, text, **kwargs)
		Encode the plain text. (str)
		
		Parameters:
		text: The text to encode. (str)
		alphabet: The alphabet for the Delastelle cube. (str)
		"""
		# check for trifid decoding
		if kwargs['decode']:
			return self.decode(text, **kwargs)
		# encode with delastelle to get the coordinates
		coordinates = delastelle(text, **kwargs)
		# split out the row and column coordinates
		coordinates = coordinates[0::3] + coordinates[1::3] + coordinates[2::3]
		# decode with delastelle to get the cipher text
		kwargs['decode'] = True
		return delastelle(coordinates, **kwargs)

# function instance
trifid = Trifid()

class TwoSquare(CipherFunction):
	"""
	two_square(self, text, **kwargs)
	Encode the text using a mid-range digraphic cipher. (str)
	
	Two Square was meant to be a compromise between the complicated Four
	Square and the less secure Playfair. It uses two squares in either a 
	vertical or horizontal arrangement. Pairs forming rectangles are coded
	as in Playfair, using the other corners of the rectangle. Other pairs
	are left uncoded (transparency), but in some cases are reversed.
	
	Note that the reverse parameter defaults to True for horizontal set ups
	and False for vertical ones.
	
	Parameters:
	text: text to encode/decode. (str)
	alphabet: Two alphabets for the two squares. (list of str)
	combines: Pairs of letters to combine into one cell. (list of str)
	deletes: Letters to remove from the alphabets and the text. (str)
	vertical: A flag for using a vertical square arrangement. (bool)
	reverse: A flag for using reverse transparency. (bool)
	"""
	
	def change_defaults(self):
		"""
		change_defaults(self)
		Set the cipher specific defaults.
		"""
		self.defaults['alphabet'] = [string.ascii_uppercase, string.ascii_uppercase[::-1]]
		self.defaults['combines'] = ['IJ']
		self.defaults['deletes'] = ''
		self.defaults['vertical'] = True
		self.defaults['reverse'] = None
		
	def encode(self, text, **kwargs):
		"""
		encode(self, text, **kwargs)
		Encode the text using a digraphic cipher. (str)
		
		Parameters:
		text: The text to encode. (str)
		alphabet: Two alphabets for the Polybius squares. (list of str)
		combines: The letters to combine in the squares. (str)
		deletes: The letters to delete from the text and alphabets. (str)
		vertical: A flag for vertical (not horizontal) square orientation. (str)
		reverse: A flag for reversing any transparency. (str)
		"""
		# default of reverse depends on vertical
		if kwargs['reverse'] is None:
			kwargs['reverse'] = not kwargs['vertical']
		# clean up alphabets:
		for char in kwargs['deletes']:
			kwargs['alphabet'][0] = kwargs['alphabet'][0].replace(char, '')
			kwargs['alphabet'][1] = kwargs['alphabet'][1].replace(char, '')
		for pair in kwargs['combines']:
			kwargs['alphabet'][0] = kwargs['alphabet'][0].replace(pair[1], '')
			kwargs['alphabet'][1] = kwargs['alphabet'][1].replace(pair[1], '')
		# check for case insensitivity
		if not kwargs['case']:
			text = text.upper()
		# get the books
		first_book, second_book = self.get_book(**kwargs)
		first_debook = {value: key for key, value in first_book.items()}
		second_debook = {value: key for key, value in second_book.items()}
		# encode the text
		first, mid, cipher = '', '', ''
		for char in text:
			if first:
				if char in second_book:
					# encode when you have two characters
					coord1 = first_book[first]
					coord2 = second_book[char]
					# check for orientation
					if kwargs['vertical']:
						# check for transparency
						if coord1[1] == coord2[1]:
							if kwargs['reverse']:
								cipher += first_debook[coord2] + mid + second_debook[coord1]
							else:
								cipher += first_debook[coord1] + mid + second_debook[coord2]
						else:
							# encode using the other corners of the rectangle
							decoord1 = coord1[0] + coord2[1]
							decoord2 = coord2[0] + coord1[1]
							cipher += first_debook[decoord1] + mid + second_debook[decoord2]
					else:
						# check for transparency
						if coord1[0] == coord2[0]:
							if kwargs['reverse']:
								cipher += first_debook[coord2] + mid + second_debook[coord1]
							else:
								cipher += first_debook[coord1] + mid + second_debook[coord2]
						else:
							# encode using the other corners of the rectangle
							decoord1 = coord2[0] + coord1[1]
							decoord2 = coord1[0] + coord2[1]
							cipher += first_debook[decoord1] + mid + second_debook[decoord2]
					# reset digraph tracking
					first, mid = '', ''
				else:
					# store uncoded characters
					mid += char
			elif char in first_book:
				# get the first part of the digraph
				first = char
			else:
				# pass on uncoded characters
				cipher += char
		# clean up combines
		for pair in kwargs['combines']:
			cipher = cipher.replace(pair[1], pair[0])
		return cipher
		
	def get_book(self, **kwargs):
		"""
		get_book(self, **kwargs)
		Return the two dictionaries for the two squares. (tuple of dict)
		
		Parameters:
		alphabet: Two alphabets for the Polybius squares. (list of str)
		combines: The letters to combine in the squares. (str)
		deletes: The letters to delete from the text and alphabets. (str)
		"""
		# split out the alphabets
		first_alpha, second_alpha = kwargs['alphabet']
		# get the first book
		kwargs['alphabet'] = first_alpha
		first_book = polybius.get_book(**kwargs)
		# get the second book
		kwargs['alphabet'] = second_alpha
		second_book = polybius.get_book(**kwargs)
		return first_book, second_book

def pad(text, n, char = 'X'):
	"""
	pad(text, n, char = 'X')
	Pad the text to fit a set number of columns or text blocks. (str)
	
	Parameters:
	text: The text to pade. (int)
	n: The size of the text block to fit. (int)
	char: The character(s) to pad the text with. (str)
	"""
	char = char * n
	if len(text) % n:
		text += char[:(n - len(text) % n)]
	return text

def full_test(text = 'Wily Python quick sort fixes dumb Java lazy learning.', verbose = 1):
	"""
	full_test(text = 'Wily Python quick sort fixes dumb Java lazy learning.',
		verbose = 1)
	Test all of the cipher functions. (dict)
	
	The return value contains the full results of all the tests. It is a 
	dictionary keyed to the names of the CipherFunction sub-classes. The 
	values are dictionaries keyed to requested (if was requested) and default
	(if the sub-class has a default test), with the results as values. The
	results are tuples of the encoded text, the match ratio for the encoded
	text (-1 for requested tests), the decoded text, and the match ratio for
	the decoded text. For information on the match ratios, see the difflib
	module.
	
	The verbose parameter has three meaningful values. 0 means no output. 1 
	means only print warnings for results with low match ratios (below 0.6).
	2 means full results for every test, with the warnings for low match
	ratios afterwards.
	
	Parameters:
	text: The text for requested tests. (str)
	verbose: How much output to print. (int)
	"""
	# get the sub-classes of CipherFunction
	ciphers = [cls for cls in CipherFunction.__subclasses__()]
	while True:
		extras = []
		for cls in ciphers:
			extras.extend([sub for sub in cls.__subclasses__() if sub not in ciphers])
		if extras:
			ciphers += extras
		else:
			break
	# prep the test loop
	results = {}
	output = [[], []]
	# test each cipher
	for cipher in ciphers:
		#print(cipher.__name__)
		cipher_func = cipher()
		results[cipher.__name__] = {}
		# do the default test if there is one
		if cipher_func.test_plain:
			default = cipher_func.test(verbose = 0)
			results[cipher.__name__]['default'] = default
			# generate output (verbose = 1)
			if default[1] < 0.6:
				message = 'Low cipher ratio ({:.3}) for {} default.'
				output[0].append(message.format(default[1], cipher.__name__))
			if default[3] < 0.6:
				message = 'Low plain ratio ({:.3}) for {} default.'
				output[0].append(message.format(default[3], cipher.__name__))
			# generate output (verbose = 2)
			output[1].append(cipher.__name__ + ' Default:')
			output[1].append('CIPHER: {} ({:.3})'.format(default[0], default[1]))
			output[1].append('PLAIN: {} ({:.3})\n'.format(default[2], default[3]))
		# run the requested test if there is one
		if text:
			requested = cipher_func.test(text, verbose = 0)
			results[cipher.__name__]['requested'] = requested
			# generate the output (verbose = 1)
			if requested[3] < 0.6:
				message = 'Low plain ratio ({:.3}) for {} requested.'
				output[0].append(message.format(requested[3], cipher.__name__))
			# generate the output (verbose = 2)
			output[1].append(cipher.__name__ + ' Requested:')
			output[1].append('CIPHER: {}'.format(requested[0]))
			output[1].append('PLAIN: {} ({:.3})\n'.format(requested[2], requested[3]))
	# final verbose = 1 output
	output[0].append('\n{} ciphers tested.'.format(len(ciphers)))
	# display output based on verbose level
	for output_index in range(verbose - 1, -1, -1):
		for line in output[output_index]:
			print(line)
		print()
	# return the full results
	return results

if __name__ == '__main__':
	results = full_test(verbose = 2)
	a = {char: index for index, char in enumerate(string.ascii_lowercase)}