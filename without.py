import string
from Resultado import *
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

def separarPalavrasRepetidas(frases):
    words=[]
    for x in frases:
        line=x.split(" ")
        for y in line:
            words.append(y)
    return words

def separarPalavras(frases):
    words=[]
    for x in frases:
        line=x.split(" ")
        for y in line:
            if y not in words:
                words.append(y)
    return words



def retirarPont(word):
    newString=""
    alfabeto=list(string.ascii_lowercase)
    alfabeto.append("'")
    for i in range(len(word)):
        letra=word[i:i+1]
        if letra in alfabeto:
            newString+=letra
    return newString


def resultados(input):
    frases=separarFrases(input)
    words=separarPalavras(frases)
    words_n=separarPalavrasRepetidas(frases)


    last=[]
    for word in words_n:
        new=retirarPont(word)
        #if new not in last:
        last.append(new)

    ll=[]
    for word in words:
        new=retirarPont(word)
        if new not in ll:
            ll.append(new)

    aparicoes=[]
    for l in ll:
        x=Aparicoes(l,last.count(l))
        aparicoes.append(x)



    result=Resultado(aparicoes,len(ll))
    return result