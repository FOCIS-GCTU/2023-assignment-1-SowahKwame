import os.path
import sys
from initials import main


def test_initials():
    try:
        exists = os.path.exists("initials.py")
        assert exists == True
    except:
        sys.exit()

    main()
