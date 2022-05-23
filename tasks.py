#! /usr/bin/env python3
import math
from operator import indexOf
import sys
from unittest import result
from collections import Counter


def get_distance():
    x1=int(input('enter x1='))
    y1=int(input('enter y1='))
    x2=int(input('enter x2='))
    y2=int(input('enter y2='))
    result=math.sqrt(math.pow((x2-x1),2)+pow((y2-y1),2))
    return result

# print(get_distance())
    
def get_uniqe(arr):
    return set(arr)

# print(get_uniqe([1,2,34,2,8,2,2,2,2]))

def get_popular(file):
    f1=open(file,'r')
    my_text=Counter(f1.read().split()).most_common(20)
    f2=open('popular_words.txt','w')
    for word in my_text :
        f2.write(word[0]+":"+str(word[1])+'\n')
    f1.close()
    f2.close()

# get_popular(sys.argv[1])

def remove_vowels(test):
    vowels=['a','e','o','u','i']
    for vowel in vowels:
        test=test.replace(vowel,'')
    return test

# print(remove_vowels('mobile'))

def get_char_location(test,char):
    arr=list(test)
    result=[]
    for i in range(len(arr)):
        if(arr[i]==char):
            result.append(i)

    return result


print(get_char_location('google','o'))
