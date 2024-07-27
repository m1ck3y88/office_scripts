import os

'''
This script formats and creates a list of named folders.
They do not need to be in any particular order but
are ordered here in this example only so that the
operating system does not automatically order them 
alphabetically. 
'''
folders = []
titles = [
    'January 2024',
    'February 2024',
    'March 2024',
    'April 2024',
    'May 2024',
    'June 2024',
    'July 2024',
    'August 2024',
    'September 2024',
    'October 2024',
    'November 2024',
    'December 2024'
]

def add_title(title, _list):
    """
    Appends a formatted string to an empty list of folders to be created.
    :param title: A string to append to an empty list.
    :param _list: An empty list that formatted strings are to be appended to.
    """
    _list.append('_'.join((title).split()))

if len(titles) != 0:
    for i in range(len(titles)):
        add_title(titles[i], folders)
else:
    print('There are no titles to add to the folders list!')

print(folders)

if len(folders) != 0:
    for i in range(len(folders)):
        if i < 9:
            os.mkdir((f'0{str(i + 1)}_' + folders[i]).lower())
        else:
            os.mkdir((f'{str(i + 1)}_' + folders[i]).lower())
else:
    print('There are no folders available to create!')