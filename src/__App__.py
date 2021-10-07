from File_handlers.txt import read, write
from Tools.uitilities import create_menu, print_dict_k, print_list, no_orders, cap, like_to_continue, exit, print_dict
from Items import Order, Product, Courier
import os

#App
class Shop:
    def __init__(self, name: str):
        self.name = name
        self.product = list()
        self.courier  = list()
        self.order  = list()
                
    def Sub_menu(self, string = "item", list = list()):
        while True :
            user_select = create_menu(list = [f"{string} Menu", f"Add New {string}", f"Edit an {string}",  f"Delete a {string}", f"Show {string} list", "Return to Main Menu"])

            if user_select == '1' :
                self.add_item(list, string)

            elif user_select == '2' :
                self.edit_item(list, string)

            elif user_select == '3' :
                self.del_item(list, string)  

            elif user_select == '4' :
                os.system('cls')
                print(f"==========[ Show {string} list]========== \n")
                if no_orders(list):
                    print_list(list, string)
                    input('\n   Press any key and to continue..') 
            elif user_select == '5' :
                break

            else :
                input('   Select Only from the list..  Press any key and try again..') 

    def Order_menu(self, string = "item", list = list()):
        while True :
            user_select = create_menu(list = [f"{string} Menu", f"Add New {string}", f"Edit an {string}", f"Update {string} status",  f"Delete a {string}", f"Show {string} list", "Return to Main Menu"])

            if user_select == '1' :
                self.create_order(list)

            elif user_select == '2' :
                self.edit_order(list, string)
                
            elif user_select == '3' :
                self.edit_order_status(list, string)

            elif user_select == '4' :
                self.del_item(list, string)  

            elif user_select == '5' :
                os.system('cls')
                print(f"==========[ Show {string} list]========== \n")
                if no_orders(list):
                    print_dict(list, string)
                    input('\n   Press any key and to continue..') 
            elif user_select == '6' :
                break

            else :
                input('   Select Only from the list..  Press any key and try again..') 
                
    def launch(self):
        #Read txt data if any
        self.product = read(".\\Data", "Product_list.txt")
        self.courier = read(".\\Data", "Courier_list.txt")
        
        while True :
            user_select = create_menu(list = ["Main Menu", "Product Menu", "Courier Menu", "Order Menu",  "Exit"])
            if user_select == '1' :
                self.Sub_menu("Product", self.product)
                
            elif user_select == '2' :
                self.Sub_menu("Courier", self.courier)
                
            elif user_select == '3' :
                self.Order_menu("Order", self.order)
            
            elif user_select == '4' :
                print('\n\n   Thank you for using this Appliation. ')
                break
                    
            else :
                input('   Select Only from the list..  Press any key and try again..') 

        #Write txt data  
        write(self.product, ".\\Data", "Product_list.txt")
        write(self.courier, ".\\Data", "Courier_list.txt")

    #Add an item to a list
    def add_item(self, log = list(), string = "Product"):
        os.system('cls')
        check = True
        while check  == True:
            os.system('cls')
            print(f"==========[ Add New {string} ]==========")
            print('   NOTE: Enter E any time to EXIT. ')  

            #ask for the item name or ID
            order_Num = cap(input(f'   Enter the {string} ID or Name. > '))

            #check if duplicate and ask if user want to continue
            if order_Num in [obj.name for obj in log]:
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
                if string == "Product":
                    log.append(Product(order_Num))
                else:
                    log.append(Courier(order_Num))
                    
                print(f'"{order_Num}" added to the database')
                if  like_to_continue(f'Would you like to continue in "Add New {string}"? - "Y" for yes and "N" for no.'):
                    check = True
                else:
                    check = False
                    return log

    def create_order(self, log = list()):
        os.system('cls')
        check = True
        while check  == True:
            os.system('cls')
            print("==========[ Add New Order ]==========")

            #ask for the order info
            dummy = {}
            c_nam = cap(input(f'   Enter the Customer Name. > '))
            c_ad = cap(input(f'   Enter the Customer Adress. > '))
            c_ph = cap(input(f'   Enter the Customer Phone number. > '))
            
            while True:
                os.system('cls')
                print_list(self.courier, "Courier")
                c_cour = input('     Select the Courier ID . > ')
                if c_cour.isnumeric() and len(self.courier)>=int(c_cour)>0:
                    break
                else:
                    input('   Select Only from the list..  Press any key and try again..')
            
            dummy["customer_name"] = c_nam
            dummy["customer_address"] = c_ad
            dummy["customer_phone"] = c_ph
            dummy["courier"] = int(c_cour)
            dummy["status"] = "Preparing"

            #add new item and ask if it wants to continue
            log.append(Order(dummy))
                    
            print(f'"Order added to the database')
            if  like_to_continue('Would you like to continue in "Add New Order"? - "Y" for yes and "N" for no.'):
                check = True
            else:
                check = False
                return log  
        
    #Edit an item in a list   
    def edit_order(self, log=list(), string = "Order"):
        check_1 = True  
        while check_1 == True:
            os.system('cls')
            print(f"==========[ Edit a {string} ]========== \n")

            #check if list is empty
            if not no_orders(log):
                return

            print_dict(log, string)

            #ask for an item to edit
            edit_id = input(f'\n     Enter the {string} ID to Edit . [E to Exit]. > ')

            #check if user wants to exit
            if exit(edit_id, f"     You select to Exit or not entered any commands from 'Editing an {string}'.. Press any key to Exit. > "):
                return log

            if edit_id.isnumeric() and len(log)>=int(edit_id)>0:

                edit_id=int(edit_id)-1
                
                #ask for the key to edit
                while True:
                    os.system('cls')
                    print(f'\n     You Select to Change "{log[edit_id].contents}".')
                    l = print_dict_k(log[int(edit_id)].contents)
                    key_edit = input('     Select the parameter to edit . > ')
                    if key_edit.isnumeric() and 5>=int(key_edit)>0:
                        key_edit = int(key_edit)-1
                        break
                    else:
                        input('   Select Only from the list..  Press any key and try again..')
                        
                if l[key_edit] == "courier":
                    while True:
                        os.system('cls')
                        print_list(self.courier, "Courier")
                        c_cour = input('     Select the new Courier ID . > ')
                        if c_cour.isnumeric() and len(self.courier)>=int(c_cour)>0:
                            break
                        else:
                            input('   Select Only from the list..  Press any key and try again..')
                    new_edit = int(c_cour)
                elif l[key_edit] == "status":
                    while True:
                        os.system('cls')
                        options = ["Preparing", "On its Way", "Delivered", "Cancelled"]
                        for count, value in enumerate(options):
                            print(f"ID-{count+1}: {value}")
                        status = input('     Select the new Status ID . > ')
                        if status.isnumeric() and len(options)>=int(status)>0:
                            status = int(status)-1
                            break
                        else:
                            input('   Select Only from the list..  Press any key and try again..')
                    new_edit = options[status]
                else:
                    #change item name or ID and ask if user want to continue
                    new_edit = cap(input(f'\n"Enter new {l[key_edit]}"'))
                if new_edit:
                    print(f"{log[edit_id].contents[l[key_edit]]} changed to {new_edit}")
                    log[edit_id].contents[l[key_edit]] = new_edit
                    if like_to_continue(f'Would you like to continue in "Edit a {string}"? - "Y" for yes and "N" for no.'):
                        continue
                    else:
                        input(f"     You select Exit from 'Editing an {string}'.. Press any key to Exit. > ")
                        check_1 = False
                        return log
                else:
                    #blank
                    if not like_to_continue(f'     You entered blank and the value was not updated. Would you like to continue in "Edit a {string}"? - "Y" for yes and "N" for no.'):
                        check_1 = False
                        return log
            else:
                #ID or name not in the databse and ask if user want to continue
                if not like_to_continue(f'     You Select an ID that is NOT Available in the Data-Base. Would you like to continue in "Edit a {string}"? - "Y" for yes and "N" for no.'):
                    check_1 = False
                    return log

    #Edit an item in a list   
    def edit_order_status(self, log=list(), string = "Order Status"):
        check_1 = True  
        while check_1 == True:
            os.system('cls')
            print(f"==========[ Edit a Status ]========== \n")

            #check if list is empty
            if not no_orders(log):
                return

            print_dict(log, string)

            #ask for an item to edit
            edit_id = input(f'\n     Enter the {string} ID to Edit . [E to Exit]. > ')

            #check if user wants to exit
            if exit(edit_id, f"     You select to Exit or not entered any commands from 'Editing an {string}'.. Press any key to Exit. > "):
                return log

            if edit_id.isnumeric() and len(log)>=int(edit_id)>0:

                edit_id=int(edit_id)-1
                
                #ask for the key to edit
                while True:
                    os.system('cls')
                    print(f'\n     You Select to Change the Status of "{log[edit_id].contents}".')
                    options = ["Preparing", "On its Way", "Delivered", "Cancelled"]
                    for count, value in enumerate(options):
                        print(f"ID-{count+1}: {value}")
                    status = input('     Select the new Status ID . > ')
                    if status.isnumeric() and len(options)>=int(status)>0:
                        status = int(status)-1
                        break
                    else:
                        input('   Select Only from the list..  Press any key and try again..')
                new_edit = options[status]
                    
                print(f"{log[edit_id].contents['status']} changed to {new_edit}")
                log[edit_id].contents['status'] = new_edit
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

    #Edit an item in a list   
    def edit_item(self, log=list(), string = "Product"):
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

                print(f'\n     You Select to Change "{log[int(edit_id)].name}".')

                #ask for the new name
                New_edit = cap(input(f'   Enter the new "{string} Name". [E to Exit]. > '))

                #check if duplicate and ask if user want to continue
                if New_edit in [obj.name for obj in log]:
                    if not like_to_continue(f'\n {string} ID or Name already on database. Duplicate not permited.. Would you like to continue in "Edit a {string}"? - "Y" for yes and "N" for no.'):
                        check_1 = False
                        return log

                #check if user wnats to exit
                elif exit(New_edit,f"     You select to Exit or not entered any commands from 'Editing an {string}'.. Press any key to Exit. > "):
                    check_1 = False
                    return log

                #change item name or ID and ask if user want to continue
                else:
                    print(f'\n"{log[edit_id].name}" changed to "{New_edit}"')
                    log[edit_id].name = New_edit
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
    def del_item(self, log, string = "Product"):
        while True:
            os.system('cls')
            print(f"==========[ Delete an {string} ]==========\n")

            #check if list is empty
            if not no_orders(log):
                return log

            if string == "Product" or string == "Courier":
                print_list(log, string)
            else:
                print_dict(log, string)

            edit_id = input(f'\n     Enter the {string} ID to Delete . [E to Exit]. > ')

            #check if user wants to exit
            if exit(edit_id, f"     You select to Exit or not entered any commands from 'Deleting a {string}'.. Press any key to Exit. > "):
                return log

            if edit_id.isnumeric() and len(log)>=int(edit_id)>0: 

                edit_id = int(edit_id)-1
                # ask if user wants to delete, and if the user wants to continue in the delete menu
                if like_to_continue(f'\nDo you want to proceed?  Y for Yes / N for No'):
                    input(f'Deleting.., Press any key to Continue..')
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
                
tienda_1 = Shop("1")
tienda_1.launch() 


    