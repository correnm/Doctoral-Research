#!/usr/bin/env python
# -*- coding: utf-8 -*-
#title           :menu.py
#description     :This program displays an interactive menu on CLI
#author          :
#date            :
#version         :0.1
#usage           :python menu.py
#notes           :
#python_version  :2.7.6  
#=======================================================================

# Import the modules needed to run the script.
import sys, os

# Main definition - constants
menu_actions  = {}  

# =======================
#     MENUS FUNCTIONS
# =======================

# Main menu
def main_menu():
    os.system('cls') # for windows
    
    print "Welcome, Entity Disambiguation\n"
    print "Please choose the menu you want to start:"
    print "1. New Search"
    print "2. Name Selection (Training Set)"
    print "3. Process All (Training Set)"
    print "\n0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)

    return

# Execute menu
def exec_menu(choice):
    os.system('cls')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print "Invalid selection, please try again.\n"
            menu_actions['main_menu']()
    return

# Menu 1: start a new search
def menu1():
    print "New Search Menu \n"
    print "1. Enter a name"
    print "9. Back"
    print "0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return


# Menu 2: Select a name
def menu2():
    print "Name Selection Menu\n"
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

# Back to main menu
def back():
    menu_actions['main_menu']()

# Exit program
def exit():
    sys.exit()

# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': menu1,
    '2': menu2,
    '9': back,
    '0': exit,
}

# =======================
#      MAIN PROGRAM
# =======================
if __name__ =="__main__":
	# launch main menu
	main_menu()
