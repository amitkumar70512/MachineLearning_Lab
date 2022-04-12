import numpy as np
import pandas as pd

data = pd.read_csv('data.csv')
concepts = np.array(data)[:,:-1]
target = np.array(data)[:,-1] 

print(data)

def training(concept,target):
    for i,val in enumerate(target):
        if val =='yes':
            specific_hypothesis = concept[i].copy()
            break
            
    for i,val in enumerate(concept):
        if target[i]=='yes':
            for x in range(len(specific_hypothesis)):
                if  val[x] != specific_hypothesis[x]:
                    specific_hypothesis[x]='?'
                else:
                    pass
    return specific_hypothesis

    
print(training(concepts,target))
