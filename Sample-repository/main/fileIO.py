"""
fileIO.py
Use scipy.io to demonstrate file input/output.
"""

import scipy.io as scio
import numpy as np

# First we need some data to write
x = np.random.rand(3, 4, 5, 6) # A 4d array of shape (3,4,5,6)
y = np.random.rand(4, 5, 6)  # a 3d array of shape (4, 5, 6)

# We'll primarily use the .mat format. It's a lossless binary popular in scientific computing that can
# store objects up to 2Gb with default parameters. A file can store many 2GB objects.
# This is Matlab Version 5.0 (current is 7.3). Higher versioning is supported by scipy but
# all major languages support v5, not all support 7.3
# .mat files use a dictionary style format

dict_to_store = {'data': x, 'labels': y}
disp(dict_to_store)
scio.savemat(file_name='filename.mat', mdict=dict_to_store)
new_dict = scio.readmat(file_name='filename.mat')
disp(new_dict)
