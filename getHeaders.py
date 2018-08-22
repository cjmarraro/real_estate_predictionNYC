#!/usr/bin/env python3
import os
import settings


allFiles = os.listdir(settings.DATA_DIR)
os.makedirs('preprocessed', exist_ok=True)

with open(settings.HEADERS_PATH, 'w') as outfile:
    for i, fname in enumerate(allFiles):
        if not fname.startswith('Q'):
            continue
        
        if i <= len(allFiles):              
            with open(os.path.join(settings.DATA_DIR, fname)) as infile:
                line = infile.readline()
                lines = "{}".format(line).strip()
                
        outfile.write(lines)
        print("Writing {} headers to file path: {}.".format(fname, settings.HEADERS_PATH))
        

if __name__ == '__main__':
    pass

