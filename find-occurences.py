file = "./pod-nodes.txt"

myfile = open("./pod-nodes.txt","r")
data = myfile.read()
LINE = []

with open(file,"r") as file:
    for line in file: 
        if line not in LINE:
            LINE.append(line)
            occurences = data.count(line)
            print("Node IP is:-",line)
            print("Occurences:-",occurences)
        


