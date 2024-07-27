from pathlib import Path
import os

'''
This script creates a calendar year directory based on the year given (stored in the 'year' variable).
Below we will create a calendar year directory for the year 2020. I used this year as an example because
it was the most recent leap year, and therefore provides the opportunity to test out the functionality of 
the script to make sure it works as intended. Note that if you do not change the 'is_leap_year' variable 
to 'False' for years that are not a leap year, then the script will still create 29 folders for the month 
of February, and vice versa.
'''

# Set up directory structure variables

months = [
    'Jan', 
    'Feb', 
    'Mar', 
    'Apr', 
    'May', 
    'Jun', 
    'Jul', 
    'Aug', 
    'Sep',
    'Oct',
    'Nov',
    'Dec'
    ]
days_in_month = 0

year = '2020'

is_leap_year = True

month_folder_paths = []

# Create year and month directories 

os.mkdir(year)

cwd = f'{os.getcwd()}\\{year}'

os.chdir(cwd)

for month in range(len(months)):
    if month < 9:
        os.mkdir(f'[0{str(month + 1)}]_{months[month]}')
    else:
        os.mkdir(f'[{str(month + 1)}]_{months[month]}')

root_dir = Path('.')

file_paths = root_dir.glob('**/*')

# Logic for creating directories in special situations listed below

'''
April, June, September and November are the months with 30 days, 
February has 28 days (29 days in a leap year) and all the remaining 
months have 31 days.
'''

for path in file_paths:
    
    if path.name == '[02]_Feb':

        if is_leap_year:
            days_in_month = 29
        else:
            days_in_month = 28

        month_folder_paths.append((cwd + f'\\{path.name}', days_in_month))
        
    elif path.name in ['[04]_Apr', '[06]_Jun', '[09]_Sep', '[11]_Nov']:

        days_in_month = 30

        month_folder_paths.append((cwd + f'\\{path.name}', days_in_month))
    else:
        
        days_in_month = 31

        month_folder_paths.append((cwd + f'\\{path.name}', days_in_month))

# Create days directories for each month

for tup in month_folder_paths:
    os.chdir(tup[0])
    for i in range(tup[1]):
        if i < 9:
            os.mkdir(f'0{str(i + 1)}')
        else:
            os.mkdir(f'{str(i + 1)}')