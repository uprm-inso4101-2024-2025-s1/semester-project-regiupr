import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'database'))

import database.courses.courses as cc

cc.main()