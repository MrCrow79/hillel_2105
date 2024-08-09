from datetime import datetime, timezone
import pytz

date_str = "2024-08-09 12:30:00"
date_with_tz_str = "2024-08-09 12:30:00 +02:00"

without_tz = datetime.fromisoformat(date_str)
without_tz.replace(tzinfo=pytz.timezone('UTC'))  # set uts as current timezone
with_tz = datetime.fromisoformat(date_with_tz_str)

print('############# without TZ')
print("base DT", without_tz)
print("UTC Time:", without_tz.astimezone(tz=pytz.timezone('UTC')))
print("Local Time:", without_tz.astimezone(tz=pytz.timezone('US/Michigan')))

print('############# with TZ')
print("base DT", with_tz)
print("UTC Time:", with_tz.astimezone(tz=pytz.timezone('UTC')))
print("Local Time:", with_tz.astimezone(tz=pytz.timezone('US/Michigan')))