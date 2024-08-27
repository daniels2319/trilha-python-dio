# Resolution of the challenge from the DIO - Data Engineer Bootcamp

intro = """
    --------------------------------------------------------
    Terminal FSG4356-GF

    Please, be advised that this terminal only works with note bills, as it cannot accept or give coins.

    Happy Banking!

    Bank Co.® - All Rights reserved
    --------------------------------------------------------
"""

open_menu = """
Please select one of the options below:
    d - deposit
    w - withdrawal
    s - bank statement
    e - end session
"""
valid_options = ('d','w','s','e')
balance = 0
withdrawal_limit = 3
transaction_records = []

print(intro)

while True:

    selected_option = input(open_menu)

    if selected_option not in valid_options:
        print(f"\nInvalid option. Please select one of the options above.\n")
        continue
    
    if selected_option == "d":
        
        while True:

            try:
                deposit = int(input("\nPlease, inform the amount to be deposited: \n"))
                
                if deposit >= 0:    
                    
                    balance += deposit
                    print(f"\n${deposit}.00 has been deposited into your bank account.\nYour current balance is ${balance}.00\n")
                    
                    transaction_records.append(f"Deposit: ${deposit}.00")                                  
                    break

                else:
                    print(f"\nThe deposit amount must be greater than zero.\n")
                    break
                
            except ValueError:
                
                print(f"\nInvalid amount. Please, provide a valid amount to proceed with the deposit.\n")
                continue
            
    elif selected_option == "w":
        
        while True:
            
            try:
                withdrawal = int(input(f"\nYour current balance is {balance} USD.\nPlease, inform the withdrawal amount or type 'return' to go back to the main menu: \n"))
                
                if withdrawal <= 0:
                    print(f"\nThe withdrawal amount must be greater than zero.\n")
                    break

                elif withdrawal > 500:
                    print(f"\nSorry, the withdrawal limit is 500 USD.\nPlease provide a valid amount\n")
                    continue                  
                
                elif withdrawal_limit == 0:
                    print(f"\nSorry, you've already withdrawn 3 times today.\n")
                    break                  
                
                elif withdrawal > balance:
                    print(f"\nSorry, you don't have enough balance to withdraw ${withdrawal}.00.\nYour current balance is ${balance}.00\nPlease provide a valid amount.\n")
                    continue                  
                    
                else:
                    balance -= withdrawal
                    withdrawal_limit -= 1

                    print(f"\n${withdrawal}.00 has been withdrawn from your bank account.\nYour current balance is ${balance}.00\nYou are entitled to {withdrawal_limit} more withdrawals today.\n")
                    
                    transaction_records.append(f"Withdrawal: ${withdrawal}.00")                                  
                    break                    
                
            # except TypeError:
            #     break
            
            except ValueError:
                break
                # print(f"\nInvalid amount. Please, provide a valid amount to proceed with the withdrawal.\n")
                # continue
    
    elif selected_option == "s":
        
        if len(transaction_records) == 0:
            print(f"\nYour account history is empty.\n")
            continue

        else:
            for i in transaction_records: print(i)
            print(f"\nYour current balance is {balance} USD.")
            continue
    
    elif selected_option == "e":
        print(f"\nThank you! Have a nice day!\n")
        break
    
    else:
        print(f"\nUnknown error.\nRestarting terminal...\n")
        break