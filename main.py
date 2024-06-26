import mysql.connector as mycon
import random
import csv
import time
from datetime import date, timedelta
from tabulate import tabulate
import matplotlib.pyplot as plt
#To connect to the database
con = mycon.connect(
    host = 'localhost', 
    user='root', 
    password ='pass'
    )
#Creates the cursor
cur = con.cursor()

#To check if the connection is successful
'''
if con.is_connected():
    print("ok")
'''
#To create the database Todo_list
'''
cur.execute("CREATE DATABASE Todo_list;")
'''
#To open the database
cur.execute("use todo_list;")

#To create the points table
'''
cur.execute("CREATE TABLE points (username varchar(255) NOT NULL, points integer);")
cur.commit()
'''
#To encrypt
def encrypt(message):
    key = random.randint(1, 10)
    encrypted_message = ""
    for char in message:
        encrypted_char = chr(ord(char) + key)
        encrypted_message += encrypted_char
    return encrypted_message, key

#To decrypt
def decrypt(encrypted_message, key):
    decrypted_message = ""
    for char in encrypted_message:
        decrypted_char = chr(ord(char) - key)
        decrypted_message += decrypted_char
    return decrypted_message

#The sign-ip page
def signup():
    global user_name  #This is the name of the user(the database) we will work with.
    global access_type  #This is the type of the user that has access to the database.
    global current_date 
    while True:
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║          This is the signup           ║")
        print("║                page.                  ║")
        print("╚═══════════════════════════════════════╝")
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║     Please create a child account     ║")
        print("║          first before creating        ║")
        print("║           a parent account.           ║")
        print("╚═══════════════════════════════════════╝")
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║              Is this a                ║")
        print("║           1. Child account            ║")
        print("║           2. Parent account           ║")
        print("║              Enter 1 or 2:            ║")
        print("╚═══════════════════════════════════════╝")
        NeedParent_choice = input("INPUT: ")
        if NeedParent_choice == "2":
            parent = True
            access_type = "Parent"
            break
        elif NeedParent_choice == "1":
            parent = False
            child = False
            access_type = "Child"
            break
        else:
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║      Invalid input. Please enter      ║")
            print("║                 1 or 2.               ║")
            print("╚═══════════════════════════════════════╝")

    while True:
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║        Enter a valid username:        ║")
        print("╚═══════════════════════════════════════╝")
        user_name = input("INPUT: ")
        with open('dat.csv', mode='r') as file:  #Read the CSV file and checks if the username already exits.
            reader = csv.reader(file)
            rows = list(reader)
            items = [row[0] for row in rows]

        if user_name in items:
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║        Username already exists.       ║")
            print("╚═══════════════════════════════════════╝")

            continue

        if len(user_name) < 8 or len(user_name) > 20:  #Checks if the username length is in between (8,20).
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║      Username should be between       ║")
            print("║         8 and 20 characters.          ║")
            print("╚═══════════════════════════════════════╝")
            continue
        break

    while True:
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║        Enter a valid password:        ║")
        print("╚═══════════════════════════════════════╝")

        password = input("INPUT: ")

        if len(password) < 8 or password.isnumeric() or password.isalpha():  #Checks if password length is in between (8,20) and has has at least 1 alphabet.
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║   Please keep the following in mind:  ║")
            print("║ - The password must have at least 1   ║")
            print("║   letter and 1 number.                ║")
            print("║ - The password must be longer than 8  ║")
            print("║   characters.                         ║")
            print("╚═══════════════════════════════════════╝")
            continue
        
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║        Confirm your password:         ║")
        print("╚═══════════════════════════════════════╝")

        confirm_password = input("INPUT: ")
        
        if password != confirm_password:  #To check if password is the same as confirm_password
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║        Passwords do not match.        ║")
            print("╚═══════════════════════════════════════╝")
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║   Please keep the following in mind:  ║")
            print("║ - The password must have at least 1   ║")
            print("║   letter and 1 number.                ║")
            print("║ - The password must be longer than 8  ║")
            print("║   characters.                         ║")
            print("╚═══════════════════════════════════════╝")
            continue

        confirm_password = encrypt(password)  #Encrypt the password
        encrypted_password = confirm_password[0]
        key = confirm_password[1] #stores the key
        break
        
    if NeedParent_choice == "2": #Connects parent account with the child account
        while True:
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║   Does your child have an account?    ║")
            print("║         (y - yes / n - no):           ║")
            print("╚═══════════════════════════════════════╝")

            child_account_choice = input("INPUT: ")
            if child_account_choice.lower() == "y":
                with open('dat.csv', mode='r') as file:
                    reader = csv.reader(file)
                    rows = list(reader)
                username_found = False
                while True:
                    time.sleep(0.18)
                    print("╔═══════════════════════════════════════╗")
                    print("║      Enter your child's username:     ║")
                    print("╚═══════════════════════════════════════╝")
                    child = input("INPUT: ")
                    for row in rows:
                        if child == row[0]:
                            while True:
                                time.sleep(0.18)
                                print("╔═══════════════════════════════════════╗")
                                print("║      Enter your child's password:     ║")
                                print("╚═══════════════════════════════════════╝")
                                child_password = input("INPUT: ")
                                if child_password == decrypt(row[1], int(row[2])):
                                    time.sleep(0.18)
                                    print("╔═══════════════════════════════════════╗")
                                    print("║           Child authenticated         ║")
                                    print("╚═══════════════════════════════════════╝")
                                    username_found = True
                                    break
                                else:
                                    time.sleep(0.18)
                                    print("╔═══════════════════════════════════════╗")
                                    print("║   Invalid password. Please try again. ║")
                                    print("╚═══════════════════════════════════════╝")
                    if not username_found:
                        time.sleep(0.18)
                        print("╔═══════════════════════════════════════╗")
                        print("║           User is not valid           ║")
                        print("╚═══════════════════════════════════════╝")
                        continue
                    break
                break
            elif child_account_choice.lower() == "n":
                time.sleep(0.18)
                print("╔═══════════════════════════════════════╗")
                print("║   Then please create a child account  ║")
                print("╚═══════════════════════════════════════╝")
                signup()
                return
            else:
                time.sleep(0.18)
                print("╔═══════════════════════════════════════╗")
                print("║     Invalid input. Please enter y     ║")
                print("╚═══════════════════════════════════════╝")

                continue

    while True:
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║Are you sure with the following details║")
        print(f"       Username: {user_name}            ")
        print(f"       Password: {password}             ") 
        print("║ (y - yes / n - no):                   ║")
        print("╚═══════════════════════════════════════╝")

        user_input = input("INPUT: ")

        if user_input.lower() == "n":
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║        Registration cancelled.        ║")
            print("╚═══════════════════════════════════════╝")
            signup()
            return
        elif user_input.lower() == "y":
            data = [user_name, encrypted_password, key, parent, child]
            with open('dat.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(data)
            current_date = date.today()
            if NeedParent_choice == "1":
                cur.execute(f"CREATE TABLE {user_name} (Task_ID INTEGER primary key, Tasks VARCHAR(225), Due_date DATE, Status VARCHAR(20) DEFAULT 'Incomplete', Points INTEGER)")
                cur.execute(f"INSERT INTO points VALUES ('{user_name}', 0)")
                con.commit()
                main_menu()
                return
            if NeedParent_choice == "2":
                user_name = child
            main_menu()
            return
        else:
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║  Invalid input. Please enter y and n  ║")
            print("╚═══════════════════════════════════════╝")

def login(): #Login
    while True:
        global user_name
        global access_type
        global current_date
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║        This is the login page.        ║")
        print("╚═══════════════════════════════════════╝")

        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║         Enter your username:          ║")
        print("╚═══════════════════════════════════════╝")

        user_name = input("INPUT: ")
        with open('dat.csv', mode='r') as file:  #Reads the CSV file to find the row in which the account details are stored
            reader = csv.reader(file)
            rows = list(reader)
        found_user = False
        for row in rows:
            if user_name == row[0]:
                found_user = True
                while True:
                    time.sleep(0.18)
                    print("╔═══════════════════════════════════════╗")
                    print("║          Enter your password:         ║")
                    print("╚═══════════════════════════════════════╝")
                    password = input("INPUT: ")
                    key = int(row[2])
                    decrypted_password = decrypt(row[1], key) #Decrypt the password    
                    if password == decrypted_password:  #checks the password is correct
                        time.sleep(0.18)
                        current_date = date.today() 
                        print("╔═══════════════════════════════════════╗")
                        print("║           Login successful            ║")
                        print("╚═══════════════════════════════════════╝")
                        if row[3] == "True": #Sets the access_type and username
                            access_type = "Parent"
                            user_name = row[4]
                        else:
                            access_type = "Child"
                        update_overdue_tasks()
                        main_menu()
                        return
                    else:
                        time.sleep(0.18)
                        print("╔═══════════════════════════════════════╗")
                        print("║  Invalid password. Please try again.  ║")
                        print("╚═══════════════════════════════════════╝")
                        continue
        
        if not found_user:
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║           User is not valid           ║")
            print("╚═══════════════════════════════════════╝")
            while True:
                time.sleep(0.18)
                print("╔═══════════════════════════════════════╗")
                print("║ Would you like to create a new account║")
                print("║                 1. Yes                ║")
                print("║                 2. No                 ║")
                print("╚═══════════════════════════════════════╝")

                exit_choice = input("INPUT: ")
                if exit_choice == "1":
                    signup()
                    return
                elif exit_choice == "2":
                    login()
                    return
                else:
                    time.sleep(0.18)
                    print("╔═══════════════════════════════════════╗")
                    print("║      Invalid Input. Please enter      ║")
                    print("║               1 or 2                  ║")
                    print("╚═══════════════════════════════════════╝")
                    continue

def homepage():
    while True:
        print("  ██████╗ ██╗   ██╗     ██████╗  ██████╗ ")
        print("  ██╔══██╗╚██╗ ██╔╝     ██╔══██╗██╔═══██╗")
        print("  ██████╔╝ ╚████╔╝█████╗██║  ██║██║   ██║")
        print("  ██╔═══╝   ╚██╔╝ ╚════╝██║  ██║██║   ██║")
        print("  ██║        ██║        ██████╔╝╚██████╔╝")
        print("  ╚═╝        ╚═╝        ╚═════╝  ╚═════╝ ")
        print("╔═══════════════════════════════════════╗")
        print("║       Welcome to the Main Menu!       ║")
        print("╚═══════════════════════════════════════╝")
        time.sleep(0.2)
        print("╔═══════════════════════════════════════╗")
        print("║       Please select an option:        ║")
        print("╚═══════════════════════════════════════╝")
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║             1. Sign up                ║")
        time.sleep(0.18)
        print("║             2. Login                  ║")
        time.sleep(0.18)
        print("║             3. Quit                   ║")
        time.sleep(0.18)
        print("║       Enter your choice (1-3):        ║")
        print("╚═══════════════════════════════════════╝")

        choice = input("INPUT: ")

        if choice == "1":
            signup()
            return
        elif choice == "2":
            login()
            return
        elif choice == "3":
            print("╔═══════════════════════════════════════╗")
            print("║       Thank you for using Py-DO.      ║")
            print("║  Stay organized and stay productive!  ║")
            print("╚═══════════════════════════════════════╝")
            print(" ██████╗  ██████╗  ██████╗ ██████╗ ██████╗ ██╗   ██╗███████╗██╗")
            print("██╔════╝ ██╔═══██╗██╔═══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝██║")
            print("██║  ███╗██║   ██║██║   ██║██║  ██║██████╔╝ ╚████╔╝ █████╗  ██║")
            print("██║   ██║██║   ██║██║   ██║██║  ██║██╔══██╗  ╚██╔╝  ██╔══╝  ╚═╝")
            print("╚██████╔╝╚██████╔╝╚██████╔╝██████╔╝██████╔╝   ██║   ███████╗██╗")
            print(" ╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝")
            quit()
        else:
            print("╔═══════════════════════════════════════╗")
            print("║ Invalid input. Please choose a number ║")
            print("║             from 1 to 3.              ║")
            print("╚═══════════════════════════════════════╝")

def main_menu():
    while True:
        print("╔═══════════════════════════════════════╗")
        print("║          Welcome to the PyDO!         ║")
        print(f"║          Today is {current_date}          ║")
        time.sleep(0.2)
        print("║       Please select an option:        ║")
        time.sleep(0.18)
        print("║          1. Task manager              ║")
        time.sleep(0.18)
        print("║          2. Reward manager            ║")
        time.sleep(0.18)
        print("║          3. Status                    ║")
        time.sleep(0.18)
        if access_type == "Parent":
            print("║          4. Parent menu               ║")
            time.sleep(0.18)
            print("║          5. Sign out                  ║")
        else:
            print("║          4. Sign out                  ║")
        print("║           Enter your choice :         ║")
        print("╚═══════════════════════════════════════╝")

        
        time.sleep(0.18)
        choice = input("INPUT: ")

        if choice == "1":
            task_manager()
            return
        elif choice == "2":
            reward_manager()
            return
        elif choice == "3":
            status()
            return
        elif choice == "4" and access_type == "Child":
            homepage()
            return
        elif choice == "4" and access_type == "Parent":
            parent_menu()
            return
        elif choice == "5" and access_type == "Parent":
            homepage()
            return
        else:
            if access_type == "Child":
                time.sleep(0.18)
                print("╔═══════════════════════════════════════╗")
                print("║ Invalid input. Please choose a number ║")
                print("║             from 1 to 4.              ║")
                print("╚═══════════════════════════════════════╝")

            elif access_type == "Parent":
                time.sleep(0.18)
                print("╔═══════════════════════════════════════╗")
                print("║ Invalid input. Please choose a number ║")
                print("║            from 1 to 5.               ║")
                print("╚═══════════════════════════════════════╝")

def task_manager():
    while True:
        print("╔═══════════════════════════════════════╗")
        print("║     This is the task manager menu     ║")
        print(f"║          Today is {current_date}          ║")
        time.sleep(0.2)
        print("║       Please select an option:        ║")
        time.sleep(0.18)
        print("║            1. View Tasks              ║")
        
        print("║            2. View Overdue Tasks      ║ ")
        time.sleep(0.18)
        print("║            3. Complete Tasks          ║")
        time.sleep(0.18)
        print("║            4. Add Task                ║")
        time.sleep(0.18)
        print("║            5. Edit Task               ║")
        time.sleep(0.18)
        print("║            6. Delete Task             ║")
        time.sleep(0.18)
        print("║            7. Delete All Tasks        ║")
        time.sleep(0.18)
        print("║            8. Back To Main Menu       ║")
        time.sleep(0.18)
        print("║          Enter your choice :          ║")
        print("╚═══════════════════════════════════════╝")
        
        choice = input("INPUT: ")
        if choice == "1":
            view_tasks()
            return
        elif choice == "2":
            view_overdue()
            return
        elif choice == "3":
            set_completed_tasks()
            return
        elif choice == "4":
            add_task()
            return
        elif choice == "5":
            edit_task()
            return
        elif choice == "6":
            delete_task()
            return
        elif choice == "7":
            delete_all_tasks()
            return
        elif choice == "8":
            main_menu()
            return
        else:
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║ Invalid input. Please choose a number ║")
            print("║            from 1 to 7.               ║")
            print("╚═══════════════════════════════════════╝")

def reward_manager():
    while True:
        print("╔═══════════════════════════════════════╗")
        print("║     This is the reward manager menu   ║")
        print(f"║          Today is {current_date}          ║")
        time.sleep(0.2)
        print("║       Please select an option:        ║")
        time.sleep(0.18)
        print("║          1. View Rewards              ║")
        time.sleep(0.18)
        print("║          2. Complete Reward           ║")
        time.sleep(0.18)
        print("║          3. Back To Main Menu         ║")
        time.sleep(0.18)
        print("║          Enter your choice :          ║")
        print("╚═══════════════════════════════════════╝")

        
        choice = input("INPUT: ")

        if choice == "1":
            view_rewards()
            return
        elif choice == "2":
            claim_rewards()
            return
        elif choice == "3":
            main_menu()
            return
        else:
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║ Invalid input. Please choose a number ║")
            print("║             from 1 to 3.              ║")
            print("╚═══════════════════════════════════════╝")

def parent_menu():
    print("╔═══════════════════════════════════════╗")
    print("║         This is the parent menu       ║")
    print(f"║          Today is {current_date}          ║")
    time.sleep(0.2)
    print("║         Please select an option:      ║")
    time.sleep(0.18)
    print("║           1. Add/Change Points        ║")
    time.sleep(0.18)
    print("║           2. Add rewards              ║")
    time.sleep(0.18)
    print("║           3. Edit Reward              ║")
    time.sleep(0.18)
    print("║           4. Delete Reward            ║")
    time.sleep(0.18)
    print("║           5. Delete All Rewards       ║")
    time.sleep(0.18)
    print("║           6. Delete Accounts          ║")
    time.sleep(0.18)
    print("║           7. Back To Main Menu        ║")
    time.sleep(0.18)
    print("║           Enter your choice :         ║")
    print("╚═══════════════════════════════════════╝")

    choice = input("INPUT: ")

    if choice == "1":
        add_points()
        return
    elif choice == "2":
        add_reward()
        return
    elif choice == "3":
        edit_reward()
        return
    elif choice == "4":
        delete_reward()
        return
    elif choice == "5":
        delete_all_rewards()
        return
    elif choice == "6":
        delete_account()
        return
    elif choice == "7":
        main_menu()
        return
    else:
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║ Invalid input. Please choose a number ║")
        print("║             from 1 to 3.              ║")
        print("╚═══════════════════════════════════════╝")

def status():
    while True:
        print("╔═══════════════════════════════════════╗")
        print("║          This is the status menu      ║")
        print(f"║          Today is {current_date}          ║")
        time.sleep(0.2)
        print("║          Please select an option:     ║")
        time.sleep(0.18)
        print("║     1. Look at performances graph     ║")
        time.sleep(0.18)
        print("║     2. Look at all the Complete tasks ║")
        time.sleep(0.18)
        print("║     3. View Total Points              ║")
        time.sleep(0.18)
        print("║     4. Back to Main menu              ║")
        time.sleep(0.18)
        print("║            Enter your choice :        ║")
        print("╚═══════════════════════════════════════╝")

        choice = input("INPUT: ")
        if choice == "1":
            view_performances()
        elif choice == "2":
            view_completed_tasks()
            return
        elif choice == "3":
            print(calculate_total_points())
        elif choice == "4":
            main_menu()
            return
        else:
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║ Invalid input. Please choose a number ║")
            print("║             from 1 to 4.              ║")
            print("╚═══════════════════════════════════════╝")


def view_tasks():
        update_overdue_tasks()
        time.sleep(0.2)
        cur.execute(f"SELECT Tasks, Due_date, Points, Status FROM {user_name} WHERE Status = 'Incomplete' ORDER BY Due_date")
        rows = cur.fetchall()
        columns = [desc[0] for desc in cur.description]
        print(tabulate(rows, headers=columns, tablefmt='double_grid'))
        while True:
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║     Would you like go to back menu?   ║")
            print("║               (1 - yes)               ║") 
            print("╚═══════════════════════════════════════╝")

            choice = input("INPUT: ")
            if choice == "1":
                task_manager()
                return
            else:
                time.sleep(0.18)
                print("╔═══════════════════════════════════════╗")
                print("║   Invalid input. Please enter only 1  ║")
                print("╚═══════════════════════════════════════╝")

def set_completed_tasks():
    update_overdue_tasks()
    time.sleep(0.2)
    cur.execute(f"SELECT * FROM {user_name} WHERE Status in ('Incomplete','Overdue') ORDER BY Due_date")
    rows = cur.fetchall()
    if not rows:  # No incomplete or overdue tasks
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║         You have no incomplete        ║")
        print("║           or overdue tasks.           ║")
        print("║        Returning to the main menu.    ║")
        print("╚═══════════════════════════════════════╝")
        time.sleep(0.18)
        task_manager()
        return
    columns = [desc[0] for desc in cur.description]
    print(tabulate(rows, headers=columns, tablefmt='double_grid'))

    time.sleep(0.18)
    print("╔═══════════════════════════════════════╗")
    print("║   Enter the number of the row (task)  ║")
    print("║          you have completed:          ║")
    print("╚═══════════════════════════════════════╝")

    choice = input("INPUT: ")
    if choice.isdigit():
        choice = int(choice) - 1
    else:
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║ Invalid task number. Please enter a   ║")
        print("║                number.                ║")
        print("╚═══════════════════════════════════════╝")
        set_completed_tasks()

    if choice < 0 or choice >= len(rows):
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║          Invalid task number.         ║")
        print("╚═══════════════════════════════════════╝")
        set_completed_tasks()
    if rows[choice][4] == None:
        task_id = rows[choice][0]
        cur.execute(f"UPDATE {user_name} SET Status = 'Complete' WHERE Task_id = {task_id}")
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║ Task marked as complete successfully! ║")
        print("╚═══════════════════════════════════════╝")
    else:
        task_id = rows[choice][0]
        task_points = int(rows[choice][4])
        cur.execute(f"SELECT points FROM points WHERE username = '{user_name}'")
        current_points = int(cur.fetchone()[0])
        cur.execute(f"UPDATE {user_name} SET Status = 'Complete' WHERE Task_id = {task_id}")
        cur.execute(f"UPDATE points SET points = {current_points + task_points} WHERE username = '{user_name}'")
        con.commit()
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║ Task marked as complete successfully! ║")
        print("╚═══════════════════════════════════════╝")


    while True:
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║ Would you like to mark another task as║")
        print("║ complete or go back to the main menu? ║")
        print("║        1. Mark another task           ║")
        print("║        2. Back to menu                ║")
        print("╚═══════════════════════════════════════╝")

        exit_choice = input("INPUT: ")
        if exit_choice == "1":
            set_completed_tasks()
            return
        elif exit_choice == "2":
            task_manager()
            return
        else:
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║ Invalid task number. Please enter     ║")
            print("║               1 or 2                  ║")
            print("╚═══════════════════════════════════════╝")
            continue

def add_task():
    time.sleep(0.2)
    print("╔═══════════════════════════════════════╗")
    print("║           Enter the task:             ║")
    print("╚═══════════════════════════════════════╝")
    task = input("INPUT: ")
    if access_type == "Child":
        while True:
            try:
                cur.execute(f"SELECT Task_id, Tasks, Due_date, Points FROM {user_name} ORDER BY Due_date")
                rows = cur.fetchall()
                columns = [desc[0] for desc in rows]
                while True:
                    task_id = random.randint(0,99999999)
                    if task_id % 10 == 0:
                        continue
                    if task_id not in columns:
                        time.sleep(0.18)
                        print("╔═══════════════════════════════════════╗")
                        print("║       Enter a date (YYYY-MM-DD):      ║")
                        print("╚═══════════════════════════════════════╝")
                        date_input = input("INPUT: ")
                        cur.execute(f"INSERT INTO {user_name} (Task_id ,Tasks, Due_date) VALUES ({task_id},'{task}', '{date_input}')")
                        con.commit()
                        time.sleep(0.18)
                        print("╔═══════════════════════════════════════╗")
                        print("║       Task inserted successfully!     ║")
                        print("╚═══════════════════════════════════════╝")
                        break
            except mycon.errors.DataError:
                current_date = date.today()
                if date_input.lower() == "today":
                    date_input = current_date
                elif date_input.lower() == "tomorrow":
                    date_input = current_date + timedelta(days=1)
                elif date_input.lower().startswith("in"):
                    day = date_input[2:].strip()
                    if day.isdigit():
                        date_input = current_date + timedelta(days=int(day))
                    else:
                        time.sleep(0.18)
                        print("╔═══════════════════════════════════════╗")
                        print("║      Invalid number. Please enter     ║")
                        print("║              a integer                ║")
                        print("╚═══════════════════════════════════════╝")
                        continue
                else:
                    time.sleep(0.18)
                    print("╔═══════════════════════════════════════╗")
                    print("║ Invalid date format. Please enter a   ║")
                    print("║    date in the format YYYY-MM-DD.     ║")
                    print("╚═══════════════════════════════════════╝")
                    continue
                cur.execute(f"INSERT INTO {user_name} (Task_id ,Tasks, Due_date) VALUES ({task_id},'{task}', '{date_input}')")
                con.commit()
                time.sleep(0.18)
                print("╔═══════════════════════════════════════╗")
                print("║       Task inserted successfully!     ║")
                print("╚═══════════════════════════════════════╝")
                break
            break
    elif access_type == "Parent":
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║    Enter the points for this task:    ║")
        print("╚═══════════════════════════════════════╝")
        points = input("INPUT: ")
        while True:
            try:
                cur.execute(f"SELECT Task_id, Tasks, Due_date, Points FROM {user_name} ORDER BY Due_date")
                rows = cur.fetchall()
                columns = [desc[0] for desc in rows]
                task_id = random.randint(0,99999999)
                while True:
                    if task_id not in columns:
                        time.sleep(0.18)
                        print("╔═══════════════════════════════════════╗")
                        print("║       Enter a date (YYYY-MM-DD):      ║")
                        print("╚═══════════════════════════════════════╝")
                        date_input = input("INPUT: ")
                        cur.execute(f"INSERT INTO {user_name} (Task_id ,Tasks, Due_date, Points) VALUES ({task_id},'{task}', '{date_input}', {points})")
                        con.commit()
                        time.sleep(0.18)
                        print("╔═══════════════════════════════════════╗")
                        print("║       Task inserted successfully!     ║")
                        print("╚═══════════════════════════════════════╝")
                        break
            except mycon.errors.DataError:
                current_date = date.today()
                if date_input.lower() == "today":
                    date_input = current_date
                elif date_input.lower() == "tomorrow":
                    date_input = current_date + timedelta(days=1)
                elif date_input.lower().startswith("in"):
                    day = date_input[2:].strip() 
                    if day.isdigit():
                        date_input = current_date + timedelta(days=int(day))
                    else:
                        time.sleep(0.18)
                        print("╔═══════════════════════════════════════╗")
                        print("║      Invalid number. Please enter     ║")
                        print("║              a integer                ║")
                        print("╚═══════════════════════════════════════╝")
                        continue
                else:
                    time.sleep(0.18)
                    print("╔═══════════════════════════════════════╗")
                    print("║ Invalid date format. Please enter a   ║")
                    print("║    date in the format YYYY-MM-DD.     ║")
                    print("╚═══════════════════════════════════════╝")
                    continue
                cur.execute(f"INSERT INTO {user_name} (Task_id ,Tasks, Due_date, Points) VALUES ({task_id},'{task}', '{date_input}', {points})")
                con.commit()
                time.sleep(0.18)
                print("╔═══════════════════════════════════════╗")
                print("║       Task inserted successfully!     ║")
                print("╚═══════════════════════════════════════╝")
                break
            break
    while True:
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║ Would you like add a new task again or║")
            print("║ to back menu?                         ║")
            print("║           1. New task                 ║")
            print("║           2. Back to menu             ║")
            print("╚═══════════════════════════════════════╝")

            exit_choice = input("INPUT: ")
            if exit_choice == "1":
                add_task()
                return
            elif exit_choice == "2":
                task_manager()
                return
            else:
                time.sleep(0.18)
                print("╔═══════════════════════════════════════╗")
                print("║   Invalid task number. Please enter   ║")
                print("║               1 or 2                  ║")
                print("╚═══════════════════════════════════════╝")

def edit_task():
    time.sleep(0.2)
    cur.execute(f"SELECT * FROM {user_name} ORDER BY Due_date")
    rows = cur.fetchall()
    if not rows:  # No incomplete or overdue tasks
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║               You have no             ║")
        print("║              tasks to edit.           ║")
        print("║       Returning to the main menu.     ║")
        print("╚═══════════════════════════════════════╝")
        time.sleep(0.18)
        task_manager()
        return
    columns = [desc[0] for desc in cur.description]
    time.sleep(0.18)
    print(tabulate(rows, headers=columns, tablefmt='double_grid'))

    time.sleep(0.18)
    print("╔═══════════════════════════════════════╗")
    print("║ Enter the number of the row (task) you║")
    print("║            want to edit:              ║")
    print("╚═══════════════════════════════════════╝")

    choice = input("INPUT: ")
    if choice.isdigit():
            choice = int(choice) - 1
    else:
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║ Invalid input. Please enter a number. ║")
        print("╚═══════════════════════════════════════╝")

    if choice < 0 or choice >= len(rows):
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║          Invalid task number.         ║")
        print("╚═══════════════════════════════════════╝")
        edit_task()
    time.sleep(0.18)
    print("╔═══════════════════════════════════════╗")
    print("║      Enter the new name for task      ║")
    print("╚═══════════════════════════════════════╝")

    new_task = input("INPUT: ")
    task_id = rows[choice][0]
    ToCheckIfOverdue = rows[choice][3]
    while True:
        try:
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║ Enter the new date (n - if you don't  ║")
            print("║        want to change the date):      ║")
            print("╚═══════════════════════════════════════╝")

            new_date = input("INPUT: ")
            if new_date == "n":
                cur.execute(f"UPDATE {user_name} SET Tasks = '{new_task}' WHERE Task_id = {task_id}")
                con.commit()
                time.sleep(0.18)
                print("╔═══════════════════════════════════════╗")
                print("║       Task updated successfully!      ║")
                print("╚═══════════════════════════════════════╝")
                break
            if ToCheckIfOverdue != "Overdue":
                cur.execute(f"UPDATE {user_name} SET Tasks = '{new_task}', Due_date = '{new_date}' WHERE Task_ID = '{task_id}'")
                con.commit()
                time.sleep(0.18)
                print("╔═══════════════════════════════════════╗")
                print("║       Task updated successfully!      ║")
                print("╚═══════════════════════════════════════╝")
                break
            cur.execute(f"UPDATE {user_name} SET Tasks = '{new_task}', Due_date = '{new_date}', Status = 'Incomplete' WHERE Task_ID = '{task_id}'")
            con.commit()
        except mycon.errors.DataError:
            current_date = date.today()
            if new_date.lower() == "today":
                new_date = current_date
            elif new_date.lower() == "tomorrow":
                new_date = current_date + timedelta(days=1)
            elif new_date.lower().startswith("in"):
                day = new_date[2:].strip() 
                if day.isdigit():
                    new_date = current_date + timedelta(days=int(day))
                else:
                    time.sleep(0.18)
                    print("╔═══════════════════════════════════════╗")
                    print("║      Invalid number. Please enter     ║")
                    print("║              a integer                ║")
                    print("╚═══════════════════════════════════════╝")
                    continue
            else:
                time.sleep(0.18)
                print("╔═══════════════════════════════════════╗")
                print("║ Invalid date format. Please enter a   ║")
                print("║    date in the format YYYY-MM-DD.     ║")
                print("╚═══════════════════════════════════════╝")
                continue
            cur.execute(f"UPDATE {user_name} SET Tasks = '{new_task}', Due_date = '{new_date}' WHERE Task_ID = '{task_id}'")
            con.commit()
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║       Task updated successfully!      ║")
            print("╚═══════════════════════════════════════╝")
            break
    while True:
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║ Would you like edit a row (task) again║")
        print("║            or to back menu?           ║")
        print("║            1. Edit again              ║")
        print("║            2. Back to menu            ║")
        print("╚═══════════════════════════════════════╝")

        exit_choice = input("INPUT: ")
        if exit_choice == "1":
            edit_task()
            return
        elif exit_choice == "2":
            task_manager()
            return
        else:
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║   Invalid task number. Please enter   ║")
            print("║               1 or 2                  ║")
            print("╚═══════════════════════════════════════╝")

def delete_task():
    time.sleep(0.2)
    cur.execute(f"SELECT * FROM {user_name} ORDER BY Due_date")
    rows = cur.fetchall()
    if not rows:  # No incomplete or overdue tasks
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║              You have no              ║")
        print("║            tasks to delete.           ║")
        print("║       Returning to the main menu.     ║")
        print("╚═══════════════════════════════════════╝")
        time.sleep(0.18)
        task_manager()
        return
    columns = [desc[0] for desc in cur.description]
    print(tabulate(rows, headers=columns, tablefmt='double_grid'))
    time.sleep(0.18)
    print("╔═══════════════════════════════════════╗")
    print("║ Enter the number of the row (task) you║")
    print("║           want to delete:             ║")
    print("╚═══════════════════════════════════════╝")

    choice = input("INPUT: ")
    if choice.isdigit():
            choice = int(choice) - 1
    else:
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║  Invalid task number, please enter a  ║")
        print("║            valid number               ║")
        print("╚═══════════════════════════════════════╝")

        delete_task()
    if choice < 0 or choice >= len(rows):
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║          Invalid task number          ║")
        print("╚═══════════════════════════════════════╝")

        delete_task()
    task_id = rows[choice][0]
    while True:  
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║ Are you sure you want to delete this  ║")
        print("║       task? (y - yes, n - no):        ║")
        print("╚═══════════════════════════════════════╝")

        conformation = input("INPUT: ")
        if conformation.lower() == "y":
            cur.execute(f"DELETE FROM {user_name} WHERE Task_id = {task_id}")
            con.commit()
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║       Task deleted successfully!      ║")
            print("╚═══════════════════════════════════════╝")
            break
        elif conformation.lower() == "n":
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║          Task not deleted.            ║")
            print("╚═══════════════════════════════════════╝")
            task_manager()
            return
        else:
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║Invalid input. Please enter only y or n║")
            print("╚═══════════════════════════════════════╝")
            continue
    while True:
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║   Would you like delete a row (task)  ║")
            print("║     again or go back to the menu?     ║")
            print("║   (1. Delete again, 2. Back to menu): ║")
            print("╚═══════════════════════════════════════╝")

            exit_choice = input("INPUT: ")
            if exit_choice == "1":
                delete_task()
                break
            elif exit_choice == "2":
                task_manager()
                break
            else:
                time.sleep(0.18)
                print("╔═══════════════════════════════════════╗")
                print("║   Invalid task number. Please enter   ║")
                print("║               1 or 2                  ║")
                print("╚═══════════════════════════════════════╝")
    time.sleep(0.18)
    print("╔═══════════════════════════════════════╗")
    print("║  Invalid task number, please enter a  ║")
    print("║              valid number             ║")
    print("╚═══════════════════════════════════════╝")
    delete_task()

def add_points():
    time.sleep(0.2)
    cur.execute(f"SELECT * FROM {user_name} WHERE Status = 'Incomplete'")
    rows = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    time.sleep(0.18)
    print(tabulate(rows, headers=columns, tablefmt='double_grid'))
    print("╔═══════════════════════════════════════╗")
    print("║ Enter the number of the row (task) to ║")
    print("║              add points:              ║")
    print("╚═══════════════════════════════════════╝")

    choice = input("INPUT: ")
    if choice.isdigit():
        choice = int(choice) - 1
    else:
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║ Invalid task number. Please enter a   ║")
        print("║             valid number.             ║")
        print("╚═══════════════════════════════════════╝")
        add_points()

    if choice < 0 or choice >= len(rows):
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║          Invalid task number          ║")
        print("╚═══════════════════════════════════════╝")
        add_points()

    task_id = rows[choice][0]
    time.sleep(0.18)
    print("╔═══════════════════════════════════════╗")
    print("║       Enter the points to add:        ║")
    print("╚═══════════════════════════════════════╝")

    points = input("INPUT: ")
    cur.execute(f"UPDATE {user_name} SET Points = {points} WHERE Task_id = {task_id}")
    con.commit()
    time.sleep(0.18)
    print("╔═══════════════════════════════════════╗")
    print("║       Points added successfully!      ║")
    print("╚═══════════════════════════════════════╝")


    while True:
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║Would you like to add points to another║")
        print("║      task or go back to the menu?     ║")
        print("║    (1. Add points, 2. Back to menu):  ║")
        print("╚═══════════════════════════════════════╝")

        exit_choice = input("INPUT: ")
        if exit_choice == "1":
            add_points()
            return
        elif exit_choice == "2":
            parent_menu()
            return
        else:
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║   Invalid task number. Please enter   ║")
            print("║               1 or 2                  ║")
            print("╚═══════════════════════════════════════╝")

def delete_account():
    time.sleep(0.2)
    print("╔═══════════════════════════════════════╗")
    print("║         This will delete your         ║")
    print("║     child and parent accounts both.   ║")
    print("╚═══════════════════════════════════════╝")

    with open('dat.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
    for row in rows:
        if user_name in row:
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║ Are you sure you want to delete your  ║")
            print("║ account? This action cannot be undone.║")
            print("║        (1. Delete, 2. Cancel):        ║")
            print("╚═══════════════════════════════════════╝")

            confirm = input("INPUT: ")
            if confirm == "1":
                for row in rows:
                    if user_name == row[4]:
                        rows.remove(row)
                for row in rows:
                    if user_name == row[0]:
                        rows.remove(row)
                with open('dat.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(rows)
                cur.execute(f"DROP TABLE {user_name}")
                cur.execute(f"DELETE FROM points WHERE username = '{user_name}'")
                time.sleep(0.18)
                print("╔═══════════════════════════════════════╗")
                print("║     Account deleted successfully.     ║")
                print("╚═══════════════════════════════════════╝")
                homepage()
                return
        elif confirm == "2":
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║       Account deletion canceled.      ║")
            print("╚═══════════════════════════════════════╝")
            parent_menu()
            return

    time.sleep(0.18)
    print("╔═══════════════════════════════════════╗")
    print("║ Username not found. Please try again. ║")
    print("╚═══════════════════════════════════════╝")
    delete_account()

def add_reward():
    time.sleep(0.2)
    print("╔═══════════════════════════════════════╗")
    print("║        Enter the reward name:         ║")
    print("╚═══════════════════════════════════════╝")

    reward_name = input("INPUT:")
    while True:
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║ Enter the points required for this    ║")
        print("║              reward:                  ║")
        print("╚═══════════════════════════════════════╝")
        reward_points = input("INPUT:")
        if reward_points.isdigit():
            reward_data = f"{reward_name},{reward_points}\n"
            if int(reward_points) > 0:
                with open(f"rewards/{user_name}.txt", mode='a') as file:
                    file.write(reward_data)
                time.sleep(0.18)
                print("╔═══════════════════════════════════════╗")
                print("║       Reward added successfully!      ║")
                print("╚═══════════════════════════════════════╝")

                break
            else:
                time.sleep(0.18)
                print("╔═══════════════════════════════════════╗")
                print("║            Invalid points.            ║")
                print("╚═══════════════════════════════════════╝")

                continue
        else:
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║  Invalid input. Please enter a valid  ║")
            print("║                number.                ║")
            print("╚═══════════════════════════════════════╝")

            continue
    while True:
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║ Would you like to add one more reward ║")
        print("║         or go back to the menu?       ║")
        print("║     (1. Add reward, 2. Back to menu)  ║")
        print("╚═══════════════════════════════════════╝")

        exit_choice = input("INPUT:")
        if exit_choice == "1":
            add_reward()
            return
        elif exit_choice == "2":
            parent_menu()
            return
        else:
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║   Invalid task number. Please enter   ║")
            print("║               1 or 2                  ║")
            print("╚═══════════════════════════════════════╝")

def view_rewards():
    time.sleep(0.2)
    reward_file = f"rewards/{user_name}.txt"
    try:
        file = open(reward_file, 'r')
        file.close()
        rewards = []
        with open(reward_file, mode='r') as file:
            for line in file:
                reward_name, reward_points = line.strip().split(',')
                rewards.append((reward_name, int(reward_points)))

        time.sleep(0.18)
        print("Available Rewards:")
        for i, reward in enumerate(rewards, start=1):
            reward_name, reward_points = reward
            time.sleep(0.18)
            print(f"{i}. {reward_name} - {reward_points} points")

    except FileNotFoundError:
        time.sleep(0.18)
        print("No reward available yet.")
    
    while True:
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║ Would you like to go to the back menu?║")
        print("║            (1. Back to menu)          ║")
        print("╚═══════════════════════════════════════╝")

        choice = input("INPUT: ")
        if choice == "1":
            reward_manager()
            return
        else:
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║   Invalid task number. Please enter   ║")
            print("║                1                      ║")
            print("╚═══════════════════════════════════════╝")

def claim_rewards():
    time.sleep(0.2)
    reward_file = f"rewards/{user_name}.txt"
    try:
        with open(reward_file, mode='r') as file:
            rewards = []
            for line in file:
                reward_name, reward_points = line.strip().split(',')
                rewards.append((reward_name, int(reward_points)))
        if len(rewards) == 0:
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║        No reward available yet.       ║")
            print("╚═══════════════════════════════════════╝")
            reward_manager()
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║          Available Rewards:           ║")
        for i, reward in enumerate(rewards, start=1):
            reward_name, reward_points = reward
            time.sleep(0.18)
            print(f"{i}. {reward_name} - {reward_points} points")
        print("╚═══════════════════════════════════════╝")
        total_points = calculate_total_points()
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print(f"     Total Points: {total_points}        ")
        print("╚═══════════════════════════════════════╝")
        if total_points > 0:
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║   Enter the number of the reward you  ║")
            print("║   want to redeem (or 'q' to quit):    ║")
            print("╚═══════════════════════════════════════╝")
            choice = input("INPUT: ")
            if choice.isdigit():
                choice = int(choice) - 1
                if 0 <= choice < len(rewards):
                    asked_reward_name, reward_points = rewards[choice]
                    if total_points >= reward_points:
                        time.sleep(0.18)
                        print("╔═══════════════════════════════════════╗")
                        print("║      Congratulations! You redeemed    ║")
                        print(f"║  the reward: {asked_reward_name}      ║")
                        print("╚═══════════════════════════════════════╝")

                        deduct_points(reward_points)
                        del rewards[choice]
                        with open(reward_file, mode='w') as file:
                            for reward in rewards:
                                reward_name, reward_points = reward
                                file.write(f"{reward_name},{reward_points}\n")
                        reward_manager()
                    else:
                        time.sleep(0.18)
                        print("╔═══════════════════════════════════════╗")
                        print("║ You don't have enough points to redeem║")
                        print("║             this reward.              ║")
                        print("╚═══════════════════════════════════════╝")
                        reward_manager()
                else:
                    time.sleep(0.18)
                    print("╔═══════════════════════════════════════╗")
                    print("║         Invalid reward number.        ║")
                    print("╚═══════════════════════════════════════╝")

                    claim_rewards()
            elif choice.lower() == 'q':
                reward_manager()
            else:
                time.sleep(0.18)
                print("╔═══════════════════════════════════════╗")
                print("║   Invalid input. Please enter a valid ║")
                print("║      reward number or 'q' to quit.    ║")
                print("╚═══════════════════════════════════════╝")

                claim_rewards()
        else:
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║  You don't have any points to redeem  ║")
            print("║               rewards.                ║")
            print("╚═══════════════════════════════════════╝")

            reward_manager()
    except FileNotFoundError:
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║       No rewards available yet.       ║")
        print("╚═══════════════════════════════════════╝")
        reward_manager()
        


def calculate_total_points():
    cur.execute(f"SELECT points FROM points WHERE username = '{user_name}'")
    total_points = int(cur.fetchone()[0])
    if total_points == None:
        return 0
    else:
        return total_points

def deduct_points(points):
    cur.execute(f"UPDATE points SET points = points - {points} where username = '{user_name}'")
    con.commit()

def view_performances():
    time.sleep(0.2)
    cur.execute(f"SELECT Status, COUNT(*) as Count FROM {user_name} GROUP BY Status")
    rows = cur.fetchall()
    statuses = [row[0] for row in rows]
    counts = [row[1] for row in rows]

    plt.bar(statuses, counts)
    plt.xlabel('Task Status')
    plt.ylabel('Count')
    plt.title('Task Performances')
    plt.show()

def view_completed_tasks():
    time.sleep(0.2)
    cur.execute(f"SELECT Tasks, Due_date, Points, Status FROM {user_name} WHERE Status = 'Complete' ORDER BY Due_date")
    rows = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    time.sleep(0.18)
    print(tabulate(rows, headers=columns, tablefmt='double_grid'))
    while True:
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║Would you like to go back to the menu? ║")
        print("║               (1 - yes):              ║")
        print("╚═══════════════════════════════════════╝")

        choice = input("INPUT: ")
        if choice == "1":
            status()
            return
        else:
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║   Invalid task number. Please enter   ║")
            print("║                 1                     ║")
            print("╚═══════════════════════════════════════╝")

def delete_all_tasks():
    time.sleep(0.2)
    print("╔═══════════════════════════════════════╗")
    print("║   Are you sure you want to delete     ║")
    print("║             all tasks?                ║")
    print("║          (1. Yes, 2. No)              ║")
    print("╚═══════════════════════════════════════╝")
    choice = input("INPUT:")
    if choice == "1":
        cur.execute(f"DELETE FROM {user_name}")
        con.commit()
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║     All tasks deleted successfully.   ║")
        print("╚═══════════════════════════════════════╝")
        task_manager()
    elif choice == "2":
        task_manager()
    else:
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║   Invalid task number. Please enter   ║")
        print("║               1 or 2                  ║")
        print("╚═══════════════════════════════════════╝")
        delete_all_tasks()

def edit_reward():
    time.sleep(0.2)
    reward_file = f"rewards/{user_name}.txt"
    try:
        with open(reward_file, 'r') as file:
            rewards = []
            for line in file:
                reward_name, reward_points = line.strip().split(',')
                rewards.append((reward_name, int(reward_points)))

        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║            Current Rewards:           ║")
        for i, reward in enumerate(rewards, start=1):
            reward_name, reward_points = reward
            print(f"   {i}. {reward_name} - {reward_points} points")
        print("╚═══════════════════════════════════════╝")
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║   Enter the number of the reward you  ║")
        print("║   want to edit (or 'q' to quit):      ║")
        print("╚═══════════════════════════════════════╝")
        choice = input("INPUT: ")
        if choice.isdigit():
            choice = int(choice) - 1
            if 0 <= choice < len(rewards):
                time.sleep(0.18)
                print("╔═══════════════════════════════════════╗")
                print("║       Enter the new reward name:      ║")
                print("╚═══════════════════════════════════════╝")
                new_reward_name = input("INPUT: ")
                time.sleep(0.18)
                print("╔═══════════════════════════════════════╗")
                print("║       Enter the new reward points:    ║")
                print("╚═══════════════════════════════════════╝")
                new_reward_points = input("INPUT: ")
                
                rewards[choice] = (new_reward_name, int(new_reward_points))
                with open(reward_file, 'w') as file:
                    for reward in rewards:
                        reward_name, reward_points = reward
                        file.write(f"{reward_name},{reward_points}\n")

                time.sleep(0.18)
                print("╔═══════════════════════════════════════╗")
                print("║       Reward edited successfully.     ║")
                print("╚═══════════════════════════════════════╝")
            else:
                time.sleep(0.18)
                print("╔═══════════════════════════════════════╗")
                print("║         Invalid reward number.        ║")
                print("╚═══════════════════════════════════════╝")

        elif choice.lower() == 'q':
            parent_menu()
        else:
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║   Invalid input. Please enter a valid ║")
            print("║      reward number or 'q' to quit.    ║")
            print("╚═══════════════════════════════════════╝")
            view_rewards()
    except FileNotFoundError:
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║         File does not exist.          ║")
        print("╚═══════════════════════════════════════╝")
        time.sleep(0.18)
        parent_menu()

def delete_reward():
    time.sleep(0.2)
    reward_file = f"rewards/{user_name}.txt"
    try:
        with open(reward_file, 'r') as file:
            rewards = []
            for line in file:
                rewards.append(line.strip())

        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║           Current Rewards:            ║")
        print("╚═══════════════════════════════════════╝")
        for i, reward in enumerate(rewards, start=1):
            print(f"{i}. {reward}")
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║   Enter the number of the reward you  ║")
        print("║   want to edit (or 'q' to quit):      ║")
        print("╚═══════════════════════════════════════╝")

        choice = input("INPUT: ")
        if choice.isdigit():
            choice = int(choice) - 1
            if 0 <= choice < len(rewards):
                deleted_reward = rewards.pop(choice)

                with open(reward_file, 'w') as file:
                    for reward in rewards:
                        file.write(f"{reward}\n")

                time.sleep(0.18)
                print("╔═══════════════════════════════════════╗")
                print(f"║      Reward '{deleted_reward}'        ║")
                print("║         deleted successfully.         ║")
                print("╚═══════════════════════════════════════╝")
                parent_menu()
            else:
                time.sleep(0.18)
                print("╔═══════════════════════════════════════╗")
                print("║         Invalid reward number.        ║")
                print("╚═══════════════════════════════════════╝")
                view_rewards()
        elif choice.lower() == 'q':
            parent_menu()
        else:
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║   Invalid input. Please enter a valid ║")
            print("║      reward number or 'q' to quit.    ║")
            print("╚═══════════════════════════════════════╝")
            view_rewards()
    except FileNotFoundError:
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║         File does not exist.          ║")
        print("╚═══════════════════════════════════════╝")
        time.sleep(0.18)
        parent_menu()

def delete_all_rewards():
    time.sleep(0.2)
    reward_file = f"rewards/{user_name}.txt"
    try:
        with open(reward_file, 'w') as file:
            file.write("")
        print("╔═══════════════════════════════════════╗")
        print("║   All rewards deleted successfully.   ║")
        print("╚═══════════════════════════════════════╝")
        time.sleep(0.18)
        parent_menu()
    except FileNotFoundError:
        print("╔═══════════════════════════════════════╗")
        print("║         File does not exist.          ║")
        print("╚═══════════════════════════════════════╝")
        time.sleep(0.18)
        parent_menu()

def view_overdue():
    update_overdue_tasks()
    time.sleep(0.2)
    cur.execute(f"SELECT Tasks, Due_date, Points, Status FROM {user_name} WHERE Status = 'Overdue' ORDER BY Due_date")
    rows = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    time.sleep(0.18)
    print(tabulate(rows, headers=columns, tablefmt='double_grid'))
    while True:
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║Would you like to go back to the menu? ║")
        print("║               (1 - yes):              ║")
        print("╚═══════════════════════════════════════╝")

        choice = input("INPUT: ")
        if choice == "1":
            task_manager()
            return
        else:
            time.sleep(0.18)
            print("╔═══════════════════════════════════════╗")
            print("║   Invalid task number. Please enter   ║")
            print("║                 1                     ║")
            print("╚═══════════════════════════════════════╝")

def update_overdue_tasks():
    cur.execute(f"SELECT COUNT(*) FROM {user_name}")
    count = cur.fetchone()[0]
    if count == 0:
        return
    cur.execute(f"SELECT Task_ID FROM {user_name} WHERE Due_date < '{current_date}' AND Status != 'Complete'")
    overdue_task_ids = cur.fetchall()
    if overdue_task_ids:
        for i in overdue_task_ids:
            a = i[0]
            if a % 10 != 0:
                cur.execute(f"UPDATE points SET points = points - 10 WHERE username = '{user_name}'")
                retask_id = random.randint(0,99999999)
                retask_id *= 10
                cur.execute(f"UPDATE {user_name} SET Task_ID = '{retask_id}' WHERE Task_ID = '{a}' ")
        
                
    cur.execute(f"UPDATE {user_name} SET Status = 'Overdue' WHERE Due_date < '{current_date}' AND Status != 'Complete'")
    con.commit()
    return

homepage()
