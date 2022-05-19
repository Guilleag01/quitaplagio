try:
    from googletrans import Translator
except:
    print ("No se ha podido importar el módulo googletrans, por favor instálelo con \"pip install googletrans==3.1.0a0\"")
    raise SystemExit(0)

def main():
    texto = input("Introduce el texto: ")
    iteraciones = int(input("introduce el número de iteraciones (a mas iteraciones menos se parecerá al original pero perderá mas el sentido): "))
    lenguages = ['en', 'fr', 'it', 'de', 'fi', 'el', 'ca', 'zh-cn', 'ja'] # 9
    numLenguages = len(lenguages)
    translator = Translator()
    texto = translator.translate(texto, dest='en', src='es').text

    for a in range(iteraciones):
        longBarra = 50
        print("\r", end = "")
        barra = int((a + 1) * longBarra / iteraciones)
        for j in range(barra):
            print("█", end = "")
        for j in range(longBarra-barra):
            print("░", end = "")
        print(" " + "{:.2f}".format((a + 1) * 100 / iteraciones) + "% (" + str(a + 1) + " / " + str(iteraciones) + ")" , end = "")

        texto = translator.translate(texto, dest=lenguages[(a+1) % numLenguages], src=lenguages[a % numLenguages]).text
        
    texto = translator.translate(texto, dest='es', src=lenguages[iteraciones % numLenguages]).text

    print("\n\nRESULTADO: " + texto + "\n")

if __name__ == "__main__":
    main()