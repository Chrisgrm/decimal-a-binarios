def convertir_decimal_dividiendo(numero):
    resultado = ''
    while numero // 2 != 0:
        resultado = asignar_caracter_a_numero(numero % 2)+resultado
        numero = numero // 2
    return asignar_caracter_a_numero(numero)+str(resultado)

def convertir_decimal_potencias(numero):
    resultado = ''
    potencias = [1024,512,256,128,64,32,16,8,4,2,1]
    for x in potencias:
        if potencias[x]<=numero:
            potencia = x
            break
    resultado = comparador(potencia, numero)+ resultado 
    while potencia != 1:       
        
            
        potencia = potencia - potencias[potencias.index(potencia)+1]    
        resultado = comparador(potencia, numero) + resultado 
            
def comparador(potencia, numero):
    if potencia > numero:
        return '0'
    else:
        return '1'



def asignar_caracter_a_numero(numero):
    return str(numero)

numero = int(input('Introduzca : '))
print(convertir_decimal_dividiendo(numero))
print(convertir_decimal_potencias(numero))


