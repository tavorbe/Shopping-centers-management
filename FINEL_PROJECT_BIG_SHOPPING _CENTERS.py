import os
import matplotlib.pyplot as plt
import pickle
import random
import webbrowser

#Constant variables
PRICEOFSTORE = 4000000
SIZEOFSTORE = 50
MASTER = "12345678"

#Main function
def main():
    #Note to the examiner
    print("MASTER Password  - 12345678 \n") 
    print("Hello and welcome to BIG - Shopping Centers operating system.\n\n")
    
    #starting menu
    choice = input("1. For employees area, please enter 1.\n2. For managers area, please press 2.\n3. For exit, please press 3.\n")
    while choice != '1' and choice != '2' and choice != '3':
        choice = input("please enter only 1/2/3\n")
    
    #go to employees area
    if choice == '1':    
        employees_enter()
    #go to managers area    
    elif choice == '2':
        password = input("Please enter MASTER Password to get access\n")
        while password != MASTER:
            password = input("access deny. try again\n")
        if password == MASTER:
            print("access approved\n")
            managers_menu()
    elif choice == '3':
        exitapp()

#add new employee to system
def new_employee():
    #creating new employee requires master code
    access = int(input("Please enter master password for creating a new employee profile:\n"))
    
    #access approval
    if access == int(MASTER):
        print("access approved")
        
    else:
        print("access deny\n")
        main()
    
    #get details of new employee
    print("please enter the next information:\n")
    Full_name = input("Full name: ")
    #only letter check
    while Full_name.isalpha() == False:
        print("please enter only alphabetic letter")
        Full_name = input("Full name: ")
    
    ID_number = input("ID number: ")
    #only numbers + 9 digits check 
    while ID_number.isdigit() == False or len(ID_number) != 9:
        print("please enter vaild ID number")
        ID_number = input("ID number: ")
       
    Phone_number = input("Phone_number: ")
    #only digits + 10 digits check 
    while Phone_number.isdigit() == False or len(Phone_number) != 10:
        print("please enter 10 digits vaild Phone number")
        Phone_number = input("Phone_number: ")
    
    Work_area = input("Work area (north/central/south): ")
    #vaild working area check
    while Work_area != 'north' and Work_area != 'central' and Work_area != 'south':
        print("please enter one of the following options")
        Work_area = input("Work area (north/central/south): ")
    #continue to password creation func    
    password = create_password(ID_number)
    
    #write the new employee details in text file
    employees_file = open('employees_file.txt','a')
    employees_file.write('Full name\n' + str(Full_name) + '\n' + 'ID number\n' + str(ID_number) + '\n' + 'Phone number\n' + str(Phone_number) + '\n' + 'Work area\n' + str(Work_area) + '\n' + 'Password\n' + str(password) + '\n')
    employees_file.close()
    
    #Approval and show new password
    print("the new employee saved to data. his password is ", password)
    #continue to employees menu
    employees_menu(Full_name)

#create password function gets ID number   
def create_password(ID_number):
    print("we will create your first password from first 4 digits from your ID number, and 4 more random numbers.\n")
    #slice first 4 digits of ID number
    password = ID_number[0:4]
    
    #add 4 random digits to password
    index = 0
    while index < 4:
        random_num = random.randint(1,9)
        password = password + str(random_num)  
        index +=1        

    return password

#create files with "BIG" compeny data for all other functions
def documents():
    
    #file contains all centers in israel
    centers_dictionary = {'north':['kiryat Shmona', 'tveria', 'carmiel', 'regba,haifa - check post', 'haifa - krayut', 'yokneam', 'pardes hana', 'afula'], 'central':['yahud', 'rishon letzion', 'beit shemesh', 'kastina'], 'south':['kiryat gat', 'beer sheva', 'eilat']} 
    #written to binary file
    centers_file = open('centers_file.dat','wb')
    pickle.dump(centers_dictionary, centers_file)
    centers_file.close() 
    
    #file contains prices per meter by center area
    prices_dictionary = {'north':'140','central':'180','south':'120'}
    #written to binary file
    prices_file = open('prices_file.dat','wb')
    pickle.dump(prices_dictionary, prices_file)
    prices_file.close()    
    
    #file contains all centers stores occupancy 
    avalibility_dictionary = {'kiryat Shmona' : [20, 18], 'tveria':[20, 18], 'carmiel':[25, 24], 'regba,haifa - check post':[20,20], 'haifa - krayut':[20,20], 'yokneam':[30,27],'pardes hana':[20,14], 'afula':[20,17], 'yahud': [20,19], 'rishon letzion': [30,30], 'beit shemesh':[20,16], 'kastina':[25,22], 'kiryat gat':[20,16], 'beer sheva':[30,26], 'eilat' :[30,27]} 
    #written to binary file
    avalibility_file = open('avalibility_file.dat', 'wb')
    pickle.dump(avalibility_dictionary, avalibility_file)
    avalibility_file.close()
    
    #open employees_file
    try:
        employees_file = open('employees_file.txt', 'r')
    
    #file doesnt exist error
    except IOError:
       
        employees_file = open('employees_file.txt', 'w')
        #write the MASTER Password to the file
        master = ['master', MASTER]
        for item in master:
            employees_file.write(str(item) + '\n')
    finally:
        employees_file.close()
        
    main()
    
