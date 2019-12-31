#File management----------------------

with open('balance_sheet.txt', 'r+') as bal_file:

    content = bal_file.readline()           #Reads first line
    print(content, end='')

    last_line = bal_file.readlines()[-1]    #Reads the last line from text file
    print(last_line)

    last_line = last_line.rstrip('\n')      #strips second line


    make_payment = input('How much you paying: ')
    inc_debt = input('How much more you owe: ')

    new_balance = (int(last_line)-int(make_payment)) + int(inc_debt)

    print('\n', end ='')
    print('New Balance is:', new_balance)

    bal_file.write(str(new_balance)+'\n')
