import os
import datetime


def show_items():
    with os.scandir('items/') as i:
        for a in i:
            with open(f'items/{a.name}','r') as f:
                print(f.readline().strip())
                print(f'Rs.{float(f.readline().strip()):.2f}')
                print('\n')


def log(cn,pn):  #This will record customer logins
    t = datetime.datetime.today()
    t = t.strftime('%Y/%m/%d - %I:%M %p')
    with open('login_record/login_record.txt','a') as f:
        f.write(f'{t}\n{cn}\n{pn}\n\n')


def login():
    while True:
        print('User login'.center(80,' '))
        print('\n')
        print('1 Login')
        print('2 New customer sign-up')
        print('3 Exit\n')
        u = int(input('Enter number: '))
        print('\n')

        if u==3:  # [Exit]
            global output
            output = 'no'
            break

        if u==1:  # [Login] (check the coustomers folder for the required information)
            print('Login'.center(80,' '))
            print('\n')
            cn = input('Name: ')
            if os.path.exists(f'customers/{cn}.txt'):
                pw = input('Password(phone number): ')
                with open(f'customers/{cn}.txt','r') as f:
                    f.readline().strip()
                    pn = f.readline().strip()
                if pw != pn:
                    print('Incorrect password or user name')
                    print('--------------------------------------------------------------------------------')
                    continue
                else:
                    log(cn,pn)
                    print('--------------------------------------------------------------------------------')
                    break
            else:  #From the login screen
                print('The name you enterd does not exist. Please check your spelling.')
                print('If you are a new customer use the sign-up function.')
                print('\n')
                continue

        if u==2:  # [New customer sign-up]
            print('Sign-up'.center(80,' '))
            print('\n')
            cn = input('Name (no spaces): ')
            if os.path.exists(f'customers/{cn}.txt'):
                print('This user name alredy exist')
                print('--------------------------------------------------------------------------------')
                print('\n')
                continue
            while True:
                pn = input('Phone number: ')
                if len(pn) == 10:
                    with open(f'customers/{cn}.txt','w') as f:
                        f.write(f'{cn}\n{pn}')
                    log(cn,pn)
                    break
                else:
                    print('\n')
                    print('Must contain 10 digits')
                    continue
            print('\n')
            print('--------------------------------------------------------------------------------')
            break


