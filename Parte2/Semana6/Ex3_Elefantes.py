def incomodam(n):
    if n<=0:
        return ""
    while n > 0:
        return ("incomodam "+str(incomodam(n-1)))

def elefantes(n,num=1):
    if num < 1:
        return ""
    if n < 2:
        return ""
    while n >= num and n>= 2:
        if num == 1:
            return ("Um elefante incomoda muita gente\n"+ str(elefantes(n,num+1)))
        else:
            return (str(num)+" elefantes "+str(incomodam(num))+"muito mais\n"+str(num)+" elefantes incomodam muita gente\n"+str(elefantes(n,num+1)))
