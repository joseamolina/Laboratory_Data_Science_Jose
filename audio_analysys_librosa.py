import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from bokeh.plotting import figure
from bokeh.io import output_file, show
fig = figure()
output_file(filename="empty_figure.html")
show(fig)
