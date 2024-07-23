

class CompanySchema:
    def __init__(self, id_, name, payment_data, rate, description=None):

        self.id_ = id_
        self.name = name
        self.description = description
        self.rate = rate
        self.payment_data = payment_data

    def __str__(self):
        pass

    def __len__(self):
        return len(self.payment_data)