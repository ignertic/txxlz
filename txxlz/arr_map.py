import sys

import numpy as np

while True:
    arr=np.random.randn(50)
    sys.stdout.write(f"\t\t\r\r{arr}")
    sys.stdout.flush()
