class Category:

    '''
        this class and its methods mirror the logic behind bank transactions such as;
            deposits, withdrawals, transfers, checking account balance. etc. 
    '''

    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=''):
        self.ledger.append({'amount':amount, 'description':description})
        
    def withdraw(self, amount, description=''):
        if self.check_funds(amount) == True:
            self.deposit(-amount, description)       
            #self.deposit(-10, 'bank charges')
            return True
        else:
            return False

    def get_balance(self):
        return sum([item['amount'] for item in self.ledger])
        
    def transfer(self, amount, other):
        if self.check_funds(amount)  == True:
            self.withdraw(amount, description='Transfer to {}'.format(other.name))
            other.deposit(amount, description='Transfer from {}'.format(self.name))
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self):
        result = ''
        maxL = 23
        x = 30 - len(self.name)
        if x % 2 == 0:
            result += '*'*(x//2)+ self.name +'*'*(x//2) + '\n'
        else:
            result += '*'*(x//2)+ self.name +'*'*(x//2+1) + '\n'
        for item in self.ledger:
            space = (30-sum((len(list(item.values())[1]), len(str(format(list(item.values())[0], '10.2f'))))))
            if len(list(item.values())[1]) <= 23:
                result += '%s'%(list(item.values())[1]) + ' '*space + '%s'%(format(list(item.values())[0], '10.2f')) + '\n'
            else:
                result += "{}".format(list(item.values())[1][:22]) + "{}".format(format(list(item.values())[0], "1.2f")) + '\n'
        #result += '_'*30 + '\n'
        result += 'total: {}'.format(sum([item['amount'] for item in self.ledger]))

        return result




def create_spend_chart(cat):
    total_deposit = [list(cat.ledger[i].values())[0] for i in range(len(salary.ledger)) if list(cat.ledger[i].values())[0] > 0]
    expenses = [list(cat.ledger[i].values())[1] for i in range(len(salary.ledger)) if list(cat.ledger[i].values())[0] < 0]
    amounts = [abs(list(cat.ledger[i].values())[0]) for i in range(len(salary.ledger)) if list(cat.ledger[i].values())[0] < 0]
    percentage_expenses = [abs(list(cat.ledger[i].values())[0])*100/sum(total_deposit) for i in range(len(salary.ledger))  if list(cat.ledger[i].values())[0] < 0]
    

    result = ''
    for i in range(0, 100+1, 10):
        result += '%s|\n'%(format(100 - i, '3.0f'))
    result += '    '
    result += '-'*30


    return result


abs = lambda x:-1*x if x<0 else x 

salary = Category('salary')
tithe = Category('tithe')
clothing = Category('clothing and utensils')
salary.deposit(10000, 'fed gov')
salary.transfer(1000, tithe)
salary.transfer(3000, clothing)
expenses = [list(salary.ledger[i].values())[1] for i in range(len(salary.ledger))]
amounts = [list(salary.ledger[i].values())[0] for i in range(len(salary.ledger))]
#[print(i,j) for i,j in zip(expenses, amounts)]
print(salary)

#print(create_spend_chart(salary))


"""
    to solve the error with __str__ not having a return statement:
        possible solutions:
        1)  Use exec("A string of code to possible solutions"):
                e.g     exec("x = 30 - len(self.name)\nif x % 2 == 0:\n\t\
                    print('*'*(x//2)+ self.name +'*'*(x//2))")
                Note: this method is the best just be careful to use \n, \t and \r where neccessary

        2)  Use a single return statement with a single string 
                Note: this method will be very difficult.
"""