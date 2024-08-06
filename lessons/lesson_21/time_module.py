import time

# print(time.time())
# print(time.sleep(1.5))
# print(time.time())

print(type(time.localtime()))
# print(time.localtime())


print(time.timezone, 'in sec')

local_time = time.localtime()

current_time_in_sec = time.time()
tz_in_sec = time.timezone  # return tim in sec uts - localtime
time_utc = time.localtime(current_time_in_sec + tz_in_sec)
tz_in_12_hours = 60*60*12
time_in_12_hours = time.localtime(current_time_in_sec + tz_in_sec + tz_in_12_hours)


print(time.localtime().tm_mday, time.localtime().tm_hour)  # day + time local time
print(time_utc.tm_mday, time_utc.tm_hour)  # day + time in utc
print(time_in_12_hours.tm_mday, time_in_12_hours.tm_hour)  # day + time in utc + 12 hours


