from File_handlers.excl_csv import read, write
from Tools.uitilities import create_menu, print_dict_k, print_list, no_orders, cap, like_to_continue, exit, print_dict, create_dict, create_dict_with_list
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
                self.edit_order(list, string)

            elif user_select == '3' :
                self.del_item(list, string)  

            elif user_select == '4' :
                os.system('cls')
                print(f"==========[ Show {string} list]========== \n")
                if no_orders(list, string):
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
                if no_orders(list, string):
                    print_list(list, string)
                    input('\n   Press any key and to continue..') 
            elif user_select == '6' :
                break

            else :
                input('   Select Only from the list..  Press any key and try again..') 
                
    def launch(self):
        #Read txt data if any
        for item in read(".\\Data", "Product_list.csv"): self.product.append(Product(item))
        for item in read(".\\Data", "Courier_list.csv"): self.courier.append(Courier(item))
        for item in read(".\\Data", "Order_list.csv"): self.order.append(Order(item))
        
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
        write(self.product, ".\\Data", "Product_list.csv")
        write(self.courier, ".\\Data", "Courier_list.csv")
        write(self.order, ".\\Data", "Order_list.csv")

    #Add an item to a list
    def add_item(self, log = list(), string = "Product"):
        os.system('cls')
        check = True
        while check  == True:
            os.system('cls')
            print(f"==========[ Add New {string} ]==========")

            #add new item and ask if it wants to continue
            if string == "Product":
                dummy = create_dict({}, ["name", "price"], self.product)
            else:
                dummy = create_dict({}, ["name", "phone"], self.courier)
                
            if not "name" in dummy.keys():
                if  like_to_continue(f'{string} ID or Name not created.. Would you like to continue in "Add New {string}"? - "Y" for yes and "N" for no.'):
                    check = True
                    continue
                else:
                    check = False
                    return log
            else:
                if string == "Product":
                    log.append(Product(dummy))
                else:
                    log.append(Courier(dummy))
                
            print(f'"{dummy["name"]}" added to the database')
            if  like_to_continue(f'Would you like to continue in "Add New {string}"? - "Y" for yes and "N" for no.'):
                check = True
            else:
                check = False
                return log

    def create_order(self, log = list()):
        os.system('cls')
        check = True
        if not no_orders(self.courier, "Courier"):
            return
        if not no_orders(self.product, "Product"):
            return
        while check  == True:
            os.system('cls')
            print("==========[ Add New Order ]==========")

            #ask for the order info
            dummy = create_dict({}, ["customer_name", "customer_address", "customer_phone"], self.order)
            
            dummy = create_dict_with_list(dummy, self.courier, "courier", multiple = False)
            
            dummy = create_dict_with_list(dummy, self.product, "product", multiple = True)
            
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
            if not no_orders(log, string):
                return

            print_list(log, string)

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
                    if key_edit.isnumeric() and len(log[int(edit_id)].contents)>=int(key_edit)>0:
                        key_edit = int(key_edit)-1
                        break
                    else:
                        input('   Select Only from the list..  Press any key and try again..')
                        
                if l[key_edit] == "courier":
                    log[edit_id].contents = create_dict_with_list(log[edit_id].contents, self.courier, "courier", multiple = False)
                    
                elif l[key_edit] == "product":
                    log[edit_id].contents = create_dict_with_list(log[edit_id].contents, self.product, "product", multiple = True)
                elif l[key_edit] == "status":
                    log[edit_id].contents = create_dict_with_list(log[edit_id].contents, ["Preparing", "On its Way", "Delivered", "Cancelled"], "status", multiple = False)
                else:
                    log[edit_id].contents = create_dict(log[edit_id].contents, [l[key_edit]], getattr(self, string.lower()))
                    
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
    def edit_order_status(self, log=list(), string = "Order Status"):
        check_1 = True  
        while check_1 == True:
            os.system('cls')
            print(f"==========[ Edit a Status ]========== \n")

            #check if list is empty
            if not no_orders(log, "Order"):
                return

            print_list(log, "Order")

            #ask for an item to edit
            edit_id = input(f'\n     Enter the {string} ID to Edit . [E to Exit]. > ')

            #check if user wants to exit
            if exit(edit_id, f"     You select to Exit or not entered any commands from 'Editing an {string}'.. Press any key to Exit. > "):
                return log

            if edit_id.isnumeric() and len(log)>=int(edit_id)>0:

                edit_id=int(edit_id)-1
                
                print(f'\n     You Select to Change the Status of "{log[edit_id].contents}".')
                log[edit_id].contents = create_dict_with_list(log[edit_id].contents, ["Preparing", "On its Way", "Delivered", "Cancelled"], "status", multiple = False)
                
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
            if not no_orders(log, string):
                return

            print_list(log, string)

            #ask for an item to edit
            edit_id = input(f'\n     Enter the {string} ID to Edit . [E to Exit]. > ')

            #check if user wants to exit
            if exit(edit_id, f"     You select to Exit or not entered any commands from 'Editing an {string}'.. Press any key to Exit. > "):
                return log

            if edit_id.isnumeric() and len(log)>=int(edit_id)>0:

                edit_id=int(edit_id)-1

                print(f'\n     You Select to Change "{log[int(edit_id)].contents}".')

                #ask for the new name
                New_edit = cap(input(f'   Enter the new "{string} Name". [E to Exit]. > '))

                #check if duplicate and ask if user want to continue
                if New_edit in [obj.contents for obj in log]:
                    if not like_to_continue(f'\n {string} ID or Name already on database. Duplicate not permited.. Would you like to continue in "Edit a {string}"? - "Y" for yes and "N" for no.'):
                        check_1 = False
                        return log

                #check if user wnats to exit
                elif exit(New_edit,f"     You select to Exit or not entered any commands from 'Editing an {string}'.. Press any key to Exit. > "):
                    check_1 = False
                    return log

                #change item name or ID and ask if user want to continue
                else:
                    print(f'\n"{log[edit_id].contents}" changed to "{New_edit}"')
                    log[edit_id].contents = New_edit
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
            if not no_orders(log, string):
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
                
                if (string.lower() == "product" or string.lower() == "courier"):
                    item_used_in_order = 0
                    for item in self.order:
                        if isinstance(item.contents[string.lower()], int):
                            if item.contents[string.lower()] == int(edit_id):
                                item_used_in_order = 1
                                if like_to_continue(f'\n{string} linked to an order. Not deleted.. Would you like to continue in "Delete a {string}"? - "Y" for yes and "N" for no.'):
                                    break
                                else:
                                    return log
                        else:
                            for i in item.contents[string.lower()]:
                                if int(edit_id) == i:
                                    item_used_in_order = 1
                                    if like_to_continue(f'\n{string} linked to an order. Not deleted.. Would you like to continue in "Delete a {string}"? - "Y" for yes and "N" for no.'):
                                        break
                                    else:
                                        return log
                        if item_used_in_order == 1:
                            break
                if item_used_in_order == 1:
                    continue
                
                edit_id = int(edit_id)-1
                

                # ask if user wants to delete, and if the user wants to continue in the delete menu
                if like_to_continue(f'\nDo you want to proceed?  Y for Yes / N for No'):
                    input(f'Deleting.., Press any key to Continue..')
                    log.pop(edit_id)
                    if (string.lower() == "product" or string.lower() == "courier"):
                        for item in self.order:
                            if isinstance(item.contents[string.lower()], int):
                                if item.contents[string.lower()] > edit_id:
                                    item.contents[string.lower()] = item.contents[string.lower()]-1
                            else:
                                for i in range(0, len(item.contents[string.lower()])):
                                    if edit_id+1 < item.contents[string.lower()][i]:
                                        item.contents[string.lower()][i] = item.contents[string.lower()][i]-1
                    
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


    