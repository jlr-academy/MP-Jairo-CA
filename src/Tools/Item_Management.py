import os
from Tools.uitilities import no_orders, like_to_continue, exit, cap, print_list

#Edit an item in a list   
def edit_item(log, string = "Product"):
    check_1 = True  
    while check_1 == True:
        os.system('cls')
        print(f"==========[ Edit a {string} ]========== \n")
        
        #check if list is empty
        if not no_orders(log):
            return

        print_list(log, string)
        
        #ask for an item to edit
        edit_id = input(f'\n     Enter the {string} ID to Edit . [E to Exit]. > ')

        #check if user wants to exit
        if exit(edit_id, f"     You select to Exit or not entered any commands from 'Editing an {string}'.. Press any key to Exit. > "):
            return log
        
        if edit_id.isnumeric() and len(log)>=int(edit_id)>0:
            
            edit_id=int(edit_id)-1
            
            print(f'\n     You Select to Change "{log[int(edit_id)]}".')
            
            #ask for the new name
            New_edit = cap(input(f'   Enter the new "{string} Name". [E to Exit]. > '))
            
            #check if duplicate and ask if user want to continue
            if New_edit in log:
                if not like_to_continue(f'\n {string} ID or Name already on database. Duplicate not permited.. Would you like to continue in "Edit a {string}"? - "Y" for yes and "N" for no.'):
                    check_1 = False
                    return log
            
            #check if user wnats to exit
            elif exit(New_edit,f"     You select to Exit or not entered any commands from 'Editing an {string}'.. Press any key to Exit. > "):
                check_1 = False
                return log
                
            #change item name or ID and ask if user want to continue
            else:
                print(f'\n"{log[edit_id]}" changed to "{New_edit}"')
                log[edit_id] = New_edit
                if like_to_continue(f'Would you like to continue in "Edit a {string}"? - "Y" for yes and "N" for no.'):
                    continue
                else:
                    input(f"     You select Exit from 'Editing an {string}'.. Press any key to Exit. > ")
                    check_1 = False
                    return log
        else:
            #ID or name not in the databse and ask if user want to continue
            if not like_to_continue(f'     You Select an ID that is NOT Available in the Data-Base. Would you like to continue in "Edit a {string}"? - "Y" for yes and "N" for no.'):
                check_1 = False
                return log          

#Delete an item in a list       
def del_item(log, string = "Product"):
    while True:
        os.system('cls')
        print(f"==========[ Delete an {string} ]==========\n")
        
        #check if list is empty
        if not no_orders(log):
            return log
        
        print_list(log, string)
        
        edit_id = input(f'\n     Enter the {string} ID to Delete . [E to Exit]. > ')

        #check if user wants to exit
        if exit(edit_id, f"     You select to Exit or not entered any commands from 'Deleting a {string}'.. Press any key to Exit. > "):
            return log

        if edit_id.isnumeric() and len(log)>=int(edit_id)>0: 
            
            edit_id = int(edit_id)-1
            # ask if user wants to delete, and if the user wants to continue in the delete menu
            if like_to_continue(f'\nDo you want to delete "{log[edit_id]}" ?  Y for Yes / N for No'):
                input(f'Deleting "{log[edit_id]}", Press any key to Continue..')
                log.pop(edit_id)
                if like_to_continue(f'\n{string} deleted.. Would you like to continue in "Delete a {string}"? - "Y" for yes and "N" for no.'):
                    continue
                else:
                    return log
            else:
                if like_to_continue(f'\n{string} not deleted.. Would you like to continue in "Delete a {string}"? - "Y" for yes and "N" for no.'):
                    continue
                else:
                    return log
        else:
            #ID or name not in the databse and ask if user want to continue
            if like_to_continue(f'     You Select an ID that is NOT Available in the Data-Base. Would you like to continue in "Delete a {string}"? - "Y" for yes and "N" for no.'):
                pass
            else:
                return log

#Add an item to a list
def add_item(log, string = "Product"):
    os.system('cls')
    check = True
    while check  == True:
        os.system('cls')
        print(f"==========[ Add New {string} ]==========")
        print('   NOTE: Enter E any time to EXIT. ')  
        
        #ask for the item name or ID
        order_Num = cap(input(f'   Enter the {string} ID or Name. > '))
        
        #check if duplicate and ask if user want to continue
        if order_Num in log:
            if  like_to_continue(f'{string} ID or Name already on database. Duplicate not permited.. Would you like to continue in "Add New {string}"? - "Y" for yes and "N" for no.'):
                check = True
            else:
                check = False
                return log
            
        #check if user want to exit
        elif exit(order_Num, f"     You select to Exit or not entered any commands from 'Add New {string}'.. Press any key to Exit. > "):
            return log
        
        #add new item and ask if it wants to continue
        else:
            log.append(order_Num)
            print(f'"{order_Num}" added to the database')
            if  like_to_continue(f'Would you like to continue in "Add New {string}"? - "Y" for yes and "N" for no.'):
                check = True
            else:
                check = False
                return log