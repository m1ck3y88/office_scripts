from faker import Faker
import time

'''
In this script I will be introducing the sleep() method of the time module
to time our script. This particular example is not a practical use of 
of the time module, however, it demonstrates how to use the sleep()
method in order to time your code to do something useful. In a later
chapter, I will demonstrate the use of the sleep() method in a more
realistic scenario.
'''

# Instantiate a Faker object to generate some fake data
fake = Faker()

# Create an empty list to store fake data in. I named the list 'profiles'
# to store fake profiles generated using the profile() method of the
# Faker module.
profiles = []

# Create a counter variable to use in a while loop.
count = 0

# Create a _range variable to store an int that represents the amount
# of fake profiles to be generated.
_range = 10

# Create a variable to represent how many seconds you want to wait
# before loop runs again.
delay = 1

# Generate fake profiles to append to profiles list.
for profile in range(_range):
    profiles.append(fake.profile())

# Print each profile to console.
while count < _range:
    
    print(f'[{str(count + 1)}] - ', profiles[count])
    
    if count == _range - 1 :
        print('\n-----------------------------------')
        print("You've reached the end of the list!")
        print('-----------------------------------\n')
        break

    count += 1

    # Stop the loop.
    time.sleep(delay)