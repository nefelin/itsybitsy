from tracker import Tracker
from torrent import Torrent
import sys


torrent = Torrent(sys.argv[1])
tracker = Tracker(torrent)
print(tracker.connect())