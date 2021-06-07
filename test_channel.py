from entity import *
from channel import *

import numpy as np 
UAV = UAV(np.array([0.0001,0.001,25]))
RIS = RIS(np.array([25,0.001,25]),np.array([-1, 0.0001, 0.0001]))
test_channel = mmWave_channel(UAV,RIS,frequncy=28e9)