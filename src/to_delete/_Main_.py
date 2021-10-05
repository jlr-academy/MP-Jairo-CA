from Menu import main_menu, add_order, edit_order, del_order, show_order
import json
import os

log = {}
while True :
    user_select = main_menu()
        
    if user_select == '1' :
        add_order(log)
        
    elif user_select == '2' :
        edit_order(log)
        
    elif user_select == '3' :
        del_order(log)  

    elif user_select == '4' :
        show_order(log)
        
    elif user_select == '9' :
        print('\n\n   Thank you for using this Appliation. ')
        break
            
    else :
        input('\n   Select Only from the list..  Press any key and try again..') 
        
with open(os.path.join("C:/Users/jcanoalo/Desktop/IW/Mini_project_1", "Log.txt"), 'w') as f:
    json.dump(log, f)
    