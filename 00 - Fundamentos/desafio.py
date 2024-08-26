# Resolution of the challenge from the DIO - Data Engineer Bootcamp

open_menu = """
    --------------------------------------------------------
    Terminal FSG4356-GF

    Welcome! Please select one of the options below:
    d - deposit
    w - withdraw
    s - bank statement
    e - end session

    Please, be advised that this terminal only works with note bills, as it cannot accept or give coins.

    Happy Banking!

    Bank Co.® - All Rights reserved
    --------------------------------------------------------

Keyboard:
"""

balance = 0
transaction_records = []

while True:

    selected_option = input(open_menu)

    if selected_option == "d":
        
        while True:

            try:
                deposit = int(input("Please, inform the amount to be deposited: "))
                print(f'$ {deposit} deposited to your bank account.')
                transaction_records += deposit
            
            except ValueError:
                print("Invalid amount. Please, provide a valid amount to proceed with the deposit.")
                continue
            
    elif selected_option == "w":
        withdraw = input("Please, inform the amount to be withdrawed: ")
    
    elif selected_option == "e":
        print("Thank you! Have a nice day!")
        break
    
    else:
        "Invalid option. Please select one of the options above."
        
#not isinstance(1, 'int')

#         if withdraw >= 0 and withdraw <= balance:
#             transaction_records -= deposit
#         else:
#             "Invalid option. "
# # the lines below are being used for tests
