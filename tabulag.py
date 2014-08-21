#!/usr/bin/env python
from collections import deque
d = deque(chr(x) for x in range(ord(' '), ord('~')+1))
print(''.join(d))
for i in range(len(d)-1):
    d.rotate(-1)
    print(''.join(d))
