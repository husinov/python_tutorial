import time
# print(time.ctime(time.time()))
# print(time.time())
today = time.gmtime()

print(time.strftime('Today is %d.%m.%y %H:%M:%S'))

good = (2021, 12, 8, 00, 40, 00, 0, 0, 0)

print(time.asctime(good))
print(time.mktime(good))
print(today)
