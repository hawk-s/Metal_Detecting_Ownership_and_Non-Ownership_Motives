import requests
from bs4 import BeautifulSoup
import pandas as pd
#import openpyxl
#import lxml

#import pandas as pd




atribut_data = {}

sites_to_visit = []
base_url = "https://www.lovecpokladu.cz/katalog-minci?page="

#session1 = requests.Session()

#for i in reversed(range(6000,6749)):
for i in range(2499,3000):
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

        

         identifikovana_mince = atributy_artefaktu.table.tr.td.get_text()
        
        
         atribut_decompose = atributy_artefaktu.table.decompose()
        # atribut_lokalita = atributy_artefaktu.table.tr.td.get_text()
        # print(atributy_artefaktu)
        # print(atribut_lokalita)
         
         #print(identifikovana_mince)
         
         podminka_m_1 = atributy_artefaktu.find(text='Průměr:')

         podminka_m_2 = atributy_artefaktu.find(text='Váha:')
         
         podminka_m_3 = atributy_artefaktu.find(text='Území ražby:')

         podminka_m_4 = atributy_artefaktu.find(text='Panovník:')
         
         podminka_m_5 = atributy_artefaktu.find(text='Rok ražby:')

         podminka_m_6 = atributy_artefaktu.find(text='Nominál:')
         
         podminka_m_7 = atributy_artefaktu.find(text='Materiál:')

         podminka_m_8 = atributy_artefaktu.find(text='Č. mince:')
         
         
         if podminka_m_1 != None:


            mince_prumer = atributy_artefaktu.table.tr.td.get_text()

            atributy_artefaktu.table.tr.decompose()


         else:
            mince_prumer = 'None'
            
            
         if podminka_m_2 != None:


            mince_vaha = atributy_artefaktu.table.tr.td.get_text()

            atributy_artefaktu.table.tr.decompose()


         else:
            mince_vaha = 'None'
         
         if podminka_m_3 != None:
         #Mince uzemi razby:
             mince_uzemi_razby = atributy_artefaktu.table.tr.td.get_text()
             atributy_artefaktu.table.tr.decompose()
         else:
             mince_uzemi_razby = 'None'
            
         if podminka_m_4 != None:
             mince_panovnik = atributy_artefaktu.table.tr.td.get_text()
             atributy_artefaktu.table.tr.decompose()
         else:
             mince_panovnik = 'None'
            
         if podminka_m_5 != None:
             mince_rok_razby = atributy_artefaktu.table.tr.td.get_text()
             atributy_artefaktu.table.tr.decompose()
         else:
             mince_rok_razby = 'None'
            
         if podminka_m_6 != None:
             mince_nominal = atributy_artefaktu.table.tr.td.get_text()
             atributy_artefaktu.table.tr.decompose()
         else:
             mince_nominal = 'None'
            
         if podminka_m_7 != None:
             mince_material = atributy_artefaktu.table.tr.td.get_text()
             atributy_artefaktu.table.tr.decompose()
         else:
             mince_material = 'None'
            
         if podminka_m_8 != None:
             mince_cislo = atributy_artefaktu.table.tr.td.get_text()
             atributy_artefaktu.table.tr.decompose()
         else:
             mince_cislo = 'None'
            
         #◘print(identifikovana_mince, mince_vaha, mince_prumer, mince_uzemi_razby, mince_panovnik, mince_rok_razby, mince_nominal, mince_material, mince_cislo)
         
         atributy_artefaktu.table.decompose()
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
            
            
            ##the following is for the case when ther is more 'NoneName's, because
            ##the dictionary does not allow duplicates as keys...the key must be unique:


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

        data_transposed.to_excel('mince_2499-3000f_.xlsx', sheet_name='2499-3000')

        """
        def save_data_to_excel(data, max_cols=16000):
            wb = openpyxl.Workbook()
            ws = wb.active
            col_idx = 1
            for key, values in data.items():
                ws.cell(row=1, column=col_idx, value=key)
                for row_idx, value in enumerate(values, start=2):
                    ws.cell(row=row_idx, column=col_idx, value=value)
                col_idx += 1

                if col_idx > max_cols:
                    filename = f"data_{col_idx // max_cols}.xlsx"
                    wb.save(filename)
                    wb = openpyxl.Workbook()
                    ws = wb.active
                    col_idx = 1

            filename = f"data_newest_7_pokrac_{(col_idx - 1) // max_cols + 1}.xlsx"
            wb.save(filename)


        save_data_to_excel(atribut_data)"""