print('\n')
print('-'*80)
print('COVID era SHOP'.center(80,' '))
print('-'*80)
print('\n')
print(' WELLCOME '.center(80,'-'))
while True:
                                #[main menu]
    print('\n')
    print('Main menu'.center(80,' '))
    print('\n')
    print('1 Seller section')
    print('2 Buyer section')
    print('3 Exit\n')

    n = int(input('Enter number: '))
        
    print('\n')
    print('--------------------------------------------------------------------------------')

    
    if n==3: #[Exit]
        print('_________________________________________________________________________________')
        print('program closed')
        print('\n')
        break

    
    elif n==1: #[Seller section]

        print('\n')
        print('Seller section'.center(80,' '))

        print('\n')
        pw = input('Enter password(0000): ')  # Just because :)
        if pw != '0000':
            print('Wrong password')
            print('-'*80)
            continue

        while True:  # To keep the user in the seller section
            print('\n')
            print('1 Show current items')
            print('2 Add new items')
            print('3 Remove items')
            print('4 Show customer details')
            print('5 Exit seller section')
            print('\n')
            
            print('To see customer activity please go to "...login_record/login_record.txt"')
            # Since the code to open a file from code differs from OS to OS,
            # I left this part to be carried out manually.
            # For windows the following code will do the trick.
            # os.system('start '+'login_record/login_record.txt')
            # (this must be integrated properly of course)
            print('\n')

            n2 = int(input('Enter number: '))
            print('--------------------------------------------------------------------------------')

            if n2==5: break  # This will ultimately resend to the main menu

            elif n2==1:  #[Show current items]
                print('\n')
                show_items()
                print('--------------------------------------------------------------------------------')

            elif n2==2:  #[Add new items]
                print('\n')
                new_items = input('Enter the new item(s) separated by a space: ')
                new_items_p = input('Enter the item price(s) in order separated by a space\n(only enter the value without units): ')
                new_items = new_items.split(' ')
                new_items_p = new_items_p.split(' ')
                for i, name in enumerate(new_items):
                    with open(f'items/{name}.txt','w') as f:
                        f.write(f'{new_items[i]}\n{new_items_p[i]}')
                print('\n')
                print('The new item(s) have been added')
                print('--------------------------------------------------------------------------------')
            
            elif n2==3:  #[Remove items]
                print('\n')
                show_items()
                print('--------------------------------------------------------------------------------')
                print('\n')
                re = input('The item(s) you want to remove separated by a space: ')
                re = re.split(' ')
                for name in re:
                    if os.path.exists(f'items/{name}.txt'):   # This will prevent any runtime errors
                        os.remove(f'items/{name}.txt')
                    else:
                        print(f'\nThe item "{name}" dose not exist\nPlease check spelling')
                print('\n')
                print('The file(s) have been removed')
                print('--------------------------------------------------------------------------------')

            elif n2==4:  #[Show customer details]
                with os.scandir('customers/') as i:
                    for a in i:
                        with open(f'customers/{a.name}','r') as f:
                            print(f.readline().strip())
                            print(f.readline().strip())


        print('...exiting the seller section'.rjust(80,' '))
        print('--------------------------------------------------------------------------------')
        continue  #continues to the main menu


    elif n==2: #[Buyer section]

        print('\n')
        print('Buyer section'.center(80,' '))
        print('\n')

        output = ''
        login()

        if output == 'no':  # Sends to the main menu from the user login screen in login()
            print('--------------------------------------------------------------------------------')
            continue
        
        show_items()
        itemsl = []
        pricel = []
        amountl= []
        
        while True:  #For buying multiple items at once without having to return
            x = input('What item do you want? ')
            
            if os.path.exists(f'items/{x}.txt'):           # If there is a spelling error,
                amount = int(input('How many? '))          # this will prevent any runtime errors
                amountl.append(amount)
                with open(f'items/{x}.txt','r') as f:
                    item = f.readline().strip()
                    itemsl.append(item)
                    p = float(f.readline().strip())
                    p = round(p,2)
                    pricel.append(p*amount)
            else:
                print(f'The item "{x}" dose not exist\nPlease check spelling')
            
            print('\n')
            mo = input('Buying anything else?(y/n) ')
            if mo == 'n':
                break      #Continues with the order
        
        if len(itemsl) == 0 :  # Can happen with a spelling error. Sends to the main menu.
            print('--------------------------------------------------------------------------------')
            continue

        print(f'price = Rs:{sum(pricel):.2f}')
        by = input('Place order?(y/n) ')          #Asking for confirmation
        if by == 'n':                             #This will return to main menu
            print('\n')
            print('Order canceled'.rjust(80,' '))
            print('--------------------------------------------------------------------------------')
            continue

        cash = int(input('Cash: '))
        if cash-sum(pricel) < 0:
            print('\n')
            print('Not enough cash'.rjust(80,' '))
            print('--------------------------------------------------------------------------------')
            continue
        balance = cash-sum(pricel)
        t = datetime.datetime.today()

        print('\n')
        print('--------------------------------------------------------------------------------')
        print('COVID era SHOP'.center(80,' '))
        print('--------------------------------------------------------------------------------')
        print('\n')
        for i in range(len(itemsl)):
            print(f' Item: {itemsl[i]}   Unit Price: Rs.{(pricel[i]/amountl[i]):.2f}   Amount: {amountl[i]}')
        print(f'\n')
        print(f' Price  : Rs.{sum(pricel):.2f}')
        print(f' Cash   : Rs.{cash:.2f}')
        print(f' Balance: Rs.{balance:.2f}')
        print('\n')
        print('--------------------------------------------------------------------------------')
        print(t.strftime(' %Y/%m/%d                                     %I:%M:%S %p '))
        print('--------------------------------------------------------------------------------')
        print('THANK YOU. COME AGAIN.'.center(80,' '))
        print('--------------------------------------------------------------------------------')
        print('\n')
        
