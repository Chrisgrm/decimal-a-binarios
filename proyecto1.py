def convertir_decimal_dividiendo(numero):
    resultado = ''
    while numero // 2 != 0:
        resultado = asignar_caracter_a_numero(numero % 2)+resultado
        numero = numero // 2
    return asignar_caracter_a_numero(numero)+str(resultado)

def convertir_decimal_potencias(numero):
    resultado = ''
    potencias = (1024,512,256,128,64,32,16,8,4,2,1)
    ##Ciclo para detectar la potencia que cabe dentro del numero
    for i in range(len(potencias)):     
      
        if potencias[i]<=numero:
            potencia = potencias[i]
            contador = i            
            break
        
    resultado = comparador(potencia, numero)+ resultado
    ##ciclo que recorre lo que falta de la tupla de potencias y construye el resultado
    while len(potencias)-contador != 1: 
        potencia = potencia + potencias[contador+1]
        resultado =  resultado +  comparador(potencia, numero)      
        if comparador(potencia , numero) == '0':
            potencia = potencia - potencias[contador+1]        
        contador +=1    
    return resultado
            
def comparador(potencia, numero):
    respuesta = 0
    if potencia > numero:
        respuesta = 0
    else:
        respuesta = 1
    return str(respuesta) 



def asignar_caracter_a_numero(numero):
    return str(numero)

numero = int(input('Introduzca : '))
print(convertir_decimal_dividiendo(numero))
print(convertir_decimal_potencias(numero))


