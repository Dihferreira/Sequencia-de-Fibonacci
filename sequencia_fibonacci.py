def fibonacci(entrada):
    numA = 0
    
    numB = 1
    
    soma = 0
    
    while soma <= entrada:
        
        if(entrada == soma):
            return "Esse número pertence ao fibonacci"
        soma = numA + numB
        
        numA = numB
        
        numB = soma
    
    return "Esse número Não é fibonacci"
    
entrada = int(input("Insira um número:\n"))

print(fibonacci(entrada))
