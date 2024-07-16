from utils.company_schema import CompanySchema


class AssertCompanies:

    def assert_company(self, company: CompanySchema, lif_of_required_fields):
        self.assert_companies_has_data(company=company, lif_of_required_fields=lif_of_required_fields)
        self.__asser_payment_required_data(company.payment_data)
        self.__assert_calculation_of_balance(company)

    def assert_companies_has_data(self, company: CompanySchema, lif_of_required_fields):
        for filed in lif_of_required_fields:
            assert getattr(company, filed) is not None

    def __assert_calculation_of_balance(self, company: CompanySchema):
        #  incomes - outcomes = balance
        incomes = company.payment_data['incomes_this_year']
        outcomes = company.payment_data['outcomes_this_year']
        balance = company.payment_data['current_balance']

        assert incomes - outcomes == balance, f'Balance is wrong\nexpected{incomes - outcomes}\nactual {balance}'

    def __asser_payment_required_data(self, company):
        #  incomes - outcomes = balance

        assert len(company) > 0  # company.__len__() => return len(company.payment_data)

        assert company.payment_data.get('incomes_this_year') is not None
        assert company.payment_data.get('outcomes_this_year') is not None
        assert company.payment_data.get('current_balance') is not None


class AssertCompanyFiltered(AssertCompanies):

    def assert_companies_are_filtered(self, request_params, response, lif_of_required_fields):
        self.assert_companies_has_data(response, lif_of_required_fields=lif_of_required_fields)
        ...
