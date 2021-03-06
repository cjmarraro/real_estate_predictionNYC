#!/usr/bin/env python3
import os
import settings
import re

allFiles = os.listdir(settings.DATA_DIR)
regex1 = re.compile(r'\D')
os.makedirs('preprocessing', exist_ok=True)

with open(settings.HEADERS_PATH, 'w') as outfile:
    for i, fname in enumerate(allFiles):
        if not fname.startswith(input("Enter filename prefix for selection:")):
            break
        
        with open(os.path.join(settings.DATA_DIR, fname)) as infile:
            line = infile.readline()
           
            if regex1.match(line): 
                lines = "{}".format(line).strip()
           
        outfile.write(lines)
        print("Writing {} headers to file path: {}.".format(fname, settings.HEADERS_PATH))
        

# if __name__ == '__main__':
#     pass

