# -*- coding: cp1252 -*-
'''
@Author Corren McCoy, 2015
@Purpose Entity Resolution of known community with online social network
'''

__author__ = 'cmccoy@cs.odu.edu (Corren McCoy)'

# Python libraries
import codecs
import collections
import csv
import datetime
import logging
import os
import sys
import time

# my libraries
import alternativeNames
import nicknames
import selectOneTraining
import searchGoogleCSE

# Main definition - constants
menu_actions  = {}
dataset_pk = None

# ======================================================================
#     MENUS FUNCTIONS
# ======================================================================

# Main menu
def main_menu():
    #os.system('cls') # for windows
    
    print "# ====================================="
    print "# MAIN MENUS FUNCTIONS"
    print "# ====================================="
    print "1. Pre-processing"
    print "2. Training mode"
    print "3. Test mode"
    print "\n0. Quit"
    choice = raw_input("Enter an option >>  ")
    exec_menu(choice)
    return


# Menu 1: pre-processing
def menu1():
    print "# ====================================="
    print "# PRE_PROCESSING FUNCTIONS"
    print "# ====================================="
    print "11. Load nicknames from default file"
    print " 9. Back to main menu"
    print " \n0. Quit"
    choice = raw_input("Enter an option >>  ")
    exec_menu(choice)
    return

# Menu 2: Select a name
def menu2():
    print "# ====================================="
    print "# TRAINING MODE FUNCTIONS"
    print "# ====================================="
    print "21: Process one name from training set"
    print "22: Process all training set"
    print "23: Enter a new name"
    print "24: Start matching"
    print " 9. Back to main menu"
    print "\n0. Quit" 
    choice = raw_input("Enter an option >>  ")
    exec_menu(choice)
    return

def menu3():
    print "# ====================================="
    print "# TEST FUNCTIONS"
    print "# ====================================="
    print "31: Process one name from test set"
    print "32: Process all training set"
    print "33: Add a new name"    
    print " 9. Back to main menu"
    print "\n0. Quit" 
    choice = raw_input("Enter an option >>  ")
    exec_menu(choice)
    return    

# Execute menu
def exec_menu(choice):
    #os.system('cls')
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

# =====================================
#    MODULES CALLED FROM MENUS
# =====================================

def loadNicknames():
    status= nicknames.load()
    # return to previous menu
    back()

def processOne():
  dataset_pk = selectOneTraining.showPeople()
  if dataset_pk == '':
    print "Invalid selection, please try again.\n"
    menu_actions['main_menu']()
  else:
    startMatching(dataset_pk)
    #  All done. Return to the main menu
    menu_actions['main_menu']()    

def startMatching(dataset_pk):
  logging.info('\n=====================================================================')
  logging.info('Started processing at: %s', time.ctime() )
  
  # Construct alternative names using nickname variations
  alternativeNames.load(dataset_pk)
            
  # Google Search for public profiles on LinkedIn
  searchGoogleCSE.linkedin(dataset_pk)

  logging.info('\n=====================================================================')
  logging.info('Completed processing at: %s', time.ctime() )  


  
# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition - each submenu will use the numbering scheme of the parent menu
# This is necessary so we have a unique menu name
menu_actions = {
    'main_menu': main_menu,
    '1':  menu1,
    '11': loadNicknames,
    '2':  menu2,
    '21': processOne,
    '24': startMatching,
    '3':  menu3,
    '9':  back,
    '0':  exit,
}

def help():
  """
  Algorithm Entity Disambiguation between social networks: LinkedIn and Twitter
  1. Load a pre-defined set of nicknames

  """
  print help.__doc__

##################################################################################             
#  This is main procedure in this package
##################################################################################
def main():
    # This program displays an interactive menu on CLI
    main_menu()     
       
if __name__ == '__main__':
    # Configure the logging for all modules
    now = datetime.datetime.today().strftime("%Y%m%d-%H%M%S")
    logging.basicConfig(
        filename='./logs/access-log.'+ now, 
        filemode='w',
        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
        datefmt='%H:%M:%S',
        level=logging.DEBUG)
    
    main()
       
 