#employees enter step    
def employees_enter():
    print("Welcome to employees area.\nto continue please enter your password(or the master password written above): ")
    #get vaild password from user by digits and length
    try:    
        password = int(input())
        
        while len(str(password)) != 8:
            print("Password length is not as required")
            password = int(input())
        
    #password contains only digits
    except ValueError:
        print("please enter only numeric numbers")
        employees_enter()

    #get employees data from file
    employees_file = open('employees_file.txt', 'r')
    employees_list = employees_file.readlines()
    employees_file.close()
    index = 0
    
    #transfer data to a list
    while index < len(employees_list):
        employees_list[index] = employees_list[index].rstrip('\n')
        index += 1
    
    #check  if password exist in the system
    if str(password) in employees_list:
        print("Access approved, You are transferred to the employed area\n\n")
        
        #gets employee name for saying hello next func
        if 'Full name' in employees_list:
            name = employees_list.index('Full name')
            name = name + 1
            #transfer to employees menu
            employees_menu(employees_list[name])
        
        #access with master code case
        else:
            name = employees_list.index(str(password))
            name = name - 1
            #transfer to employees menu
            employees_menu(str(employees_list[name]))
    
    #case password is incorrect    
    else:
        print("The password is incorrect or does not exist in the system. Please contact your personal manager\n\n")
        main()    
    

#only employees access menu
def employees_menu(name):
    
    print ("\nWelcome back dear " + name + '\n\n')
    print("1. To calculate and prepare a price offer for a store rental - press 1\n2. To search for available stores for rent - press 2\n3. To display or change employee details press 3\n4. To update transaction (store rent/cancellation) - press 4\n5. To add a new employee - press 5\n6. back - press 6\n\n")
    #all employees options 
    choice = int(input())
    while choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and choice != 6:
        choice = input("invaild input. please try again\n")    
    
    if choice == 1:
        price_offer()                                                                
    elif choice == 2:
        finding_store()
    elif choice == 3:
        employees_info()  
    elif choice == 4:
        update_transaction()    
    elif choice == 5:
        new_employee()
    elif choice == 6:
        main()

#function update stores occupancy in case of new rent
def update_transaction():
    
    #if its about cancellation, transfer to leaving_store func
    answer = input("1. New rent deal\n2. cancellation\n")
    while answer != '1' and answer != '2':
        anwser = input("please enter only 1 or 2")
        
    if answer == '2':
        leaving_store()
    
    #open relevant files
    centers_file = open('centers_file.dat','rb')
    centers = pickle.load(centers_file)
    centers_file.close()
    avalibility_file = open('avalibility_file.dat', 'rb')
    stores = pickle.load(avalibility_file)
    avalibility_file.close()
    
    #copy the dictionary to a list for better print
    lis = list(centers['north']) + list(centers['central']) +list(centers['south'])
    for item in lis:
        print(item)
    
    center_name = input("please enter the name of the center the store is rent from: ")
    #verify vaild center name 
    while center_name not in stores:
        center_name = input("please enter vaild center name\n")
    
    #check for available stores for rent in the center
    index = stores[center_name]
    gap = index[0]-index[1]
    #case no available stores
    if gap < 1:
        print("no available store for rent")
    
    #update occupancy and announces the user
    else:
        print("\nthis center has ", index[1], " of ", index[0], " stores at rent.\n") 
        index[1] = index[1] + 1
        print("Occupancy updated\n")
        print("after the update, the store has: " , index[0] - index[1], " available stores\n")
        boolian = 'true'
    
    #update binary file
    avalibility_file = open('avalibility_file.dat', 'wb')
    pickle.dump(stores, avalibility_file)
    avalibility_file.close()
    input("please press enter to continue")
    
    #back to employees menu
    employees_menu(" ")

