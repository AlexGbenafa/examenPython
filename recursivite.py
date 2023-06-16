def divin(a,b):
    d=0
    while a>=b:
        d=d+1
        a=a-b
        print(d)
    return d

#L'expression recursive est  1 + divin(a - b, b) avec d=a-b et le critere d'arret est quand a devient strictement inferieur a b
def divinRec(a, b):
    d = a-b
    if a < b:
        print (0)
        return 0
    else:
        print (1+divinRec(d, b))
        return 1 + divinRec(d, b)


#2.2
# a- Critere d'arret B = 0
# b- 
def fonctionRecursive(a, b):
    if b == 0:
        print(a)
        return a
    else:
        print(fonctionRecursive(a, b-1))
        return fonctionRecursive(a, b-1)
 
# Pour a=2 et b=3, il y a un total de 4 appels récursifs effectués


divin(3,2)
divinRec(3,2)
fonctionRecursive(3,2)