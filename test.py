#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'stringAnagram' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY dictionary
#  2. STRING_ARRAY query
#

def stringAnagram(dictionary, query):
    for i in range(len(dictionary)):
        dictionary[i] = ''.join(sorted(dictionary[i]))

    for i in range(len(query)):
        query[i] = ''.join(sorted(query[i]))

    result = []
    for q in query:
        count = 0
        for word in dictionary:
            if q == word:
                count += 1
        result.append(count)

    return result
    
    

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    dictionary_count = int(input().strip())

    dictionary = []

    for _ in range(dictionary_count):
        dictionary_item = input()
        dictionary.append(dictionary_item)

    query_count = int(input().strip())

    query = []

    for _ in range(query_count):
        query_item = input()
        query.append(query_item)

    result = stringAnagram(dictionary, query)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
