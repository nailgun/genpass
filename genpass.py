import hashlib
import sys
import common

counter = int(sys.argv[1])
digest = 'hello'

common.set_niceness()

while counter:
    digest = hashlib.md5(digest).hexdigest()
    counter -= 1

print digest[:10]
