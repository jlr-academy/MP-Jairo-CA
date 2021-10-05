import json
def main_menu():
    print("==========[ Main Menu ]==========")
    print('     1. Add New Order.')
    print('     2. Edit an Order.')
    print('     3. Delete an Order.')
    print('     4. Show Orders.')
    print('     9. Exit.')
    
    user_choice = input("      Select from the Menu: > ") 
    
    # we will return the user choice.
    return user_choice
def no_orders(log):
    if not log:
        return input('No orders in the database. Press any key to Continue..') 
    else:
        return 1

def edit_order(log):
    print("==========[ Edit an Order ]==========")
    if not no_orders(log):
        return
    
    edit_id = input('\n     Enter the Product Name to be Edit . [E to Exit]. > ')
    edit_id = " ".join([word.capitalize() for word in edit_id.split(" ")]) 

    # Check user input e or empty or space.
    if edit_id.upper()=="E" or edit_id ==' ' or edit_id == '':
        input("\n     You select to Exit from 'Editing and Order'.. Press any key to Exit. > ")
        return
        
    # Check if user input not available or not Numeric 
    if edit_id in log.keys()  : 
        # Code to Edit order to the database 
        print(f'==========[ Edit "{edit_id}" ]==========')
        print('     1. Edit Order ID or Name.')
        print('     2. Edit Courier.')
        print('     3. Edit Status.')
        print('     9. Exit.')
    
        user_choice = input("      Select from the Menu: > ")
        if user_choice=='' or user_choice==' ':
            input("\n     You select Wrong value or Exit from 'Editing and Order'.. Press any key to Exit. > ")
            return
        else:
            user_choice=int(user_choice)

        if 3>=user_choice>0:
            list_keys=list(log[edit_id])
            user_choice=list_keys[user_choice-1]
            print(f'     You Select to Change "{user_choice}".')
            New_edit = input(f'   Enter the new "{user_choice}". > ')
            New_edit = " ".join([word.capitalize() for word in New_edit.split(" ")])
            if user_choice == "order_ID" and  New_edit in log.keys():
                input('Product ID or Name already on database. Duplicate not permited. Press any key to Continue..')
                return  
            log[edit_id][user_choice] = New_edit
            if user_choice == "order_ID":
                log[New_edit] = log.pop(edit_id)
            return log
        else:
            input("\n     You select Wrong value or Exit from 'Editing and Order'.. Press any key to Exit. > ")
            return
    else:
        input('\n     You Select an ID or name that NOT Available in the Data-Base. Press any key and Select Again. > ')
        return 
            
        
def del_order(log):
    print("==========[ Delete an Order ]==========")
    if not no_orders(log):
        return
    
    edit_id = input('\n     Enter the Product Name to Edit . [E to Exit]. > ')
    edit_id = " ".join([word.capitalize() for word in edit_id.split(" ")]) 
        
    # Check user input e or empty or space.
    if edit_id.upper()=="E" or edit_id ==' ' or edit_id == '':
        input("\n     You select to Exit from 'Deleting an order'.. Press any key to Exit. > ")
        return
        
    if edit_id in log.keys()  : 
        # Code to Edit order to the database 
        answer=input(f'Do you want to delete "{edit_id}" ?  Y for Yes / N for No')
        if answer.upper()=="Y" or answer ==' ' or answer == '':
            input(f'Deleting "{edit_id}", Press any key to Continue..')
            del log[edit_id]
            return log
        else:
            input("\n     You select to Exit from 'Deleting an order'.. Press any key to Exit. > ")
            return 
    else:
        input('\n     You Select an ID or name that NOT Available in the Data-Base. Press any key and Select Again. > ')
        return 
    input('      Press any key to Continue..')    
        
def q_to_quit(check):
        
    # If the user enter [q or Q] the function will return quit function. 
    if check.upper == 'Q' :
        return quit()

def add_order(log):
    print("==========[ Add New Order ]==========")
    print('   NOTE: Enter Q any time to EXIT/Quit. ')  
    
    order_Num = input('   Enter the order ID or Name. > ')
    order_Num = " ".join([word.capitalize() for word in order_Num.split(" ")])
    if order_Num in log.keys():
        input('Product ID or Name already on database. Duplicate not permited. Press any key to Continue..')
        return
    q_to_quit(order_Num)
    
    order_c = input('   Enter the courier. > ')
    q_to_quit(order_c)
    
    order_q  = input('   Enter the status of the order. > ')
    q_to_quit(order_q)
     
    order_c = " ".join([word.capitalize() for word in order_c.split(" ")]) 
    
    log[order_Num] = {"order_ID":order_Num, "Courier":order_c, "order_status":order_q}
    input('      Press any key to Continue..')
    return log

def show_order(log):
    print("==========[ Show Orders ]==========")  
    if not no_orders(log):
        return
    for key in log:
        
        print("   ID: ",log[key]["order_ID"])  
        print("Product: ",log[key]["Courier"])
        print("Quantity: ",log[key]["order_status"])
        
        print("-------------------------------------------------------------------\n")
    
    
    
    input('\n      Press any key to Continue..  ')  