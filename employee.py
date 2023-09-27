"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, wage, commission):
        self.name = name
        self.wage = wage
        self.commission = commission

    def get_pay(self):
        return self.wage.get_pay() + self.commission.get_commission()

    def __str__(self):
        return self.name + " works on a " + str(self.wage) + str(self.commission) + " Their total pay is {}.".format(self.get_pay())
    
# Wage

class Wage:
    def get_pay(self):
        pass

    def __str__(self):
        pass

class SalariedWage(Wage):
    def __init__(self, salary):
        self.salary = salary

    def get_pay(self):
        return self.salary
    
    def __str__(self):
        return "monthly salary of {}".format(self.salary)

class HourlyWage(Wage):
    def __init__(self, hours, hourly_pay):
        self.hours = hours
        self.hourly_pay = hourly_pay

    def get_pay(self):
        return self.hours * self.hourly_pay
    
    def __str__(self):
        return "contract of {} hours at {}/hour".format(self.hours, self.hourly_pay)
    
# Commission

class Commission:
    def get_commission(self):
        pass

    def __str__(self):
        pass

class NoCommission(Commission):
    def get_commission(self):
        return 0
    
    def __str__(self):
        return "."
    
class BonusCommission(Commission):
    def __init__(self, bonus):
        self.bonus = bonus
    
    def get_commission(self):
        return self.bonus
    
    def __str__(self):
        return " and receives a bonus commission of {}.".format(self.bonus) 
    
class ContractCommission(Commission):
    def __init__(self, amount_per_contract, number_of_contracts):
        self.amount_per_contract = amount_per_contract
        self.number_of_contracts = number_of_contracts

    def get_commission(self):
        return self.amount_per_contract * self.number_of_contracts
    
    def __str__(self):
        return " and receives a commission for {} contract(s) at {}/contract.".format(self.number_of_contracts, self.amount_per_contract)

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', SalariedWage(4000), NoCommission())

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', HourlyWage(100, 25), NoCommission())

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', SalariedWage(3000), ContractCommission(200, 4))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlyWage(150, 25), ContractCommission(220, 3))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', SalariedWage(2000), BonusCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', HourlyWage(120, 30), BonusCommission(600))

print(str(robbie))
