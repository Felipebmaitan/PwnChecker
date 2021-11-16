# Pwnchecker - a simple script to check if your passwords are compromised.

PwnChecker is a simple script written in Python that uses [HaveIBeenPwned API](https://haveibeenpwned.com/API/v3#PwnedPasswords) to search for breaches that contain your password. The script hashes the password with SHA-1 and **NEVER** sends the full hash to the API, only the first 5 characters.