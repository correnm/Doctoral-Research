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

# Python libraries
import sys, os

# my libraries
import nicknames

# Main definition - constants
menu_actions  = {}  

# ======================================================================
#     MENUS FUNCTIONS
# ======================================================================

# Main menu
def main_menu():
    os.system('cls') # for windows
    
    print "# ====================================="
    print "# MAIN MENUS FUNCTIONS"
    print "# ====================================="
    print "Choose an option:"
    print "1. Pre-processing"
    print "2. Training mode"
    print "3. Test mode"
    print "\n0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return


# Menu 1: pre-processing
def menu1():
    print "# ====================================="
    print "# PRE_PROCESSING FUNCTIONS"
    print "# ====================================="
    print "11. Load nicknames from default file"
    print " 9. Back"
    print " 0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def menu11():
    status= nicknames.load()

# Menu 2: Select a name
def menu2():
    print "Name Selection Menu\n"
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def menu3():
    print "# ====================================="
    print "# TBD FUNCTIONS"
    print "# ====================================="
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
    '11': menu11,
    '2': menu2,
    '3': menu3,
    '9': back,
    '0': exit,
}

# =======================
#      MAIN PROGRAM
# =======================
if __name__ =="__main__":
	# launch main menu
	main_menu()
