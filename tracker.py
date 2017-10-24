# import aiohttp
import bencodepy
from torrent import Torrent
from urllib.parse import urlencode
from urllib import request
import random

def _generate_peer_id():
	return '-PC0001-' + ''.join([str(random.randint(0, 9)) for _ in range(12)])

class Tracker():
	def __init__(self, torrent):
		self.torrent = torrent
		self.peer_id = _generate_peer_id()
		# self.http_client = aiohttp.ClientSession()

	def connect(self):
		params = {
			'info_hash': self.torrent.info_hash,
			'peer_id': self.peer_id,
			'port': 6889,
			'uploaded': 0,
			'downloaded': 0,
			'left': self.torrent.total_size,
			'compact': 1,
		}

		url = self.torrent.announce + '?' + urlencode(params)

		print(url)
		data = request.urlopen(url).read()
		return bencodepy.decode(data)
		# with self.http_client.get(url) as response:
		# with request.urlopen(url) as response:
		# 	if not response.status == 200:
		# 		raise ConnectionError('unable to connect to tracker')
		# 	data = response.read()
		# 	return bencodepy.decode(data)