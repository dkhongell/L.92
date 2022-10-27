#Brenna and Kalena
string='SPAM!HelloSPAM! worldSPAM!!'
def remove_substring(string, remove):
    output=[]
    index=0
    while index < len(string):
        if string[index:index+ len(remove)]==remove:
            index += len(remove)
        else:
            output.append(string[index])
            index+=1
    print("".join(output))

    
