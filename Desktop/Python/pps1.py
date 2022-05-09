myStr= input()
strings, numbers=[],[]
tempNumber,tempString='',''
for ch in myStr:
    if ch.isdigit():
        tempNumber+=ch
        if len(tempString)>0:
            strings.append(tempString)
            tempString=''
    else:
        tempString+=ch
        if len(tempNumber)>0:
            numbers.append(int(tempNumber))
            tempNumber=''
if len(tempNumber)>0:
    numbers.append(int(tempNumber))

combined=list(zip(numbers,strings))
combined.sort()
print(''.join([pair[1] for pair in combined]))
