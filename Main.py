import pandas as pd
import numpy as np
from Slices import Slices, Slice
from UseCases import UseCases
from Calculations import Calculations
import matplotlib.pyplot as plt


class Simulator:
    capacity = 30
    new_thresh = 10
    handoff_thresh = 30
    mMTC_thresh = 15
    mMTC_cap = 15
    data_dict = {}

    def __init__(self):
        print('Handover Algorithm initialised')

    @property
    def initialise_slices(self):
        """Function that initialises the slices"""
        slices = ['eMBB', 'uRLLC', 'mMTC']
        for slice_name in slices:
            if slice_name is 'eMBB' or slice_name is 'uRLLC':
                initialise = Slices(slice_name, self.capacity, self.new_thresh, self.handoff_thresh).slice

            else:
                initialise = Slice(slice_name, self.mMTC_cap, self.mMTC_thresh).slice

        return initialise

    @staticmethod
    def allocates_bbu(slice_name):

        useCase = UseCases()
        bbu = useCase.allocate_bbu(slice_name)
        return bbu

    @property
    def execute(self):
        slice_type = self.initialise_slices
        calc = Calculations()
        for key in slice_type:
            if key == 'eMBB' or key == 'uRLLC':
                probabilities = calc.calculations(key, slice_type[key])
                print('The blocking probability for {} slice is: {} \n'.format(probabilities[0], probabilities[1]))
                print('The dropping probability for {} slice is: {} \n'.format(probabilities[0], probabilities[2]))
                print('******************************************************************************************')
                self.data_dict.update({key: probabilities[1]})
            else:
                probabilities = calc.calculations(key, slice_type[key])
                print('The blocking probability for {} slice is: {} \n'.format(probabilities[0], probabilities[1]))
                self.data_dict.update({key: probabilities[1]})
        data_set = pd.DataFrame(self.data_dict, index=np.arange(1.0, 6, 0.5))
        print(data_set)
        data_set.reset_index().plot(x='index', y=['uRLLC'])
        # plt.axis([0, 5, 0, 1])
        plt.show()


simulation = Simulator()

simulation.execute
