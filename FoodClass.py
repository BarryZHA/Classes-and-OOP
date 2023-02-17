class Customer: 

    def __init__(self,cust_id,name,address,email,phone,memberstat): 
        self.__cust_id = cust_id
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__memberstat = memberstat

class Transaction:
    def __init__(self, date, item_name, cost, cust_id):
        self.__date = date
        self.__item_name = item_name
        self.__cost = cost
        self.__cust_id = cust_id
        self.__totalcost = 0
        self.__memberdiscount = 0
        self.__costafterdiscount = 0

    def total_cost(self, transaction, customerid):
        for n in transaction:
            if transaction[n][3] == customerid:
                self.__totalcost += transaction[n][2]

    def member_discount(self,memberstat,totalcost):
        if memberstat == True: 
            self.__memberdiscount = totalcost * 0.2
            self.__costafterdiscount = totalcost - self.__memberdiscount

    # def total_cost(self, transaction, customerid):
    #     for n in transaction:
    #         match transaction[n][3]:
    #             case customerid:
    #                 self.__totalcost += transaction[n][2]
    
    def get_total_cost(self): 
        return self.__totalcost

    def get_discount(self): 
        return format(self.__memberdiscount,'.2f')
    
    def get_cost_after_discount(self): 
        return format(self.__costafterdiscount,'.2f')