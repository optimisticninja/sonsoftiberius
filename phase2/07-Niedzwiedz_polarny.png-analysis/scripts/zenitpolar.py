#!/usr/bin/env

known = 'https://bit.ly'
cipher = '4ralop43'
decrypted = cipher.replace('p', 'z').replace('o', 'e').replace('l', 'n').replace('a', 'i').replace('r', 't')
print(known + decrypted)
