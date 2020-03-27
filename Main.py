import pandas as pd
import numpy as np
from Slices import Slices, Slice
from UseCases import UseCases
from Calculations import IntraCalculations, InterCalculations
import matplotlib.pyplot as plt


class Simulator:
    capacity = 30
    new_thresh = 10
    handoff_thresh = 30
    mMTC_thresh = 15
    mMTC_cap = 15
    data_dict = {}
    data2_dict = {}

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
        # choice = eval(input('Enter handover type to simulate: \n'))
        choice = 1
        while choice < 3:

            if choice == 1:
                print('Implementing Intra Slice handover\n')
                calc = IntraCalculations()
                for key in slice_type:
                    if key == 'eMBB' or key == 'uRLLC':
                        probabilities = calc.calculations(key, slice_type[key])
                        print(f'The blocking probability for {probabilities[0]} slice is: {probabilities[1]} \n')
                        print(f'The dropping probability for {probabilities[0]} slice is: {probabilities[2]} \n')
                        print('******************************************************************************\n')
                        self.data_dict.update({key: probabilities[1]})
                    else:
                        probabilities = calc.calculations(key, slice_type[key])
                        print(f'The blocking probability for {probabilities[0]} slice is: {probabilities[1]} \n')
                        self.data_dict.update({key: probabilities[1]})
                data_set = pd.DataFrame(self.data_dict, index=np.arange(1.0, 6, 0.5))
                print(data_set)
                # data_set.reset_index().plot(x='index', y=['uRLLC'])
                # plt.axis([0, 5, 0, 1])
                # plt.show()
            else:
                print('Implementing Inter Slice handover\n')
                calc = InterCalculations()
                for key in slice_type:
                    if key == 'eMBB' or key == 'uRLLC':
                        probabilities = calc.calculations(key, slice_type[key])
                        print(f'The blocking probability for {probabilities[0]} slice is: {probabilities[1]} \n')
                        print(f'The dropping probability for {probabilities[0]} slice is: {probabilities[2]} \n')
                        print('******************************************************************************\n')
                        self.data2_dict.update({key: probabilities[1]})
                    else:
                        probabilities = calc.calculations(key, slice_type[key])
                        print(f'The blocking probability for {probabilities[0]} slice is: {probabilities[1]} \n')
                        self.data2_dict.update({key: probabilities[1]})
                data_set2 = pd.DataFrame(self.data2_dict, index=np.arange(1.0, 6, 0.5))
            choice += 1

        fig = plt.figure()
        for data in [data_set.reset_index(), data_set2.reset_index()]:
            plt.plot(data['index'], data['mMTC'])
        plt.show()


simulation = Simulator()

simulation.execute