#function update stores occupancy in case of cancellation
def leaving_store():
    
    #open relevant files
    centers_file = open('centers_file.dat','rb')
    centers = pickle.load(centers_file)
    centers_file.close()
    avalibility_file = open('avalibility_file.dat', 'rb')
    stores = pickle.load(avalibility_file)
    avalibility_file.close()
    
    #copy the dictionary to a list for better print
    lis = list(centers['north']) + list(centers['central']) +list(centers['south'])
    for item in lis:
        print(item)
    
    #verify vaild center name    
    center_name = input("please enter the name of the center the store is located: ")
    while center_name not in lis:
        center_name = input("please enter vaild center name")
    
    #update occupancy and announces the user    
    index = stores[center_name]
    print("\nthis center has ", index[1], " of ", index[0], " stores at rent.\n")
    index[1] = index[1] - 1
    print("Occupancy updated\n")
    print("after the update, the store has: " , index[0] - index[1], " available stores\n")
    
    #update binary file
    avalibility_file = open('avalibility_file.dat', 'wb')
    pickle.dump(stores, avalibility_file)
    avalibility_file.close()
    input("please press enter to continue")
    
    #back to employees menu
    employees_menu(" ")

#The function displays employee details
def employees_info():
    #open relevant file
    employees_file = open('employees_file.txt', 'r')
    employees_details = employees_file.readlines()
    employees_file.close()
    
    #copy to a list
    index = 0
    
    while index < len(employees_details):
        
        employees_details[index] = (employees_details[index].rstrip('\n'))
        index += 1
    
    #gets vaild ID number from user
    ID_number = input("please enter employee ID number:\n")
    while ID_number.isdigit() == False or len(ID_number) != 9:
        print("please enter vaild ID number")
        ID_number = input("ID number: ")
    
    #display employees details    
    if ID_number in employees_details:
        #get the id number index in the list
        id_index = int(employees_details.index(ID_number))
        #get the end of person information index
        end_index = id_index
        #Adjust on right details    
        try:
            
            while employees_details[end_index] != "Full name" and end_index < len(employees_details):
               
               end_index = end_index + 1

        except IndexError:
            
            end_index = end_index + 1        
        
        #slice the list to the relevant information
        employee_information = employees_details[id_index - 3 : end_index]
    #case id number wasnt found
    else:
        print("the id number is not exist at the system")
        employees_menu(' ')        

    #display employee information
    print('\n')        
    for item in employee_information:
        print(item)
    
    #display options
    print("\n1. to change employee details - enter 1\n2. to delete employee details - enter 2\n3. to add a new employee - enter 3\n4. to go back - enter 4\n")
    choice = input()
    #verify vaild input
    while choice != '1' and choice != '2' and choice != '3' and choice != '4':
        print("wrong input please try again")
        choice = input()
        
    if choice == '1':
        change_details()
        
    elif choice == '2':
        del_employee(ID_number)
    
    elif choice == '3':
        new_employee()
    
    elif choice == '4':
        employees_menu(' ')

#delete an employee
def del_employee(ID_number):
    
    #open relevant file
    employees_file = open('employees_file.txt', 'r')
    employees_details = employees_file.readlines()
    employees_file.close()
    index = 0
    #copy to list
    while index < len(employees_details):
        
        employees_details[index] = (employees_details[index].rstrip('\n'))
        index += 1
    
    #adjust on right details
    id_index = int(employees_details.index(ID_number))
    end_index = int(id_index)
    
    while employees_details[end_index]!= 'Full name' and employees_details[end_index] != 'Password':
        end_index +=1
    
    end_index +=2
    #delete action
    del employees_details[id_index-3:end_index]
    
    #write updated data to text file
    employees_file = open('employees_file.txt', 'w')
    
    for item in employees_details:
            employees_file.write(str(item) + '\n')
    
    employees_file.close()
    
    print("The details deleted. you are transfer to employee menu")
    #transfer to employees_menu
    employees_menu(' ')    

#employee can change password or other details
def change_details():

    print("please enter the next information:\n")
    #open relevant file
    employees_file = open('employees_file.txt', 'r')
    employees_details = employees_file.readlines()
    employees_file.close()
    
    #copy to a list
    index = 0
    
    while index < len(employees_details):
        
        employees_details[index] = (employees_details[index].rstrip('\n'))
        index += 1
        
    #getting new details and delete previos details 
    Full_name = input("Full name: ")
    while Full_name.isalpha() == False:
        print("please enter only alphabetic letter")
        Full_name = input("Full name: ")
    
    name_index = employees_details.index('Full name')
    del employees_details[name_index + 1]
    employees_details.insert(name_index + 1, Full_name)
    
    ID_number = input("ID number: ")
    while ID_number.isdigit() == False or len(ID_number) != 9:
        print("please enter vaild ID number")
        ID_number = input("ID number: ")
    
    id_index = employees_details.index('ID number')
    del employees_details[id_index + 1]
    employees_details.insert(id_index + 1, ID_number)
    
    Phone_number = input("Phone_number: ")
    while Phone_number.isdigit() == False or len(Phone_number) != 10:
        print("please enter 10 digits vaild Phone number")
        Phone_number = input("Phone_number: ")
    
    phone_index = employees_details.index('Phone number')
    del employees_details[phone_index + 1]
    employees_details.insert(phone_index + 1, Phone_number)
    
    Work_area = input("Work area (north/central/south): ")
    while Work_area != 'north' and Work_area != 'central' and Work_area != 'south':
        print("please enter one of the following options")
        Work_area = input("Work area (north/central/south): ")
    
    area_index = employees_details.index('Work area')
    del employees_details[area_index + 1]
    employees_details.insert(area_index + 1, Work_area)
    
    
    Password = input("new password: ")
    while Password.isdigit() == False or len(Password) != 8:
        print("please enter 8 digits only password")
        Password = input("new password: ")
    
    password_index = employees_details.index('Password')
    del employees_details[password_index + 1]
    employees_details.insert(password_index + 1, Password)

    #write new info to text file
    employees_file = open('employees_file.txt', 'w')
    
    for item in employees_details:
            employees_file.write(str(item) + '\n')
    
    employees_file.close()
    
    print("The details have been changed. you are transfer to employee menu")
    #transfer to employees menu
    employees_menu(' ')

