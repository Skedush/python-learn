def cult(a,b,c):
    if a=='+':
        return b+c
    if a=='-':
        return b-c
    if a=='*':
        return b*c
    if a=='/':
        return b/c
def myFunction(inp):
    result=0
    tmp=''
    for item in inp:
        if item.isdigit():

            if result==0:
                result=int(item)

            if(tmp==''):
                continue
            result=cult(tmp,result,int(item))
            
        else:
            tmp=item

    return result

inp=input()

result=myFunction(inp)

print(result)
