print ('''**************************************
**    Welcome to the Snakes Cafe!   **
**    By Amer   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

''')
print('''***********************************
    ** What would you like to order? **
    ***********************************\n> ''')
menu={"wings":0,"cookies":0,"spring rolls":0,"salmon":0,"steak":0,"meat tornado":0,"a Literal Garden":0,
"ice Cream":0,"cake":0,"pie":0,"coffee":0,"tea":0,"unicorn tears":0}
order=input("Enter your order")
order.lower()
if order in menu :
    menu[order]=menu[order]+1
    print(f'** {menu[order]} order of {order} have been added to your meal **')
elif order == "quit":
    pass
else:
     menu[order]=1
     print('the item you ordered is not on the menu but we will get it for you')
     print(f'** {menu[order]} order of {order} have been added to your meal **')



x=input("Do you want to quit?")
while order != "quit":
    
      print("***********************************")
      order=input('** What would you like to order?  \n >').lower()
      print("***********************************")
      if order=='quit':
          break
      if order in menu :
        menu[order]=menu[order]+1
        for food in menu:
            if(menu[food]>0):
               print(f'** {menu[food]} order of {food} have been added to your meal **')
      else:
        menu[order]=1
        print('the item you ordered is not on the menu but we will get it for you')
        print(f'** {menu[order]} order of {order} have been added to your meal **')