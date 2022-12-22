#!/usr/bin/env python2

import base64


def rot47(s):
    x = []
    for i in xrange(len(s)):
        j = ord(s[i])
        if j >= 33 and j <= 126:
            x.append(chr(33 + ((j + 14) % 94)))
        else:
            x.append(s[i])
    return ''.join(x)


b64_encoded = 'OUVFQURpXl4zOkVdPUpeYSVhJCgncg=='
decoded = base64.b64decode(b64_encoded)
print(rot47(decoded))
