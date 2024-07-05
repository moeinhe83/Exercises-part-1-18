# Practice_18

# Library
from os import system as sys
from termcolor2 import colored
from pyfiglet import figlet_format

# Clear Terminal
sys('cls')

# Intro
print(colored(figlet_format("Exercises Part 1"), color='cyan'))
print(colored('=====================================================================', color='red'))
print(colored('Question Number ===> 18', color='blue'))
print(colored('// Be Sure To Read The README File To See The Question //', color='blue'))
print('                                            ')

number = {'a':15, 'b':25, 'c':35, 'd':45} 

print(sum(number.values()))

# Finish
# Create By Moein Heshmati
