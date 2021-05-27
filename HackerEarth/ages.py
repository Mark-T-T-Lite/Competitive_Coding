august = 22
joseph = 22
peter = 20
timothy = 25

name_list = [august,joseph,peter,timothy]
name_dict = {1:"august",2:"joseph",3:"peter",4:"timothy"}
n = 0

for name in name_list:
    if name == max(name_list):
        print(name_dict[n+1]+" is the oldest")
    if name == min(name_list):
        print(name_dict[n+1]+" is the youngest")
    

    k=name_list[n]

    if k in name_list[n+1:]:
        x = name_list[n+1:].index(k)
        print(name_dict[x+n+2]+" and "+name_dict[x+1]+" have same age")
    n+=1
    
