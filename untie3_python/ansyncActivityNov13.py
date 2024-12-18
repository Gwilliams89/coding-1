def intergerDection(x):
    if x > 0:
        print("This number is positive")
    elif x == 0:
        print("This number is zero")
    else:
        print("This number is negitve")
       

intergerDection(2)
intergerDection(0)
intergerDection(-2)


def netflixAge(Age):
    if Age <= 10 or Age >= 65:
        print("You have to pay $5.00")
    elif Age <= 16 or Age >= 16: 
        print("You have to pay $10.00")
    elif Age >= 20:
        print("You have to pay $15.00")

netflixAge(20)

# Depening on your memebership is how much of a discout you have and the item

def discountShoping(membership, itemPrice):
    if membership == 'superShopper':
        print('you are getting 10 percent off')
        discount= itemPrice * .1
        total= itemPrice - discount
        print(discount)
    elif membership ==  'megaShopper':
        print('you are getting 15 percent off')
        discount= itemPrice * .15
        total= itemPrice - discount
        print(discount)
    elif membership == 'ultraShopper':
        print('you are getting 20 percent off')
        discount= itemPrice * .2
        total= itemPrice - discount
        print(discount)
    else:
        print('Erorr: sorry, that membership type dosent exist') 