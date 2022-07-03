import numpy as np
import pandas as pd
import copy as cp
import time
from os import listdir
from os.path import isfile, join
from os import walk
import h5py
import heapq

import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import cm
import matplotlib
from scipy.stats import pearsonr
from matplotlib.colors import ListedColormap
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

from scipy.stats import pearsonr

from PCAfold import preprocess
from PCAfold import reduction
from PCAfold import analysis
from PCAfold.styles import *

updated_DNS_SLF_labels = ['$T$',
 'O$_2$',
 'C$_2$H$_5$',
 'A1',
 'O',
 'H$_2$',
 'CH$_3$',
 'CO$_2$',
 'C$_2$H$_4$',
 'N-C$_3$H$_7$',
 'T-CH$_2$',
 'HO$_2$',
 'CH',
 'C$_2$H',
 'A-C$_3$H$_5$',
 'C$_5$H$_5$',
 'A-C$_3$H$_4$',
 'CH$_2$O',
 'C$_5$H$_6$',
 'A$_1$CHO',
 'A$_1$C$_2$H',
 'C$_5$H$_{10}$',
 'C$_7$H$_{15}$',
 'HCCO',
 'A$_1$C$_2$Hs',
 'P-C$_3$H$_4$',
 'C$_5$H$_{11}$',
 'OH',
 'CO',
 'A1-',
 'C$_2$H$_3$',
 'C$_3$H$_6$',
 'H',
 'A2-',
 'A$_1$CH$_2$',
 'CH$_4$',
 'H$_2$O',
 'C$_4$H$_8$',
 'C$_2$H$_6$',
 'A$_1$CH$_3$',
 'A2',
 'C$_3$H$_3$',
 'HCO',
 'N-C$_7$H$_{16}$',
 'A$_1$C$_2$H$_2$',
 'S-CH$_2$',
 'C$_2$H$_2$']