# Example file for Advanced Python by Joe Marini
# Using special module names


# __name__ is the name of the module
print("Module name: ", __name__)

# __file__ contains the path to the file from which the module was loaded
print("File name: ", __file__)

# __package__ indicates the package that the module belongs to.
print("Package name: ", __package__)