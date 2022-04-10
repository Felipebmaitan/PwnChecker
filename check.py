import hashlib
import requests
from asyncore import read
import time
from pathlib import Path

api = 'https://api.pwnedpasswords.com/range/'

opt = input('[1] Single password test \n[2] Bulk password testing\n')

if opt == '1':
    # Defines the variables and hashes the input password.

    passwd = input('Type the password you want to test here: ')
    passhash = hashlib.sha1(passwd.encode('UTF-8')).hexdigest().upper()

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
    # At this point I was so tried of trying to find the right way to do that that I ended up with this quick fix. I may fix this in the future if there is any way to do so.
            flag = True
    try:
        flag
    except NameError: 
        print('Your password was not found on our databases.')

elif opt == '2':

    filepath = input("Full path to the file with the passwords you want to test: ")
    file = open(filepath, 'r')
    lines = file.readlines()

    a = 0

    for line in lines:
        linehash = hashlib.sha1(lines[a].replace('\n', '').encode('UTF-8')).hexdigest().upper()

        a = a + 1

        resp = requests.get(api + linehash[:5])

        if resp.status_code != 200:
            print('An error hapened while contacting the API')

        for line in resp.text.splitlines():
            hash = line.split(':')[0]
            n = line.split(':')[1]
            if hash == linehash[5:]:
                print ('Your password was found in one of our databases. \nThe hash of your password is: {}. \nIt was leaked {} times.'.format(linehash, n))
                flag = True
        try:
            flag
            del(flag)
        except NameError:
            print('Your password was not found on our databases.')