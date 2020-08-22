import numpy as np
import pandas as pd
from pandas import ExcelWriter
import matplotlib.pyplot as plt

print("Hie")

df = pd.read_excel("new.xlsx")
#df.set_index("index", inplace=True)
slices = ['eMBB_BP', 'eMBB_DP' ,'uRLLC_BP', 'mMTC_BP', 'uRLLC_DP']
g = df.groupby('method')[slices].mean()

indx = np.arange(len(slices))
labels = np.arange(0,1,0.0001)
inter_vals = list(g.T['Inter Slice'])
intra_vals = list(g.T['Intra Slice'])
bar_width = 0.35

fig , ax =plt.subplots()
bar_inter = ax.bar(indx - bar_width/2, inter_vals, bar_width, label="Inter Slice")
bar_intra = ax.bar(indx + bar_width/2, intra_vals, bar_width, label="Intra Slice")

ax.set_xticks(indx)
ax.set_xticklabels(slices)
ax.legend()

for i in indx:
    ax.annotate('{0:.4f}'.format(bar_inter[i].get_height()),xy=(bar_inter[i].get_x() + bar_inter[i].get_width()//2, bar_inter[i].get_height()),xytext=(0,3),textcoords="offset points", ha="center", va="bottom")
#
for i in indx:
    ax.annotate('{0:.4f}'.format(bar_intra[i].get_height()), xy=(bar_intra[i].get_x() + bar_intra[i].get_width()//2, bar_intra[i].get_height()),xytext=(0,3),textcoords="offset points", ha="center", va="bottom")

plt.savefig("Comparison Bar")
plt.show()



#print(inter_vals)
#eMBB_BP = df['eMBB_BP']
#eMBB_DP = df['eMBB_DP']
#mMTC_BP = df['mMTC_BP']
#uRLLC_BP = df['uRLLC_BP']
#uRLLC_DP = df['uRLLC_BP']

#eMBB_BP_inter = df['eMBB_BP_inter']
#eMBB_DP_inter = df['eMBB_DP_inter']
#mMTC_BP_inter = df['mMTC_BP_inter']
#uRLLC_BP_inter = df['uRLLC_BP_inter']
#uRLLC_DP_inter = df['uRLLC_BP_inter']




