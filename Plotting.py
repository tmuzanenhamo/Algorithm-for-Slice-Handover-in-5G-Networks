import pandas as pd
import matplotlib.pyplot as plt


def plotting():
    """Function used to plot graphs"""
    columns = ['eMBB_BP', 'eMBB_DP', 'uRLLC_BP', 'uRLLC_DP', 'mMTC_BP']  # Columns in the dataFrame

    # Load the excel files into data frames.

    df = pd.read_excel(r'C:\Users\tmuza\Desktop\Final Year\Handover\Results\effect of bbu\IntraSlice\effect of bbu on '
                       r'IntraSlice.xlsx')

    # Plot individual graphs

    for data in [df.reset_index()]:
        for i in range(5):
            plt.figure(i)
            plt.plot(data['index'], data[columns[i]])
            plt.grid()
            plt.xlabel('Basic Bandwidth Unit (BBU)')
            plt.grid()
            if columns[i][5:] == 'BP' or columns[i][5:] == '_BP':
                prob = 'Call Blocking Probability'
                plt.ylabel(f'{prob}')
                plt.title(f'Effect of Increasing BBU on {columns[i][0:5]} {prob}')
                figname = f'Effect of BBU on {columns[i]} {prob}'
                plt.savefig(f'Results/effect of bbu/IntraSlice/{figname}')
            elif columns[i][5:] == 'DP' or columns[i][5:] == '_DP':
                prob = 'Call Dropping Probability'
                plt.ylabel(f'{prob}')
                plt.title(f'Effect of Increasing BBU on {columns[i][0:5]} {prob}')
                figname = f'Effect of BBU on {columns[i]} {prob}'
                plt.savefig(f'Results/effect of bbu/IntraSlice/{figname}')
    plt.close('all')

    # Plot eMBB BP Vs DP on the same axis

    axx = plt.gca()
    df.plot(kind='line', x='index', y='eMBB_BP', ax=axx)
    df.plot(kind='line', x='index', y='eMBB_DP', ax=axx)
    plt.xlabel('Basic Bandwidth Unit (BBU)')
    plt.ylabel('Call Blocking/Dropping Probability')
    plt.title('Effect of Increasing BBU on IntraSlice Call Blocking/Dropping Probability')
    figname = 'eMBB BP vs DP'
    plt.grid()
    plt.savefig(f'Results/effect of bbu/IntraSlice/{figname}')
    plt.close('all')

    # Plot uRLLC BP vs DP on the same axis

    axx1 = plt.gca()
    df.plot(kind='line', x='index', y='uRLLC_BP', ax=axx1)
    df.plot(kind='line', x='index', y='uRLLC_DP', ax=axx1)
    plt.xlabel('Basic Bandwidth Unit (BBU)')
    plt.ylabel('Call Blocking/Dropping Probability')
    plt.title('Effect of Increasing BBU on IntraSlice Call Blocking/Dropping Probability')
    figname = 'uRLLC BP vs DP'
    plt.grid()
    plt.savefig(f'Results/effect of bbu/IntraSlice/{figname}')
    plt.close('all')

    # Plot all graphs on the same axis

    ax = plt.gca()
    df.plot(kind='line', x='index', y='eMBB_BP', ax=ax)
    df.plot(kind='line', x='index', y='eMBB_DP', ax=ax)
    df.plot(kind='line', x='index', y='uRLLC_DP', ax=ax)
    df.plot(kind='line', x='index', y='uRLLC_BP', ax=ax)
    df.plot(kind='line', x='index', y='mMTC_BP', ax=ax)
    plt.xlabel('Basic Bandwidth Unit (BBU)')
    plt.ylabel('Call Blocking/Dropping Probability')
    plt.title('Effect of Increasing BBU on IntraSlice Call Blocking/Dropping Probability')
    figname = 'All graphs'
    plt.grid()
    plt.savefig(f'Results/effect of bbu/IntraSlice/{figname}')
    plt.close('all')

    # Load the data into a dataFrame
    df2 = pd.read_excel(r'C:\Users\tmuza\Desktop\Final Year\Handover\Results\effect of bbu\InterSlice\effect of bbu on '
                        r'InterSlice.xlsx')

    # Plot individual graphs

    for data in [df2.reset_index()]:
        for i in range(5):
            plt.figure(i)
            plt.plot(data['index'], data[columns[i]])
            plt.xlabel('Basic Bandwidth Unit (BBU)')
            plt.grid()
            if columns[i][5:] == 'BP' or columns[i][5:] == '_BP':
                prob = 'Call Blocking Probability'
                plt.ylabel(f'{prob}')
                plt.title(f'Effect of Increasing BBU on {columns[i][0:5]} {prob}')
                figname = f'Effect of BBU on {columns[i]} {prob}'
                plt.savefig(f'Results/effect of bbu/InterSlice/{figname}')
            elif columns[i][5:] == 'DP' or columns[i][5:] == '_DP':
                prob = 'Call Dropping Probability'
                plt.ylabel(f'{prob}')
                plt.title(f'Effect of Increasing BBU on {columns[i][0:5]} {prob}')
                figname = f'Effect of BBU on {columns[i]} {prob}'
                plt.savefig(f'Results/effect of bbu/InterSlice/{figname}')
    plt.close('all')

    # Plot eMBB BP Vs DP on the same axis

    axx2 = plt.gca()
    df2.plot(kind='line', x='index', y='eMBB_BP', ax=axx2)
    df2.plot(kind='line', x='index', y='eMBB_DP', ax=axx2)
    plt.xlabel('Basic Bandwidth Unit (BBU)')
    plt.ylabel('Call Blocking/Dropping Probability')
    plt.title('Effect of Increasing BBU on InterSlice Call Blocking/Dropping Probability')
    figname = 'eMBB BP vs DP'
    plt.grid()
    plt.savefig(f'Results/effect of bbu/InterSlice/{figname}')
    plt.close('all')

    # Plot uRLLC BP vs DP on the same axis

    axx3 = plt.gca()
    df2.plot(kind='line', x='index', y='uRLLC_BP', ax=axx3)
    df2.plot(kind='line', x='index', y='uRLLC_DP', ax=axx3)
    plt.xlabel('Basic Bandwidth Unit (BBU)')
    plt.ylabel('Call Blocking/Dropping Probability')
    plt.title('Effect of Increasing BBU on InterSlice Call Blocking/Dropping Probability')
    figname = 'uRLLC BP vs DP'
    plt.grid()
    plt.savefig(f'Results/effect of bbu/InterSlice/{figname}')
    plt.close('all')

    # Plot all graphs on the same axis

    ax1 = plt.gca()
    df2.plot(kind='line', x='index', y='eMBB_BP', ax=ax1)
    df2.plot(kind='line', x='index', y='eMBB_DP', ax=ax1)
    df2.plot(kind='line', x='index', y='uRLLC_DP', ax=ax1)
    df2.plot(kind='line', x='index', y='uRLLC_BP', ax=ax1)
    df2.plot(kind='line', x='index', y='mMTC_BP', ax=ax1)
    plt.xlabel('Basic Bandwidth Unit (BBU)')
    plt.ylabel('Call Blocking/Dropping Probability')
    plt.title('Effect of Increasing BBU on InterSlice Call Blocking/Dropping Probability')
    figname = 'All graphs'
    plt.grid()
    plt.savefig(f'Results/effect of bbu/InterSlice/{figname}')
    plt.close('all')

    # Load the data into a dataFrame
    df3 = pd.read_excel(r'C:\Users\tmuza\Desktop\Final Year\Handover\Results\effect of capacity\Inter Slice\Effect of '
                        r'Capacity on InterSlice probabilities.xlsx')

    # Plot individual graphs

    for data in [df3.reset_index()]:
        for i in range(5):
            plt.figure(i)
            plt.plot(data['index'], data[columns[i]])
            plt.xlabel('Capacity')
            plt.grid()
            if columns[i][5:] == 'BP' or columns[i][5:] == '_BP':
                prob = 'Call Blocking Probability'
                plt.ylabel(f'{prob}')
                plt.title(f'Effect of Capacity on {columns[i][0:5]} {prob}')
                figname = f'Effect of Capacity on {columns[i]} {prob}'
                plt.savefig(f'Results/effect of capacity/Inter Slice/{figname}')
            elif columns[i][5:] == 'DP' or columns[i][5:] == '_DP':
                prob = 'Call Dropping Probability'
                plt.ylabel(f'{prob}')
                plt.title(f'Effect of Capacity on {columns[i][0:5]} {prob}')
                figname = f'Effect of Capacity on {columns[i]} {prob}'
                plt.savefig(f'Results/effect of capacity/Inter Slice/{figname}')

    plt.close('all')

    # Plot eMBB BP Vs DP on the same axis

    axx4 = plt.gca()
    df3.plot(kind='line', x='index', y='eMBB_BP', ax=axx4)
    df3.plot(kind='line', x='index', y='eMBB_DP', ax=axx4)
    plt.xlabel('Capacity')
    plt.ylabel('Call Blocking/Dropping Probability')
    plt.title('Effect of Increasing Capacity on InterSlice Call Blocking/Dropping Probability')
    figname = 'eMBB BP vs DP'
    plt.grid()
    plt.savefig(f'Results/effect of capacity/Inter Slice/{figname}')
    plt.close('all')

    # Plot uRLLC BP vs DP on the same axis

    axx5 = plt.gca()
    df3.plot(kind='line', x='index', y='uRLLC_BP', ax=axx5)
    df3.plot(kind='line', x='index', y='uRLLC_DP', ax=axx5)
    plt.xlabel('Capacity')
    plt.ylabel('Call Blocking/Dropping Probability')
    plt.title('Effect of Increasing Capacity on InterSlice Call Blocking/Dropping Probability')
    figname = 'uRLLC BP vs DP'
    plt.grid()
    plt.savefig(f'Results/effect of capacity/Inter Slice/{figname}')
    plt.close('all')

    # Plot all graphs on the same axis

    ax2 = plt.gca()
    df3.plot(kind='line', x='index', y='eMBB_BP', ax=ax2)
    df3.plot(kind='line', x='index', y='eMBB_DP', ax=ax2)
    df3.plot(kind='line', x='index', y='uRLLC_DP', ax=ax2)
    df3.plot(kind='line', x='index', y='uRLLC_BP', ax=ax2)
    df3.plot(kind='line', x='index', y='mMTC_BP', ax=ax2)
    plt.xlabel('Capacity')
    plt.ylabel('Call Blocking/Dropping Probability')
    plt.title('Effect of Increasing Capacity on Call Blocking/Dropping Probability')
    figname = 'All graphs'
    plt.grid()
    plt.savefig(f'Results\\effect of capacity\\Inter Slice\\{figname}')
    plt.close('all')

    df4 = pd.read_excel(r'C:\Users\tmuza\Desktop\Final Year\Handover\Results\effect of capacity\Intra Slice\Effect of '
                        r'Capacity on IntraSlice probabilities.xlsx')
    for data in [df4.reset_index()]:
        for i in range(5):
            plt.figure(i)
            plt.plot(data['index'], data[columns[i]])
            plt.xlabel('Capacity')
            plt.grid()
            if columns[i][5:] == 'BP' or columns[i][5:] == '_BP':
                prob = 'Call Blocking Probability'
                plt.ylabel(f'{prob}')
                plt.title(f'Effect of Capacity on {columns[i][0:5]} {prob}')
                figname = f'Effect of Capacity on {columns[i]} {prob}'
                plt.savefig(f'Results/effect of capacity/Intra Slice/{figname}')
            elif columns[i][5:] == 'DP' or columns[i][5:] == '_DP':
                prob = 'Call Dropping Probability'
                plt.ylabel(f'{prob}')
                plt.title(f'Effect of Capacity on {columns[i][0:5]} {prob}')
                figname = f'Effect of Capacity on {columns[i]} {prob}'
                plt.savefig(f'Results/effect of capacity/Intra Slice/{figname}')
    plt.close('all')

    # Plot eMBB BP Vs DP on the same axis

    axx6 = plt.gca()
    df4.plot(kind='line', x='index', y='eMBB_BP', ax=axx6)
    df4.plot(kind='line', x='index', y='eMBB_DP', ax=axx6)
    plt.xlabel('Capacity')
    plt.ylabel('Call Blocking/Dropping Probability')
    plt.title('Effect of Increasing Capacity on IntraSlice Call Blocking/Dropping Probability')
    figname = 'eMBB BP vs DP'
    plt.grid()
    plt.savefig(f'Results/effect of capacity/Intra Slice/{figname}')
    plt.close('all')

    # Plot uRLLC BP vs DP on the same axis

    axx7 = plt.gca()
    df4.plot(kind='line', x='index', y='uRLLC_BP', ax=axx7)
    df4.plot(kind='line', x='index', y='uRLLC_DP', ax=axx7)
    plt.xlabel('Capacity')
    plt.ylabel('Call Blocking/Dropping Probability')
    plt.title('Effect of Increasing Capacity on IntraSlice Call Blocking/Dropping Probability')
    figname = 'uRLLC BP vs DP'
    plt.grid()
    plt.savefig(f'Results/effect of capacity/Intra Slice/{figname}')
    plt.close('all')

    # Plot all graphs on the same axis

    ax3 = plt.gca()
    df4.plot(kind='line', x='index', y='eMBB_BP', ax=ax3)
    df4.plot(kind='line', x='index', y='eMBB_DP', ax=ax3)
    df4.plot(kind='line', x='index', y='uRLLC_DP', ax=ax3)
    df4.plot(kind='line', x='index', y='uRLLC_BP', ax=ax3)
    df4.plot(kind='line', x='index', y='mMTC_BP', ax=ax3)
    plt.xlabel('Capacity')
    plt.ylabel('Call Blocking/Dropping Probability')
    plt.title('Effect of Increasing Capacity on Call Blocking/Dropping Probability')
    figname = 'All graphs'
    plt.grid()
    plt.savefig(f'Results\\effect of capacity\\Intra Slice\\{figname}')
    plt.close('all')

    # Load the data into a dataFrame
    df5 = pd.read_excel(r'C:\Users\tmuza\Desktop\Final Year\Handover\Results\effect of threshold\Inter Slice\efffect '
                        r'of threshold on InterSlice.xlsx')

    # plot individual graphs

    for data in [df5.reset_index()]:
        for i in range(5):
            plt.figure(i)
            plt.plot(data['index'], data[columns[i]])
            plt.xlabel('Threshold')
            plt.grid()
            if columns[i][5:] == 'BP' or columns[i][5:] == '_BP':
                prob = 'Call Blocking Probability'
                plt.ylabel(f'{prob}')
                plt.title(f'Effect of Threshold on {columns[i][0:5]} {prob}')
                figname = f'Effect of Threshold on {columns[i]} {prob}'
                plt.savefig(f'Results/effect of threshold/Inter Slice/{figname}')
            elif columns[i][5:] == 'DP' or columns[i][5:] == '_DP':
                prob = 'Call Dropping Probability'
                plt.ylabel(f'{prob}')
                plt.title(f'Effect of Threshold on {columns[i][0:5]} {prob}')
                figname = f'Effect of Threshold on {columns[i]} {prob}'
                plt.savefig(f'Results/effect of threshold/Inter Slice/{figname}')
    plt.close('all')

    # Plot eMBB BP Vs DP on the same axis

    axx8 = plt.gca()
    df5.plot(kind='line', x='index', y='eMBB_BP', ax=axx8)
    df5.plot(kind='line', x='index', y='eMBB_DP', ax=axx8)
    plt.xlabel('Threshold')
    plt.ylabel('Call Blocking/Dropping Probability')
    plt.title('Effect of Increasing Threshold on InterSlice Call Blocking/Dropping Probability')
    figname = 'eMBB BP vs DP'
    plt.grid()
    plt.savefig(f'Results/effect of threshold/Inter Slice/{figname}')
    plt.close('all')

    # Plot uRLLC BP vs DP on the same axis

    axx9 = plt.gca()
    df5.plot(kind='line', x='index', y='uRLLC_BP', ax=axx9)
    df5.plot(kind='line', x='index', y='uRLLC_DP', ax=axx9)
    plt.xlabel('Threshold')
    plt.ylabel('Call Blocking/Dropping Probability')
    plt.title('Effect of Increasing Threshold on InterSlice Call Blocking/Dropping Probability')
    figname = 'uRLLC BP vs DP'
    plt.grid()
    plt.savefig(f'Results/effect of threshold/Inter Slice/{figname}')
    plt.close('all')

    # Plot all graphs on the same axis

    ax4 = plt.gca()
    df5.plot(kind='line', x='index', y='eMBB_BP', ax=ax4)
    df5.plot(kind='line', x='index', y='eMBB_DP', ax=ax4)
    df5.plot(kind='line', x='index', y='uRLLC_DP', ax=ax4)
    df5.plot(kind='line', x='index', y='uRLLC_BP', ax=ax4)
    df5.plot(kind='line', x='index', y='mMTC_BP', ax=ax4)
    plt.xlabel('Threshold')
    plt.ylabel('Call Blocking/Dropping Probability')
    plt.title('Effect of Increasing Threshold on Call Blocking/Dropping Probability')
    figname = 'All graphs'
    plt.grid()
    plt.savefig(f'Results\\effect of threshold\\Inter Slice\\{figname}')
    plt.close('all')

    # Load the data into a dataFrame

    df6 = pd.read_excel(r'C:\Users\tmuza\Desktop\Final Year\Handover\Results\effect of threshold\Intra '
                        r'Slice\effects of threshold on IntraSlice.xlsx')

    # Plot individual graphs

    for data in [df6.reset_index()]:
        for i in range(5):
            plt.figure(i)
            plt.plot(data['index'], data[columns[i]])
            plt.xlabel('Threshold')
            plt.grid()
            if columns[i][5:] == 'BP' or columns[i][5:] == '_BP':
                prob = 'Call Blocking Probability'
                plt.ylabel(f'{prob}')
                plt.title(f'Effect of Threshold on {columns[i][0:5]} {prob}')
                figname = f'Effect of Threshold on {columns[i]} {prob}'
                plt.savefig(f'Results/effect of threshold/Intra Slice/{figname}')
            elif columns[i][5:] == 'DP' or columns[i][5:] == '_DP':
                prob = 'Call Dropping Probability'
                plt.ylabel(f'{prob}')
                plt.title(f'Effect of Threshold on {columns[i][0:5]} {prob}')
                figname = f'Effect of Threshold on {columns[i]} {prob}'
                plt.savefig(f'Results/effect of threshold/Intra Slice/{figname}')
    plt.close('all')

    # Plot eMBB BP Vs DP on the same axis

    axx10 = plt.gca()
    df6.plot(kind='line', x='index', y='eMBB_BP', ax=axx10)
    df6.plot(kind='line', x='index', y='eMBB_DP', ax=axx10)
    plt.xlabel('Threshold')
    plt.ylabel('Call Blocking/Dropping Probability')
    plt.title('Effect of Increasing Threshold on IntraSlice Call Blocking/Dropping Probability')
    figname = 'eMBB BP vs DP'
    plt.grid()
    plt.savefig(f'Results/effect of threshold/Intra Slice/{figname}')
    plt.close('all')

    # Plot uRLLC BP vs DP on the same axis

    axx11 = plt.gca()
    df6.plot(kind='line', x='index', y='uRLLC_BP', ax=axx11)
    df6.plot(kind='line', x='index', y='uRLLC_DP', ax=axx11)
    plt.xlabel('Threshold')
    plt.ylabel('Call Blocking/Dropping Probability')
    plt.title('Effect of Increasing Threshold on IntraSlice Call Blocking/Dropping Probability')
    figname = 'uRLLC BP vs DP'
    plt.grid()
    plt.savefig(f'Results/effect of threshold/Intra Slice/{figname}')
    plt.close('all')

    # Plot all graphs on the same axis
    ax5 = plt.gca()
    df6.plot(kind='line', x='index', y='eMBB_BP', ax=ax5)
    df6.plot(kind='line', x='index', y='eMBB_DP', ax=ax5)
    df6.plot(kind='line', x='index', y='uRLLC_DP', ax=ax5)
    df6.plot(kind='line', x='index', y='uRLLC_BP', ax=ax5)
    df6.plot(kind='line', x='index', y='mMTC_BP', ax=ax5)
    plt.xlabel('Threshold')
    plt.ylabel('Call Blocking/Dropping Probability')
    plt.title('Effect of Increasing Threshold on Call Blocking/Dropping Probability')
    figname = 'All graphs'
    plt.grid()
    plt.savefig(f'Results\\effect of threshold\\Intra Slice\\{figname}')
    plt.close('all')

    # Load the data into the dataFrame

    df7 = pd.read_excel(r'C:\Users\tmuza\Desktop\Final Year\Handover\Results\effect of arrival '
                        r'rate\IntraSlice\effect of arrival rate on intraslice.xlsx')

    # Plot individual graphs

    for data in [df7.reset_index()]:
        for i in range(5):
            plt.figure(i)
            plt.plot(data['index'], data[columns[i]])
            plt.xlabel('Arrival Rate')
            plt.grid()
            if columns[i][5:] == 'BP' or columns[i][5:] == '_BP':
                prob = 'Call Blocking Probability'
                plt.ylabel(f'{prob}')
                plt.title(f'Effect of Arrival Rate on {columns[i][0:5]} {prob}')
                figname = f'Effect of Arrival Rate on {columns[i]} {prob}'
                plt.savefig(f'Results/effect of arrival rate/IntraSlice/{figname}')
            elif columns[i][5:] == 'DP' or columns[i][5:] == '_DP':
                prob = 'Call Dropping Probability'
                plt.ylabel(f'{prob}')
                plt.title(f'Effect of Arrival Rate on {columns[i][0:5]} {prob}')
                figname = f'Effect of Arrival Rate on {columns[i]} {prob}'
                plt.savefig(f'Results/effect of arrival rate/IntraSlice/{figname}')
    plt.close('all')

    # Plot eMBB BP Vs DP on the same axis

    axy = plt.gca()

    df7.plot(kind='line', x='index', y='eMBB_BP', ax=axy)
    df7.plot(kind='line', x='index', y='uRLLC_BP', ax=axy)
    df7.plot(kind='line', x='index', y='mMTC_BP', ax=axy)
    plt.xlabel('Arrival Rate')
    plt.ylabel('Call Blocking/Dropping Probability')
    plt.title('Effect of Increasing Arrival Rate on Call Blocking/Dropping Probability')
    figname = 'Intra Slice graphs'
    plt.grid()
    plt.savefig(f'Results/effect of arrival rate/IntraSlice/{figname}')
    plt.close('all')

    axx12 = plt.gca()
    df7.plot(kind='line', x='index', y='eMBB_BP', ax=axx12)
    df7.plot(kind='line', x='index', y='eMBB_DP', ax=axx12)
    plt.xlabel('Arrival Rate')
    plt.ylabel('Call Blocking/Dropping Probability')
    plt.title('Effect of Increasing Arrival Rate on IntraSlice Call Blocking/Dropping Probability')
    figname = 'eMBB BP vs DP'
    plt.grid()
    plt.savefig(f'Results/effect of arrival rate/IntraSlice/{figname}')
    plt.close('all')

    # Plot uRLLC BP vs DP on the same axis

    axx13 = plt.gca()
    df7.plot(kind='line', x='index', y='uRLLC_BP', ax=axx13)
    df7.plot(kind='line', x='index', y='uRLLC_DP', ax=axx13)
    plt.xlabel('Arrival Rate')
    plt.ylabel('Call Blocking/Dropping Probability')
    plt.title('Effect of Increasing Arrival Rate on IntraSlice Call Blocking/Dropping Probability')
    figname = 'uRLLC BP vs DP'
    plt.grid()
    plt.savefig(f'Results/effect of arrival rate/IntraSlice/{figname}')
    plt.close('all')

    # Plot all graphs on the same axis
    ax6 = plt.gca()
    df7.plot(kind='line', x='index', y='eMBB_BP', ax=ax6)
    df7.plot(kind='line', x='index', y='eMBB_DP', ax=ax6)
    df7.plot(kind='line', x='index', y='uRLLC_DP', ax=ax6)
    df7.plot(kind='line', x='index', y='uRLLC_BP', ax=ax6)
    df7.plot(kind='line', x='index', y='mMTC_BP', ax=ax6)
    plt.xlabel('Arrival Rate')
    plt.ylabel('Call Blocking/Dropping Probability')
    plt.title('Effect of Increasing Arrival Rate on Call Blocking/Dropping Probability')
    figname = 'All graphs'
    plt.grid()
    plt.savefig(f'Results\\effect of arrival rate\\IntraSlice\\{figname}')
    plt.close('all')

    # Load the data into the dataFrame

    df8 = pd.read_excel(r'C:\Users\tmuza\Desktop\Final Year\Handover\Results\effect of arrival '
                        r'rate\InterSlice\effect of arrival rate on interslice.xlsx')

    # Plot individual graphs

    for data in [df8.reset_index()]:
        for i in range(5):
            plt.figure(i)
            plt.plot(data['index'], data[columns[i]])
            plt.xlabel('Arrival Rate')
            plt.grid()
            if columns[i][5:] == 'BP' or columns[i][5:] == '_BP':
                prob = 'Call Blocking Probability'
                plt.ylabel(f'{prob}')
                plt.title(f'Effect of Arrival Rate on {columns[i][0:5]} {prob}')
                figname = f'Effect of Arrival Rate on {columns[i]} {prob}'
                plt.savefig(f'Results/effect of arrival rate/InterSlice/{figname}')
            elif columns[i][5:] == 'DP' or columns[i][5:] == '_DP':
                prob = 'Call Dropping Probability'
                plt.ylabel(f'{prob}')
                plt.title(f'Effect of Arrival Rate on {columns[i][0:5]} {prob}')
                figname = f'Effect of Arrival Rate on {columns[i]} {prob}'
                plt.savefig(f'Results/effect of arrival rate/InterSlice/{figname}')
    plt.close('all')

    # Plot eMBB BP Vs DP on the same axis

    axx14 = plt.gca()
    df8.plot(kind='line', x='index', y='eMBB_BP', ax=axx14)
    df8.plot(kind='line', x='index', y='eMBB_DP', ax=axx14)
    plt.xlabel('Arrival Rate')
    plt.ylabel('Call Blocking/Dropping Probability')
    plt.title('Effect of Increasing Arrival Rate on InterSlice Call Blocking/Dropping Probability')
    figname = 'eMBB BP vs DP'
    plt.grid()
    plt.savefig(f'Results/effect of arrival rate/InterSlice/{figname}')
    plt.close('all')

    # Plot uRLLC BP vs DP on the same axis

    axx15 = plt.gca()
    df8.plot(kind='line', x='index', y='uRLLC_BP', ax=axx15)
    df8.plot(kind='line', x='index', y='uRLLC_DP', ax=axx15)
    plt.xlabel('Arrival Rate')
    plt.ylabel('Call Blocking/Dropping Probability')
    plt.title('Effect of Increasing Arrival Rate on Call Blocking/Dropping Probability')
    figname = 'uRLLC BP vs DP'
    plt.grid()
    plt.savefig(f'Results/effect of arrival rate/InterSlice/{figname}')
    plt.close('all')

    # Plot all graphs on the same axis
    ax7 = plt.gca()
    df8.plot(kind='line', x='index', y='eMBB_BP', ax=ax7)
    df8.plot(kind='line', x='index', y='eMBB_DP', ax=ax7)
    df8.plot(kind='line', x='index', y='uRLLC_DP', ax=ax7)
    df8.plot(kind='line', x='index', y='uRLLC_BP', ax=ax7)
    df8.plot(kind='line', x='index', y='mMTC_BP', ax=ax7)
    plt.xlabel('Arrival Rate')
    plt.ylabel('Call Blocking/Dropping Probability')
    plt.title('Effect of Increasing Arrival Rate on Call Blocking/Dropping Probability')
    figname = 'All graphs'
    plt.grid()
    plt.savefig(f'Results\\effect of arrival rate\\InterSlice\\{figname}')
    plt.close('all')

    # Load the data into the dataFrame

    df9 = pd.read_excel(r'C:\Users\tmuza\Desktop\Final Year\Handover\Results\effect of departure rate\Intra '
                        r'Slice\effect of departure rate on intraslice.xlsx')

    # Plot individual graphs

    for data in [df9.reset_index()]:
        for i in range(5):
            plt.figure(i)
            plt.plot(data['index'], data[columns[i]])
            plt.xlabel('Departure Rate')
            plt.grid()
            if columns[i][5:] == 'BP' or columns[i][5:] == '_BP':
                prob = 'Call Blocking Probability'
                plt.ylabel(f'{prob}')
                plt.title(f'Effect of Departure Rate on {columns[i][0:5]} {prob}')
                figname = f'Effect of Departure Rate on {columns[i]} {prob}'
                plt.savefig(f'Results/effect of departure rate/Intra Slice/{figname}')
            elif columns[i][5:] == 'DP' or columns[i][5:] == '_DP':
                prob = 'Call Dropping Probability'
                plt.ylabel(f'{prob}')
                plt.title(f'Effect of Departure Rate on {columns[i][0:5]} {prob}')
                figname = f'Effect of Departure Rate on {columns[i]} {prob}'
                plt.savefig(f'Results/effect of departure rate/Intra Slice/{figname}')
    plt.close('all')

    # Plot eMBB BP Vs DP on the same axis

    axx16 = plt.gca()
    df9.plot(kind='line', x='index', y='eMBB_BP', ax=axx16)
    df9.plot(kind='line', x='index', y='eMBB_DP', ax=axx16)
    plt.xlabel('Departure Rate')
    plt.ylabel('Call Blocking/Dropping Probability')
    plt.title('Effect of Increasing Departure Rate on IntraSlice Call Blocking/Dropping Probability')
    figname = 'eMBB BP vs DP'
    plt.grid()
    plt.savefig(f'Results/effect of departure rate/Intra Slice/{figname}')
    plt.close('all')

    # Plot uRLLC BP vs DP on the same axis

    axx17 = plt.gca()
    df9.plot(kind='line', x='index', y='uRLLC_BP', ax=axx17)
    df9.plot(kind='line', x='index', y='uRLLC_DP', ax=axx17)
    plt.xlabel('Departure Rate')
    plt.ylabel('Call Blocking/Dropping Probability')
    plt.title('Effect of Increasing Departure Rate on IntraSlice Call Blocking/Dropping Probability')
    figname = 'uRLLC BP vs DP'
    plt.grid()
    plt.savefig(f'Results/effect of departure rate/Intra Slice/{figname}')
    plt.close('all')

    # Plot all graphs on the same axis
    ax8 = plt.gca()
    df9.plot(kind='line', x='index', y='eMBB_BP', ax=ax8)
    df9.plot(kind='line', x='index', y='eMBB_DP', ax=ax8)
    df9.plot(kind='line', x='index', y='uRLLC_DP', ax=ax8)
    df9.plot(kind='line', x='index', y='uRLLC_BP', ax=ax8)
    df9.plot(kind='line', x='index', y='mMTC_BP', ax=ax8)
    plt.xlabel('Departure Rate')
    plt.ylabel('Call Blocking/Dropping Probability')
    plt.title('Effect of Increasing Departure Rate on Call Blocking/Dropping Probability')
    figname = 'All graphs'
    plt.grid()
    plt.savefig(f'Results\\effect of departure rate\\Intra Slice\\{figname}')
    plt.close('all')

    # Load the data into a dataFrame

    df10 = pd.read_excel(r'C:\Users\tmuza\Desktop\Final Year\Handover\Results\effect of departure rate\Inter '
                         r'Slice\effect of departure rate on interslice.xlsx')

    # Plot individual graphs

    for data in [df10.reset_index()]:
        for i in range(5):
            plt.figure(i)
            plt.plot(data['index'], data[columns[i]])
            plt.xlabel('Departure Rate')
            plt.grid()
            if columns[i][5:] == 'BP' or columns[i][5:] == '_BP':
                prob = 'Call Blocking Probability'
                plt.ylabel(f'{prob}')
                plt.title(f'Effect of Departure Rate on {columns[i][0:5]} {prob}')
                figname = f'Effect of Departure Rate on {columns[i]} {prob}'
                plt.savefig(f'Results/effect of departure rate/Inter Slice/{figname}')
            elif columns[i][5:] == 'DP' or columns[i][5:] == '_DP':
                prob = 'Call Dropping Probability'
                plt.ylabel(f'{prob}')
                plt.title(f'Effect of Departure Rate on {columns[i][0:5]} {prob}')
                figname = f'Effect of Departure Rate on {columns[i]} {prob}'
                plt.savefig(f'Results/effect of departure rate/Inter Slice/{figname}')
    plt.close('all')

    # Plot eMBB BP Vs DP on the same axis

    axx18 = plt.gca()
    df10.plot(kind='line', x='index', y='eMBB_BP', ax=axx18)
    df10.plot(kind='line', x='index', y='eMBB_DP', ax=axx18)
    plt.xlabel('Departure Rate')
    plt.ylabel('Call Blocking/Dropping Probability')
    plt.title('Effect of Increasing Departure Rate on InterSlice Call Blocking/Dropping Probability')
    figname = 'eMBB BP vs DP'
    plt.grid()
    plt.savefig(f'Results/effect of departure rate/Inter Slice/{figname}')
    plt.close('all')

    # Plot uRLLC BP vs DP on the same axis

    axx19 = plt.gca()
    df10.plot(kind='line', x='index', y='uRLLC_BP', ax=axx19)
    df10.plot(kind='line', x='index', y='uRLLC_DP', ax=axx19)
    plt.xlabel('Departure Rate')
    plt.ylabel('Call Blocking/Dropping Probability')
    plt.title('Effect of Increasing Departure Rate on InterSlice Call Blocking/Dropping Probability')
    figname = 'uRLLC BP vs DP'
    plt.grid()
    plt.savefig(f'Results/effect of departure rate/Inter Slice/{figname}')
    plt.close('all')

    # Plot all graphs on the same axis
    ax9 = plt.gca()
    df10.plot(kind='line', x='index', y='eMBB_BP', ax=ax9)
    df10.plot(kind='line', x='index', y='eMBB_DP', ax=ax9)
    df10.plot(kind='line', x='index', y='uRLLC_DP', ax=ax9)
    df10.plot(kind='line', x='index', y='uRLLC_BP', ax=ax9)
    df10.plot(kind='line', x='index', y='mMTC_BP', ax=ax9)
    plt.xlabel('Departure Rate')
    plt.ylabel('Call Blocking/Dropping Probability')
    plt.title('Effect of Increasing Departure Rate on Call Blocking/Dropping Probability')
    figname = 'All graphs'
    plt.grid()
    plt.savefig(f'Results\\effect of departure rate\\Inter Slice\\{figname}')
    plt.close('all')

    # Comparing Inter Slice vs Intra Slice

    # Effect of BBU on Inter vs Intra Call Blocking Probability
    a = plt.gca()
    df.plot(kind='line', x='index', y='eMBB_BP', label='Intra eMBB_BP', ax=a)
    df2.plot(kind='line', x='index', y='eMBB_BP', label='Inter eMBB_BP', ax=a)
    plt.xlabel('Basic Bandwidth Unit (BBU)')
    plt.ylabel('Call Blocking Probability')
    plt.title('Effect of Increasing BBU on Inter and Intra Slice Blocking Probability')
    figname = 'effect of BBU on Inter vs Intra eMBB Blocking Probability'
    plt.grid()
    plt.legend(loc='lower right')
    plt.savefig(f'Results\\comparison\\effect of bbu\\{figname}')
    plt.close('all')

    # Effect of BBU on Inter vs Intra Call Dropping Probability
    a1 = plt.gca()
    df.plot(kind='line', x='index', y='eMBB_DP', label='Intra eMBB_DP', ax=a1)
    df2.plot(kind='line', x='index', y='eMBB_DP', label='Inter eMBB_DP', ax=a1)
    plt.xlabel('Basic Bandwidth Unit (BBU)')
    plt.ylabel('Call Dropping Probability')
    plt.title('Effect of Increasing BBU on Inter and Intra Slice Dropping Probability')
    figname = 'effect of BBU on Inter vs Intra eMBB Dropping Probability'
    plt.grid()
    plt.legend(loc='upper left')
    plt.savefig(f'Results\\comparison\\effect of bbu\\{figname}')
    plt.close('all')

    # Effect of BBU on Inter vs Intra Call Blocking Probability
    a2 = plt.gca()
    df.plot(kind='line', x='index', y='uRLLC_BP', label='Intra uRLLC_BP', ax=a2)
    df2.plot(kind='line', x='index', y='uRLLC_BP', label='Inter uRLLC_BP', ax=a2)
    plt.xlabel('Basic Bandwidth Unit (BBU)')
    plt.ylabel('Call Blocking Probability')
    plt.title('Effect of Increasing BBU on Inter and Intra Slice Blocking Probability')
    figname = 'effect of BBU on Inter vs Intra uRLLC Blocking Probability'
    plt.grid()
    plt.legend(loc='lower right')
    plt.savefig(f'Results\\comparison\\effect of bbu\\{figname}')
    plt.close('all')

    # Effect of BBU on Inter vs Intra Call Dropping Probability
    a3 = plt.gca()
    df.plot(kind='line', x='index', y='uRLLC_DP', label='Intra uRLLC_DP', ax=a3)
    df2.plot(kind='line', x='index', y='uRLLC_DP', label='Inter uRLLC_DP', ax=a3)
    plt.xlabel('Basic Bandwidth Unit (BBU)')
    plt.ylabel('Call Dropping Probability')
    plt.title('Effect of Increasing BBU on Inter and Intra Slice Dropping Probability')
    figname = 'effect of BBU on Inter vs Intra uRLLC Dropping Probability'
    plt.grid()
    plt.legend(loc='upper left')
    plt.savefig(f'Results\\comparison\\effect of bbu\\{figname}')
    plt.close('all')

    # Effect of BBU on Inter vs Intra Call Dropping Probability
    a4 = plt.gca()
    df.plot(kind='line', x='index', y='mMTC_BP', label='Intra mMTC_BP', ax=a4)
    df2.plot(kind='line', x='index', y='mMTC_BP', label='Inter mMTC_BP', ax=a4)
    plt.xlabel('Basic Bandwidth Unit (BBU)')
    plt.ylabel('Call Blocking Probability')
    plt.title('Effect of Increasing BBU on Inter and Intra Slice Blocking Probability')
    figname = 'effect of BBU on Inter vs Intra mMTC Blocking Probability'
    plt.grid()
    plt.legend(loc='upper left')
    plt.savefig(f'Results\\comparison\\effect of bbu\\{figname}')
    plt.close('all')

    # Effect of Capacity on Inter vs Intra Call Blocking Probability
    a5 = plt.gca()
    df4.plot(kind='line', x='index', y='eMBB_BP', label='Intra eMBB_BP', ax=a5)
    df3.plot(kind='line', x='index', y='eMBB_BP', label='Inter eMBB_BP', ax=a5)
    df4.plot(kind='line', x='index', y='eMBB_DP', label='Intra eMBB_DP', ax=a5)
    df3.plot(kind='line', x='index', y='eMBB_DP', label='Inter eMBB_DP', ax=a5)
    plt.xlabel('Capacity')
    plt.ylabel('Call Blocking/Dropping Probability')
    plt.title('Effect of Increasing Capacity on Call Blocking/Dropping Probability')
    figname = 'effect of Capacity on Inter vs Intra eMBB Blocking Probability'
    plt.grid()
    plt.legend(loc='upper right')
    plt.savefig(f'Results\\comparison\\effect of capacity\\{figname}')
    plt.close('all')

    # Effect of Capacity on Inter vs Intra Call Dropping Probability
    a6 = plt.gca()
    df4.plot(kind='line', x='index', y='eMBB_DP', label='Intra eMBB_DP', ax=a6)
    df3.plot(kind='line', x='index', y='eMBB_DP', label='Inter eMBB_DP', ax=a6)
    plt.xlabel('Capacity')
    plt.ylabel('Call Dropping Probability')
    plt.title('Effect of Increasing Capacity on Inter and Intra Slice Dropping Probability')
    figname = 'effect of Capacity on Inter vs Intra eMBB Dropping Probability'
    plt.grid()
    plt.legend(loc='upper right')
    plt.savefig(f'Results\\comparison\\effect of capacity\\{figname}')
    plt.close('all')

    # Effect of Capacity on Inter vs Intra Call Blocking Probability
    a7 = plt.gca()
    df4.plot(kind='line', x='index', y='uRLLC_BP', label='Intra uRLLC_BP', ax=a7)
    df3.plot(kind='line', x='index', y='uRLLC_BP', label='Inter uRLLC_BP', ax=a7)
    df4.plot(kind='line', x='index', y='uRLLC_DP', label='Intra uRLLC_DP', ax=a7)
    df3.plot(kind='line', x='index', y='uRLLC_DP', label='Inter uRLLC_DP', ax=a7)
    plt.xlabel('Capacity')
    plt.ylabel('Call Blocking/Dropping Probability')
    plt.title('Effect of Increasing Capacity on Call Blocking/Dropping Probability')
    figname = 'effect of Capacity on Inter vs Intra uRLLC Blocking Probability'
    plt.grid()
    plt.legend(loc='center right')
    plt.savefig(f'Results\\comparison\\effect of capacity\\{figname}')
    plt.close('all')

    # Effect of Capacity on Inter vs Intra Call Dropping Probability
    a8 = plt.gca()
    df4.plot(kind='line', x='index', y='uRLLC_DP', label='Intra uRLLC_DP', ax=a8)
    df3.plot(kind='line', x='index', y='uRLLC_DP', label='Inter uRLLC_DP', ax=a8)
    plt.xlabel('Capacity')
    plt.ylabel('Call Dropping Probability')
    plt.title('Effect of Increasing Capacity on Inter and Intra Slice Dropping Probability')
    figname = 'effect of Capacity on Inter vs Intra uRLLC Dropping Probability'
    plt.grid()
    plt.legend(loc='upper right')
    plt.savefig(f'Results\\comparison\\effect of capacity\\{figname}')
    plt.close('all')

    # Effect of Capacity on Inter vs Intra Call Dropping Probability
    a9 = plt.gca()
    df4.plot(kind='line', x='index', y='mMTC_BP', label='Intra mMTC_BP', ax=a9)
    df3.plot(kind='line', x='index', y='mMTC_BP', label='Inter mMTC_BP', ax=a9)
    plt.xlabel('Capacity')
    plt.ylabel('Call Blocking Probability')
    plt.title('Effect of Increasing Capacity on Inter and Intra Slice Blocking Probability')
    figname = 'effect of Capacity on Inter vs Intra mMTC Blocking Probability'
    plt.grid()
    plt.legend(loc='upper right')
    plt.savefig(f'Results\\comparison\\effect of capacity\\{figname}')
    plt.close('all')

    # Effect of Threshold on Inter vs Intra Call Blocking Probability
    a10 = plt.gca()
    df6.plot(kind='line', x='index', y='eMBB_BP', label='Intra eMBB_BP', ax=a10)
    df5.plot(kind='line', x='index', y='eMBB_BP', label='Inter eMBB_BP', ax=a10)
    plt.xlabel('Threshold')
    plt.ylabel('Call Blocking Probability')
    plt.title('Effect of Increasing Threshold on Inter and Intra Slice Blocking Probability')
    figname = 'effect of Threshold on Inter vs Intra eMBB Blocking Probability'
    plt.grid()
    plt.legend(loc='upper right')
    plt.savefig(f'Results\\comparison\\effect of threshold\\{figname}')
    plt.close('all')

    # Effect of Threshold on Inter vs Intra Call Dropping Probability
    a11 = plt.gca()
    df6.plot(kind='line', x='index', y='eMBB_DP', label='Intra eMBB_DP', ax=a11)
    df5.plot(kind='line', x='index', y='eMBB_DP', label='Inter eMBB_DP', ax=a11)
    plt.xlabel('Threshold')
    plt.ylabel('Call Dropping Probability')
    plt.title('Effect of Increasing Threshold on Inter and Intra Slice Dropping Probability')
    figname = 'effect of Threshold on Inter vs Intra eMBB Dropping Probability'
    plt.grid()
    plt.legend(loc='center right')
    plt.savefig(f'Results\\comparison\\effect of threshold\\{figname}')
    plt.close('all')

    # Effect of Threshold on Inter vs Intra Call Blocking Probability
    a12 = plt.gca()
    df6.plot(kind='line', x='index', y='uRLLC_BP', label='Intra uRLLC_BP', ax=a12)
    df5.plot(kind='line', x='index', y='uRLLC_BP', label='Inter uRLLC_BP', ax=a12)
    plt.xlabel('Threshold')
    plt.ylabel('Call Blocking Probability')
    plt.title('Effect of Increasing Threshold on Inter and Intra Slice Blocking Probability')
    figname = 'effect of Threshold on Inter vs Intra uRLLC Blocking Probability'
    plt.grid()
    plt.legend(loc='upper right')
    plt.savefig(f'Results\\comparison\\effect of threshold\\{figname}')
    plt.close('all')

    # Effect of Threshold on Inter vs Intra Call Dropping Probability
    a13 = plt.gca()
    df6.plot(kind='line', x='index', y='uRLLC_DP', label='Intra uRLLC_DP', ax=a13)
    df5.plot(kind='line', x='index', y='uRLLC_DP', label='Inter uRLLC_DP', ax=a13)
    plt.xlabel('Threshold')
    plt.ylabel('Call Dropping Probability')
    plt.title('Effect of Increasing Threshold on Inter and Intra Slice Dropping Probability')
    figname = 'effect of Threshold on Inter vs Intra uRLLC Dropping Probability'
    plt.grid()
    plt.legend(loc='center right')
    plt.savefig(f'Results\\comparison\\effect of threshold\\{figname}')
    plt.close('all')

    # Effect of Threshold on Inter vs Intra Call Dropping Probability
    a14 = plt.gca()
    df6.plot(kind='line', x='index', y='mMTC_BP', label='Intra mMTC_BP', ax=a14)
    df5.plot(kind='line', x='index', y='mMTC_BP', label='Inter mMTC_BP', ax=a14)
    plt.xlabel('Threshold')
    plt.ylabel('Call Blocking Probability')
    plt.title('Effect of Increasing Threshold on Inter and Intra Slice Blocking Probability')
    figname = 'effect of Threshold on Inter vs Intra mMTC Blocking Probability'
    plt.grid()
    plt.legend(loc='upper right')
    plt.savefig(f'Results\\comparison\\effect of threshold\\{figname}')
    plt.close('all')

    # Effect of Arrival Rate on Inter vs Intra Call Dropping Probability

    a15 = plt.gca()
    df7.plot(kind='line', x='index', y='mMTC_BP', label='Intra mMTC_BP', ax=a15)
    df8.plot(kind='line', x='index', y='mMTC_BP', label='Inter mMTC_BP', ax=a15)
    plt.xlabel('Arrival Rate')
    plt.ylabel('Call Blocking Probability')
    plt.title('Effect of Increasing Arrival Rate on Inter and Intra Slice Blocking Probability')
    figname = 'effect of Arrival Rate on Inter vs Intra mMTC Blocking Probability'
    plt.grid()
    plt.legend(loc='center right')
    plt.savefig(f'Results\\comparison\\effect of arrival rate\\{figname}')
    plt.close('all')

    # Efeect of Arrival Rate on Inter vs Intra Call Dropping Probability

    a16 = plt.gca()
    df7.plot(kind='line', x='index', y='eMBB_BP', label='Intra eMBB_BP', ax=a16)
    df8.plot(kind='line', x='index', y='eMBB_BP', label='Inter eMBB_BP', ax=a16)
    plt.xlabel('Arrival Rate')
    plt.ylabel('Call Blocking Probability')
    plt.title('Effect of Increasing Arrival Rate on Inter and Intra Slice Blocking Probability')
    figname = 'effect of Arrival Rate on Inter vs Intra eMBB Blocking Probability'
    plt.grid()
    plt.legend(loc='center right')
    plt.savefig(f'Results\\comparison\\effect of arrival rate\\{figname}')
    plt.close('all')

    # Efeect of Arrival Rate on Inter vs Intra Call Dropping Probability

    a17 = plt.gca()
    df7.plot(kind='line', x='index', y='uRLLC_BP', label='Intra uRLLC_BP', ax=a17)
    df8.plot(kind='line', x='index', y='uRLLC_BP', label='Inter uRLLC_BP', ax=a17)
    plt.xlabel('Arrival Rate')
    plt.ylabel('Call Blocking Probability')
    plt.title('Effect of Increasing Arrival Rate on Inter and Intra Slice Blocking Probability')
    figname = 'effect of Arrival Rate on Inter vs Intra uRLLC Blocking Probability'
    plt.grid()
    plt.legend(loc='center right')
    plt.savefig(f'Results\\comparison\\effect of arrival rate\\{figname}')
    plt.close('all')

    # Efeect of Arrival Rate on Inter vs Intra Call Dropping Probability

    a18 = plt.gca()
    df7.plot(kind='line', x='index', y='uRLLC_DP', label='Intra uRLLC_DP', ax=a18)
    df8.plot(kind='line', x='index', y='uRLLC_DP', label='Inter uRLLC_DP', ax=a18)
    plt.xlabel('Arrival Rate')
    plt.ylabel('Call Dropping Probability')
    plt.title('Effect of Increasing Arrival Rate on Inter and Intra Slice Dropping Probability')
    figname = 'effect of Arrival Rate on Inter vs Intra uRLLC Dropping Probability'
    plt.grid()
    plt.legend(loc='center right')
    plt.savefig(f'Results\\comparison\\effect of arrival rate\\{figname}')
    plt.close('all')

    # Efeect of Arrival Rate on Inter vs Intra Call Dropping Probability

    a19 = plt.gca()
    df7.plot(kind='line', x='index', y='eMBB_DP', label='Intra eMBB_DP', ax=a19)
    df8.plot(kind='line', x='index', y='eMBB_DP', label='Inter eMBB_DP', ax=a19)
    plt.xlabel('Arrival Rate')
    plt.ylabel('Call Dropping Probability')
    plt.title('Effect of Increasing Arrival Rate on Inter and Intra Slice Dropping Probability')
    figname = 'effect of Arrival Rate on Inter vs Intra eMBB Dropping Probability'
    plt.grid()
    plt.legend(loc='center right')
    plt.savefig(f'Results\\comparison\\effect of arrival rate\\{figname}')
    plt.close('all')

    # Effect of Departure Rate on Inter vs Intra Call Dropping Probability

    a20 = plt.gca()
    df9.plot(kind='line', x='index', y='mMTC_BP', label='Intra mMTC_BP', ax=a20)
    df10.plot(kind='line', x='index', y='mMTC_BP', label='Inter mMTC_BP', ax=a20)
    plt.xlabel('Departure Rate')
    plt.ylabel('Call Blocking Probability')
    plt.title('Effect of Increasing Departure Rate on Inter and Intra Slice Blocking Probability')
    figname = 'effect of Departure Rate on Inter vs Intra mMTC Blocking Probability'
    plt.grid()
    plt.legend(loc='upper right')
    plt.savefig(f'Results\\comparison\\effect of departure rate\\{figname}')
    plt.close('all')

    # Effect of Departure Rate on Inter vs Intra Call Dropping Probability

    a21 = plt.gca()
    df9.plot(kind='line', x='index', y='eMBB_BP', label='Intra eMBB_BP', ax=a21)
    df10.plot(kind='line', x='index', y='eMBB_BP', label='Inter eMBB_BP', ax=a21)
    plt.xlabel('Departure Rate')
    plt.ylabel('Call Blocking Probability')
    plt.title('Effect of Increasing Departure Rate on Inter and Intra Slice Blocking Probability')
    figname = 'effect of Departure Rate on Inter vs Intra eMBB Blocking Probability'
    plt.grid()
    plt.legend(loc='upper right')
    plt.savefig(f'Results\\comparison\\effect of departure rate\\{figname}')
    plt.close('all')

    # Effect of Departure Rate on Inter vs Intra Call Dropping Probability

    a22 = plt.gca()
    df9.plot(kind='line', x='index', y='uRLLC_BP', label='Intra uRLLC_BP', ax=a22)
    df10.plot(kind='line', x='index', y='uRLLC_BP', label='Inter uRLLC_BP', ax=a22)
    plt.xlabel('Departure Rate')
    plt.ylabel('Call Blocking Probability')
    plt.title('Effect of Increasing Departure Rate on Inter and Intra Slice Blocking Probability')
    figname = 'effect of Departure Rate on Inter vs Intra uRLLC Blocking Probability'
    plt.grid()
    plt.legend(loc='upper right')
    plt.savefig(f'Results\\comparison\\effect of departure rate\\{figname}')
    plt.close('all')

    # Effect of Departure Rate on Inter vs Intra Call Dropping Probability

    a23 = plt.gca()
    df9.plot(kind='line', x='index', y='uRLLC_DP', label='Intra uRLLC_DP', ax=a23)
    df10.plot(kind='line', x='index', y='uRLLC_DP', label='Inter uRLLC_DP', ax=a23)
    plt.xlabel('Departure Rate')
    plt.ylabel('Call Dropping Probability')
    plt.title('Effect of Increasing Departure Rate on Inter and Intra Slice Dropping Probability')
    figname = 'effect of Departure Rate on Inter vs Intra uRLLC Dropping Probability'
    plt.grid()
    plt.legend(loc='upper right')
    plt.savefig(f'Results\\comparison\\effect of departure rate\\{figname}')
    plt.close('all')

    # Effect of Departure Rate on Inter vs Intra Call Dropping Probability

    a24 = plt.gca()
    df9.plot(kind='line', x='index', y='eMBB_DP', label='Intra eMBB_DP', ax=a24)
    df10.plot(kind='line', x='index', y='eMBB_DP', label='Inter eMBB_DP', ax=a24)
    plt.xlabel('Departure Rate')
    plt.ylabel('Call Dropping Probability')
    plt.title('Effect of Increasing Departure Rate on Inter and Intra Slice Dropping Probability')
    figname = 'effect of Departure Rate on Inter vs Intra eMBB Dropping Probability'
    plt.grid()
    plt.legend(loc='upper right')
    plt.savefig(f'Results\\comparison\\effect of departure rate\\{figname}')
    plt.close('all')


plotting()
