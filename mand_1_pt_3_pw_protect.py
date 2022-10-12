# The shadow file of a Linux operating system contains the following line:
# “$6$penguins$eP.EvNiF2A.MmRVWNgGj5WSXKK8DAf7oeK8/kkbollee.F0T4KAy.QEgNAX.6wLQY1XHmSID/5VkeFiEaSA2b0”
# You’re asked to crack the given hash, knowing that the password is in a 3-digit format.
# You’re encouraged to solve this exercise using Python. 
# Once you’redone, and if you want, you can use a password-cracking toollike John the Ripper to confirm the result.

from passlib.hash import sha512_crypt
import itertools

orig_hash = '$6$penguins$eP.EvNiF2A.MmRVWNgGj5WSXKK8DAf7oeK8/kkbollee.F0T4KAy.QEgNAX.6wLQY1XHmSID/5VkeFiEaSA2b0'
splitted = orig_hash.split('$')
salt = splitted[2]

digits = itertools.product('123456789', repeat=3)
combinations = [''.join(tups) for tups in digits]
print(str(combinations))

for nr in combinations:
    new_hash = sha512_crypt.using(salt=salt, rounds=5000).hash(nr)
    if new_hash == orig_hash:
        print('the password is: ' + str(nr))