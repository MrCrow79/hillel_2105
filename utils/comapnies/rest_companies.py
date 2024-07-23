

class CompanySchema:
    def __init__(self, id_, name, payment_data, description=None):

        self.id_ = id_
        self.name = name
        self.description = description
        self.payment_data = payment_data

    def __str__(self):
        pass

    def __len__(self):
        return len(self.payment_data)