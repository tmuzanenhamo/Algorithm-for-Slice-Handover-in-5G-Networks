import pandas as pd
import numpy as np
from Slices import Slices, Slice
from UseCases import UseCases
from Calculations import IntraCalculations, InterCalculations
import matplotlib.pyplot as plt
from pandas import ExcelWriter
from datetime import datetime


class Simulator:
    capacity = 30
    new_thresh = 15
    handoff_thresh = 30
    mMTC_thresh = 15
    mMTC_cap = 15
    data_dict = {}
    data2_dict = {}
    dropping_dict = {}
    dropping2_dict = {}

    def __init__(self):
        print('Handover Algorithm initialised')

    @property
    def initialise_slices(self):
        """Function that initialises the slices"""
        slices = ['eMBB', 'uRLLC', 'mMTC']
        for slice_name in slices:
            if slice_name is 'eMBB' or slice_name is 'uRLLC':
                # create Slices object
                initialise = Slices(slice_name, self.capacity, self.new_thresh, self.handoff_thresh).slice

            else:
                # create a Slice object
                initialise = Slice(slice_name, self.mMTC_cap, self.mMTC_thresh).slice

        # return a dict with slice name as the key and an array of parameters as values
        return initialise

    @staticmethod
    def allocates_bbu(slice_name):

        useCase = UseCases()
        bbu = useCase.allocate_bbu(slice_name)
        return bbu

    @property
    def execute(self):
        slice_type = self.initialise_slices

        print('Choose the type of handover you want to simulate: ')
        print('1. Intra Slice handover')
        print('2. Inter Slice handover')

        choice = 1
        while choice < 3:

            if choice == 1:
                algorithm = 'Intra'
                print('Implementing Intra Slice handover\n')
                calc = IntraCalculations()
                for key in slice_type:
                    if key == 'eMBB' or key == 'uRLLC':
                        probabilities = calc.calculations(key, slice_type[key])
                        print(f'The blocking probability for {probabilities[0]} slice is: {probabilities[1]} \n')
                        print(f'The dropping probability for {probabilities[0]} slice is: {probabilities[2]} \n')
                        print('******************************************************************************\n')
                        self.data_dict.update({key: probabilities[1]})
                        self.dropping_dict.update({key: probabilities[2]})
                    else:
                        probabilities = calc.calculations(key, slice_type[key])
                        print(f'The blocking probability for {probabilities[0]} slice is: {probabilities[1]} \n')
                        self.data_dict.update({key: probabilities[1]})
                data_set = pd.DataFrame(self.data_dict, index=np.arange(1.0, 6, 0.5))
                dropping_data = pd.DataFrame(self.dropping_dict, index=np.arange(1.0, 6, 0.5))
                writer = ExcelWriter(f'{algorithm}_blocking_probabilities.xlsx')
                writer2 = ExcelWriter(f'{algorithm}_dropping_probabilities.xlsx')
                data_set.to_excel(writer, sheet_name='Sheet1')
                dropping_data.to_excel(writer2, sheet_name='Sheet1')
                writer.save()
                writer2.save()

            else:
                print('Implementing Inter Slice handover\n')
                calc = InterCalculations()
                algorithm = 'Inter'
                for key in slice_type:
                    if key == 'eMBB' or key == 'uRLLC':
                        probabilities = calc.calculations(key, slice_type[key])
                        print(f'The blocking probability for {probabilities[0]} slice is: {probabilities[1]} \n')
                        print(f'The dropping probability for {probabilities[0]} slice is: {probabilities[2]} \n')
                        print('******************************************************************************\n')
                        self.data2_dict.update({key: probabilities[1]})
                        self.dropping2_dict.update({key: probabilities[2]})
                    else:
                        probabilities = calc.calculations(key, slice_type[key])
                        print(f'The blocking probability for {probabilities[0]} slice is: {probabilities[1]} \n')
                        self.data2_dict.update({key: probabilities[1]})
                data_set2 = pd.DataFrame(self.data2_dict, index=np.arange(1.0, 6, 0.5))
                dropping2_data = pd.DataFrame(self.dropping2_dict, index=np.arange(1.0, 6, 0.5))
                writer = ExcelWriter(f'{algorithm}_blocking_probabilities.xlsx')
                writer2 = ExcelWriter(f'{algorithm}_dropping_probabilities.xlsx')
                data_set2.to_excel(writer, sheet_name='Sheet1')
                dropping2_data.to_excel(writer2,sheet_name='Sheet1')
                writer.save()
                writer2.save()
            choice += 1

        # fig = plt.figure()
        for data in [data_set.reset_index(), data_set2.reset_index()]:
            plt.plot(data['index'], data['eMBB'])
        # #     plt.legend(['Intra'], ['Inter'])
        plt.show()

        # ax = data_set.plot()
        # m = ax.get_lines()
        # data_set2.plot(ax=ax, linestyle='--')
        # plt.show()

        #
        # for dropping in [dropping_data.reset_index(), dropping2_data.reset_index() ]:
        #     plt.plot(dropping['index'], dropping['eMBB'])
        # plt.show()
        # print(data_set['eMBB'])
        # print(data_set2['eMBB'])
        # print(dropping_data>dropping2_data)
        # print(dropping2_data>dropping_data)
        # print(data_set['mMTC'])
        #
        # print(data_set2['mMTC'])
        print(data_set['eMBB'])
        print(data_set2['eMBB']>data_set['eMBB'])

        # print(data_set2)
        # data_set
        # data_set.plot.bar()
        # ax= plt.gca()
        # data_set.reset_index()
        # m = data_set2['mMTC']
        # data_set.plot(y=['mMTC',m], use_index=True, kind='bar')
        # plt.show()

        # df = pd.merge(data_set.reset_index(), data_set2.reset_index(), on='index', suffixes=('_intra', '_inter'))
        # print(df)
        # # df.plot.bar(x='index')
        # # data_set.plot(y=['mMTC'], use_index=True)
        #
        # ax = plt.axes(projection='3d')
        # ax.plot3D(df['index'],df['eMBB_intra'],df['index'],'red')
        # plt.show()
        # fig = plt.figure()
        # ax = plt.axes(projection="3d")
        # ax.bar3d(df['eMBB_intra'],1,1,df['index'],df['index'],df['index'] )
        # plt.show()


simulation = Simulator()

simulation.execute
