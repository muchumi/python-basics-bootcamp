import os
# Returns the current working directory
os.getcwd()

# Changing the current working directory
os.chdir('/server/accesslogs.txt')

# Running the command mkdir in the system shell
os.system('mkdir today')

# Printing a list of all os module functions
print(dir(os))

# Prints an extensive manual page created from the os module's docstrings
print(help(os))

