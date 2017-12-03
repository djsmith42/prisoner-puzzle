from random import shuffle, seed
from collections import defaultdict
from datetime import datetime

ITERATIONS = 1000000
PRISONER_COUNT = 100

def main():
    successful_runs = 0
    histogram = defaultdict(int)
    for run in xrange(ITERATIONS):
        if run > 0 and run % 10000 == 0:
            print "run {} of {} ({}%)".format(run+1, ITERATIONS, run*100/ITERATIONS)
        boxes = generate_boxes(PRISONER_COUNT)
        prisoners_who_found_their_number = sum(find_prisoner_number(prisoner, boxes) for prisoner in range(PRISONER_COUNT))
        histogram[prisoners_who_found_their_number] += 1
        if prisoners_who_found_their_number >= PRISONER_COUNT:
            successful_runs += 1

    print 'Histogram of successful prisoner counts:'
    for count in range(PRISONER_COUNT+1):
        print '{}\t{}'.format(count, histogram[count])

    print 'Successful runs: {} of {} ({}%)'.format(successful_runs, ITERATIONS,
            round(float(successful_runs)/float(ITERATIONS)*100, 3))

def find_prisoner_number(prisoner, boxes):
    number = boxes[prisoner] # starting number
    max_tries = len(boxes)/2
    for _ in range(max_tries):
        if number == prisoner: # found my number
            return True
        number = boxes[number]
    return False

def generate_boxes(n):
    seed(datetime.now()) # to ensure nice random box shuffling
    boxes = range(n)
    shuffle(boxes)
    assert len(set(boxes)) == n
    return boxes

if __name__ == '__main__':
    main()
