#!/usr/bin/env python3
import os
import settings
import pandas as pd 


with open(settings.HEADERS_PATH) as header:
    headerQ = header.readline().split(',')


HEADERS = {
    "RepeatSales": [
        "sales",
        "MoM",
        "YoY"
    ],

    "Quarterly": [
     input(headerQ)
    ]
                 
    }

SELECT = {
    "RepeatSales": HEADERS["RepeatSales"],
    "Quarterly": headerQ   
    }

def concatenate(prefix="RepeatSales"):
    files = os.listdir(settings.DATA_DIR)
    full = []
    for f in files:
        if not f.startswith(prefix):
            continue
        
        if prefix is not "Quarterly":
            data = pd.read_csv(os.path.join(settings.DATA_DIR, f), sep=',', header=None, names=HEADERS[prefix], index_col=False)
        else:
            data = pd.read_csv(os.path.join(settings.DATA_DIR, f), sep=',', header=None, names=headerQ, index_col=False)
        
        data = data[SELECT[prefix]]
        full.append(data)

    full = pd.concat(full, axis=0)
    full.to_csv(os.path.join(settings.PROCESSED_DIR, "{}.txt".format(prefix)), header=SELECT[prefix], sep=",", index=False)

if __name__ == "__main__":
    concatenate("RepeatSales")
    concatenate("Quarterly")
