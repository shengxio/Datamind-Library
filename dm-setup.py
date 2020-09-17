# this main script is to create a genenral run file for datamind runtime environment
# following code block will import all contents for the programming.
try:
  import sklearn
  import pandas as pd
  import numpy as np
  import sweetviz as sv
  import seaborn as sns
except ImportError:
  userChoice = input("Found missing package, auto install? (yes/no):\n")
  if userChoice.lower()=="yes":
    ! pip install sklearn
    ! pip install pandas
    ! pip install numpy
    ! pip install sweetviz
    ! pip install seaborn
   elif userChoice.lower() =="no":
    print("exiting Datamind initial setup....")
   else:
    print("don't know what I have read. terminating.....BANG!")
except Exception as error:
  print(error,False)
  print(error.__class__.__name__ + ": " + error.message)