#func give info on occupancy of centers    
def finding_store():
    
    #open relevant files
    centers_file = open('centers_file.dat','rb')
    
    avalibility_file = open('avalibility_file.dat', 'rb')
    
    stores = pickle.load(avalibility_file)
    
    centers = pickle.load(centers_file)
    
    centers_file.close()
    
    avalibility_file.close()
    
    #get vaild area from user
    area = input("please enter which area you would like to check about: north/central/south\n")
    while area != 'north' and area != 'south' and area != 'central':
        area = input("please enter vaild area name\n")
    
    print('\n')
    #print centers name at choosen area
    lis = centers[area]
    for item in lis:
        print(item)
    #get vaild center choice from user
    center_name = input("\nplease choose one from the cities above\n")
    while center_name not in stores:
        center_name = input("please enter vaild center name\n")    
    
    #get occupancy info    
    value2 = stores[center_name]
            
    available_stores = value2[0]-value2[1]
            
    print("the center you chose has: ", available_stores , "available stores out of ",value2[0], 'stores in the center\n' )
    
    #display continue options     
    choose = input("what whould you like to do next:\n1. to choose another city enter 1\n2. to create a price offer enter 2\n3.to return to employees menu enter 3\n")
    #verify vaild input
    while choose != '1' and choose != '2' and choose != '3':
        choose = input("please enter only 1/2/3\n")
    
    if choose == '1':
        finding_store()
    elif choose == '2':
        price_offer()
    elif choose == '3':
        employees_menu(" ")
          
 
#create price offer for client and save it as a file at desktop
def price_offer():
    
    #open relevant file
    prices = open('prices_file.dat', 'rb')
    pricesb = pickle.load(prices)
    prices.close()
    
    area = input("\nPlease enter the area you whould like to check about: north/central/south\n")
    while area != 'north' and area != 'south' and area != 'central':
        area = input("please enter vaild area name\n")
        
    boolian = 'false'
    while boolian == 'false':
        try:
            print("please enter size of surface(by meters)\n")
            size = int(input())
            boolian = 'true'
            
            #get price of area from binary file
            if area == 'north':
                key = 'north'            
                value = int(pricesb.get('north', 'price not found'))
                
            elif area == 'central':
                key = 'central'
                value = int(pricesb.get('central', 'price not found'))
                
            elif area == 'south':
                key = 'south'
                value = int(pricesb.get('south', 'price not found'))
             
            print("The price of the surface requested in the area you selected is: ",'{:10,.2f}'.format(size * value), "₪\n\n")
        #invaild input
        except ValueError:
            print("please enter only numbers\n")
            boolian = 'false'
    
    #create price_offer with client detail, save to desktop and ready to send.
    print("whould you like to create a price offer? enter 'yes'\nelse enter anything else")
    offer = str(input())
    if offer == 'yes': 
        price_offer = open('price_offer.txt', 'w')
        name = input("please enter person/company name\n")
        signature = "This is an official price offer for renting a store space at BIG shoping centers.\nThe Company may change its opinion and price at any given time, as long as the transaction is not signed\n\n"
        BIG_phone = 123456789
        BIG_FAX = 123456789
        price = '{:10,.2f}'.format(size*value)
        price_offer.write('To ' + str(name) + '\n' + 'The price for renting a store at size of ' + str(size) + ' meters ' + 'at the ' + str(key) + ' is ' + str(price) + '₪ per month' + '\n\n\n\n' + str(signature) +'BIG phone - ' + str(BIG_phone) + '\n' + 'BIG fax - ' + str(BIG_FAX) + '\n')
        price_offer.close()
        name = name + '_price_offer.txt'
        os.rename('price_offer.txt', name)
        print("the price offer has created and saved on your desktop\n")
    
    
    #continue options
    print("\n1. back to employees_menu, press 1\n2. to make another price offer, press 2\n3. exit to main menu, press 3")
    back = input()
    
    while back != '1' and back != '2' and back != '3':
        print("please choose one of the option")
        back = int(input())
    
    if back == '1':
        employees_menu(' ')
    elif back == '2':
        price_offer()
    elif back == '3':
        main()    
