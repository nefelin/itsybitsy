from hashlib import sha1
import sys
import bencodepy

class Torrent():
	def __init__(self, filepath):
		self.file = filepath

		with open(self.file, 'rb') as f:
			self.meta_info = f.read()
			self.meta_info = bencodepy.decode(self.meta_info)
			info = bencodepy.encode(self.meta_info[b'info'])
			self.info_hash = sha1(info).digest()
			self.count_files()

	def count_files(self):
		if b'files' in self.meta_info[b'info']:
			raise RuntimeError('One file at a time please!')

	@property
	def announce(self):
		return self.meta_info[b'announce'].decode('utf-8')

	@property
	def total_size(self):
		return self.meta_info[b'info'][b'length']

