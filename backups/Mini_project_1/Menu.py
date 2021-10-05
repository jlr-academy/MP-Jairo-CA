import os
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

def edit_order():
    print("==========[ Edit an Order ]==========")
    input('      Press any key to Continue..')
        
def del_order():
    print("==========[ Delete an Order ]==========")
    input('      Press any key to Continue..')    
        
def q_to_quit(check):
        
    # If the user enter [q or Q] the function will return quit function. 
    if check.upper == 'Q' :
        return quit()

def add_order(log):
    print("==========[ Add New Order ]==========")
    print('   NOTE: Enter Q any time to EXIT/Quit. ')  
    
    order_Num = input('   Enter the order ID or Number. > ')
    q_to_quit(order_Num)
    
    order_p = input('   Enter the Product. > ')
    q_to_quit(order_p)
    
    order_c = input('   Enter the courier. > ')
    q_to_quit(order_c)
    
    order_q  = input('   Enter the quantity of the order. > ')
    q_to_quit(order_q)
    
    order_p = " ".join([word.capitalize() for word in order_p.split(" ")]) 
    order_c = " ".join([word.capitalize() for word in order_c.split(" ")]) 
    
    log[order_Num] = {"order_ID":order_Num, "Product":order_p , "Courier":order_c, "order_quantity":order_q}
    import json
    with open(os.path.join("C:/Users/jcanoalo/Desktop/IW/Mini_project_1", "Log.txt"), 'w') as f:
        json.dump(log, f)
    input('      Press any key to Continue..')
    return log

def show_order(log):
    print("==========[ Show Orders ]==========")  
    for key in log:
        
        print("   ID: ",log[key]["order_ID"])  
        print("Product: ",log[key]["Product"])
        print("Product: ",log[key]["Courier"])
        print("Quantity: ",log[key]["order_quantity"])
        
        print("-------------------------------------------------------------------\n")
    
    
    
    input('\n      Press any key to Continue..  ')  