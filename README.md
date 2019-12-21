# expense-tracker
A simple API for an expense tracking application along with a multiple interfaces to use it.

Watch the video here: https://youtu.be/sYBDJ15dNVc


A demonstration of programming with a database and creating an abstracted API, along with various interfaces which use it.

## Requirements
- Python
- docopt
- tabulate
- sqlite3 for desktop (helpful, but not necessary)

To install a python package use the following command:

```sh
pip install <package_name>
```

Alternatively, to install all the packages at once, use this command:
```sh
pip install -r requirements.txt
```
## Using the CLI
You can use the binary directly, in `bin/`. Add the folder to your `PATH` and then just perform an initialization to use it.

If you're using the python file,
```sh
$ python spent_driver.py init
```

If you're using the binary,
```sh
$ spent init
```
*The following examples are for using the binary. If you're using the python file, modify accordingly.*

Logging an expense:
```sh
$ spent <amount> <category> [<profile>] [<message>]
```
`message` is optional.
`profile` is optional.

If profile is not specified the default user profile is "home".

For example,
```sh
$ spent 50 food "snacks in the evening"
$ spent 100 transport
```

Viewing your expenditure for all profiles:
```sh
spent_driver.py view
```
For example,
```sh
$ spent_driver.py view
```

The first command shows you your total expenditure, along with a list of all transactions you've made.

Viewing your expenditure for a particular user profile:
```sh
$ spent_driver.py view <user_profile> <category>
```
For example,
```sh
$ spent_driver.py view work transport
```
The second one is more streamlined, and gives you the details for the specified user profile and category.

*An example output*
```sh
$ spent_driver.py view
Total expense:  5200
----  ----  ---------  ----------------------  --------------------------
work   100  food                               2019-12-21 06:51:22.323043
home   200  cinema                             2019-12-21 06:51:41.695574
work   300  taxi                               2019-12-21 06:52:04.985462
home   100  groceries                          2019-12-21 06:52:18.811124
work  1500  travel     air tickets to go home  2019-12-21 06:53:04.812908
home  3000  rent       security deposit        2019-12-21 06:53:46.783464
----  ----  ---------  ----------------------  --------------------------
```

# Contributions

Want to contribute? Great! 

There's a list of features which can be added under Issues. If you have something totally new, even better! 

