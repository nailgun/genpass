import hashlib
import sys
import common
import time
import pickle

test_duration = 10
digest = 'test'

common.set_niceness()

total_time = None
iterations_to_measure = 100000
total_measures = 0
iterations = iterations_to_measure
total_iterations = 0
starttime = time.time()
while total_time is None:
    digest = hashlib.md5(digest).hexdigest()
    total_iterations += 1
    iterations -= 1
    if iterations == 0:
        total_measures += 1
        iterations = iterations_to_measure
        endtime = time.time()
        total_time = endtime - starttime
        if total_time < test_duration:
            total_time = None

speed = total_iterations / total_time
print 'total measures done: %d' % total_measures
print 'speed: %d hashes/sec' % speed
print '1 day needs %d iterations' % (speed * 24 * 60 * 60)

speed_file = open(common.here('speed.dat'), 'wb')
pickle.dump(speed, speed_file, pickle.HIGHEST_PROTOCOL)
del speed_file
