import requests
from bs4 import BeautifulSoup

with open('sample.csv','w') as f:

    for i in range(5): #the nomber of the pages

        result = requests.get('https://example.com/page/{}/'.format(i))
        print(result)
        soup = BeautifulSoup(result.text, 'html.parser')
        list = soup.find_all('h2', class_='entry-title2') #tag name and class name you want to search

        for h2 in list:
            data = h2.a['title'] #title attr inside <a> inside <h2>
            f.write('{0}\n'.format(data)) #write into csv file










    










# with open('surasura-sample.csv','w') as f:


#     f.write('"{0}","{1}"\n'.format('language',' title'))

#     for a in presentation_list:
#         row_text = a.h3.get_text()

#         if '(en)' in row_text:
#             lang = 'english'
#             new_title = row_text.replace('\xa0(en)', '')


#         if '(ja)' in row_text:
#             lang = 'japanese'
#             new_title = row_text.replace('\xa0(en)', '')

#         f.write('"{0}","{1}"\n'.format(lang, new_title)) 



# 
#     r = f.read()
#     f.write(r)