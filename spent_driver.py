from tabulate import tabulate
from spent import *
from docopt import docopt
usage = '''

Expense Tracker CLI.

Usage:
  spent_driver.py init
  spent_driver.py view [<view_category>]
  spent_driver.py <amount> <category> [<message>]

'''


args = docopt(usage)

if args['init']:
    init()
    print("User Profile Created")

if args['view']:
    category = args['<view_category>']
    amount, results = view(category)
    print("Total expense: ", amount)
    print(tabulate(results))

if args['<amount>']:
    try:
        amount = float(args['<amount>'])
        log(amount, args['<category>'], args['<message>'])
    except BaseException:
        print(usage)
