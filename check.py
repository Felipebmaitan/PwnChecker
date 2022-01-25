import hashlib
import requests

# Defines the variables and hashes the input password.

passwd = input('Type the password you want to test here: ')
passhash = hashlib.sha1(passwd.encode('UTF-8')).hexdigest().upper()
api = 'https://api.pwnedpasswords.com/range/'

# Contacts the API and informs the user if there were any errors.

resp = requests.get(api + passhash[:5])
if resp.status_code != 200:
    print('An error happened while contacting the API.')

# Searches the API response for the password hash and if found returns the hash of the password and 
# the amount of times it was leaked.

for line in resp.text.splitlines():
    hash = line.split(':')[0]
    n = line.split(':')[1]
    if hash == passhash[5:]: 
        print ('Your password was found in one of our databases. \nThe hash of your password is: {}. \nIt was leaked {} times.'.format(passhash, n))

# At this point I was so tried of trying to find the right way to do that that I ended up with this quick fix. 
# I may fix this in the future if there is any way to do so.
        flag = True
try:
    flag
except NameError: 
    print('Your password was not found on our databases. \nThe hash of your password is: {}'.format(passhash))