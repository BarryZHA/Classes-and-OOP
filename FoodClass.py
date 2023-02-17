## Customer Class - that has the following attributes - customerid, name, address, 
##                                      email, phone, member_status (True or False). 
## The Customer class’s __init__ method should accept an argument for each attribute.
## The Customer class should have accessor methods only for each attribute. 

## Transaction Class - that has the following attributes - date, item name,cost and customerid. 
## The Procedure class’s __init__ method should accept an argument for each attribute. 
## The Transaction class should have accessor methods only for each attribute.

class Customer: 

    def __init__(self,cust_id,name,address,email,phone,memberstat): 
        self.__cust_id = cust_id
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__memberstat = memberstat
        self.__totalcost = 0 
        self.__memberdiscount = 0 

class Transaction: 
    def __init__(self,date,item_name,cost,cust_id):
        self.__date = date
        self.__item_name = item_name
        self.__cost = cost
        self.__cust_id = cust_id

    def total_cost(self,transaction,cust_id): 
        for n in transaction: 
            match cust_id: 
                case transaction[n][3]:
                    self.__totalcost += transaction[n][3]
    
    def get_total_cost(self): 
        return self.__totalcost

