from datetime import datetime, timedelta
import time

from utils.date_utils import DateUtils

# dt_in_str = '2-29-24 PM 5:06:35 +23:00'
# format_dt = "%m-%d-%y %p %I:%M:%S %z"
#
# datetime.strptime(dt_in_str, format_dt)

dt_now = datetime.now()

two3_hours_ago = dt_now - timedelta(hours=23)

print(dt_now)
print(two3_hours_ago)

dt_delta = dt_now - two3_hours_ago


def test_create_user_between_dates():
    create_start = datetime.now()

    # call API
    time.sleep(1)
    response = {'created_at': datetime.now().isoformat()}
    time.sleep(1)

    api_date = datetime.fromisoformat(response['created_at'])
    now_date = datetime.now()

    # assertation part
    assert DateUtils.compare_3_dates(bigger_date=now_date,
                                     medium=datetime.fromisoformat(response['created_at']),
                                     less_date=create_start), \
        f'Expected api date {api_date} between {now_date} and {create_start}'


def test_get_data_in_2_hours():
    test_start = datetime.now()

    # send request to get data for last 2 hours
    response = [
        {'date': "2024-08-06 19:06:35.459687"},
        {'date': "2024-08-06 19:06:35.459687"},
        {'date': "2024-08-05 19:06:35.459687"},  # failed
        {'date': "2024-08-06 19:06:35.459687"}
    ]

    for k in response:
        res = DateUtils.difference_in_hours(test_start, datetime.fromisoformat(k['date']))
        assert res < 2
