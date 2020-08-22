import pandas as pd
import numpy as np
from Slices import Slices, Slice
from UseCases import UseCases
from Calculations import IntraCalculations, InterCalculations
import matplotlib.pyplot as plt
from pandas import ExcelWriter
import time


class Simulator:
    capacity = 30
    new_thresh = 0.5 * capacity
    handoff_thresh = capacity
    mMTC_thresh = 0.5 * capacity
    mMTC_cap = 0.5 * capacity
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

    @staticmethod
    def plot_graphs(algorithm, df):

        print(f'Plotting {algorithm} Slice Handover Algorithms\n')
        fig1 = plt.figure(1)
        plt.plot(df['index'], df['eMBB_BP'])
        plt.xlabel('Call Arrival Rate')
        plt.ylabel('Call Blocking Probabilty')
        plt.title(f'Effect of Arrival Rate on New Call Blocking Probability')
        plt.grid()
        plt.savefig(f'{algorithm} Slice eMBB blocking Probability')
        fig2 = plt.figure(2)
        plt.plot(df['index'], df['eMBB_DP'])
        plt.xlabel('Call Arrival Rate')
        plt.ylabel('Call Dropping Probabilty')
        plt.title(f'Effect of Arrival Rate on Handoff Call Dropping Probability')
        plt.grid()
        plt.savefig(f'{algorithm} Slice eMBB dropping Probability')
        fig2 = plt.figure(3)
        plt.plot(df['index'], df['mMTC'])
        plt.xlabel('Call Arrival Rate')
        plt.ylabel('Call Blocking Probabilty')
        plt.title(f'Effect of Arrival Rate on New Call Blocking Probability')
        plt.grid()
        plt.savefig(f'{algorithm} Slice mMTC blocking Probability')
        fig2 = plt.figure(4)
        plt.plot(df['index'], df['uRLLC_BP'])
        plt.xlabel('Call Arrival Rate')
        plt.ylabel('Call Blocking Probabilty')
        plt.title(f'Effect of Arrival Rate on New Call Blocking Probability')
        plt.grid()
        plt.savefig(f'{algorithm} Slice uRLLC blocking Probability')
        fig2 = plt.figure(5)
        plt.plot(df['index'], df['uRLLC_DP'])
        plt.xlabel('Call Arrival Rate')
        plt.ylabel('Call Dropping Probabilty Intra Slice')
        plt.title(f'Effect of Arrival Rate on Handoff Call Dropping Probability')
        plt.grid()
        plt.savefig(f'{algorithm} Slice uRLLC dropping Probability')
        plt.show()

    @property
    def execute(self):
        slice_type = self.initialise_slices

        # Choose Algorithm to Simulate.
        print('Choose the type of handover you want to simulate: ')
        print('1. Intra Slice handover')
        print('2. Inter Slice handover')

        choice = eval(input("Enter your choice: "))
        if choice == 1:
            start = time.time()
            print('Simulating Intra Slice handover\n')
            # Create the IntraSlice object
            calc = IntraCalculations()
            algorithm = 'Intra'
            for key in slice_type:
                if key == 'eMBB' or key == 'uRLLC':
                    # pass slice parameters
                    probabilities = calc.calculations(key, slice_type[key])
                    # display probabilities
                    print(f'The blocking probability for {probabilities[0]} slice is: {probabilities[1]} \n')
                    print(f'The dropping probability for {probabilities[0]} slice is: {probabilities[2]} \n')
                    print('******************************************************************************\n')
                    # update data dictionaries
                    self.data_dict.update({key: probabilities[1]})
                    self.dropping_dict.update({key: probabilities[2]})
                else:
                    probabilities = calc.calculations(key, slice_type[key])
                    print(f'The blocking probability for {probabilities[0]} slice is: {probabilities[1]} \n')
                    print('******************************************************************************\n')
                    self.data_dict.update({key: probabilities[1]})
            # pass blocking data into a pandas data frame

            data_set = pd.DataFrame(self.data_dict, index=np.arange(3, 8, .5))
            # pass dropping data into a pandas data frame
            dropping_data = pd.DataFrame(self.dropping_dict, index=np.arange(3, 8, .5))
            # merge data frames
            df = pd.merge(data_set.reset_index(), dropping_data.reset_index(), on='index', suffixes=('_BP', '_DP'))
            # save the data as excel files
            writer = ExcelWriter(f'{algorithm}_blocking_probabilities.xlsx')
            writer2 = ExcelWriter(f'{algorithm}_dropping_probabilities.xlsx')
            writer3 = ExcelWriter('Effect_of_call_Arrival_rate_on_Intra_Slice_Probabilities.xlsx')
            data_set.to_excel(writer, sheet_name='Sheet1')
            dropping_data.to_excel(writer2, sheet_name='Sheet1')
            df.to_excel(writer3, sheet_name='Sheet1')
            writer.save()
            writer2.save()
            writer3.save()
            stop = time.time()
            print(f'The time elapsed is: {stop-start}')
            self.plot_graphs(algorithm, df)

        else:
            print('Simulating Inter Slice handover\n')
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
                    print('******************************************************************************\n')
                    self.data2_dict.update({key: probabilities[1]})
            data_set2 = pd.DataFrame(self.data2_dict, index=np.arange(3, 8, .5))
            dropping2_data = pd.DataFrame(self.dropping2_dict, index=np.arange(3, 8, .5))
            df2 = pd.merge(data_set2.reset_index(), dropping2_data.reset_index(), on='index', suffixes=('_BP', '_DP'))
            inter_writter = ExcelWriter('Effect_of_call_Arrival_rate_on_Inter_Slice_Probabilities.xlsx')
            writer = ExcelWriter(f'{algorithm}_blocking_probabilities.xlsx')
            writer2 = ExcelWriter(f'{algorithm}_dropping_probabilities.xlsx')
            df2.to_excel(inter_writter, sheet_name='Sheet1')
            data_set2.to_excel(writer, sheet_name='Sheet1')
            dropping2_data.to_excel(writer2, sheet_name='Sheet1')
            writer.save()
            writer2.save()
            inter_writter.save()
            self.plot_graphs(algorithm, df2)


simulation = Simulator()

simulation.execute
