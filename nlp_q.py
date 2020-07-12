import pandas as pd
import numpy as np

files=pd.read_csv("files.csv")
nodes=pd.read_csv("nodes.csv")

files.sort_values("size",axis=0, ascending=False,inplace=True)
files.reset_index(inplace=True)
nodes.sort_values("space",axis=0, ascending=False,inplace=True)
nodes.reset_index(inplace=True)

nf = len(files)
node = []
file = []

for i in range(len(nodes)):
    for j in range(len(files)):

        if files['size'][j] > nodes['space'][i]:
            if i != (len(nodes) - 1) and files['size'][j] <= nodes['space'][i + 1]:
                continue
            else:
                node.append('NULL')
                file.append(files['filename'][j])
                files = files.drop([j])
        elif files['size'][j] <= nodes['space'][i]:
            node.append(nodes['node'][i])
            file.append(files['filename'][j])
            nodes['space'][i] = nodes['space'][i] - files['size'][j]
            files = files.drop([j])
    files.reset_index(drop=True, inplace=True)

res=list(zip(file, node))
result=pd.DataFrame(res,columns=['File_name','Node'])
print(result)