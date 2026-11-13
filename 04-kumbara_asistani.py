#klavyeden girilen dolar kuru ve dolar miktarını girerek TL karşılığını bulan program.

dolarKuru=float(input("Dolar kurunu gir : "))
dolarMiktari=float(input("Kaç doların var : "))

tlTutar=dolarKuru*dolarMiktari

print(f"{dolarMiktari} doların TL karşılığı {tlTutar} TL dir")