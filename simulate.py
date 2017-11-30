from random import shuffle, seed
from collections import defaultdict
from datetime import datetime

ITERATIONS = 100000
PRISONER_COUNT = 100

def main():
    successful_runs = 0
    histogram = defaultdict(int)
    for _ in xrange(ITERATIONS):
        boxes = generate_boxes(PRISONER_COUNT)
        prisoners_who_found_their_number = 0
        for prisoner in range(len(boxes)):
            if find_prisoner_number(prisoner, boxes):
                prisoners_who_found_their_number += 1
        histogram[prisoners_who_found_their_number] += 1
        if prisoners_who_found_their_number >= len(boxes)/2:
            successful_runs += 1

    print 'Histogram of successful prisoner counts:'
    for success_count in range(PRISONER_COUNT):
        print '{}\t{}'.format(success_count, histogram[success_count])

    print 'Successful runs: {} of {} ({}%)'.format(successful_runs, ITERATIONS,
            round(float(successful_runs)/float(ITERATIONS)*100, 1))


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
    return boxes

if __name__ == '__main__':
    main()