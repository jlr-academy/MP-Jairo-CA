from File_handlers.excl_csv import write, read
from Tools.uitilities import create_menu, print_dict_k, print_list, no_orders, cap, like_to_continue, exit, print_dict, create_dict, create_dict_with_list, clear
from Items import Order, Product, Courier
from Tools.sql_utilities import add_item_table, edit_item_table, delete_item_table, add_order_table, fetch_orders, fetch_orders_details, fetch_orders_status, edit_order_products, delete_order, fetch_orders_courier
from Tools.sql_utilities import read as read_sql
from colorama import Fore, Back, Style
import os
from colorama import init
init(autoreset=True)

#App
class Shop:
    def __init__(self, name: str):
        self.name = name
        self.product = list()
        self.courier  = list()
        self.order  = list()
                
    def Sub_menu(self, string = "item"):
        
        if string.lower() == "product": 
            self.product.clear()
            for item in read_sql("products"): self.product.append(Product(item))
            list = self.product
        
        else: 
            self.courier.clear()
            for item in read_sql("couriers"): self.courier.append(Courier(item))
            list = self.courier
            
        while True :
            user_select = create_menu(list = [f"{string} Menu", f"Add New {string}", f"Edit an {string}",  f"Delete a {string}", f"Show {string} list", "Return to Main Menu"])

            if user_select == '1' :
                self.add_item(string)

            elif user_select == '2' :
                self.edit_item(string)

            elif user_select == '3' :
                self.del_item(string)  

            elif user_select == '4' :
                clear()
                print(Back.LIGHTBLACK_EX + '{:=^100}'.format(f'Show {string} list'), "\n")
                

                if no_orders(list, string):
                    print_list(list)
                    input('\n {:<50}'.format(Fore.CYAN + 'Press any key and to continue..'))
                    
            elif user_select == '5' :
                break

            else :
                input('\n {:<50}'.format(Back.RED + Fore.WHITE + 'Select Only from the list..  Press any key and try again..'))
                
                
    def Order_menu(self, string = "item"):
        while True :
            user_select = create_menu(list = [f"{string} Menu", f"Add New {string}", f"Edit an {string}", f"Update {string} status",  f"Delete a {string}", f"Show {string} list", "Return to Main Menu"])

            if user_select == '1' :
                self.create_order()
                
            elif user_select == '2' :
                self.edit_order(string)
                
            elif user_select == '3' :
                self.edit_order_status(string)

            elif user_select == '4' :
                self.del_order(string)  

            elif user_select == '5' :
                self.show_orders()
                        
            elif user_select == '6' :
                break

            else :
                input('\n {:<50}'.format(Back.RED + Fore.WHITE + 'Select Only from the list..  Press any key and try again..'))
                
                                
    def Customer_menu(self, string = "item", list = list()):
        while True :
            user_select = create_menu(list = [f"{string} Menu", f"Add New {string}", f"Edit a {string}",  f"Delete a {string}", f"Show {string} list", "Return to Main Menu"])

            if user_select == '1' :
                self.add_customer("Customer")
                
            elif user_select == '2' :
                self.edit_customer(string)

            elif user_select == '3' :
                self.del_customer(string)  

            elif user_select == '4' :
                clear()
                print(Back.LIGHTBLACK_EX + '{:=^100}'.format(f'Show {string} list'), "\n")
                list = read_sql("customers")
                if no_orders(list, string):
                    print_list(list)
                    input('\n {:<50}'.format(Fore.CYAN + 'Press any key to continue..'))
                        
            elif user_select == '5' :
                break

            else :
                input('\n {:<50}'.format(Back.RED + Fore.WHITE + 'Select Only from the list..  Press any key and try again..'))
                
                                
    def launch(self):
        #Read txt data if any
        read_sql("products")
        read_sql("couriers")
        read_sql("orders")
        
        while True :
            user_select = create_menu(list = ["Main Menu", "Product Menu", "Courier Menu", "Customer Menu", "Order Menu",  "Exit"])
            if user_select == '1' :
                self.Sub_menu("Product")
                
            elif user_select == '2' :
                self.Sub_menu("Courier")
                
            elif user_select == '3' :
                self.Customer_menu("Customer")
                
            elif user_select == '4' :
                self.Order_menu("Order")
            
            elif user_select == '5' :
                print('\n\n   Thank you for using this Appliation. ')
                break
                    
            else :
                input('\n {:<50}'.format(Back.RED + Fore.WHITE + 'Select Only from the list..  Press any key and try again..'))
                
                
        #Write txt data  
        write(self.product, "Data", "Product_list.csv")
        write(self.courier, "Data", "Courier_list.csv")
        write(self.order, "Data", "Order_list.csv")

    #Add an item to a list
    def add_item(self, string = "Product"):
        clear()
        
        if string.lower() == "product": 
            self.product.clear()
            for item in read_sql("products"): self.product.append(Product(item))
            log = self.product
        
        else: 
            self.courier.clear()
            for item in read_sql("couriers"): self.courier.append(Courier(item))
            log = self.courier
            
        check = True
        while check  == True:
            clear()
            print(Back.LIGHTBLACK_EX + '{:=^100}'.format(f'Add New {string}'), "\n")
            

            #add new item and ask if it wants to continue
            if string == "Product":
                dummy = create_dict({}, ["name", "price", "quantity"], self.product)
            else:
                dummy = create_dict({}, ["name", "phone"], self.courier)
                
            if not "name" in dummy.keys():
                if  like_to_continue(f'{string} Item not created.. Would you like to continue in "Add New {string}"? - "Y" for yes and "N" for no.'):
                    check = True
                    continue
                else:
                    check = False
                    return log
            else:
                if string == "Product":
                    dummy = add_item_table(dummy, "products")
                    log.append(Product(dummy))
                else:
                    dummy = add_item_table(dummy, "couriers")
                    log.append(Courier(dummy))
                
            print('\n {:<50}'.format(f'"{dummy["name"]}"' + Fore.CYAN + ' added to the database'))
            
            if  like_to_continue(f'Would you like to continue in "Add New {string}"? - "Y" for yes and "N" for no.'):
                check = True
            else:
                check = False
                return log

    #Add an customer
    def add_customer(self, string = "Customer"):
        clear()
        check = True
        while check  == True:
            clear()
            print(Back.LIGHTBLACK_EX + '{:=^100}'.format(f'Add New {string}'), "\n")
            

            log = read_sql("customers")

            #add new item and ask if it wants to continue
            dummy = create_dict({}, ["name", "address", "phone"], log)
                
            if not "name" in dummy.keys():
                if  like_to_continue(f'{string} Item not created.. Would you like to continue in "Add New {string}"? - "Y" for yes and "N" for no.'):
                    check = True
                    continue
                else:
                    check = False
                    return
            else:
                dummy = add_item_table(dummy, "customers")
                
            print('\n {:<50}'.format(f'"{dummy["name"]}"' + Fore.CYAN + ' added to the database'))
            if  like_to_continue(f'Would you like to continue in "Add New {string}"? - "Y" for yes and "N" for no.'):
                check = True
            else:
                check = False
                return
            
    def create_order(self):
        clear()
        
        check = True
        
        while check  == True:
        
            self.product.clear()
            self.courier.clear()

            for item in read_sql("products"): 
                if item["quantity"] > 0: self.product.append(Product(item))

            for item in read_sql("couriers"): self.courier.append(Courier(item))

            if not no_orders(self.courier, "Courier"):
                return
            if not no_orders(self.product, "Product"):
                return
        
            clear()
            print(Back.LIGHTBLACK_EX + '{:=^100}'.format('Add New Order'), "\n")
            

            #ask for the order info
            dummy_customers = read_sql("customers")
            
            if not no_orders(dummy_customers, "Customer"):
                return
            
            dummy = {}
            
            dummy = create_dict_with_list(dummy, dummy_customers, "customer", multiple = False)
            
            dummy = create_dict_with_list(dummy, self.courier, "courier", multiple = False)
            
            dummy = create_dict_with_list(dummy, self.product, "product", multiple = True)
            
            dummy["status"] = "Preparing"

            #add new item and ask if it wants to continue
            add_order_table(dummy, "orders")
                    
            print('\n {:<50}'.format(Fore.CYAN + f'"Order added to the database'))
            if  like_to_continue('Would you like to continue in "Add New Order"? - "Y" for yes and "N" for no.'):
                check = True
            else:
                check = False
        
    #Edit an item in a list   
    def edit_item(self, string = "Order"):
        
        if string.lower() == "product": 
            self.product.clear()
            for item in read_sql("products"): self.product.append(Product(item))
            log = self.product
        
        else: 
            self.courier.clear()
            for item in read_sql("couriers"): self.courier.append(Courier(item))
            log = self.courier
            
        check_1 = True  
        while check_1 == True:
            clear()
            print(Back.LIGHTBLACK_EX + '{:=^100}'.format(f'Edit a {string}'), "\n")
            

            #check if list is empty
            if not no_orders(log, string):
                return

            print_list(log)

            #ask for an item to edit
            edit_id = input('\n {:<50}'.format(Fore.CYAN + f'Enter the {string} ID to Edit . [E to Exit]. > ' + Style.RESET_ALL))

            #check if user wants to exit
            if exit(edit_id, f"     You select to Exit or not entered any commands from 'Editing an {string}'.. Press any key to Exit. > "):
                return log
            
            if edit_id.isnumeric() and int(edit_id) in [obj.contents["id"] for obj in log]:

                for i in range(0,len(log)):
                    if int(edit_id) == log[i].contents["id"]:
                        edit_id = i
                        break
                                
                #ask for the key to edit
                while True:
                    clear()
                    print(Back.LIGHTBLACK_EX + '{:=^100}'.format(f'Edit a {string}'), "\n")
                    print('\n {:<50}'.format(Fore.CYAN + f'You Select to Change: ' + Fore.WHITE + f'"{log[edit_id].contents}".'))
                    
                    l = print_dict_k(log[int(edit_id)].contents)
                    key_edit = input('\n {:<50}'.format(Fore.CYAN + 'Select the parameter ID to edit . > ' + Style.RESET_ALL))
                    
                    if key_edit.isnumeric() and len(log[int(edit_id)].contents)-1>=int(key_edit)>0:
                        key_edit = int(key_edit)-1
                        break
                    else:
                        input('\n {:<50}'.format(Back.RED + Fore.WHITE + 'Select Only from the list..  Press any key and try again..' + Style.RESET_ALL))
                        
                log[edit_id].contents = create_dict(log[edit_id].contents, [l[key_edit]], getattr(self, string.lower()))
                
                if string == "Product" and log[edit_id]:
                    edit_item_table(log[edit_id].contents["id"], log[edit_id].contents, l[key_edit], "products")
                if string == "Courier" and log[edit_id]:
                    edit_item_table(log[edit_id].contents["id"], log[edit_id].contents, l[key_edit], "couriers")
                    
                if like_to_continue(f'Would you like to continue in "Edit a {string}"? - "Y" for yes and "N" for no.'):
                    continue
                else:
                    check_1 = False
                    return log
            else:
                #ID or name not in the databse and ask if user want to continue
                if not like_to_continue(f'You Select an ID that is NOT Available in the Data-Base. Would you like to continue in "Edit a {string}"? - "Y" for yes and "N" for no.'):
                    check_1 = False
                    return log
                
    def edit_customer(self, string = "Customer"):
        check_1 = True  
        while check_1 == True:
            clear()
            print(Back.LIGHTBLACK_EX + '{:=^100}'.format(f'Edit a {string}'), "\n")
            

            log = read_sql("customers")

            #check if list is empty
            if not no_orders(log, string):
                return

            print_list(log)

            #ask for an item to edit
            edit_id = input('\n {:<50}'.format(Fore.CYAN + f'Enter the {string} ID to Edit . [E to Exit]. > ' + Style.RESET_ALL))

            #check if user wants to exit
            if exit(edit_id, f"     You select to Exit or not entered any commands from 'Editing an {string}'.. Press any key to Exit. > "):
                return log
            
            if edit_id.isnumeric() and int(edit_id) in [obj["id"] for obj in log]:

                for i in range(0,len(log)):
                    if int(edit_id) == log[i]["id"]:
                        edit_id = i
                        break
                                
                #ask for the key to edit
                while True:
                    clear()
                    print(Back.LIGHTBLACK_EX + '{:=^100}'.format(f'Edit a {string}'), "\n")
                    print('\n {:<50}'.format(Fore.CYAN + f'You Select to Change: ' + Fore.WHITE + f'"{log[edit_id]}".'))
                    
                    l = print_dict_k(log[int(edit_id)])
                    key_edit = input('\n {:<50}'.format(Fore.CYAN + 'Select the parameter ID to edit . > ' + Style.RESET_ALL))
                    
                    if key_edit.isnumeric() and len(log[int(edit_id)])-1>=int(key_edit)>0:
                        key_edit = int(key_edit)-1
                        break
                    else:
                        input('\n {:<50}'.format(Back.RED + Fore.WHITE + 'Select Only from the list..  Press any key and try again..' + Style.RESET_ALL))
                        
                                        
                log[edit_id] = create_dict(log[edit_id], [l[key_edit]], log)
                
                if log[edit_id]: edit_item_table(log[edit_id]["id"], log[edit_id], l[key_edit], "customers")
                    
                if like_to_continue(f'Would you like to continue in "Edit a {string}"? - "Y" for yes and "N" for no.'):
                    continue
                else:
                    input('\n {:<50}'.format(Fore.CYAN + f"You select Exit from 'Editing an {string}'.. Press any key to Exit. > " + Style.RESET_ALL))
                    check_1 = False
                    return log
            else:
                #ID or name not in the databse and ask if user want to continue
                if not like_to_continue(f'You Select an ID that is NOT Available in the Data-Base. Would you like to continue in "Edit a {string}"? - "Y" for yes and "N" for no.'):
                    check_1 = False
                    return log

    def edit_order(self, string = "Order"):
        check_1 = True  
        while check_1 == True:
            clear()
            print(Back.LIGHTBLACK_EX + '{:=^100}'.format(f'Edit a {string}'), "\n")
            

            log = fetch_orders("orders")
            
            #check if list is empty
            if not no_orders(log, string):
                return
            
            self.product.clear()
            self.courier.clear()

            for item in read_sql("products"): 
                if item["quantity"] > 0: self.product.append(Product(item))

            for item in read_sql("couriers"): self.courier.append(Courier(item))

            if not no_orders(self.courier, "Courier"):
                return
            if not no_orders(self.product, "Product"):
                return

            print_list(log)

            #ask for an item to edit
            edit_id = input('\n {:<50}'.format(Fore.CYAN + f'Enter the {string} ID to Edit . [E to Exit]. > ' + Style.RESET_ALL))

            #check if user wants to exit
            if exit(edit_id, f"     You select to Exit or not entered any commands from 'Editing an {string}'.. Press any key to Exit. > "):
                return log
            
            if edit_id.isnumeric() and (int(edit_id) in [obj["id"] for obj in log]):
                
                [x, dummy_p] = fetch_orders_details(edit_id)
                                
                for i in range(0,len(log)):
                    if int(edit_id) == log[i]["id"]:
                        edit_id = i
                        break
                    
                log[int(edit_id)]["product"] = dummy_p
                                
                #ask for the key to edit
                while True:
                    clear()
                    print(Back.LIGHTBLACK_EX + '{:=^100}'.format(f'Edit a {string}'), "\n")
                    print('\n {:<50}'.format(Fore.CYAN + f'You Select to Change: ' + Fore.WHITE + f'"{log[edit_id]}".'))
                    
                    l = ["customer", "courier", "product", "status"]
                    print_list(l)
                    key_edit = input('\n {:<50}'.format(Fore.CYAN + 'Select the parameter ID to edit . > ' + Style.RESET_ALL))
                    
                    if key_edit.isnumeric() and len(log[int(edit_id)])-1>=int(key_edit)>0:
                        key_edit = int(key_edit)-1
                        break
                    else:
                        input('\n {:<50}'.format(Back.RED + Fore.WHITE + 'Select Only from the list..  Press any key and try again..' + Style.RESET_ALL))
                        
                                                
                if l[key_edit] == "courier":
                    log[edit_id] = create_dict_with_list(log[edit_id], self.courier, "courier", multiple = False)
                    edit_item_table(log[edit_id]["id"], log[edit_id], l[key_edit], "orders")
                    
                elif l[key_edit] == "product":
                    log[edit_id] = create_dict_with_list(log[edit_id], self.product, "product", multiple = True)
                    edit_order_products(log[edit_id]["id"], log[edit_id], l[key_edit], "order_products")
                    
                elif l[key_edit] == "status":
                    log[edit_id] = create_dict_with_list(log[edit_id], ["Preparing", "On its Way", "Delivered", "Cancelled"], "status", multiple = False)
                    edit_item_table(log[edit_id]["id"], log[edit_id], l[key_edit], "orders")
                    
                else:
                    dummy_c = read_sql("customers")
                    log[edit_id] = create_dict_with_list(log[edit_id], dummy_c , "customer", multiple = False)
                    edit_item_table(log[edit_id]["id"], log[edit_id], l[key_edit], "orders")
                    
                print('\n {:<50}'.format(Fore.CYAN + "Order updated"))
                
                if like_to_continue(f'Would you like to continue in "Edit a {string}"? - "Y" for yes and "N" for no.'):
                    continue
                else:
                    check_1 = False
                    return log
            else:
                #ID or name not in the databse and ask if user want to continue
                if not like_to_continue(f'     You Select an ID that is NOT Available in the Data-Base. Would you like to continue in "Edit a {string}"? - "Y" for yes and "N" for no.'):
                    check_1 = False
                    return log
                
    #Edit an item in a list   
    def edit_order_status(self, string = "Order Status"):
        check_1 = True  
        while check_1 == True:
            clear()
            print(Back.LIGHTBLACK_EX + '{:=^100}'.format(f'Edit a {string}'), "\n")
            

            log = fetch_orders("orders")
            
            #check if list is empty
            if not no_orders(log, string):
                return

            print_list(log)

            #ask for an item to edit
            edit_id = input('\n {:<50}'.format(Fore.CYAN + f'Enter the Order ID to Edit . [E to Exit]. > ' + Style.RESET_ALL))

            #check if user wants to exit
            if exit(edit_id, f"     You select to Exit or not entered any commands from 'Editing an {string}'.. Press any key to Exit. > "):
                return log
            
            if edit_id.isnumeric() and (int(edit_id) in [obj["id"] for obj in log]):
                
                [x, dummy_p] = fetch_orders_details(edit_id)
                                
                for i in range(0,len(log)):
                    if int(edit_id) == log[i]["id"]:
                        edit_id = i
                        break
                    
                log[int(edit_id)]["product"] = dummy_p
                                
                #ask for the key to edit
                clear()
                print(Back.LIGHTBLACK_EX + '{:=^100}'.format(f'Edit a {string}'), "\n")
                print('\n {:<50}'.format(Fore.CYAN + f'You Select to Change: ' + Fore.WHITE + f'"{log[edit_id]}".'))
                
                log[edit_id] = create_dict_with_list(log[edit_id], ["Preparing", "On its Way", "Delivered", "Cancelled"], "status", multiple = False)
                edit_item_table(log[edit_id]["id"], log[edit_id], "status", "orders")
                    
                if like_to_continue(f'Would you like to continue in "Edit a {string}"? - "Y" for yes and "N" for no.'):
                    continue
                else:
                    check_1 = False
                    return log
            else:
                #ID or name not in the databse and ask if user want to continue
                if not like_to_continue(f'     You Select an ID that is NOT Available in the Data-Base. Would you like to continue in "Edit a {string}"? - "Y" for yes and "N" for no.'):
                    check_1 = False
                    return log
                
    def show_orders(self):
        clear()
        
        list = fetch_orders("orders")
                
        if no_orders(list, "Orders"):
            user_select = create_menu(list = ["Show Order list", "Generic Order List", "Order list by 'status'", f"Order list by 'courier'"])
            
            if user_select == "1":
                
                print_list(list)
                dummy = input('\n {:<50}'.format(Fore.CYAN + 'Select Order id for more details or Press any other key and to continue..' + Style.RESET_ALL) )
                
                for i in range(0, len(list)): 
                    if dummy and int(dummy) == list[i]["id"]:
                        
                        print(list[i])
                        [dummy_p, lid] = fetch_orders_details(dummy)
                    
                        print("List of products:", dummy_p)
                        input('\n {:<50}'.format(Fore.CYAN + 'Press any other key and to continue..' + Style.RESET_ALL))
                        break
                    
            elif user_select == "2":
                while True:
                    dummy_status = ["Preparing", "On its Way", "Delivered", "Cancelled"]
                    print_list(dummy_status)
                    
                    dummy = input('\n {:<50}'.format(Fore.CYAN + 'Select Status ID for more details..' + Style.RESET_ALL))
                    if 4>=int(dummy)>0:
                        dummy = int(dummy) - 1
                        dummy_s = fetch_orders_status(dummy_status[dummy])
                        
                        print(f"Orders - {dummy_status[dummy]} \n") 
                        if dummy_s: print_list(dummy_s) 
                        else: print("Nothing in the database")
                        input('\n {:<50}'.format(Fore.CYAN + 'Press any other key and to continue..' + Style.RESET_ALL))
                        break
                    else:
                        input('\n {:<50}'.format(Back.RED + Fore.WHITE + 'Select Only from the list..  Press any key and try again..' + Style.RESET_ALL))
                        
                                                
            elif user_select == "3":
                while True:
                    
                    print_list(self.courier)
                    
                    dummy = input('\n {:<50}'.format(Fore.CYAN + 'Select courier id for more details..' + Style.RESET_ALL))
                    if dummy.isnumeric() and int(dummy) in [obj.contents["id"] for obj in self.courier]:

                        dummy_s = fetch_orders_courier(dummy)
                        if no_orders(dummy_s, "Orders"):
                            print_list(dummy_s) 
                        else: return
                        
                        input('\n {:<50}'.format(Fore.CYAN + 'Press any other key and to continue..' + Style.RESET_ALL))
                        break
                    else:
                        input('\n {:<50}'.format(Back.RED + Fore.WHITE + 'Select Only from the list..  Press any key and try again..' + Style.RESET_ALL))
                        
            else: 
                input('\n {:<50}'.format(Back.RED + Fore.WHITE + 'Select Only from the list..  Press any key and try again..' + Style.RESET_ALL))
            
                
    #Delete an item in a list       
    def del_item(self, string = "Product"):
        
        if string.lower() == "product": 
            self.product.clear()
            for item in read_sql("products"): self.product.append(Product(item))
            log = self.product
        
        else: 
            self.courier.clear()
            for item in read_sql("couriers"): self.courier.append(Courier(item))
            log = self.courier
            
        while True:
            clear()
            print(Back.LIGHTBLACK_EX + '{:=^100}'.format(f'Delete an {string}'), "\n")
            

            #check if list is empty
            if not no_orders(log, string):
                return log

            print_list(log)

            edit_id = input('\n {:<50}'.format(Fore.CYAN + f'Enter the {string} ID to Delete . [E to Exit]. > ' + Style.RESET_ALL))

            #check if user wants to exit
            if exit(edit_id, f"     You select to Exit or not entered any commands from 'Deleting a {string}'.. Press any key to Exit. > "):
                return log

            if edit_id.isnumeric() and int(edit_id) in [obj.contents["id"] for obj in log]:
                
                item_used_in_order = 0
                dummy = read_sql("orders")
                
                for item in dummy:
                    if isinstance(item[string.lower()], int):
                        if item[string.lower()] == int(edit_id):
                            item_used_in_order = 1
                            if like_to_continue(f'\n{string} linked to an order. Not deleted.. Would you like to continue in "Delete a {string}"? - "Y" for yes and "N" for no.'):
                                break
                            else:
                                return log
                    else:
                        for i in item[string.lower()]:
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
                
                for i in range(0,len(log)):
                    if int(edit_id) == log[i].contents["id"]:
                        edit_id = i
                        break
                

                # ask if user wants to delete, and if the user wants to continue in the delete menu
                if like_to_continue(f'\nDo you want to proceed?  Y for Yes / N for No'):
                    input('\n {:<50}'.format(Fore.CYAN + f'Deleting.., Press any key to Continue..' + Style.RESET_ALL))
                    
                    if string.lower() == "product":
                        delete_item_table(log[edit_id].contents["id"], "products")
                    if string.lower() == "courier":
                        delete_item_table(log[edit_id].contents["id"], "couriers")
                        
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
                
    #Delete an item in a list       
    def del_customer(self, string = "Customer"):
        while True:
            clear()
            print(Back.LIGHTBLACK_EX + '{:=^100}'.format(f'Delete an {string}'), "\n")
            

            log = read_sql("customers")

            #check if list is empty
            if not no_orders(log, string):
                return log

            print_list(log)

            edit_id = input('\n {:<50}'.format(Fore.CYAN + f'Enter the {string} ID to Delete . [E to Exit]. > ' + Style.RESET_ALL))

            #check if user wants to exit
            if exit(edit_id, f"     You select to Exit or not entered any commands from 'Deleting a {string}'.. Press any key to Exit. > "):
                return log

            if edit_id.isnumeric() and int(edit_id) in [obj["id"] for obj in log]:
                
                item_used_in_order = 0
                dummy = read_sql("orders")
                
                for item in dummy:
                    if item["customer"] == int(edit_id):
                        item_used_in_order = 1
                        if like_to_continue(f'\n{string} linked to an order. Not deleted.. Would you like to continue in "Delete a {string}"? - "Y" for yes and "N" for no.'):
                            break
                        else:
                            return log

                        
                if item_used_in_order == 1:
                    continue
                
                for i in range(0,len(log)):
                    if int(edit_id) == log[i]["id"]:
                        edit_id = i
                        break
                

                # ask if user wants to delete, and if the user wants to continue in the delete menu
                if like_to_continue(f'\nDo you want to proceed?  Y for Yes / N for No'):
                    input('\n {:<50}'.format(Fore.CYAN + f'Deleting.., Press any key to Continue..' + Style.RESET_ALL))
                    
                    delete_item_table(log[edit_id]["id"], "customers")
                                            
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
                
    #Delete an item in a list       
    def del_order(self, string = "Order"):
        while True:
            clear()
            print(Back.LIGHTBLACK_EX + '{:=^100}'.format(f'Delete an {string}'), "\n")
            

            log = fetch_orders("orders")

            #check if list is empty
            if not no_orders(log, string):
                return log

            print_list(log)

            edit_id = input('\n {:<50}'.format(Fore.CYAN + f'Enter the {string} ID to Delete . [E to Exit]. > ' + Style.RESET_ALL))

            #check if user wants to exit
            if exit(edit_id, f"     You select to Exit or not entered any commands from 'Deleting a {string}'.. Press any key to Exit. > "):
                return log

            if edit_id.isnumeric() and (int(edit_id) in [obj["id"] for obj in log]):
                
                for i in range(0,len(log)):
                    if int(edit_id) == log[i]["id"]:
                        edit_id = i
                        break
                

                # ask if user wants to delete, and if the user wants to continue in the delete menu
                if like_to_continue(f'\nDo you want to proceed?  Y for Yes / N for No'):
                    input('\n {:<50}'.format(Fore.CYAN + f'Deleting.., Press any key to Continue..' + Style.RESET_ALL))
                    
                    delete_order(log[edit_id]["id"])

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

if __name__ == '__main__':
    tienda_1 = Shop("1")
    tienda_1.launch() 


    