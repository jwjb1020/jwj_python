class Deposit:
    def __init__(self,init,inter,n):
        self.initial = init
        self.interest = inter
        self.n= n
    def profit(self):
        return int(self.initial *(1+self.interest)**self.n)   
deposit = Deposit(1000000,0.035,7)
print(deposit)
deposit.profit()
