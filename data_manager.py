import numpy as np
import scipy.io
import pandas as pd
import os
import time

class DataManager(object):
    """
    class to read and store simulation results
    before use, please create a direction under current file path './data'
    and must have a file 'init_location.xlsx' which contain the position of each entities
    """
    def __init__(self, store_list = ['beamforming_matrix', 'reflecting_coefficient', 'UAV_state', 'user_capacity'],file_path = './data', store_path = './data/storage'):
        # 1 init location data
        self.store_list = store_list
        self.init_data_file = file_path + '/init_location.xlsx'
        self.time_stemp = time.strftime('/%Y-%m-%d %H_%M_%S',time.localtime(time.time()))
        self.store_path = store_path + self.time_stemp 
        os.makedirs(self.store_path) 
        # self.writer = pd.ExcelWriter(self.store_path + '/simulation_result.xlsx', engine='openpyxl')  # pylint: disable=abstract-class-instantiated 
        self.simulation_result_dic = {}
        self.init_format()

    def save_file(self, episode_cnt = 0):
        # when ended, auto save to .mat file
        scipy.io.savemat(self.store_path + '/simulation_result_ep_' + str(episode_cnt) + '.mat', {'result_' + str(episode_cnt):self.simulation_result_dic})
        self.simulation_result_dic = {}
        self.init_format()

    def save_meta_data(self, meta_dic):
        """
        save system and agent information
        """
        scipy.io.savemat(self.store_path + '/meta_data.mat', {'meta_data': meta_dic})
        
    def init_format(self):
        """
        used only one time in env.py
        """
        for store_item in self.store_list:
            self.simulation_result_dic.update({store_item:[]})

    def read_init_location(self, entity_type = 'user', index = 0):
        if entity_type == 'user' or 'attacker' or 'RIS' or 'RIS_norm_vec' or 'UAV':
            return np.array([\
            pd.read_excel(self.init_data_file, sheet_name=entity_type)['x'][index],\
            pd.read_excel(self.init_data_file, sheet_name=entity_type)['y'][index],\
            pd.read_excel(self.init_data_file, sheet_name=entity_type)['z'][index]])
        else:
            return None
    
    def store_data(self, row_data, value_name):
        """
        docstring
        """
        self.simulation_result_dic[value_name].append(row_data)