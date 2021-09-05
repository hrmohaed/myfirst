daleel = {1111111111: 'Amal', 2222222222: 'Mohammed',
          3333333333: 'Khadijah', 4444444444: 'Abdullah',
          5555555555: 'Rawan', 6666666666: 'Faisal', 7777777777: 'Layla'}
for i,j in daleel.items():
    search = eval(input("enter a number"))
    if search > 999999999 and search <= 9999999999:
        if i == search:
            print(j)
        else:
            print("Sorry, the number is not found")
    else:
        print("This is invalid number")


