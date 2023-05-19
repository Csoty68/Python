#---------------------2. Program---------------------

#   pip install forex-python
#   pip install python-pyfiglet

from forex_python.converter import CurrencyRates
from pyfiglet import Figlet

f = Figlet(font='slant')
print (f.renderText('Currency Converter'))

cr = CurrencyRates()

print("------------------------------------------------")

amount = int(input("Add meg kérlek az összeget amit át szeretnél váltani: "))

print("------------------------------------------------")

from_currency = input("Add meg kérlek a pénznem kódját amiből váltasz: ").upper()

print("------------------------------------------------")

to_currency = input("Add meg kérlek a pénznem kódját amibe váltani szeretnél: ").upper()

print("------------------------------------------------")

print(amount, from_currency,"-t váltasz", to_currency,"-ba/be")

print("------------------------------------------------")

output = cr.convert(from_currency, to_currency, amount)

print("------------------------------------------------")

print("Az Átváltás eredménye:", round(output,2), to_currency)

print("------------------------------------------------")
