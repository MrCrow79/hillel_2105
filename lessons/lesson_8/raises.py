# raise AttributeError('My error')


def read_row_from_db(item_id):

    #rsult =  select from ...
    result = (10, 5, -5)  # id, count, ROI

    if result[2] <0 or result[2] >100:
        raise ValueError(f'ROI for id={item_id} is incorrect: {result[2]}')

    return result

item_id = 10

try:
    res = read_row_from_db(item_id)
except ValueError as e:
    msg = 'Data is incorrect'

    raise AssertionError(msg + ', ' + str(e))

# try:
#     assert res[0] == item_id
# except IndexError as e:
#     raise IndexError(f'Db has no data for id={item_id}\n' + str(e))
#
# try:
#     assert res[1] > 0
# except IndexError as e:
#     raise IndexError(f'Db has no data for id={item_id}\n' + str(e))


# try:
#     assert res[2] >= 0  and res[2] <=100      # if res[2] >= 0  and res[2] <=100 : raise AssertionError
# except AssertionError as e:
#     raise ValueError(f'ROI for id={item_id} is incorrect: {res[2]}')




# assert condition  -> Викличе AssertionError якщо bool(condition) != True