#Greeting
def exitapp():
    print("Good bye, come back soon!")
    input()

#managers area    
def managers_menu():
    print("\nWelcome to managers area")
    print("1. To watch the amount of profit from stores rent - press 1\n2. To compare between two centers/areas - press 2\n3. KPI'S Dashboard\n4. back\n")
    choose = input()
    
    while choose != '1' and choose != '2' and choose != '3' and choose != '4':
        choose = input("invaild input, please try again\n")
    
    if choose == '1':
        profit_func()
    elif choose == '2':
        compare_func()
    elif choose == '3':
        KPI_dashboard()
    elif choose == '4':
        main()
    
   
#KPI dashboard for managers
def KPI_dashboard():

    #choose vaild option
    print("1. Profit\n2. Occupancy\n3. ROI - Return on invest\n4. KPI Website\n5. back")
    choose = input()
    while choose != '1' and choose != '2' and choose != '3' and choose != '4' and choose != '5':
        choose = input("please enter vaild input\n")
        
    #open relevant files
    prices = open('prices_file.dat', 'rb')
    pricesb = pickle.load(prices)
    prices.close()

    avalibility_file = open('avalibility_file.dat', 'rb')
    stores = pickle.load(avalibility_file)
    avalibility_file.close()

    centers_file = open('centers_file.dat','rb')
    centers = pickle.load(centers_file)
    centers_file.close()
    
    #calculate profit, loss, rents - over all centers and display information pie 
    if choose == '1':
        max_profit = 0
        current_profit = 0
        num_of_stores = 0
        num_of_rent_stores = 0
        #sum profit&loss&rents
        for key in stores:
            if key in centers['north']:
                price = pricesb['north']
            elif key in centers['central']:
                price = pricesb['central']
            elif key in centers['south']:
                price = pricesb['south']
            current_profit += int(stores[key][1]) * SIZEOFSTORE * int(price)*12
            max_profit += int(stores[key][0]) * SIZEOFSTORE * int(price)*12
            num_of_stores += stores[key][0]            
            num_of_rent_stores += stores[key][1]
        
        #display information
        print("current situation: \nmax profit: ", '{:10,.2f}'.format(max_profit), "per year\ncurrent profit: ", '{:10,.2f}'.format(current_profit), "per year\nPercentage profit out of total possible profit: ", "{:.2%}".format(current_profit/max_profit), "\nPercentage of Occupancy: ","{:.2%}".format(num_of_rent_stores/num_of_stores))
        pie_chart_profit(max_profit, current_profit, num_of_rent_stores, num_of_stores)
        KPI_dashboard()
            
    #calculate occupancy over all centers and display information pie
    elif choose == '2':
        num_of_stores = 0
        num_of_rent_stores = 0
        #sum rents number
        for key in stores:
            num_of_stores += stores[key][0]            
            num_of_rent_stores += stores[key][1]
        
        #display information    
        print("current situation:\ntotal number of stores: ", num_of_stores, "\ncurrent stores rented: ", num_of_rent_stores, "\nPercentage of Occupancy: ","{:.2%}".format(num_of_rent_stores/num_of_stores))
        pie_chart_occupancy(num_of_stores, num_of_rent_stores)
        KPI_dashboard()
        
    #calculate ROI per center (profit from rents(per year) compared to building price) 
    elif choose == '3':
        
        #choose center
        for key in stores:
            print(key)
        center = input("\nplease choose a center from above to calculate his ROI\n")
        
        while center not in stores:
            center = input("please enter vaild center name")
        #get area price
        if center in centers['north']:
            price = pricesb['north']
        elif center in centers['central']:
            price = pricesb['central']
        elif center in centers['south']:
            price = pricesb['south']
        
        #calculate and display information
        print("\nThe cost of a shopping center is determined by the price of 4 million NIS, double the number of stores built in the shopping center\n")
        print("The cost of the shopping center you choosen is: ",'{:10,.2f}'.format(4000000*stores[center][0]) + ' NIS')
        print("For now, this shopping center has ", stores[center][1], "of ", stores[center][0], " stores at rent")   
        print("Price for a store in this center is 50 meters * ", price, " = ", '{:10,.2f}'.format(SIZEOFSTORE*int(price)), " NIS per month")
        print("per year, the profit will be 12 * ", '{:10,.2f}'.format(SIZEOFSTORE*int(price)), " * ", stores[center][1], " = " ,'{:10,.2f}'.format(12*SIZEOFSTORE*int(price)*int(stores[center][1])), "NIS per year\n")
        print("so, your ROI from this center is: " ,"{:.2%}".format((12*SIZEOFSTORE*int(price)*int(stores[center][1]))/(PRICEOFSTORE*int(stores[center][0]))), "per year\n")
        KPI_dashboard()
    
    #return    
    elif choose == '4':
        #KPI_Website
        webbrowser.open("https://kpidashboards.com/kpi/industry/real-estate-and-rental-and-leasing/")
        KPI_dashboard()
        
    elif choose == '5':    
        managers_menu()
    
