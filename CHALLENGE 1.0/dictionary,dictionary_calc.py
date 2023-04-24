shop1={'mango':20,'banana':30.4,'apple':15.4,'orange':40.12}
shop2={'mango':50,'banana':26,'apple':35.71,'orange':15.78}
(shop1['orange']*5) + (shop2['apple']*7)
shop1['strawberry']=38
shop2['pawpaw']=120
print(shop1)
print(shop2)

totalcost={'mango':'','banana':'','apple':'','orange':''}
totalcost['apple']=shop1['apple'] + shop2['apple']
totalcost['banana']=shop1['banana'] + shop2['banana']
totalcost['mango']=shop1['mango'] + shop2['mango']
totalcost['orange']=shop1['orange'] + shop2['orange']

