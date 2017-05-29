import string
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
alfabeto=list(string.ascii_lowercase)

for y in words:
    word=y.lower()
    if word[0:1] not in alfabeto:
        if (word.startswith("...")):
            new=word[3:]
            if new not in words:
                words.append(new)

                words.remove(y)

        elif (word[0:1])=="-":
            words.remove(y)
        elif(words[0:1])=='"':
            new=word[1:-1]
            if new not in words:
                words.append(new)

                words.remove(y)
        elif(word[0:1])=='[':
            new=word[1:-1]
            if new not in words:
                words.append(new)

                words.remove(y)

        else:
            new=word[1:]
            if new not in words:
                words.append(new)

                words.remove(y)
    elif word[-1] not in alfabeto:
        if (word.endswith(".")):
            if (word.endswith("...")):
                new = word[1:-3]

            else:
                new=word[1:-1]
            if new not in words:
                words.append(new)
                words.remove(y)



        elif (word.endswith("?")):

            new=word[1:-1]
            if new not in words:
                words.append(new)

                words.remove(y)
        elif (word.endswith("]")):

            new=word[1:-1]
            if new not in words:
                words.append(new)

                words.remove(y)

print(words)

print("You need to know at least %a words to understand that episode without subititles"%len(words))