#function produces pie chart for occupancy
def pie_chart_occupancy(num_of_stores, num_of_rent_stores):
    
    pie_values = (num_of_rent_stores, num_of_stores - num_of_rent_stores)
    plt.title("Occupancy status")
    slice_lables = ['current rents:' + str(num_of_rent_stores), 'current empty: ' + str(num_of_stores - num_of_rent_stores)]
    colors = ('yellowgreen', 'lightcoral')
    explode = (0, 0.2)
    legend_labels = ['max occupancy: ' + str(num_of_stores), 'current occupancy' + str(num_of_rent_stores)]
    plt.pie(pie_values,labels = slice_lables, explode = explode, colors = colors, shadow = True, startangle = 340, autopct=('%1.1f%%'))
    plt.legend(legend_labels, loc = 3)
    #Display the pie chart
    
    plt.show()
    return
#function produces pie chart for profit    
def pie_chart_profit(max_profit, current_profit, num_of_rent_stores, num_of_stores):
    
    pie_values = (current_profit, max_profit - current_profit)
    plt.title("profit & missed profit from rent")
    slice_lables = ['current profit:' + str('{:10,.2f}'.format(current_profit)), 'missed_profit: ' + str('{:10,.2f}'.format(max_profit - current_profit))]
    colors = ('yellowgreen', 'lightcoral')
    explode = (0, 0.2)
    legend_labels = ['max profit: ' + str('{:10,.2f}'.format(max_profit)) + '₪ per year', 'current_profit: ' + str('{:10,.2f}'.format(current_profit)) + '₪ per year']
    plt.pie(pie_values,labels = slice_lables, explode = explode, colors = colors, shadow = True, startangle = 340, autopct=('%1.1f%%'))
    plt.legend(legend_labels, loc = 3)
    #Display the pie chart
    
    plt.show()
    return
