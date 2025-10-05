class Account:
    def __init__(self):
        self.__account_no = None
        self.__account_bal = None
        self.__security_code = None

    def set_data(self, no, bal, code):
        self.__account_no = no
        self.__account_bal = bal
        self.__security_code = code

    def show_data(self):
        print("Account No:", self.__account_no)
        print("Account Balance:", self.__account_bal)
        print("Security Code:", self.__security_code)

a = Account()
a.set_data(76541, 55656, 456)
a.show_data()

