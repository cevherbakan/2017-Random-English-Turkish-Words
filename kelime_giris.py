while 1==1:
    turk_ayni=False
    ing_ayni=False
    kilit=True
    bit=0
    
    turkce=raw_input("kelimenin türkcesini giriniz:")
    ingilizce=raw_input("kelimenin ingilizcesini giriniz:")

    dosya=open("kelimeler.txt","r")
    liste=dosya.read()
    dosya.close()
    liste=liste.split(":")

    for i in range(len(liste)):
        
        
        if (liste[i]==turkce) and (liste[i+1]==ingilizce+"\n"):
           kilit=False
           break
        elif liste[i]==turkce:
            bit=bit+len(liste[i])+1
            turk_ayni=True
            satir=i/2
            break
        elif liste[i+1]==ingilizce:
            bit=bit+len(liste[i])
            bit=bit+len(liste[i+1])+1
            ing_ayni=True
            satir=(i+1)/2
            break
        else:
            bit=bit+len(liste[i])
            bit=bit+len(liste[i+1])+1
            pass
            
    if kilit==True:
        if turk_ayni==True:
            with open("kelimeler.txt", "r+") as f:
                f.seek(bit)
                f.writelines(","+ingilizce)

        elif ing_ayni==True:
            with open("kelimeler.txt", "r+") as f:
                f.seek(bit)
                f.writelines(","+turkce)
        else:    
            dosya=open("kelimeler.txt","a")
            dosya.write(":")
            dosya.write(turkce)
            dosya.write(":")
            dosya.write(ingilizce)
            dosya.write("\n")
            dosya.close()

    else:
        print "ayni kelime bir daha girilemez!!!"
    
    cikis=raw_input("cikmak icin 1 e basin devam etmek icin Enter basin:")
    
    if cikis=="1":
        break
    else:
        pass