#func compare two centers/areas values    
def compare_func():
    
    #open relevant files
    prices = open('prices_file.dat', 'rb')
    pricesb = pickle.load(prices)
    prices.close()
    
    avalibility_file = open('avalibility_file.dat', 'rb')
    stores = pickle.load(avalibility_file)
    avalibility_file.close()
    
    centers_file = open('centers_file.dat','rb')
    centers = pickle.load(centers_file)
    centers_file.close() 
    
    #get vaild choice from user
    choice = input("please choose 1 from the following options:\n1. compare centers\n2. compare areas\n")
    while choice != '1' and choice != '2':
        choice = int(input("please enter only 1 or 2\n"))
    
    #comparing centers
    if choice == '1':
        
        city_list = list(centers['north']) + list(centers['central']) + list(centers['south'])
        #get vaild centers names from user 
        for item in city_list:
            print(item)        
        
        center1 = input("\nplease enter the names of the centers you want to compare:\n")
        
        while center1 not in stores:
            center1 = input("please enter vaild center name\n")
        
        center2 = input()
        while center2 not in stores:
            center2 = input("please enter vaild center name\n")
        
        #get centers rent price
        if center1 in centers['north']:
            price1 = pricesb['north']
        elif center1 in centers['central']:
            price1 = pricesb['central']
        elif center1 in centers['south']:
            price1 = pricesb['south']     

        if center2 in centers['north']:
            price2 = pricesb['north']
        elif center2 in centers['central']:
            price2 = pricesb['central']
        elif center2 in centers['south']:
            price2 = pricesb['south']     

        #calculate values for center 1
        index1 = stores[center1]
        profit1 = float(int(index1[1]) * SIZEOFSTORE * int(price1))
        loss1 = float(int((index1[0]-index1[1]) * int(price1) * SIZEOFSTORE))
        stores_in_rent1 = index1[1]
        empty_stores1 = index1[0] - index1[1]        
        
        #calculate values for center 2
        index2 = stores[center2]
        profit2 = float(int(index2[1]) * SIZEOFSTORE * int(price2))
        loss2 = float(int((index2[0]-index2[1]) * int(price2) * SIZEOFSTORE))
        stores_in_rent2 = index2[1]
        empty_stores2 = index2[0] - index2[1]
        
        #display info to screen
        print('        ', center1, '            ', center2, '\nprofit: ', '{:10,.2f}'.format(profit1), '     ', '{:10,.2f}'.format(profit2), '      per month\nloss: ', '{:10,.2f}'.format(loss1), '     ', '{:10,.2f}'.format(loss2), '     per month\nrent: ', stores_in_rent1, " out of ", index1[0], '      ', stores_in_rent2," out of ", index2[0], '\nempty:      ', empty_stores1, '           ', empty_stores2)
        #display info by bar chart
        compare_bar_chart(profit1, profit2, center1, center2)
        #back to menu
        managers_menu()
    #comparing areas    
    elif choice == '2':
    
        for key in centers:
            print(key)
        #get vaild areas names from user
        area1 = input("\nplease enter two areas you would like to compare\n")
        
        
        while area1 not in centers:
            area1 = input("please enter vaild area name\n")
            
        area2 = input()    
        while area2 not in centers:
            area2 = input("please enter vaild area name\n")
        #get areas prices
        price1 = pricesb.get(area1,'invaild area')
        price2 = pricesb.get(area2,'invaild area')
        
        citylist1 = list(centers[area1])  
        citylist2 = list(centers[area2])
        
        #reset values
        profit1 = 0
        loss1 = 0
        stores_in_rent1 = 0
        empty_stores1 = 0
        
        profit2 = 0
        loss2 = 0
        stores_in_rent2 = 0
        empty_stores2 = 0
        
        #calculate values for areas 
        for key in stores:
            if key in citylist1:
                
                stores_in_rent1 += stores[key][1]
                
                empty_stores1 += (stores[key][0]-stores[key][1])
                profit1 += float(int(stores[key][1]) * int(price1) * SIZEOFSTORE)
                loss1 += float(int(stores[key][0] - stores[key][1]) * int(price1) * SIZEOFSTORE)
                
            
            elif key in citylist2:
                stores_in_rent2 += stores[key][1]
                empty_stores2 += (stores[key][0]-stores[key][1])
                profit2 += float(int(stores[key][1]) * int(price2) * SIZEOFSTORE)
                loss2 += float(int(stores[key][0] - stores[key][1]) * int(price2) * SIZEOFSTORE)
        
        #display information to screen
        print('\n', area1, ':\n')        
        print("profit:",'{:10,.2f}'.format(profit1),"₪ per month\nloss:",'{:10,.2f}'.format(loss1),"₪ per month\nnumber of stores in rent:",stores_in_rent1,'\nnumber of empty stores:', empty_stores1)
        print('\n', area2, ':\n')
        print("profit:",'{:10,.2f}'.format(profit2),"₪ per month\nloss:",'{:10,.2f}'.format(loss2),"₪ per month\nnumber of stores in rent:",stores_in_rent2,'\nnumber of empty stores:', empty_stores2)
        
        #display information by bar chart
        compare_bar_chart(profit1, profit2, area1, area2)
        
        #back to menu
        managers_menu()

#function produces ber chart for comparing centers/areas  
def compare_bar_chart(profit1, profit2, name1, name2):
    
    left_edges = [10, 20, 30, 40, 50]
    heights = [0, profit1, 0, profit2, 0]
    bar_width = 10
    
    plt.bar(left_edges, heights, bar_width, color = ('c'))
    plt.title('profit compare between ' + name1 + ' and ' + name2)
    plt.xlabel('centers')
    plt.ylabel('profit')
    plt.xticks([10, 20, 30, 40, 50],
               [' ', name1, ' ',  name2, ' '])
    
    if profit1 > profit2:
        y1 = profit1
        y2 = profit2
    else:
        y1 = profit2
        y2 = profit1
    
    plt.yticks([0, y2, 0, y1, 0],
               ['₪30m', '{:10,.2f}'.format(y2) , '₪90M', '{:10,.2f}'.format(y1), '₪150M'])    
    plt.show()
    return  

