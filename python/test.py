#!/usr/bin/env python
import csv
from run import Person


def make_bool(value):
    if value == 'Yes':
        return True
    if value == 'No':
        return False
    return None


if __name__ == "__main__":
    # open up the csv file containing the tests
    with open('../shared/example_beards.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        passes = 0
        failures = 0

        # Read each line
        for row in csv_reader:
            if line_count > 0: # skip the line with headers
                test_num = line_count - 1

                # call our Rules as Code python
                bob = Person()
                bob.facial_hair_length_gt_5 = make_bool(row[0])
                bob.facial_hair_on_chin = make_bool(row[1])
                bob.facial_hair_uninterupted = make_bool(row[2])

                expected = make_bool(row[3]) # value the csv says we should get
                result = bob.has_a_beard() # the value our code retuns

                # Check we got the same result as the csv said
                try:
                    assert result == expected
                except AssertionError as e:
                    # got a different result, print it
                    print("Test {test_num}. Expected {expected}, got {result}.".format(
                        test_num=test_num, result=result, expected=expected))
                    failures += 1
                else:
                    passes += 1

            line_count += 1
        # Print a summary
        print('Run {line_count} tests. {passes} passes. {failures} failures.'.format(
            line_count=line_count-1, passes=passes, failures=failures))
