import os


newpath = "data/"

for i in range(54, 100):
  #add folders for each count
  os.makedirs(newpath + str(i))
