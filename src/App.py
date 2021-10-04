from Tools.Item_Management import add_item, edit_item, del_item
from File_handlers.txt import read, write
from Tools.uitilities import create_menu, print_list, no_orders
import os

#PK extra comment here

#Read txt data if any
list_product = read('C:/Users/jcanoalo/Desktop/IW/Mini_project_1/Data', "Product_list.txt")
list__courier = read('C:/Users/jcanoalo/Desktop/IW/Mini_project_1/Data', "Courier_list.txt")

#Item Submenu
def Sub_menu(string = "item", list = []):
    while True :
        user_select = create_menu(list = [f"{string} Menu", f"Add New {string}", f"Edit an {string}",  f"Delete a {string}", f"Show {string} list", "Return to Main Menu"])

        if user_select == '1' :
            add_item(list, string)

        elif user_select == '2' :
            edit_item(list, string)

        elif user_select == '3' :
            del_item(list, string)  

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

#Main Menu         
while True :
    user_select = create_menu(list = ["Main Menu", "Product Menu", "Courier Menu", "Exit"])
        
    if user_select == '1' :
        Sub_menu("Product", list_product)
        
    elif user_select == '2' :
        Sub_menu("Courier", list__courier)
        
    elif user_select == '3' :
        print('\n\n   Thank you for using this Appliation. ')
        break
            
    else :
        input('   Select Only from the list..  Press any key and try again..') 

#Write txt data  
write(list_product, "C:/Users/jcanoalo/Desktop/IW/Mini_project_1/Data", "Product_list.txt")
write(list__courier, "C:/Users/jcanoalo/Desktop/IW/Mini_project_1/Data", "Courier_list.txt")
    