import random
puan=0
devam=1


dosya=open("kelimeler.txt","r")
liste=dosya.read()
dosya.close()


liste=liste.split(":")
while devam==1:
        
    rast_no=random.randint(1,len(liste)-1)
    
    if rast_no%2==0:
        dil="ingilizce"
    else:
        dil="turkce"
        
    kelime=liste[rast_no]
    print "\n",liste[rast_no]
    
    if dil=="turkce":
        anlam=raw_input("ingilizcesini girin:")
        anlam=anlam+"\n"
        if liste[rast_no+1]==anlam:
            puan=puan+5
            print "dogru"
        else:
            puan=puan-5
            print "yanlis",liste[rast_no+1]


    elif dil=="ingilizce":
        anlam=raw_input("turkcesini girin:")
        if liste[rast_no-1]==anlam:
            puan=puan+5
            print "dogru"
        else:
            puan=puan-5
            print "yanlis",liste[rast_no-1]

    else:
        print "hata hata hata"

    print "puan= ",puan
    devam=input("devam etmek icin 1 e basin:")

