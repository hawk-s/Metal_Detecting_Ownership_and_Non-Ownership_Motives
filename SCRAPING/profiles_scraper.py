import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
prefix = "https://www.lovecpokladu.cz/uzivatel/"

zebricek = requests.get("https://www.lovecpokladu.cz/lovci-historie/zebricky-cele").text

soup = BeautifulSoup(zebricek, "html.parser")
# print(soup)

lovec = soup.find('div', class_="column_right")

# print(lovec)


lovec1 = lovec.a
lovec1attrs = lovec.a.attrs
lovec1name = lovec.a.name

# print(lovec1)

# print(lovec1attrs)

# print(lovec1name)


lovec_links = lovec.find_all('img')

# print(lovec_links)

links = []

# for child in lovec_links.td.children:
# print(child)

for img in lovec_links:
    if img.has_attr('title'):
        img.get('title')

        ##print(img.get('title'))

        title = img.get('title')
        wow = links.append(prefix + title)
        # print(wow)

        # links_list = list(img.get('title'))
        # wow = links.append(prefix+links_list)
        # print(wow)

# print(type(img.get('title')))


# appended_links = links.append(prefix+img['title'])
# print(appended_links)


##empty dictionary:
lovec_data = {}

for link in links:
    lovec = requests.get(link)
    turtle = BeautifulSoup(lovec.content, "html.parser")         ## this should be soup from the each profiles site
    # print(turtle)

    ####till here it is ok!!

    lovec_name = turtle.h1.get_text()
    # print(lovec_name)

    lovec_attr = turtle.find('table', class_='simple align_top')

    # print(lovec_attr)
    # if lovec_attr.find('td') is not 'None':

    lovecc = lovec_attr.find_all('td')

    # loveccc = lovec_attr.select('tr > td')

    # print(lovecc)



    uuu = turtle.find(text ='Město:')

    #print(uuu)

    tag = lovec_attr.td

    if lovec_attr.td != None:
        if uuu != None:
          tag.name = "ies"

        # print(tag)



          #print(lovecik_mesto)



        #print(lovecik_odkaz)

    ouu = turtle.find(text='Detektor:')
    tag2 = lovec_attr.td

    if lovec_attr.td != None:
        if ouu != None:
          tag2.name = "no"

             #print(tag2)

          lovec_detik = lovec_attr.find_all('no')

            #print(lovecik_detik)

          zkusenost = turtle.find('span', class_='points').get_text()
          lovec_odkaz = lovec_attr.select('td > ul')
          lovec_mesto = lovec_attr.find_all('ies')

          # print(zkusenost)






           #pocet_komentaru = turtle.select('p')

           #lovec_attr = turtle.find('table', class_='simple align_top')

          ahoj = turtle.find('p')

          ahoj.decompose()
           # print(ahoj)

           # tag3 = ahoj.a
             # tag3.name = 'alee'
             #print(tag3)


          bhoj = turtle.p
          bhoj.decompose()
          # print(bhoj)

          choj = turtle.p
          choj.decompose()
          # print(choj)

          dhoj = turtle.p

          pocet_clanku_nebo_prispevku = dhoj.strong.get_text()

          dhoj.decompose()
            #print(dhoj)

          ehoj = turtle.p
          #print(ehoj)

          pocet_komentaru = ehoj.strong.get_text()

          #ehoj.decompose()
          
          
          art_a_minc = turtle.find('article', class_='row')
          artaminc = art_a_minc.find('a', class_='nice-button')
          #print(artaminc)
          if artaminc != None:
              pod1 = artaminc.find(string=re.compile('artefaktů'))
          else:
              pod1 = None
          #print(pod1)
          

          if pod1 != None:
              pocet_artefaktu = artaminc.get_text().replace('Zobrazit', '').replace('artefaktů', '') 

              artaminc.decompose()
          else:
              pocet_artefaktu = 'nula_a'
              
              
          artaminc = art_a_minc.find('a', class_='nice-button')
          if artaminc != None:
              pod2 = artaminc.find(string=re.compile('mincí'))   
          else:
              pod2 = None
          
            
          if pod2 != None:
              pocet_minci = artaminc.get_text().replace('Zobrazit', '').replace('mincí', '')
              
          else:
              pocet_minci = 'nula_m'
          

          # print(pocet_komentaru)

          ##lovec_data[lovec_name] = [pocet_minci]   ##19.1.23

          lovec_data[lovec_name] = [lovec_mesto, lovec_detik, lovec_odkaz, zkusenost, pocet_clanku_nebo_prispevku,
                                    pocet_komentaru, pocet_artefaktu, pocet_minci]
          # print(lovec_data)

          # for sibling in lovec_attr.previous_siblings:
          # print(repr(sibling))

          # print(len(lovec_data))



          data = pd.DataFrame.from_dict(lovec_data)
          data_t = data.T

          print(data)

          data_t.to_excel('data_lovci_final_TTT.xlsx', sheet_name='Sheet1')
