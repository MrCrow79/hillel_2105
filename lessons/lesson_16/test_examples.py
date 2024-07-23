from pytest import mark

from utils.assert_companies import AssertCompanies
from utils.company_schema import CompanySchema
from lessons.lesson_16.abstract import Animal


# # # precondition # # #

# data from API
response_data = [
    {'id_': 10, 'name': 'Apple', 'payment_data': {'current_balance': 100000, 'incomes_this_year': 5000}},
    {'id_': 20, 'name': None, 'description': 'asd', 'payment_data':
        {'current_balance': 5000, 'incomes_this_year': 5000, 'outcomes_this_year': 6000}, 'asd': 12},
    {'id_': 30, 'name': 'NVidea', 'description': 'asd', 'payment_data':
        {'current_balance': -1000, 'incomes_this_year': 5000, 'outcomes_this_year': 6000}},
]


# expected result
list_required_fields = ['id_', 'name', 'payment_data']


@mark.smoke
@mark.parametrize('data', response_data)
def test_company_schema_smoke(data):
    response_obj = CompanySchema(**data)   # call __init__
    # response_obj = CompanySchema(id_=response_data['id_'],
    #                              name=response_data['name'],
    #                              description=response_data.get('description', None),
    #                              payment_data=response_data['payment_data'])

    AssertCompanies().assert_companies_has_data(company=response_obj, lif_of_required_fields=list_required_fields)


@mark.regression
@mark.parametrize('data', response_data)
def test_company_check_balance(data):
    # response = request_to_api..
    response_obj = CompanySchema(**data)

    AssertCompanies().assert_company(company=response_obj, lif_of_required_fields=list_required_fields)

    # for filed_name in list_required_fields:
    #
    #     # assert response_obj.__getattribute__(filed_name) is not None
    #     assert getattr(response_obj, filed_name) is not None, f'{filed_name} is not None'


