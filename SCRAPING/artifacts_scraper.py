# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 15:06:30 2023

@author: janhr
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
#import openpyxl
#import lxml

#import pandas as pd




atribut_data = {}

sites_to_visit = []
base_url = "https://www.lovecpokladu.cz/artefakty/c/?page="

#session1 = requests.Session()

#for i in reversed(range(6000,6749)):
for i in range(4973,5003):
    site = f"{base_url}{i}"
    sites_to_visit.append(site)

for url in sites_to_visit:
    response = requests.get(url)
    artefaktsoup = BeautifulSoup(response.content, "lxml")


    nalezy = artefaktsoup.find('section', class_='optimize_columns')
    #nalez_jmeno = nalezy.article.div.header.h3.a.get_text()

    nalezy_links = nalezy.find_all('a', class_='image')

    #print(nalezy_links)

    prefix = 'https://www.lovecpokladu.cz'


    links = []


    for a in nalezy_links:
        if a.has_attr('href'):
            a.get('href')

            ##print(img.get('title'))
            href = a.get('href')
            #href = a.get('href').replace('"', '').replace('"', '')
            #print(href)
            wow = links.append(prefix + href)
            #print(wow)

    #session2 = requests.Session()

    for link in links:
        lovec = requests.get(link)
        artefakty_soup = BeautifulSoup(lovec.content, "lxml")   #soup z jednotlivych stranek artefaktu - 6749 


