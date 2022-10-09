# Random password generating sys is significant as it automates the everyday task of thinking new passwords
# whenever you create account on some site. Most of the passwords we create, are not much secure
# and does not meet the security standards.

# Passwords are necessary to keep the privacy of users and their data safe from malicious users.

# We should not use the random module in these type of systems, as it is possible that this module can
# generate the same password for multiple users. Hence, the secret module is always used for the projects
# where security is highly concerned. Secret module can do the following tasks:
# 1- It can generate sequences of random numbers that are secure for cryptographic applications.
# 2- It provides functions like choice(), randbits(), and randbelow() to generate secure random numbers.
# 3 -Generate tokens for a password reset, temporary URLs, and more.

import secrets
import string

# define the alphabet
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

# fix password length
pwd_length = 12

# generate a password string
pwd = ''
for i in range(pwd_length):
  pwd += ''.join(secrets.choice(alphabet))

print(pwd)

# generate password meeting constraints
while True:
  pwd = ''
  for i in range(pwd_length):
    pwd += ''.join(secrets.choice(alphabet))

  if (any(char in special_chars for char in pwd) and
      sum(char in digits for char in pwd)>=2):
          break
print(pwd)
