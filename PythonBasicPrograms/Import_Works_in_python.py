import pandas as pd
print(pd.__version__)

# Now lets see from where it will be the module
import sys
print(sys.path)

import File2
print(File2.a)
File2.printjoke("Adarsh Vajpayee!!")
