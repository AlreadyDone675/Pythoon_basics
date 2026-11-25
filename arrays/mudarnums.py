from time import sleep as s

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
forca = 1
teste = 1
while True:    
    s(0.5)
    forca += 0.1
    teste = teste*forca
    if teste > 36:
        teste = teste + 1
        forca = 1
        print(teste)

        if teste > 40:
            s(1)
            teste = teste + 1
            forca = 0
            
    if teste < 36:
        print(teste)
        teste += 1
        forca += 0.05
        

