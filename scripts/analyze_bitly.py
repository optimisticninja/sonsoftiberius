#!/usr/bin/env python3

cipher = list('hrrzs://bar.ny/4ralop43')
known = list('https://bit.ly')

for i in range(len(known)):
    print("%s - %d" % (known[i], ord(known[i]) - ord(cipher[i])))

