import shutil

# For daily file and directory management tasks, the shutil module provides a higher level interface that is easier to use

source = "C:/Users/ADMIN/Documents/source"

destination = "C:/Users/ADMIN/Documents/destination"

# Copying the contents of source to destination
try:
    shutil.copy(source, destination)
    print("File copied successfully")
# If source and destination are the same
except shutil.SameFileError:
    print("Source and Destination represents the same file")
# If there is any permission issue
except PermissionError:
    print("Permission Denied")
# For other errors
except:
    print("Error occurred while copying file")
