input=open("friends.s01e01.720p.bluray.x264-psychd.str","r")
def separarFrases(input):
    linhas=input.readlines()
    frases=[]
    numeros=["0","1","2","3","4","5","6","7","8","9"]
    for i in range(0,len(linhas)):
        lin=linhas[i]
        if lin[0:1] not in numeros:
            if lin.rstrip()!="":
                frases.append(lin.rstrip())
    return frases

def separarPalavras(frases):
    words=[]
    for x in frases:
        line=x.split(" ")
        for y in line:
            if y not in words:
                words.append(y)
    return words

frases=separarFrases(input)
words=separarPalavras(frases)
print(words)
print("You need to know at least %a words to understand that episode without subititles"%len(words))
