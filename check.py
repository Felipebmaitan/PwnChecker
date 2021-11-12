import hashlib
import requests

# Defines the variables and already hash the password inputed by the user.

passwd = '123'
# passwd = input('Type the password you want to test here: ')
passhash = hashlib.sha1(passwd.encode('UTF-8')).hexdigest().upper()
api = 'https://api.pwnedpasswords.com/range/'

# Contacts the API and informs the user if there was any errors.

resp = requests.get(api + passhash[:5])
if resp.status_code != 200:
    print('An error happened while contacting the API.')

# TODO:
#       - Sort to the request and find the hash of the password provided
#       - Return to the user the hash of their password and how many times it was leaked.