############### SOURDOUGH RECIPE SCRIPT #################
## Python3
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
################ BAKE #################################
##
##    Preheat Oven & Dutch Oven for 1 Hour @500F/260C
##    Bake Covered for 20 Minutes
##    Uncover & Lower Temperature to 450F/232C
##    Continue Baking for ~20 Minutes
##
#######################################################

import datetime
from datetime import timedelta

#Print Ingredients
print("")
print("############### INGREDIENTS #############################\n"\
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
        "\n\t18g Fine Sea Salt\n"\
    "\nBaking Instructions"\
        "\n\tPreheat Oven & Dutch Oven for 1 Hour @500F/260C"\
        "\n\tBake Covered for 20 Minutes"\
        "\n\tUncover & Lower Temperature to 450F/232C"\
        "\n\tContinue Baking for ~20 Minutes\n"\
)


#Get Start Time from User
start_time = datetime.datetime.strptime(input("Start time? HHMM : "), "%H%M")

#Calculate Time for Sourdough Recipe Steps
def calc_time(hour,minute):
    fulltime = datetime.datetime.strftime(start_time + timedelta(hours=hour,minutes=minute),"%H:%M")
    return fulltime

#Print Time Schedule

print("\nStarted Levain @ "+calc_time(0,0))

print("\nAutolyse Dough @ "+calc_time(4,0))

print("\nMix Levain into Dough using Rubaud Method @ "+calc_time(5,0))

print("\nAdd Salt Mixture & Slap/Fold @ "+calc_time(5,20))

print("\nFold #1 @ "+calc_time(5,35))

print("\nFold #2 @ "+calc_time(5,50))

print("\nFold #3 @ "+calc_time(6,5))

print("\nFold #4 @ "+calc_time(6,35))

print("\nFold #5 @ "+calc_time(7,5))

print("\nFold #6 @ "+calc_time(7,35))

print("\nSplit & Shape @ "+calc_time(9,5))

print("\nCold Proof for 12 Hours Minimum @ "+calc_time(9,25))

print("\nEarliest Bake @ "+calc_time(21,25))
