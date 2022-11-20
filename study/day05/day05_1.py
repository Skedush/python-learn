# init=input()

str1='1+2+3+4+5/3*2'

result=0
tmp=''



for item in str1:
    if item.isdigit():

        if result==0:
            result=int(item)
        if tmp=='+':
            result=result+int(item)
        if tmp=='-':
            result=result-int(item)
        if tmp=='*':
            result=result*int(item)
        if tmp=='/':
            result=result/int(item)
        
    else:
        tmp=item

print(result)


print('-------------------------')
