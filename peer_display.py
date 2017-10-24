#parse torrent file
import bencodepy
import sys

class Parser():
	def __init__(self, filepath):
		print("hello")
		self.file = filepath
		self.data = self.parse_file(self.file)

	def read_file(self, input_file):
		with open(input_file, 'rb') as file:
			data = file.read()
		return data

	def parse_file(self, input_file):
		data = self.read_file(input_file)
		data = bencodepy.decode(data)
		return data

	def __repr__(self):
		return '<Parser>' + str(self.data[b'info'][b'name'])


if __name__ == "__main__":
	try:
		p = Parser(sys.argv[1])
		print(p)
		pass

	except IndexError:
			print("Need file as argument")



#connect to the tracker

#populate list of available peers

#display that list