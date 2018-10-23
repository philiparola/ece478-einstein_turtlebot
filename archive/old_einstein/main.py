"""
Example program of using command line arguments with Einstein class

Written by William Harrington for ECE478 HW1
"""
from Einstein import Einstein # grab the einstein class
import argparse # library for parsing command line arguments
import random # library for random numbers

# initialize argument parser
parser = argparse.ArgumentParser()

# these lines are here to show that we can make his personality traits customizable on the command line
#parser.add_argument('-m', action = 'store', dest = 'meanness', required = True, help = 'Meanness is a personality quality of Einstein, required for init')
#parser.add_argument('-n', action = 'store', dest = 'niceness', required = True, help = 'Niceness is a personality quality of Einstein, required for init')

# argument for getting mood of Einstein
parser.add_argument('-mood', action = 'store_true', help = 'gets einsteins mood')

# argument for getting personality traits (niceness, meanness) of Einstein
parser.add_argument('--personality', action = 'store_true', help = 'gets personality traits of Einstein')

# argument for asserting action that Einstein will react to
# should be integer between 1-10
parser.add_argument('-a', action = 'store', dest = 'Action', required = False, help = 'optional argument for action to einstein to react to')

# argument for getting robot to perform command
parser.add_argument('-c', type = int, action = 'store', dest = 'Command', required = False, help = 'optional argument for getting robot to perform command')

# parse the arguments
arguments = parser.parse_args()

# again this line just shows we can customize the personality traits from the command line
#Einstein = Einstein(arguments.niceness, arguments.meanness)

# for example sake and testing purposes, I'm just gonna make it random for now
Einstein = Einstein(random.randint(1,10), random.randint(1,10))

if(arguments.Command):
    print arguments.Command
    print Einstein.command(arguments.Command)

# mood argument present
if(arguments.mood):
    # show his mood
    print Einstein.mood()

# personality argument present
if(arguments.personality):
    # show personality traits
    print Einstein.personality()

# action argument present
if(arguments.Action):
    # show reaction of Einstein
    print Einstein.reaction(arguments.Action)
