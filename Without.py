import string
#input=open("friends.s01e01.720p.bluray.x264-psychd.str","r")
input=open("star_wars.str","r")
def separarFrases(input):
    linhas=input.readlines()
    frases=[]
    numeros=["0","1","2","3","4","5","6","7","8","9"]
    for i in range(0,len(linhas)):
        lin=linhas[i]
        if lin[0:1] not in numeros:
            if lin.rstrip()!="":
                frases.append(lin.rstrip().lower())
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


def retirarPont(word):
    newString=""
    alfabeto=list(string.ascii_lowercase)
    for i in range(1,len(word)+1):
        letra=word[i-1:i]
        if letra in alfabeto:
            newString+=letra
    return newString


last=[]
for word in words:
    new=retirarPont(word)
    if new not in last:
        last.append(new)
print(last)
print(len(last)/7)

print("You need to know at least %a words to understand this episode without subititles"%len(last))
