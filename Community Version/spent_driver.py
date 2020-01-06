#spent_driver.py use [<profile_name>]
usage = '''

Expense Tracker CLI.

Usage:
  spent_driver.py init
  spent_driver.py view [<view_profile>] [<view_category>] 
  spent_driver.py <amount> <category> [<profile_name>] [<message>] 

'''

from docopt import docopt
from spent import *
from tabulate import tabulate

args = docopt(usage)
#print(args)

if args['init']:
    init()
    print("User Profile Created")

if args['view']:
    category = args['<view_category>']
    profile = args['<view_profile>']
    if profile:
        amount, results = view(category, profile)

    else:
        amount, results = view(category)
    print("Total expense: ", amount)
    print(tabulate(results))

if args['<amount>']:
    try:
        amount = float(args['<amount>'])
        if(args['<profile_name>']):
            log(amount, args['<category>'],args['<message>'],args['<profile_name>'])
        else:
            log(amount, args['<category>'],args['<message>'])


    except:
        print(usage)
