import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    a=max(arr)
    b=min(arr)
    c=sum(arr)
    print(c-a,c-b)
