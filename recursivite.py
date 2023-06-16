def divin(a,b):
    d=0
    while a>=b:
        d=d+1
        a=a-b
    return d

#L'expression recursive est  1 + divin(a - b, b) avec d=a-b et le critere d'arret est quand a devient strictement inferieur a b
def divinRec(a, b):
    d = a-b
    if a < b:
        return 0
    else:
        return 1 + divinRec(d, b)


#2.2
# a- Critere d'arret B = 0
# b- 
def fonctionRecursive(a, b):
    if b == 0:
        return a
    else:
        return fonctionRecursive(a, b-1)
 
 # Pour a=2 et b=3, il y a un total de 4 appels récursifs effectués