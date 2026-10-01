
with open("WL.txt", 'r') as wl:
    
    content = wl.readlines()   
    
    weights = []
    
    for line in content:

        if line.startswith('('):
            weights.append(line)
            
    for line in weights:
        line = line.strip(line[0:8])
        
        line = line.strip('kg')
            
                
        print(line)