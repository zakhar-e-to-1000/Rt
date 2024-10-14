class Bank:
    def __init__(self, name="", clients_count=0, credits_count=0,
                 luck = 0, nick_name = ''):
        self._name = name
        self._clients_count = clients_count
        self._credits_count = credits_count
        self.luck = luck
        self.nick_name = nick_name
    def __str__(self):
        return (f"Bank Info:\n"
                + f'Name: {self._name}\n'
                + f'Clients count: {self._clients_count}\n'
                + f'Bank credits given: {self._credits_count}')

    def __repr__(self):
        blank = "Bank({}, {}, {}, {}, {})"
        return blank.format(repr(self._name),
                            self._clients_count,
                            self._credits_count,
                            self.luck,
                            repr(self.nick_name))

    def get_name(self):
        return self._name

    def get_clients_count(self):
        return self._clients_count

    def get_credits_count(self):
        return self._credits_count
    
    def set_name(self, name):
        self._name = name

    def set_clients_count(self, clients_count):
        self._clients_count = clients_count

    def set_credits_count(self, credits_count):
        self._credits_count = credits_count
    def __del__(self):
        print("I think I'm done at this point.")
def main():
    bank1 = Bank("Lviv", 1000, 50)
    bank2 = Bank("Жytomyr", 10, 4)
    bank3 = Bank("Ternopil", 10000000, 5000000000000000000)
    for bank in (bank1, bank2, bank3):
        print(repr(bank))
        # print(bank.get_name(),
        #       bank.get_clients_count(),
        #       bank.get_credits_count(),
        #       bank.luck,
        #       bank.nick_name, sep='\n')
    print()
if __name__=='__main__':
    main()