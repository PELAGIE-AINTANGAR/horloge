import time
import threading
 
current_time = [int(time.strftime("%H")), int(time.strftime("%M")), int(time.strftime("%S"))]
alarme_time=[]
print("voulez vous une alarm?")
reponse=input("reponse:")


           
def affiche_horloge():
    global current_time
    while True:
        if alarme_time[0]==current_time[0] and alarme_time[1]==current_time[1] and alarme_time[2]==current_time[2]:
            print("il est l'heure")
            break
        print(current_time)
        current_time[2] += 1
        if current_time[2]==60:
            current_time[2]=0
            current_time[1]+=1
        if current_time[1]==60:
            current_time[1]=0
            current_time[0]+=1
        if current_time[0]==24:
            current_time[0]=0
        time.sleep(1)

if reponse=="oui":
    alarme=input("Entrez des valeurs séparées par des virgules: ").split(',')
    alarme_time = [int(x) for x in alarme]
    affiche_horloge()  
else:
    affiche_horloge()
    




   
    

