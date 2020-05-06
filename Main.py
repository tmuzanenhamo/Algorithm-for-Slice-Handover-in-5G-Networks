import pandas as pd
import numpy as np
from Slices import Slices, Slice
from UseCases import UseCases
from Calculations import IntraCalculations, InterCalculations
import matplotlib.pyplot as plt
from pandas import ExcelWriter


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

    @staticmethod
    def plot_graphs(algorithm, df):

        print(f'Plotting {algorithm} Slice Handover Algorithms\n')
        fig1 = plt.figure(1)
        plt.plot(df['index'], df['eMBB_BP'])
        plt.xlabel('Call Arrival Rate')
        plt.ylabel('Call Blocking Probabilty')
        plt.title(f'eMBB Slice {algorithm} Slice')
        plt.savefig(f'{algorithm} Slice eMBB blocking Probability')
        fig2 = plt.figure(2)
        plt.plot(df['index'], df['eMBB_DP'])
        plt.xlabel('Call Arrival Rate')
        plt.ylabel('Call Dropping Probabilty')
        plt.title(f'eMBB Slice {algorithm} Slice')
        plt.savefig(f'{algorithm} Slice eMBB dropping Probability')
        fig2 = plt.figure(3)
        plt.plot(df['index'], df['mMTC'])
        plt.xlabel('Call Arrival Rate')
        plt.ylabel('Call Blocking Probabilty')
        plt.title(f'mMTC Slice {algorithm} Slice')
        plt.savefig(f'{algorithm} Slice mMTC blocking Probability')
        fig2 = plt.figure(4)
        plt.plot(df['index'], df['uRLLC_BP'])
        plt.xlabel('Call Arrival Rate')
        plt.ylabel('Call Blocking Probabilty')
        plt.title(f'uRLLC Slice {algorithm} Slice')
        plt.savefig(f'{algorithm} Slice uRLLC blocking Probability')
        fig2 = plt.figure(5)
        plt.plot(df['index'], df['uRLLC_DP'])
        plt.xlabel('Call Arrival Rate')
        plt.ylabel('Call Dropping Probabilty Intra Slice')
        plt.title(f'uRLLC Slice {algorithm} Slice')
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
            print('Simulating Intra Slice handover\n')
            calc = IntraCalculations()
            algorithm = 'Intra'
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
                    print('******************************************************************************\n')
                    self.data_dict.update({key: probabilities[1]})
            data_set = pd.DataFrame(self.data_dict, index=np.arange(.5, 5.5, .5))
            dropping_data = pd.DataFrame(self.dropping_dict, index=np.arange(.5, 5.5, .5))
            df = pd.merge(data_set.reset_index(), dropping_data.reset_index(), on='index', suffixes=('_BP', '_DP'))
            writer = ExcelWriter(f'{algorithm}_blocking_probabilities.xlsx')
            writer2 = ExcelWriter(f'{algorithm}_dropping_probabilities.xlsx')
            writer3 = ExcelWriter('Intra_Slice_Probabilities.xlsx')
            data_set.to_excel(writer, sheet_name='Sheet1')
            dropping_data.to_excel(writer2, sheet_name='Sheet1')
            df.to_excel(writer, sheet_name='Sheet1')
            writer.save()
            writer2.save()
            writer3.save()
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
            data_set2 = pd.DataFrame(self.data2_dict, index=np.arange(.5, 5.5, .5))
            dropping2_data = pd.DataFrame(self.dropping2_dict, index=np.arange(.5, 5.5, .5))
            df2 = pd.merge(data_set2.reset_index(), dropping2_data.reset_index(), on='index', suffixes=('_BP', '_DP'))
            inter_writter = ExcelWriter('Inter_Slice_Probabilities.xlsx')
            writer = ExcelWriter(f'{algorithm}_blocking_probabilities.xlsx')
            writer2 = ExcelWriter(f'{algorithm}_dropping_probabilities.xlsx')
            df2.to_excel(inter_writter, sheet_name='Sheet1')
            data_set2.to_excel(writer, sheet_name='Sheet1')
            dropping2_data.to_excel(writer2, sheet_name='Sheet1')
            writer.save()
            writer2.save()
            inter_writter.save()
            self.plot_graphs(algorithm, df2)

        # # fig = plt.figure()
        # for data in [data_set.reset_index()]:
        #     plt.plot(data['index'], data['mMTC'])
        # plt.show()
        # # Merge the Data Frames
        # df = pd.merge(data_set.reset_index(), dropping_data.reset_index(), on='index', suffixes=('_BP', '_DP'))
        # print(df)
        # writer = ExcelWriter('Intra_Slice_Probabilities.xlsx')
        # df.to_excel(writer, sheet_name='Sheet1')
        # writer.save()
        #
        # # fig = plt.figure()
        # # ax1 = fig.add_subplot(311)
        # # ax2 = fig.add_subplot(322)
        # # ax3 = fig.add_subplot(313)
        # # df.plot(kind='line', x='index', y='uRLLC_BP', ax=ax1)
        # # df.plot(kind='line', x='index', y='uRLLC_DP', ax=ax2)
        # # df.plot(kind='line', x='index', y='uRLLC_BP', ax=ax3)
        # # df.plot(kind='line', x='index', y='uRLLC_DP', ax=ax3)
        # #
        # # # df.plot(kind='line', x='index', color='red', y='uRLLC_DP', ax=ax)
        # # plt.show()
        #
        # df2 = pd.merge(data_set2.reset_index(), dropping2_data.reset_index(), on='index', suffixes=('_BP', '_DP'))
        # print(df2)
        # inter_writter = ExcelWriter('Inter_Slice_Probabilities.xlsx')
        # df2.to_excel(inter_writter, sheet_name='Sheet1')
        # inter_writter.save()

        # fig2 = plt.figure()
        # ay1 = fig2.add_subplot(311)
        # ay2 = fig2.add_subplot(321)
        # ay3 = fig2.add_subplot(313)
        #
        # df2.plot(kind='line', x='index', y='uRLLC_BP', ax=ay1)
        # df2.plot(kind='line', x='index', y='uRLLC_DP', ax=ay2)
        # df2.plot(kind='line', x='index', y='uRLLC_BP', ax=ay3)
        # df2.plot(kind='line', x='index', y='uRLLC_DP', ax=ay3)
        #
        # plt.show()

        # fig1 = plt.figure(1)
        # plt.plot(df['index'], df['eMBB_BP'])
        # plt.xlabel('Call Arrival Rate')
        # plt.ylabel('Call Blocking Probabilty')
        # plt.title('eMBB Slice Intra Slice')
        # plt.savefig('Intra Slice eMBB blocking Probability')
        # fig2 = plt.figure(2)
        # plt.plot(df['index'], df['eMBB_DP'])
        # plt.xlabel('Call Arrival Rate')
        # plt.ylabel('Call Dropping Probabilty')
        # plt.title('eMBB Slice Intra Slice')
        # plt.savefig('Intra Slice eMBB dropping Probability')
        # fig2 = plt.figure(3)
        # plt.plot(df['index'], df['mMTC'])
        # plt.xlabel('Call Arrival Rate')
        # plt.ylabel('Call Blocking Probabilty')
        # plt.title('mMTC Slice Intra Slice')
        # plt.savefig('Intra Slice mMTC blocking Probability')
        # fig2 = plt.figure(4)
        # plt.plot(df['index'], df['uRLLC_BP'])
        # plt.xlabel('Call Arrival Rate')
        # plt.ylabel('Call Blocking Probabilty')
        # plt.title('uRLLC Slice Intra Slice')
        # plt.savefig('Intra Slice uRLLC blocking Probability')
        # fig2 = plt.figure(5)
        # plt.plot(df['index'], df['uRLLC_DP'])
        # plt.xlabel('Call Arrival Rate')
        # plt.ylabel('Call Dropping Probabilty Intra Slice')
        # plt.title('uRLLC Slice Intra Slice')
        # plt.savefig('Intra Slice uRLLC dropping Probability')
        # # Inter Slice
        #
        # fig1 = plt.figure(6)
        # plt.plot(df2['index'], df2['eMBB_BP'])
        # plt.xlabel('Call Arrival Rate')
        # plt.ylabel('Call Blocking Probabilty')
        # plt.title('eMBB Slice Inter Slice')
        # plt.savefig('Inter Slice eMBB blocking Probability')
        # fig2 = plt.figure(7)
        # plt.plot(df2['index'], df2['eMBB_DP'])
        # plt.xlabel('Call Arrival Rate')
        # plt.ylabel('Call Dropping Probabilty')
        # plt.title('eMBB Slice Inter Slice')
        # plt.savefig('Inter Slice eMBB dropping Probability')
        # fig2 = plt.figure(8)
        # plt.plot(df2['index'], df2['mMTC'])
        # plt.xlabel('Call Arrival Rate')
        # plt.ylabel('Call Blocking Probabilty')
        # plt.title('mMTC Slice Inter Slice')
        # plt.savefig('Inter Slice mMTC blocking Probability')
        # fig2 = plt.figure(9)
        # plt.plot(df2['index'], df2['uRLLC_BP'])
        # plt.xlabel('Call Arrival Rate')
        # plt.ylabel('Call Blocking Probabilty')
        # plt.title('uRLLC Slice Inter Slice ')
        # plt.savefig('Inter Slice uRLLC blocking Probability')
        # fig2 = plt.figure(10)
        # plt.plot(df2['index'], df2['uRLLC_DP'])
        # plt.xlabel('Call Arrival Rate')
        # plt.ylabel('Call Dropping Probabilty')
        # plt.title('uRLLC Slice Inter Slice')
        # plt.savefig('Inter Slice uRLLC dropping Probability')
        #
        # fig2 = plt.figure(11)
        # plt.plot(df['index'], df['eMBB_BP'], df['eMBB_DP'])
        # plt.xlabel('Call Arrival Rate')
        # plt.ylabel('Call Blocking/Dropping Probabilty')
        # plt.title('eMBB Slice Intra Slice')
        # plt.savefig('Intra Slice eMBB Comparison')
        #
        # fig2 = plt.figure(12)
        # plt.plot(df['index'], df['uRLLC_BP'], df['uRLLC_DP'])
        # plt.xlabel('Call Arrival Rate')
        # plt.ylabel('Call Blocking/Dropping Probabilty')
        # plt.title('uRLLC Slice Intra Slice')
        # plt.savefig('Intra Slice uRLLC Comparison')
        #
        # fig2 = plt.figure(13)
        # plt.plot(df['index'], df2['eMBB_BP'], df2['eMBB_DP'])
        # plt.xlabel('Call Arrival Rate')
        # plt.ylabel('Call Blocking/Dropping Probabilty')
        # plt.title('eMBB Slice Inter Slice')
        # plt.savefig('Inter Slice eMBB Comparison')
        #
        # fig2 = plt.figure(14)
        # plt.plot(df['index'], df2['uRLLC_BP'], df2['uRLLC_DP'])
        # plt.xlabel('Call Arrival Rate')
        # plt.ylabel('Call Blocking/Dropping Probabilty')
        # plt.title('uRLLC Slice Inter Slice')
        # plt.savefig('Inter Slice uRLLC Comparison')
        #
        # plt.show()


simulation = Simulator()

simulation.execute
