import os

"""
This simple script automates the creation of an ordered list 
of folders based on an int passed to the range() function and
names each folder after its corresponding index in the list.
In this example we create 10 ordered folders.
"""

for i in range(10):
    if i < 9:
        os.mkdir(f'0{str(i + 1)}')
    else:
        os.mkdir(f'{str(i + 1)}')