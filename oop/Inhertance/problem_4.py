class Bill:
    def __init__(self,amount,bill_no):
        self.amount = amount
        self.billNo = bill_no
    
    def show_bill(self):
        print(f"Bill No: {self.billNo} , Amount:{self.amount}")

class CashPayment(Bill):
    def pay(self):
        super().show_bill()
        print("Payment done using Cash")

class ChequePayment(Bill):
    def __init__(self,amount,bill_no,cheque_no,bank_name):
        super().__init__(amount,bill_no)
        self.chequeNo = cheque_no
        self.bankName = bank_name
    
    def pay(self):
        super().show_bill()
        print(f"Payment done using Cheque No: {self.chequeNo} , Bank Name: {self.bankName}")

cash_payment = CashPayment(1000, 101)

cash_payment.pay()

cheque_payment = ChequePayment(12000,102,"cheawi123","bank of nepal")
cheque_payment.pay()