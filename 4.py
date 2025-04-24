import datetime
import locale
locale.setlocale(locale.LC_ALL, "")
date = datetime.datetime.strptime(input('dd.mm.yyyy\n'),'%d.%m.%Y')
def product(date):
    date = datetime.datetime.strptime(date,'%A,%d %B,%Y год')
    print(date)
product(date)