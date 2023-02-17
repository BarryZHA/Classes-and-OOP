import FoodClass as fc

# cust_id = 570
# name = "Danni Sellyar"
# address = "97 Mitchell Way Hewitt Texas 76712"
# email = "dsellyarft@gmpg.org"
# phone = "254-555-9362"
# memberstat = False
# customer1 = fc.Customer(cust_id,name,address,email,phone,memberstat)

cust_id = "569"
name = "Aubree Himsworth"
address = "1172 Moulton Hill Waco Texas 76710"
email = "ahimsworthfs@list-manage.com"
phone = "254-555-2273"
memberstat = True
customer1 = fc.Customer(cust_id,name,address,email,phone,memberstat)

dict = {'trans1':['2/15/2023','The Lone Patty',17,569],
                'trans2':['2/15/2023','The Octobreakfast',18,569],
                'trans3':['2/15/2023','The Octoveg',16,570],
                'trans4':['2/15/2023','The Octoburger',20,570],
}
date = '2/15/2023'
NameOfItem = 'The Lone Patty'
cost = 17
customerid = 569 
trans1 = fc.Transaction(date,NameOfItem,cost,customerid)

date = '2/15/2023'
NameOfItem = 'The Octobreakfast'
cost = 18
customerid = 569 
trans2 = fc.Transaction(date,NameOfItem,cost,customerid)
trans2.total_cost(dict,customerid)
trans2.member_discount(memberstat,trans2.get_total_cost())

date = '2/15/2023'
NameOfItem = 'The Octoveg'
cost = 16
customerid = 570

date = '2/15/2023'
NameOfItem = 'The Octoburger'
cost = 20
customerid = 570
trans4 = fc.Transaction(date,NameOfItem,cost,customerid)
trans4 = fc.Transaction(date,NameOfItem,cost,customerid)
trans4.total_cost(dict,customerid)
trans4.member_discount(memberstat,trans4.get_total_cost())

print("Customer Name: ", name)
print("Phone: ", phone)
print("Total Cost: $" + format(trans2.get_total_cost(),'.2f'))
print("Member Discount: $" + str(trans2.get_discount()))
print("Total Cost After Discount: $" + str(trans2.get_cost_after_discount()))
# print("Total Cost: " + format(trans4.get_total_cost(),'.2f')
# print("Member Discount: " + str(trans4.get_discount()))
# print("Total Cost After Discount: " + str(trans4.get_cost_after_discount()))



