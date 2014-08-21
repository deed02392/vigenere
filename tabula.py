#!/usr/bin/env python
from collections import deque

ascii_min = ord(' ')
ascii_max = ord('~')

d = deque(chr(x) for x in range(ascii_min, ascii_max + 1))

print(''.join(d))
for i in range(len(d)-1):
    d.rotate(-1)
    print(''.join(d))
