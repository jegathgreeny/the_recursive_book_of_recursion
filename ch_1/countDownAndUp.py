def countDownAndUp(number):
    print(number)
    if number == 0:
        # BASE CASE
        print('reached base case')
        return
    else:
        # RECURSIVE CASE
        countDownAndUp(number - 1)
        # after 
        print(f'{number} returning')
        return

countDownAndUp(3)
