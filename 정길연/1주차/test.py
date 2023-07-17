#!/bin/python3

import math
import os
import random
import re
import sys


def getFinalString(s):
    
    while True:
        if 'AWS' in s :
            s = s.replace('AWS', '')
        else:
            break
    
    if len(s) == 0 : return "-1"
    return s

    
    
   
# def getFinalString(s):
    # li = list(s)
    # idx = len(s) -1

    # while True:
    #     if idx <= 0:
    #         break
        
    #     if li[idx] == 'S':
    #         if li[idx - 1] == 'W' and li[idx - 2] == 'A':
    #             li.pop(idx)
    #             li.pop(idx - 1)
    #             li.pop(idx - 2)
    #             idx = len(li) - 1
    #         else : idx = idx - 1
    #     else : idx = idx - 1
    
    # if len(li) == 0 : return "-1"
    # else : 
    #     ans = ''.join(li) 
    #     return ans 


        
print(getFinalString("AAWSWS"))