import time
import notify2
import os
from xmlParse import Matches

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
iconPath = dname + "/cricbuzz.png"

Matches = Matches()

notify2.init("Score Notifier")

n = notify2.Notification(None,icon = iconPath)

n.set_urgency(notify2.URGENCY_NORMAL)

n.set_timeout(10000)

for match in Matches:
	n.update(match['name'], match['status'])
	n.show()
	time.sleep(15)