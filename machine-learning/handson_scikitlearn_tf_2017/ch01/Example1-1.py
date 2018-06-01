import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn

# load the data
x = pd.read_csv("oecd_bli_2015.csv", error_bad_lines=False)
print(x.head(10))
