#!/usr/bin/env python3
import os
import settings
import pandas as pd 


# with open(settings.HEADERS_PATH) as header:
#     headerQ = header.readline().split(',')


HEADERS = {
    "RepeatSales": [
       
    ],

    "Quarterly": [
    
    ],
                 
    }

SELECT = {
    "RepeatSales": HEADERS["RepeatSales"],
    "Quarterly": HEADERS["Quarterly"]  
    }

def concatenate(prefix="RepeatSales"):
    allFiles = os.listdir(settings.DATA_DIR)
    full = []
    for fName in allFiles:
        if not fName.startswith(prefix):
            continue
        
        data = pd.read_csv(os.path.join(settings.DATA_DIR, fName), sep=',', header=0, index_col=False)
        # data = data[SELECT[prefix]]
        full.append(data)

    full = pd.concat(full, axis=0)
    full.to_csv(os.path.join(settings.PROCESSED_DIR, "{}.txt".format(prefix)), sep=",", index=False)

if __name__ == "__main__":
    concatenate("RepeatSales")
    concatenate("Quarterly")
