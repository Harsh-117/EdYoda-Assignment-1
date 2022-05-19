print(end="Enter the String: ")
text = str(input())
textLen = len(text)
textList = list(text)
for i in range(textLen):
    ch = textList[i]
    if i==0:
        ascVal = ord(ch)
        if ascVal>=97 and ascVal<=122:
            index = 0
            textList[index] = ch.upper()
            text = "".join(textList)
    if ch==" ":
        ch = textList[i+1]
        ascVal = ord(ch)
        if ascVal>=97 and ascVal<=122:
            index = i+1
            textList[index] = ch.upper()
            text = "".join(textList)
print("\nThe New String is: " + text)