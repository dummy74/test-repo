import sys
import os
from glob import glob

MODULES = glob(os.path.join(os.path.dirname(__file__),'**','*.py'),recursive=True)