#print(artefaktsoup)

        #print(artefakty_soup)

        atributy_artefaktu = artefakty_soup.find('article', class_='row')
        if atributy_artefaktu != None:
         if atributy_artefaktu.h1 != None:
          atribut_name = atributy_artefaktu.h1.get_text()  ##this gives the name of the atribute from the 1st site

         else:
            for m in range(0, 16000):
                atribut_name = 'NoneName' + str(m)
            # print('')
        # print('')
        # print(atribut_name)




         pocet_liku = atributy_artefaktu.find('div', class_='clearfix')

        #print(atribut_name)

        #print(pocet_liku)

         pocet_liku_cislo = pocet_liku.find('div', id='likes_num_bar').get_text()  ##this gives the number of likes

        # print('Liků: ', pocet_liku_cislo)

         zobrazeno = atributy_artefaktu.find('footer', id='finding_footer')

         zobrazeno_kolikrat = zobrazeno.dl.dd.get_text()
        # print('Zobrazeno: ', zobrazeno_kolikrat)

         zobrazeno.dl.dd.decompose()

         atribut_pocet_komentaru = zobrazeno.dl.dd.get_text()

        # print('Okomentováno: ', atribut_pocet_komentaru)

         zobrazeno.dl.dd.decompose()

         if zobrazeno.dl.dd.strong.a != None:

            nalezce = zobrazeno.dl.dd.strong.a.get_text()

         elif zobrazeno.dl.dd.strong != None:

            nalezce = zobrazeno.dl.dd.strong.get_text()

         else: nalezce = 'None'

         #print(nalezce)



        # print('Nálezce: ', nalezce)

        # print(zobrazeno)

         zobrazeno.dl.decompose()
         #print(zobrazeno)
         podminka_0 = zobrazeno.find(text='vyfotografováno: ')
         podminka_1 = zobrazeno.find(text='vloženo: ')
         #print(zobrazeno.dl)

         if podminka_0 != None:

            vyfotografovano = zobrazeno.dl.dd.get_text()

            # print('Vyfotografováno: ', vyfotografovano)

            zobrazeno.dl.dd.decompose()

         else:
            vyfotografovano = 'None'

         if podminka_1 != None:

            vlozeno = zobrazeno.dl.dd.get_text()

         else:
            vlozeno = 'None'

        #print('Vlozeno: ', vlozeno)

        

         atribut_decompose = atributy_artefaktu.table.decompose()
        # atribut_lokalita = atributy_artefaktu.table.tr.td.get_text()
        # print(atributy_artefaktu)
        # print(atribut_lokalita)

        ##the following gives okolnosti nalezu, jako lokalita, stav pudy, hloubka nalezu a pouzity detektor:

         podminka1 = atributy_artefaktu.find(text='Lokalita:')

         podminka2 = atributy_artefaktu.find(text='Stav půdy:')

         podminka3 = atributy_artefaktu.find(text='Hloubka nálezu:')

         podminka4 = atributy_artefaktu.find(text='Použitý detektor:')

         podminka5 = atributy_artefaktu.find(text='Odevzdáno do:')





         if atributy_artefaktu.table != None:
            if atributy_artefaktu.table.tr != None:
                if atributy_artefaktu.table.tr.td != None:
                    if podminka1 != None:


                       atribut_lokalita = atributy_artefaktu.table.tr.td.get_text()

                       atributy_artefaktu.table.tr.decompose()

            # print('Lokalita: ', atribut_lokalita)
                    else:
                       atribut_lokalita = 'None'
                else:
                       atribut_lokalita = 'None'
            else:
                       atribut_lokalita = 'None'
         else:
                       atribut_lokalita = 'None'
         # print('Lokalita: ', atribut_lokalita)




         if atributy_artefaktu.table != None:
          if atributy_artefaktu.table.tr != None:
            if atributy_artefaktu.table.tr.td != None:

             if podminka2 != None:
               atribut_stav_pudy = atributy_artefaktu.table.tr.td.get_text()

               atributy_artefaktu.table.tr.decompose()

            # print('Stav půdy: ', atribut_stav_pudy)
             else:
               atribut_stav_pudy = 'None'
            else:
               atribut_stav_pudy = 'None'
          else:
               atribut_stav_pudy = 'None'
         else:
               atribut_stav_pudy = 'None'

            # print('Stav půdy: ', atribut_stav_pudy)



         if atributy_artefaktu.table != None:
          if atributy_artefaktu.table.tr != None:
            if atributy_artefaktu.table.tr.td != None:

             if podminka3 != None:
               atribut_hloubka_nalezu = atributy_artefaktu.table.tr.td.get_text()

               atributy_artefaktu.table.tr.decompose()

              # print('Hloubka nálezu: ', atribut_hloubka_nalezu)
             else:
               atribut_hloubka_nalezu = 'None'
            else:
                atribut_hloubka_nalezu = 'None'
          else:
                atribut_hloubka_nalezu = 'None'
         else:
            atribut_hloubka_nalezu = 'None'
        # print('Hloubka nálezu: ', atribut_hloubka_nalezu)   ##this is the right one print, not that above.

        # print(atributy_artefaktu.table.tr.td)



         if atributy_artefaktu.table != None:
          if atributy_artefaktu.table.tr != None:
            if atributy_artefaktu.table.tr.td != None:

                if podminka4 != None:
                 atribut_pouzity_detektor = atributy_artefaktu.table.tr.td.get_text()

                 atributy_artefaktu.table.tr.decompose()

                    # print('Použitý detektor: ', atribut_pouzity_detektor)
                else:
                  atribut_pouzity_detektor = 'None'
            else:
                atribut_pouzity_detektor = 'None'
          else:
                  atribut_pouzity_detektor = 'None'
         else:
            atribut_pouzity_detektor = 'None'
                    # print('Použitý detektor: ', atribut_pouzity_detektor)




         if atributy_artefaktu.table != None:
            if atributy_artefaktu.table.tr != None:
             if atributy_artefaktu.table.tr.td != None:
                if podminka5 != None:
                 odevzdano_do = atributy_artefaktu.table.tr.td.get_text()

                    # print('Použitý detektor: ', atribut_pouzity_detektor)
                else:
                 odevzdano_do = 'None'
             else:
                 odevzdano_do = 'None'
            else:
                odevzdano_do = 'None'
         else:
            odevzdano_do = 'None'

        else:
            for m in range(0, 16000):
                atribut_name = 'NoneName' + str(m)
            #atribut_name = ['NoneName' + str(m) for m in range(0, 16000)]  



        atribut_data[atribut_name + ' ; ' + str(zobrazeno_kolikrat) + str(vlozeno)] = [pocet_liku_cislo, zobrazeno_kolikrat,
                                                                    atribut_pocet_komentaru, nalezce,
                                                                    vyfotografovano, vlozeno, atribut_lokalita,
                                                                    atribut_stav_pudy,
                                                                    atribut_hloubka_nalezu, atribut_pouzity_detektor,
                                                                    odevzdano_do]
        print(nalezce)
        print(vyfotografovano)
        print(vlozeno)

        data = pd.DataFrame.from_dict(atribut_data)
        data_transposed = data.T

        #print(data)

        data_transposed.to_excel('artefakty_4974-5003.xlsx', sheet_name='4974-5003')