def profit_func():
    
    #open relevant files
    prices = open('prices_file.dat', 'rb')
    pricesb = pickle.load(prices)
    prices.close()
    avalibility_file = open('avalibility_file.dat', 'rb')
    stores = pickle.load(avalibility_file)
    avalibility_file.close()
    centers_file = open('centers_file.dat','rb')
    centers = pickle.load(centers_file)
    centers_file.close() 
    
    #get vaild choose from user - calculate per center/area/general
    print("How whould you like to check profits?\n1.per center\n2.per area\n3.general profit\n")
    choice = int(input())
    while choice != 1 and choice != 2 and choice != 3:
        print("please enter only 1/2/3")
        choice = int(input())
    #calculate per center
    if choice == 1:
        
        #get vaild area
        area = input("please enter the area(north/central/south)\n")
        
        while area != 'north' and area != 'central' and area != 'south':
            area = input("please enter vaild area\n")
        
        for val in centers[area]:
            print(val)
        
        #get vaild center    
        center = input("\nplease choose 1 center from above\n")
        while center not in stores:
            center = input("please enter vaild center\n")
        
        #get price        
        price = pricesb.get(area,'price not found')
        index = stores[center]
        #calculate
        profit = float(int(index[1]) * SIZEOFSTORE * int(price))
        loss = float(int((index[0]-index[1]) * int(price) * SIZEOFSTORE))
        #display info    
        print("This center profit is:",'{:10,.2f}'.format(profit),"₪ per month\nThis area loss is:",'{:10,.2f}'.format(loss),'₪ per month\nstores in rent', index[1],'\nempty stores', index[0] - index[1], '\n' )
            
        total_stores = index[0]
        stores_in_rent = index[1]
        empty_stores = index[0] - index[1]
        #display info by pie chart    
        pie_chart(stores_in_rent, empty_stores, center, profit, loss)
    
    #calculate profit per area         
    elif choice == 2:
    
        for key in centers:
            print(key)
        
        #get vaild area name
        area = input("\nplease enter the area you whould like to check about \n")
        
        while area != 'north' and area != 'central' and area != 'south':
            area = input("please enter vaild area\n")
        #get price
        price = pricesb[area]
        
        #reset values
        profit = 0
        loss = 0
        stores_in_rent = 0
        empty_stores = 0
        
        area_stores = centers[area]
        city_list = list(area_stores)
        #sum profit from all center
        for key in stores:
            if key in city_list:
                stores_in_rent += stores[key][1]
                empty_stores += (stores[key][0]-stores[key][1])
                profit += float(int(stores[key][1]) * int(price) * SIZEOFSTORE)
                loss += float(int(stores[key][0] - stores[key][1]) * int(price) * SIZEOFSTORE)
            
        
        #display to screen
        print("This area profit is:",'{:10,.2f}'.format(profit),"₪ per month\nThis area loss is:",'{:10,.2f}'.format(loss),"₪ per month\nnumber of stores in rent:",stores_in_rent,'\nnumber of empty stores:', empty_stores)        
        #display by pie chart
        pie_chart(stores_in_rent, empty_stores, area, profit, loss)
        managers_menu()
        
    #calculate general profit    
    elif choice == 3:
        
        #reset values
        profit = 0
        loss = 0
        stores_in_rent = 0
        empty_stores = 0
        
        #get prices
        price_north = pricesb['north']
        price_central = pricesb['central']
        price_south = pricesb['south']
        
        city_list = []
        for val in centers.values():
            city_list.append(val)
        
        #sum all profit from centers with price difference
        for key in stores:
            if key in centers['north']:
                price = pricesb['north']
            elif key in centers['central']:
                price = pricesb['central']
            elif key in centers['south']:
                price = pricesb['south']
    
            stores_in_rent += stores[key][1]
            empty_stores += (stores[key][0]-stores[key][1])
            profit += float(int(stores[key][1]) * int(price) * SIZEOFSTORE)
            loss += float(int(stores[key][0] - stores[key][1]) * int(price) * SIZEOFSTORE)
        
        #display to screen 
        print("the general profit is:",'{:10,.2f}'.format(profit),"₪\nThis general loss is(for empty stores):",'{:10,.2f}'.format(loss),"₪\nnumber of stores in rent:",stores_in_rent,'\nnumber of empty stores:', empty_stores)
        
        #display to pie chart
        pie_chart(stores_in_rent, empty_stores, 'israel', profit, loss)  
    
    #back to menu
    managers_menu()

#function produces pie chart for display profit
def pie_chart(stores_in_rent, empty_stores, center, profit, loss):
    
    pie_values = (stores_in_rent, empty_stores)
    plt.title('rent/empty stores status at ' + center )
    slice_lables = ['stores in rent:' + str(stores_in_rent), 'empty stores: ' + str(empty_stores)]
    colors = ('yellowgreen', 'lightcoral')
    explode = (0, 0.2)
    legend_labels = ['profit: ' + str('{:10,.2f}'.format(profit)) + '₪ per month', 'loss(empty stores): ' + str('{:10,.2f}'.format(loss)) + '₪ per month']
    plt.pie(pie_values,labels = slice_lables, explode = explode, colors = colors, shadow = True, startangle = 340, autopct=('%1.1f%%'))
    plt.legend(legend_labels, loc = 3)
    #Display the pie chart
    
    plt.show()
    return
            
documents()