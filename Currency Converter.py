#Adam Baker
#6.7.17
#Currency Converter Test
git+ssh://git@github.com/lxml/lxml.git lxml
from lxml import html
import requests
##import time
##print('Launching Arc OS v1.11,Installing Required Data')
##print('10101010010101010100101010010101001010101010010')
##time.sleep(0.5)
##print()
##print('java-147.exe has been damaged creating new file java-871.exe')
##time.sleep(1.5)
##print('launching new file...')
##time.sleep(0.5)
##print('file created and launched succsefuly')
##time.sleep(0.5)
##print('continuing with launch process')
##time.sleep(0.5)
##print('retrying launch of Arc OS v1.09')
##time.sleep(1.5)
##print('succsessful, tried 3 times')
##time.sleep(0.5)
##print('downloading -Currency Converter-')
##time.sleep(2)
##print('download complete')
##time.sleep(0.5)
##print('launching selected program')
##time.sleep(1)
##print('launch finished')
##time.sleep(0.5)
##print('opening window')
##time.sleep(1.5)
##print()
##print('----------------------------------------------------------------------')
##print()
##print('Welcome to the Currency Converter!')
##repeat = 'true'
##time.sleep(0.2)
##def gorun():
##    go = input('Do you want to run again? [yes] [no] ')
##    if go.lower() == 'yes':
##        code()
##    elif go.lower() == 'no':
##        print('Goodbye <o/')
##    else:
##        print('Please Listen To Me')
##        gorun()
##def code():
##    print('Be Aware That This Calculator Is Not 100% Accurate Due To Roundings And Convertion Rates')
##    currency = input('What Currency Would You Like? [yen] [bitcoin] [dollar] ')
##    if currency.lower() == ('bitcoin'):
##        print('-Downloading Conversion Rates-')
##        time.sleep(1)
##        print('-Found 1839.95 for One Bitcoin-')
##        time.sleep(1.5)
##        money = float(input('Please Input The Amount Of £ You Want To Convert: '))
##        calc = (money/1837.18)
##        total = round(calc,2)
##        print ('Ƀ',total)
##        gorun()
##    elif currency.lower() == ('yen'):
##        print('-Downloading Conversion Rates-')
##        time.sleep(1)
##        print('-Found 0.0068 for One Yen-')
##        time.sleep(1.5)
##        money = float(input('Please Input The Amount Of £ You Want To Convert: '))
##        calc = (money/0.0068)
##        total = round(calc,2)
##        print ('¥',total)
##        gorun()
##    elif currency.lower() == ('dollar'):
##        print('-Downloading Conversion Rates-')
##        time.sleep(1)
##        print('-Found 0.77 for One Dollar-')
##        time.sleep(1.5)
##        money = float(input('Please Input The Amount Of £ You Want To Convert: '))
##        calc = (money/0.77)
##        total = round(calc,2)
##        print ('$',total)
##        gorun()
##    else:
##        print('Please enter a correct currnecy i.e yen')
##        code()
##code()
## <a href="/currencycharts/?from=XBT&amp;to=GBP" onmousedown="ga('send','event','RatesTable','Flyout','Open');" rel="GBP,XBT,4,3">1826.59</a>       
page = requests.get('http://www.xe.com/?c=XBT')
tree = html.fromstring(page.content)  
buyers = tree.xpath("//a[@href='/currencycharts/?from=XBT&amp;to=GBP' onmousedown='ga('send','event','RatesTable','Flyout','Open');' rel='GBP,XBT,4,3']/text()'")     
