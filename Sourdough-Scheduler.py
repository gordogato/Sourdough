############### SOURDOUGH RECIPE SCRIPT #################

############### INGREDIENTS #############################
##
##    Levain (100% Hydration)
##        35g Sourdough Starter
##        35g Whole Wheat Flour
##        35g All Purpose Flour
##        70g Room Temperature Water
##        #######################################
##        Add to Quart Mason Jar and Cover Loosly
##        Store @77F/25C
##
##    Autolyse Dough (85% Hydration)
##        810g Bread Flour
##        90g Whole Wheat Flour
##        580g Room Temperature Water
##        #######################################
##        Mix in Large Bowl and Cover Loosly
##        Store @77F/25C
##
##    Salt Mixture
##        100g Room Temperature Water
##        18g Fine Sea Salt
##
#######################################################

import datetime
from datetime import timedelta

#Print Ingredients
print("\n############### INGREDIENTS #############################\n"\
      "\nLevain (100% Hydration)"\
        "\n\t35g Sourdough Starter"\
        "\n\t35g Whole Wheat Flour"\
        "\n\t35g All Purpose Flour"\
        "\n\t70g Room Temperature Water"\
        "\n\t#######################################"\
        "\n\tAdd to Quart Mason Jar and Cover Loosly"\
        "\n\tStore @77F/25C\n"\
    "\nAutolyse Dough (85% Hydration)"\
        "\n\t810g Bread Flour"\
        "\n\t90g Whole Wheat Flour"\
        "\n\t580g Room Temperature Water"\
        "\n\t#######################################"\
        "\n\tMix in Large Bowl and Cover Loosly"\
        "\n\tStore @77F/25C\n"\
    "\nSalt Mixture"\
        "\n\t100g Room Temperature Water"\
        "\n\t18g Fine Sea Salt"\
"\n")


#Get Start Time from User
start_time = datetime.datetime.strptime(raw_input("Start time? HHMM : "), "%H%M")

#Calculate Time for Sourdough Recipe Steps
def calc_time(hour,minute):
    fulltime = datetime.datetime.strftime(start_time + timedelta(hours=hour,minutes=minute),"%H:%M")
    return fulltime

#Print Time Schedule

print("\nStarted Levain @ ")
print(calc_time(0,0))

print("\nAutolysed Dough @ ")
print(calc_time(4,0))

print("\nMix Levain into Dough using Rubaud Method @ ")
print(calc_time(5,0))

print("\nAdd Salt Mixture & Slap/Fold @ ")
print(calc_time(5,20))

print("\nFold #1 @ ")
print(calc_time(5,35))

print("\nFold #2 @ ")
print(calc_time(5,50))

print("\nFold #3 @ ")
print(calc_time(6,05))

print("\nFold #4 @ ")
print(calc_time(6,35))

print("\nFold #5 @ ")
print(calc_time(7,05))

print("\nFold #6 @ ")
print(calc_time(8,35))

print("\nSplit & Shape @ ")
print(calc_time(9,05))

print("\nCold Proof for 12 Hours Minimum @ ")
print(calc_time(9,25))

print("\nEarliest Bake @ ")
print(calc_time(21,25))


