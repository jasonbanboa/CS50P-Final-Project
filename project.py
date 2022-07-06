import keyboard
from pyautogui import click
from pynput.mouse import Listener
import time
import csv
import re
import sys

""" Store the mouse clicks in this List"""
DATA = []

""" The main function """
def main():
    total_clicks = get_number_of_clicks()
    print("please start clicking")
    for _ in range(total_clicks):
        store_data()
    if question(input("Would you like to store your cursor positions in a csv file? (yes/no): ").lower().strip()):
        csv_file = get_csv()
        if write_header(csv_file):
            if write_data_in_csv(DATA, csv_file):
                print(f"Successfully logged in {csv_file}")
    if ask(input("Would you like to start the program? (yes/no): ").lower().strip()):
        time.sleep(1)
        print("If you wish to STOP press ESC")
        for _ in range(number_of_iterations()):
            if action(DATA):
                continue
            else:
                sys.exit("Error")
    else:
        sys,exit(0)
    print("Finished!")
    
 
"""  Gets users input: int number of clicks to store in autoclicker"""
def get_number_of_clicks(): 
    while True:
        try:
            number_of_times = int(input("How many clicks are you going to record: "))
            if number_of_times <= 0:
                raise ValueError
                    
        except ValueError:
            time.sleep(0.5)
            print("Error only takes in posstive numbers")
            time.sleep(0.5)
            pass
    
        else:
            return number_of_times
        
        
""" asks if user would like to store their clicks in a csv file"""
def question(user_input):
    if user_input == "yes":
        return True

    else:
        return False
    

""" gets users input The name of csv file to store cursor positions """
def get_csv():
    print("-" * 50)
    while True:
        try:
            csv_location = input("Name of the csv file to store mouse clicks: ").strip()
            if re.search("^[\w]+(\.csv)$", csv_location):
                print(f"Storing in {csv_location}")
            else:
                raise NameError
            
        except NameError:
            print("ERROR: csv should be nammed with only '_', numbers, alphabets and '.csv' at the end ie: (example.csv)")
            pass
        else:
            return csv_location


""" writes the header in the given csv file """
def write_header(csv_name):
    with open(csv_name, "w", newline="") as file:
        writer = csv.writer(file)
        header = ["x", "y"]
        writer.writerow(header)
        return True


""" gets the data and stores it in to the users choice of csv file """
def write_data_in_csv(data_list, file_name):
    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        for i in range(len(data_list)):
            writer.writerow(data_list[i])
    return True
            
            
""" appends and returns the users cursor postion when mouse is clicked to a list """
def write_cursor_location(x, y, _, pressed):
    if pressed:
            DATA.append([x, y])
            print("successfully logged")
    else:
        return False
    return DATA
            

""" listnes to the users mouse clicks """
def store_data():
    with Listener(on_click=write_cursor_location) as listener:
        listener.join()
        

""" asks if user would like to start the program """
def ask(user_input):
    if user_input == "yes":
        return True
    else:
        return False
    
    
""" asks user for the number of iteration """
def number_of_iterations():
    while True:
        try:
            iterations = int(input("for how many repetitions would you like? "))
            if iterations <= 0:
                raise ValueError
        except ValueError:
            print("Only takes positive numbers as input")
            pass
        else:
            return iterations


"""  clicks on the exact location of the list """
def action(list):
    for i in range(len(list)):
        for _ in range(1):
            x = list[i][0]
            y = list[i][1]
            click(x, y)
            break_iteration()
    return True


""" stoped the function when ESC key is pressed """ 
def break_iteration():
    if keyboard.is_pressed('esc'):
        sys.exit("Iteration Stopped")


if  __name__ == "__main__":
    main()
    
    