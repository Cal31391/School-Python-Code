import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 
from pandas import Series, DataFrame





data = pd.DataFrame()
data = pd.read_csv('P00000001-ALL.csv', skiprows=1, names=['cmte_id', 'cand_id', 'cand_nm', 'contbr_nm', 'contbr_city',
					'contbr_state', 'contbr_zip', 'contbr_employer', 'contbr_occupation', 'contb_receipt_amt', 'contb_receipt_dt', 'receipt_desc',
					'memo_cd', 'memo_text', 'form_tp', 'file_num'], low_memory=False)

#BAR PLOT: CANDIDATES SUPPORTED BY UNEMPLOYED GROUP
candidates = []#empty list for candidate names
name ='contbr_occupation'
for index, row in data.iterrows():#iterate through dataset and pull what is needed
    if pd.notnull(row[name]):#check to make sure not null 
        if row[name] == 'NOT EMPLOYED' or row[name] == 'UNEMPLOYED': 
            candidates.append(row['cand_nm'])
            

#np array of each unique name and another np array for their counts   
unique, counts = np.unique(candidates, return_counts=True)


fig1 = plt.figure("Bar Plot")

#horizontal bar graph
plt.barh(range(len(unique)), counts, align='center')
plt.yticks(range(len(unique)), unique, fontsize='8')
plt.title("2012 Presidential Candidate Support by the Unemployed")
plt.xlabel("# of Unemployed")
plt.ylabel("Candidates")


#PIE CHART: CANDIDATES SUPPORTED BY UNEMPLOYED GROUP
candidates2 = []#empty list for candidate names(pie chart version)
for index, row in data.iterrows():
    if pd.notnull(row[name]):
        if row[name] == 'NOT EMPLOYED' or row[name] == 'UNEMPLOYED': 
            if row['cand_nm'] != 'Obama, Barack' and row['cand_nm'] != 'Paul, Ron':
                row['cand_nm'] = 'Other'#put 'lesser' names in category 'Other'
            candidates2.append(row['cand_nm'])

unique, counts= np.unique(candidates2, return_counts=True)


fig2 = plt.figure("Pie Chart")
plt.pie(counts, labels=unique, autopct='%1.1f%%')
plt.title("2012 Presidential Candidate Support by the Unemployed")
plt.axis('equal') 

plt.tight_layout()
plt.show()

