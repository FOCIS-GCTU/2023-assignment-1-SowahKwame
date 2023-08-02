import os.path
import sys
from initials import main

def initials_test():
  try:
    exists=os.path.exists("initials.py")
    assert exists == true
  except:
    sys.exit()

  
  main()

