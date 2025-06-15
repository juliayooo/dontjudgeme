import json 

jsonfile = open("mydata.json", "w", encoding="utf-8" )


filename = 'mydata.txt'

# dictionary where the lines from
# text will be stored

# creating dictionary
dict1 = {}    
counter = 0
with open(filename) as fh:

    for line in fh:
        counter += 1
        # reads each line and trims of extra the spaces 
        # and gives only the valid words
        line = line.strip()
        line = line.lower()
        if "does anyone else" in line:
            if "?" in line:
                line = line.replace("?", ".")
        
            line = line.replace("does anyone else", "i")
            dict1[counter] = line
            
        elif "does anyone" in line:

            if "?" in line:
                line = line.replace("?", ".")
    
            line = line.replace("does anyone", "i")
            dict1[counter] = line
        elif "anyone else" in line:
            if "?" in line:
                line = line.replace("?", ".")
    
            line = line.replace("anyone else", "i")
            dict1[counter] = line
        elif "suicide" in line: 
            continue
        elif "fuck" in line: 
            line = line.replace("fuck", "f***")
            dict1[counter] = line
        elif line == "":
            continue

        else:
            dict1[counter] = line
        
        


json.dump(dict1, jsonfile, indent = 4, sort_keys = False)
jsonfile.close()