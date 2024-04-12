import os

CUR_DIR =os.path.dirname(os.path.abspath(__file__)) #__file__: will return the part of actual script
#abspath :to retrieve absolute path
DATA_DIR =os.path.join(CUR_DIR, "data") #DATA_DIR: variable used to save our list created with our class
print(DATA_DIR)