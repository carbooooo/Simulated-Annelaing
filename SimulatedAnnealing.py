import random
import math
from random import randint
import matplotlib.pyplot as plt

def stampa_aula(aula):
    for i in range(0,8):
        print(f"Fila {i+1}:  ", end="")
        for j in range(0,8):
            print(f"{aula[i][j]}", end="  ")
        print()

def verifica_coordinate(x,y,aula):
    if(aula[x][y]==0):
        return True
    return False

def genera_disposizione(aula):

    secchioni = 10
    innamorati = 3
    bulli = 5
    nulla_facenti = 4

    while(secchioni+innamorati+bulli+nulla_facenti>0):
        tipo = randint(1,4)
        x = randint(0,7)
        y = randint(0,7)

        if(tipo==1):
            if(secchioni>0):
                if(verifica_coordinate(x,y,aula)):
                    aula[x][y] = 1
                    secchioni-=1
        elif(tipo==2):
            if(innamorati>0):
                if(verifica_coordinate(x,y,aula)):
                    aula[x][y] = 2
                    innamorati-=1
        elif(tipo==3):
            if(bulli>0):
                if(verifica_coordinate(x,y,aula)):
                    aula[x][y] = 3
                    bulli-=1
        else:
            if(nulla_facenti>0):
                if(verifica_coordinate(x,y,aula)):
                    aula[x][y] = 4
                    nulla_facenti-=1

def verifica_disposizione(disp):
    valore = [0,0,0,0,0,0,0,0]
    size = [0,0,0,0]
    for i in range(0,8):
        for j in range(0,8):

            # Controllo secchioni
            if(disp[i][j]==1):
                size[disp[i][j]-1]+=1
                if(i>=0 and i<=3):
                    valore[i]+=100
                    if((i>0 and i<7)and (j>0 and j<7)):
                        
                        if(disp[i][j+1]==1):
                            valore[i]+=20
                        if(disp[i+1][j]==1):
                            valore[i]+=20
                        if(disp[i-1][j+1]==1):
                            valore[i]+=20
                        if(disp[i][j-1]==1):
                            valore[i]+=20

                    elif(i==0):
                        if(disp[i+1][j]==1):
                            valore[i]+=15
                    elif(j==0):
                        if(disp[i][j+1]==1):
                            valore[i]+=15
                    elif(i==7):
                        if(disp[i-1][j]==1):
                            valore[i]+=15
                    elif(j==7):
                        if(disp[i][j-1]==1):
                            valore[i]+=15
                else:
                    valore[i]+=2

            # Controllo innamorati
            elif(disp[i][j]==2):
                size[disp[i][j]-1]+=1
                if(i>=4 and (j<=3 and j>=6)):
                    valore[i]+=80
                    if((i>0 and i<7)and (j>0 and j<7)):
                        if(disp[i][j+1]==0 or disp[i][j+1]==2):
                            valore[i]+=25
                        if(disp[i+1][j]==0 or disp[i+1][j]==2):
                            valore[i]+=25
                        if(disp[i-1][j]==0 or disp[i-1][j]==2):
                            valore[i]+=25
                        if(disp[i][j-1]==0 or disp[i][j-1]==2):
                          valore[i]+=25
                elif(i==0):
                    valore[i]+=3   
                else:
                    valore[i]+=1                                   
            
            # Controllo bulli
            elif(disp[i][j]==3):
                size[disp[i][j]-1]+=1
                if(i>=5 and i<7):
                    valore[i]+=90
                if((i>0 and i<7)and (j>0 and j<7)):
                    if(disp[i][j+1]==4 or disp[i][j+1]==1):
                        valore[i]+=30
                    if(disp[i+1][j]==4 or disp[i+1][j]==1):
                        valore[i]+=30
                    if(disp[i-1][j]==4 or disp[i-1][j]==1):
                        valore[i]+=30
                    if(disp[i][j-1]==4 or disp[i][j-1]==1):
                        valore[i]+=30
                if(i==1 or i==7):
                    valore[i]+=5 
            
            # Controllo nullafacenti
            elif(disp[i][j]==4):
                size[disp[i][j]-1]+=1
                if(i==7):
                    valore[i]+=100
                    if((i>0 and i<7)and (j>0 and j<7)):
                        if(disp[i][j+1]==3):
                            valore[i]+=15
                        if(disp[i+1][j]==3):
                            valore[i]+=15
                        if(disp[i-1][j]==3):
                            valore[i]+=15
                        if(disp[i][j-1]==3):
                            valore[i]+=15
                        else:
                            valore[i]+=2
                else:
                    valore[i]+=1 
    
    return valore


def scelta_soluzione(delta_energia, temperatura):
    """
    Calcola la probabilità di accettare una soluzione peggiore secondo la formula di Metropolis.

    Parametri:
    - delta_energia: Differenza di energia tra la nuova soluzione e la soluzione corrente.
    - temperatura: Temperatura corrente del sistema.

    Ritorna:
    - probabilita: Probabilità di accettare la soluzione peggiore.
    """
    if delta_energia < 0:
        # Se la nuova soluzione è migliore, accettala sempre.
        return True
    else:
        # Calcola la probabilità di accettare una soluzione peggiore.

        if((random.uniform(0,1))<=(math.exp(-delta_energia / temperatura))):
            return True
        else:
            return False

    
MAX_ATTEMPTS = 10000  # Iterazioni massime che può fare il programma
TEMPERATURE = 1000# Temperatura
K = 0.999 # Costante per dimiunuire la temperatura

aula = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
genera_disposizione(aula)
stampa_aula(aula)
punti_aula = []
punti_aula_i = []
y = []
x = []
soglia=10000

while(MAX_ATTEMPTS>0 and TEMPERATURE>0.0001):

    aula_ipotetica = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    
    genera_disposizione(aula_ipotetica)
    punti_aula = verifica_disposizione(aula)
    punti_aula_i = verifica_disposizione(aula_ipotetica)

    for k in range(0,8):
        if(scelta_soluzione((punti_aula[k]-punti_aula_i[k]),TEMPERATURE)):
            aula[k]=aula_ipotetica[k]

    # Aggiungo i dati al grafico
    if(MAX_ATTEMPTS==soglia):
        soglia-=500
        x.append(10000-MAX_ATTEMPTS)
        y.append(sum(punti_aula))

    if(MAX_ATTEMPTS==5000):
        print()
        stampa_aula(aula)

    MAX_ATTEMPTS-=1
    TEMPERATURE*=K

# Inserisco i dati delle coordinate
plt.plot(x, y)

# Imposto vari titoli
plt.xlabel('Iterazioni')
plt.ylabel('Valore Funzione Obbiettivo')
plt.title('Grafico Funzione Obbiettivo')

# Stampo la matrice con la disposizione
print()
print("Ecco la disposizione migliore per gli studenti:")
print()
stampa_aula(aula)
print()

# Visualizzo il grafico
plt.show()