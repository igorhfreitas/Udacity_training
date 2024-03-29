# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 12:59:01 2018

@author: Igor
"""
def create_groups(items, n):
    """Splits items into n groups of equal size, although the last one may be shorter."""
    # determine the size each group should be
    try:
        size = len(items) // n  # this line could cause a ZeroDivisionError exception
    except ZeroDivisionError:
        print("WARNING:  Returning empty list. Please use a nonzero number.")
        print("0 groups returned.")        
        return ""
        
    # create each group and append to a new list
    groups = []
    for i in range(0, len(items), size):
        groups.append(items[i:i + size])

    # print the number of groups and return groups    
    print("{} groups returned.".format(n))
    return groups

print("Creating 6 groups...")
for group in create_groups(range(32), 6):
    print(list(group))

print("\nCreating 0 groups...")
for group in create_groups(range(32), 0):
    print(list(group))