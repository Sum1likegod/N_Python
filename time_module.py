import time as t

print(t.strftime('%c'))

tal = t.gmtime()

print(t.strftime('%c', tal))

