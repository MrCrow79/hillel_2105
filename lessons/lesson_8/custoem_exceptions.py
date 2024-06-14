

class DbRoiExceptions(Exception):
     def __init__(self, message, *args, **kwargs):
         super().__init__(message)


def read_row_from_db(item_id):

    #rsult =  select from ...
    result = (10, 5, -5)  # id, count, ROI

    if result[2] <0 or result[2] >100:
        raise DbRoiExceptions(f'ROI for id={item_id} is incorrect: {result[2]}')

    return result


read_row_from_db(10)


def test_db_has_data():

    result = []  #  get_data_from_db(item_id=10)
    1/0
    result[0] + result[1]
    assert result  # assert len(result) > 0