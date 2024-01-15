
from pytube import YouTube,Search,Stream
import datetime
import time
import os





def buscarVideo(busqueda):
    

    s1 = Search(busqueda)
    os.system('clear')
    i=0

    videos=[]

    for e in s1.results:
        if e.length != 0:
            videos.append(e)
            print("cargando video...")
    print('Busqueda completada')
    os.system('clear') 



    videos=videos[:10]
    print("RESULTADO PARA: ",busqueda)
    for e in videos:
        i+=1
        print('[VIDEO ',i,']')
        print('|TITULO: ',e.title)
        print('|CANAL: ', e.author)
        if e.length > 3600:
            duracion = datetime.timedelta(seconds=e.length)
            print('|DURACIÓN: ',duracion)
        else:
            duracion = datetime.timedelta(seconds=e.length)
            minutos, segundos = divmod(duracion.seconds, 60)
            print('|DURACIÓN: ',f'{minutos}:{segundos}',)

        print('|VISITAS: ',e.views)
        print('|----------------------------------------------------------------------------')
    
    lecturaVideo=input('Elija el video que desea descargar: ')   
    lecturaVideo = int(lecturaVideo)
    while lecturaVideo <= 0 or lecturaVideo > 10:
        print('ERROR: Ese video no existe')
        lecturaVideo=int(input('Elija el video que desea descargar: '))
    video = videos[lecturaVideo-1].streams.get_highest_resolution()
    
   
   
    print('DESCARGANDO VIDEO:', video.title)
    print('Espere unos segundos')
    video.download(output_path='./Videos')
    print('VIDEO DESCARGADO')
    time.sleep(1)  
    os.system('clear')


def descargarPorURL(url):
    video = YouTube(url).streams.get_highest_resolution()
    print('DESCARGANDO VIDEO:', video.title)
    print('Espere unos segundos')
    
    if video.title != '':  
        video.download(output_path='./Videos') 
        time.sleep(1)  

        print('VIDEO DESCARGADO')
        os.system('clear')
    else:
        print('NO SE HA PODIDO DESCARGAR EL VIDEO')
        time.sleep(1)  
        
    
    

def main():  
    
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    print("    ___________       _     __               ")
    print("   / ____/__  /_   __(_)___/ /__  ____  _____")
    print("  / __/    / /| | / / / __  / _ \/ __ \/ ___/")
    print(" / /___   / /_| |/ / / /_/ /  __/ /_/ (__  ) ")
    print("/_____/  /____/___/_/\__,_/\___/\____/____/  ")
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    print("by carmeloDEV")
    
    
    print('1.Convertir video por URL')
    print('2.Buscar video')
    print('3.Salir')
    
    
    lectura = int(input('Elija una opcion:'))
    
    while lectura!=3:
        
        if lectura == 2:
            busqueda=input('Bucar: ')
            buscarVideo(busqueda)
            
            
        if lectura == 1:
            url=input('Inserte URL: ')
            descargarPorURL(url)
            
        
        
        while lectura <= 0 or lectura>3:
            os.system('clear')
            print("+++++++++++++++++++++++++++++++++++++++++++++")
            print("    ___________       _     __               ")
            print("   / ____/__  /_   __(_)___/ /__  ____  _____")
            print("  / __/    / /| | / / / __  / _ \/ __ \/ ___/")
            print(" / /___   / /_| |/ / / /_/ /  __/ /_/ (__  ) ")
            print("/_____/  /____/___/_/\__,_/\___/\____/____/  ")
            print("+++++++++++++++++++++++++++++++++++++++++++++")
            print("by carmeloDEV")
            
            
            print('1.Convertir video por URL')
            print('2.Buscar video')
            print('3.Salir')
            
            lectura = int(input('Elija una opcion correcta:'))
        os.system('clear')
        print("+++++++++++++++++++++++++++++++++++++++++++++")
        print("    ___________       _     __               ")
        print("   / ____/__  /_   __(_)___/ /__  ____  _____")
        print("  / __/    / /| | / / / __  / _ \/ __ \/ ___/")
        print(" / /___   / /_| |/ / / /_/ /  __/ /_/ (__  ) ")
        print("/_____/  /____/___/_/\__,_/\___/\____/____/  ")
        print("+++++++++++++++++++++++++++++++++++++++++++++")
        print("by carmeloDEV")
            
            
        print('1.Convertir video por URL')
        print('2.Buscar video')
        print('3.Salir')
        lectura = int(input('Elija una opcion:'))
    
    os.system('clear')
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    print("    ___________       _     __               ")
    print("   / ____/__  /_   __(_)___/ /__  ____  _____")
    print("  / __/    / /| | / / / __  / _ \/ __ \/ ___/")
    print(" / /___   / /_| |/ / / /_/ /  __/ /_/ (__  ) ")
    print("/_____/  /____/___/_/\__,_/\___/\____/____/  ")
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    print("by carmeloDEV")
    return print('GRACIAS POR UASR EZvideos, ten un buen dia')
main()








                                             
