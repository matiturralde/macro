# encoding: utf-8

# Websites

from bs4 import BeautifulSoup
import requests
import datetime
today = datetime.date.today()
import numpy as np
import pandas as pd
from pandas import Series
from pandas import DataFrame

page_bcra= requests.get("http://www.bcra.gov.ar/PublicacionesEstadisticas/Principales_variables.asp")
soup_bcra = BeautifulSoup(page_bcra.content, 'html.parser')

#page_bcra_02= requests.get("http://www.bcra.gov.ar/Pdfs/Prensa_comunicacion/LELIQ.xml")
#soup_bcra_02 = BeautifulSoup(page_bcra_02.content, 'html.parser')

page_bna = requests.get("http://www.bna.com.ar/")
soup_bna = BeautifulSoup(page_bna.content, 'html.parser')

page_bolsar = requests.get("https://www.bolsar.com/vistasdl/paginachequespagodiferido.aspx")
soup_bolsar = BeautifulSoup(page_bolsar.content, 'html.parser')

page_bind = requests.get("https://capitaldetrabajo.bind.com.ar/?gclid=EAIaIQobChMI-_-s_t7L2wIVhgiRCh2I1QQ_EAAYBCAAEgLA1vD_BwE#/home")
soup_bind = BeautifulSoup(page_bind.content, 'html.parser')

page_rofex= requests.get("http://www.rofex.com.ar/", verify=False)
soup_rofex = BeautifulSoup(page_rofex.content, 'html.parser')

page_indec = requests.get("https://www.indec.gob.ar/index.asp")
soup_indec = BeautifulSoup(page_indec.content, 'html.parser')

page_mav= requests.get("http://www.mav-sa.com.ar")
soup_mav = BeautifulSoup(page_mav.content, 'html.parser')

#page_ciudad = requests.get("https://www.bancociudad.com.ar/institucional/pymes/Prestamos/Ciudad%20Productiva")
#soup_ciudad = BeautifulSoup(page_ciudad.content, 'html.parser')

page_santanderrio = requests.get("https://www.santanderrio.com.ar/banco/online/personas/acerca-de-nosotros/legales/comisiones-BCRA")
soup_santanderrio = BeautifulSoup(page_santanderrio.content, 'html.parser')

page_tasasnacion = requests.get("https://docs.google.com/a/credility.com/spreadsheets/d/e/2PACX-1vQO9BxwDGXL5EIr0rAohUuAr10Fi3hiYPHQfTNCN17opmNz2IGHiSKEEPTFR-3FvYbPQKmEi1Dw6Hoh/pubhtml/sheet?headers=false&gid=0")
soup_tasasnacion = BeautifulSoup(page_tasasnacion.content, 'html.parser')

url_ciudad_01 = 'https://www.bancociudad.com.ar/cms/archivo/institucional/menu/INSTITUCIONAL/Normativa/Tasasycomisiones/solapasPersonalizadas/OTRAS%20TASAS%20Y%20COMISIONES/archivos/'
url_ciudad_02 = str(today.strftime('%Y%m%d'))
url_ciudad_03 = '%20TasasComercialeseIndividuos.pdf'
url_ciudad = str(url_ciudad_01+url_ciudad_02+url_ciudad_03)
#url_ciudad = 'https://www.bancociudad.com.ar/cms/archivo/institucional/menu/INSTITUCIONAL/Normativa/Tasasycomisiones/solapasPersonalizadas/OTRAS%20TASAS%20Y%20COMISIONES/archivos/20190621%20TasasComercialeseIndividuos.pdf'

page_puente= requests.get("https://www.puentenet.com/cotizaciones/riesgo-pais")
soup_puente = BeautifulSoup(page_puente.text, 'html.parser')

import re
from urllib.request import urlopen
from urllib.request import urlretrieve

html = urlopen("https://www.bancoprovincia.com.ar/CDN/Get/A5388_Banca_Empresa_tasas_costos_condiciones_vigentes")
html_doc = html.read()
pdf_url = "https://www.bancoprovincia.com.ar/CDN/Get/A5388_Banca_Empresa_tasas_costos_condiciones_vigentes"

urlretrieve(pdf_url, "download.pdf")

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

# Data

bcra_base_fecha = str(soup_bcra.find_all('td')[3].get_text).split('>')[1].split('<')[0]
bcra_base = str(soup_bcra.find_all('td')[4].get_text).split('>')[1].split('<')[0]
bcra_reservas_fecha = str(soup_bcra.find_all('td')[6].get_text).split('>')[1].split('<')[0]
bcra_reservas = str(soup_bcra.find_all('td')[7].get_text).split('>')[1].split('<')[0]
bcra_leliq_fecha = str(soup_bcra.find_all('td')[24].get_text).split('>')[1].split('<')[0]
bcra_leliq = str(soup_bcra.find_all('td')[25].get_text).split('>')[1].split('<')[0]
bcra_badlar_fecha = str(soup_bcra.find_all('td')[27].get_text).split('>')[1].split('<')[0]
bcra_badlar = str(soup_bcra.find_all('td')[28].get_text).split('>')[1].split('<')[0]
bcra_depositos_fecha = str(soup_bcra.find_all('td')[71].get_text).split('>')[1].split('<')[0]
bcra_depositos = str(soup_bcra.find_all('td')[72].get_text).split('>')[1].split('<')[0]

tna_bind =str(soup_bind.find_all('p')[0])
tna_bind_2 = tna_bind.split("anual: ",1)[1]
bind = tna_bind_2[0:3]

print('Base Monetaria:', bcra_base_fecha, '-', bcra_base)
print('Reservas:', bcra_reservas_fecha, '-', bcra_reservas)
print('Leliqs:', bcra_leliq_fecha, '-', bcra_leliq)
print('Badlar:', bcra_badlar_fecha, '-', bcra_badlar)
print('Depositos:', bcra_depositos_fecha, '-', bcra_depositos)
print ()

fecha_riesgo = (str(soup_puente.find_all('td')[3].get_text).split('>')[1].split('<')[0]).strip()
riesgo = int(str(soup_puente.find_all('td')[1].get_text).split('>')[1].split('<')[0])

print('Riesgo País:', fecha_riesgo, '-', riesgo)
print ()

dolar_compra = soup_bna.find_all('td')[1].get_text()
dolar_venta = soup_bna.find_all('td')[2].get_text()

print ('Dolar Comprador: ', dolar_compra)
print ('Dolar Vendedor: ', dolar_venta)
print ()

print ('Tasa Bind: ', bind)
print ()

rofex_01_fecha = soup_rofex.find_all('td')[0].text
rofex_01_value = soup_rofex.find_all('td')[1].text
rofex_02_fecha = soup_rofex.find_all('td')[5].text
rofex_02_value = soup_rofex.find_all('td')[6].text
rofex_03_fecha = soup_rofex.find_all('td')[10].text
rofex_03_value = soup_rofex.find_all('td')[11].text
rofex_04_fecha = soup_rofex.find_all('td')[15].text
rofex_04_value = soup_rofex.find_all('td')[16].text
rofex_05_fecha = soup_rofex.find_all('td')[20].text
rofex_05_value = soup_rofex.find_all('td')[21].text
rofex_06_fecha = soup_rofex.find_all('td')[25].text
rofex_06_value = soup_rofex.find_all('td')[26].text
rofex_07_fecha = soup_rofex.find_all('td')[30].text
rofex_07_value = soup_rofex.find_all('td')[31].text
rofex_08_fecha = soup_rofex.find_all('td')[35].text
rofex_08_value = soup_rofex.find_all('td')[36].text
rofex_09_fecha = soup_rofex.find_all('td')[40].text
rofex_09_value = soup_rofex.find_all('td')[41].text
rofex_10_fecha = soup_rofex.find_all('td')[45].text
rofex_10_value = soup_rofex.find_all('td')[46].text
rofex_11_fecha = soup_rofex.find_all('td')[50].text
rofex_11_value = soup_rofex.find_all('td')[51].text
rofex_12_fecha = soup_rofex.find_all('td')[55].text
rofex_12_value = soup_rofex.find_all('td')[56].text

rofex_01_fecha2 = str(rofex_01_fecha[5:9])+"-"+str(rofex_01_fecha[3:5])
rofex_02_fecha2 = str(rofex_02_fecha[5:9])+"-"+str(rofex_02_fecha[3:5])
rofex_03_fecha2 = str(rofex_03_fecha[5:9])+"-"+str(rofex_03_fecha[3:5])
rofex_04_fecha2 = str(rofex_04_fecha[5:9])+"-"+str(rofex_04_fecha[3:5])
rofex_05_fecha2 = str(rofex_05_fecha[5:9])+"-"+str(rofex_05_fecha[3:5])
rofex_06_fecha2 = str(rofex_06_fecha[5:9])+"-"+str(rofex_06_fecha[3:5])
rofex_07_fecha2 = str(rofex_07_fecha[5:9])+"-"+str(rofex_07_fecha[3:5])
rofex_08_fecha2 = str(rofex_08_fecha[5:9])+"-"+str(rofex_08_fecha[3:5])
rofex_09_fecha2 = str(rofex_09_fecha[5:9])+"-"+str(rofex_09_fecha[3:5])
rofex_10_fecha2 = str(rofex_10_fecha[5:9])+"-"+str(rofex_10_fecha[3:5])
rofex_11_fecha2 = str(rofex_11_fecha[5:9])+"-"+str(rofex_11_fecha[3:5])
rofex_12_fecha2 = str(rofex_12_fecha[5:9])+"-"+str(rofex_12_fecha[3:5])

print(rofex_01_fecha2 , rofex_01_value)
print(rofex_02_fecha2 , rofex_02_value)
print(rofex_03_fecha2 , rofex_03_value)
print(rofex_04_fecha2 , rofex_04_value)
print(rofex_05_fecha2 , rofex_05_value)
print(rofex_06_fecha2 , rofex_06_value)
print(rofex_07_fecha2 , rofex_07_value)
print(rofex_08_fecha2 , rofex_08_value)
print(rofex_09_fecha2 , rofex_09_value)
print(rofex_10_fecha2 , rofex_10_value)
print(rofex_11_fecha2 , rofex_11_value)
print(rofex_12_fecha2 , rofex_12_value)
print()

ipcfecha_1 = str(soup_indec.find_all('div')[307])
ipcfecha_2 = ipcfecha_1.split("Variación ",1)[1]
ipcfecha_3 = str(ipcfecha_2.split(" ")[0]) + " " + str(ipcfecha_2.split(" ")[1])
ipc_1 = str(soup_indec.find_all('div')[308])
ipc_2 = ipc_1.split("""eco bold">""",1)[1]
ipc_3 = ipc_2.split('%',1)[0]
len_ipc2 = int (len(ipc_2)) - int(len (ipc_3))
ipc_4 = ipc_2 [0:len_ipc2]

desofecha_1 = str(soup_indec.find_all('div')[313])
desofecha_2 = desofecha_1.split("""fontsize14">""",1)[1]
desofecha_3 = str(desofecha_2.split(" ")[23]) + " " + str(desofecha_2.split(" ")[24])+ " " + str(desofecha_2.split(" ")[25][0:4])
deso_1 = str(soup_indec.find_all('div')[314])
deso_2 = deso_1.split("""soc bold">""",1)[1]
deso_3 = deso_1.split('%',1)[1]
len_deso2 = int (len(deso_2)) - int(len (deso_3))
deso_4 = deso_2 [0:len_deso2]

actifecha_1 = str(soup_indec.find_all('div')[319])
actifecha_2 = actifecha_1.split("Variación ",1)[1]
actifecha_3 = str(actifecha_2.split(" ")[0]) + " " + str(actifecha_2.split(" ")[1][0:4])
acti_1 = str(soup_indec.find_all('div')[320])
acti_2 = acti_1.split("""eco bold">""",1)[1]
acti_3 = acti_1.split('%',1)[1]
len_acti2 = int (len(acti_2)) - int(len (acti_3))
acti_4 = acti_2 [0:len_acti2]

pbifecha_1 = str(soup_indec.find_all('div')[325])
pbifecha_2 = pbifecha_1.split("Variación ",1)[1]
pbifecha_3 = str(pbifecha_2.split(" ")[0]) + " " + str(pbifecha_2.split(" ")[1])+" " + str(pbifecha_2.split(" ")[2][0:4])
pbi_1 = str(soup_indec.find_all('div')[326])
pbi_2 = pbi_1.split("""eco bold">""",1)[1]
pbi_3 = pbi_1.split('%',1)[1]
len_pbi2 = int (len(pbi_2)) - int(len (pbi_3))
pbi_4 = pbi_2 [0:len_pbi2]

pobfecha_1 = str(soup_indec.find_all('div')[337])
pobfecha_2 = pobfecha_1.split("""fontsize14">""",1)[1]
pobfecha_3 = str(pobfecha_2.split(" ")[23]) + " " + str(pobfecha_2.split(" ")[24])+ " " + str(pobfecha_2.split(" ")[25])+ " " + str(pobfecha_2.split(" ")[26][0:4])
pob_1 = str(soup_indec.find_all('div')[338])
pob_2 = pob_1.split("""soc bold">""",1)[1]
pob_3 = pob_1.split('%',1)[1]
len_pob2 = int (len(pob_2)) - int(len (pob_3))
pob_4 = pob_2 [0:len_pob2]

print('IPC', '('+ipcfecha_3+'):', ipc_3)
print('Desocupación' , '('+desofecha_3+'):', deso_4)
print('Actividad', '('+actifecha_3+'):', acti_4)
print('PBI', '('+pbifecha_3+'):', pbi_4)
print('Pobreza', '('+pobfecha_3+'):', pob_4)
print()

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text

text = convert_pdf_to_txt("download.pdf")
text2 = str (text)
text3 = text2.split("--",1)[1]

tasas_prov_01 = str(text3.split("\n")[42][0:6])
tasas_prov_02 = str(text3.split("\n")[46][0:6])
tasas_prov_03 = str(text3.split("\n")[50][0:6])

print(tasas_prov_01, "Provincia TNA a 24 meses")
print(tasas_prov_02, "Provincia TNA a 360 dias") 
print(tasas_prov_03, "Provincia TNA a 180 dias")
print()

html = urlopen(url_ciudad)
html_doc = html.read()
urlretrieve(url_ciudad, "download_ciudad.pdf")

def convert_pdf_to_txt_ciudad(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text

text_ciudad = convert_pdf_to_txt_ciudad("download_ciudad.pdf")
text2_ciudad = str (text_ciudad)
text3_ciudad = text2_ciudad.split("Créditos a Empresas y Personas Jurídicas en Pesos",1)[1]
text4_ciudad = text3_ciudad.split("TNA",1)[1]
text5_ciudad = text2_ciudad.split("Capital de Trabajo",1)[1]
text6_ciudad = text5_ciudad.split("TNA",1)[1]

text_ciudad_TNA36 = str(text6_ciudad.split("\n")[44][0:6])
text_ciudad_TNA12 = str(text6_ciudad.split("\n")[46][0:6])
text_ciudad_TNASGR = str(text4_ciudad.split("\n")[32][0:6])

print(text_ciudad_TNA36+': TNA Fija Ciudad 36 meses')
print(text_ciudad_TNA12+': TNA Fija Ciudad 12 meses')
print(text_ciudad_TNASGR+': TNA Fija Ciudad SGR 36 meses')
print()

#tna_ciudad1 = str(soup_ciudad.find_all())
#tna_ciudad2 = tna_ciudad1.split("TASA NOMINAL ANUAL FIJA (TNA): ",1)[1][0:6]
#tna_ciudad3 = tna_ciudad1.split("TASA EFECTIVA ANUAL (TEA): ",1)[1][0:6]
#tna_ciudad4 = tna_ciudad1.split("C.F.T. C/IVA: ",1)[1][0:6]

#print ('TNA Banco Ciudad con Aval', tna_ciudad2)
#print ('TEA Banco Ciudad con Aval', tna_ciudad3)
#print ('CFT Banco Ciudad con Aval', tna_ciudad4)
#print(" ")

#santander_acuerdo_comun_min_tna = soup_santanderrio.find_all("td")[5069].get_text()
#santander_acuerdo_comun_min_cft = soup_santanderrio.find_all("td")[5071].get_text()
#santander_acuerdo_comun_max_tna = soup_santanderrio.find_all("td")[5065].get_text()
#santander_acuerdo_comun_max_cft = soup_santanderrio.find_all("td")[5067].get_text()
#santander_acuerdo_especial_min_tna = soup_santanderrio.find_all("td")[5078].get_text()
#santander_acuerdo_especial_min_cft = soup_santanderrio.find_all("td")[5080].get_text()
#santander_acuerdo_especial_max_tna = soup_santanderrio.find_all("td")[5074].get_text()
#santander_acuerdo_especial_max_cft = soup_santanderrio.find_all("td")[5076].get_text()
#santander_prestamo_amortizable_12meses_min_tna = soup_santanderrio.find_all("td")[5105].get_text()
#santander_prestamo_amortizable_12meses_min_cft = soup_santanderrio.find_all("td")[5107].get_text()
#santander_prestamo_amortizable_12meses_max_tna = soup_santanderrio.find_all("td")[5101].get_text()
#santander_prestamo_amortizable_12meses_max_cft = soup_santanderrio.find_all("td")[5103].get_text()
#santander_prestamo_bullet_12meses_min_tna = soup_santanderrio.find_all("td")[5114].get_text()
#santander_prestamo_bullet_12meses_min_cft = soup_santanderrio.find_all("td")[5116].get_text()
#santander_prestamo_bullet_12meses_max_tna = soup_santanderrio.find_all("td")[5110].get_text()
#santander_prestamo_bullet_12meses_max_cft = soup_santanderrio.find_all("td")[5112].get_text()

#rio_acuerdo_promedio = (float(str(santander_acuerdo_comun_min_tna[0:2])+"."+str(santander_acuerdo_comun_min_tna[3:5])) + float(str(santander_acuerdo_comun_max_tna[0:2])+"."+str(santander_acuerdo_comun_max_tna[3:5]))) / 200
#rio_amortizable_promedio = (float(str(santander_prestamo_amortizable_12meses_min_tna[0:2])+"."+str(santander_prestamo_amortizable_12meses_min_tna[3:5])) + float(str(santander_prestamo_amortizable_12meses_max_tna[0:2])+"."+str(santander_prestamo_amortizable_12meses_max_tna[3:5]))) / 200

#print("Santander acuerdo común mínimo : (TNA)"+santander_acuerdo_comun_min_tna, "(CFT)"+santander_acuerdo_comun_min_cft)
#print("Santander acuerdo común máximo : (TNA)"+santander_acuerdo_comun_max_tna,"(CFT)"+santander_acuerdo_comun_max_cft)
#print("Santander prestamo amortizable h/12meses min : (TNA)"+santander_prestamo_amortizable_12meses_min_tna, "(CFT)"+santander_prestamo_amortizable_12meses_min_cft)
#print("Santander prestamo amortizable h/12meses max : (TNA)"+santander_prestamo_amortizable_12meses_max_tna,"(CFT)"+santander_prestamo_amortizable_12meses_max_cft)
#print("Santander acuerdo especial mínimo : (TNA)"+santander_acuerdo_especial_min_tna, "(CFT)"+santander_acuerdo_especial_min_cft)
#print("Santander acuerdo especial máximo : (TNA)"+santander_acuerdo_especial_max_tna,"(CFT)"+santander_acuerdo_especial_max_cft)
#print("Santander prestamo bullet h/12meses min : (TNA)"+santander_prestamo_bullet_12meses_min_tna, "(CFT)"+santander_prestamo_bullet_12meses_min_cft)
#print("Santander prestamo bullet h/12meses max : (TNA)"+santander_prestamo_bullet_12meses_max_tna,"(CFT)"+santander_prestamo_bullet_12meses_max_cft)
print(" ")

TNA_Nacion_Acuerdo = soup_tasasnacion.find_all("td")[30].get_text()
TNA_Nacion_Descubierto = soup_tasasnacion.find_all("td")[34].get_text()

nacion_acuerdo = (str(TNA_Nacion_Acuerdo[0:2])+","+str(TNA_Nacion_Acuerdo[3:5])+"%")
nacion_descubierto = (str(TNA_Nacion_Descubierto[0:2])+","+str(TNA_Nacion_Descubierto[3:5])+"%")

print ("Nación Adelanto Cta. Cte. con acuerdo (TNA):", nacion_acuerdo)
print ("Nación Descubierto en Cta. Cte. Previamente Solicitado(TNA):", nacion_descubierto)
print (" ")

tabla = soup_mav.find_all('table')[0]
headings = tabla.find_all('th')
rows = tabla.find_all('tr')[1:]

def parse_table(table):
    return [
        [cell.get_text().strip() for cell in row.find_all(['th', 'td'])]
           for row in table.find_all('tr')
    ]

my_list = parse_table(tabla)
my_list_final = [] 
for x in my_list:
    for y in x:
        my_list_final.append(y)
my_list_final = [w.replace(' días', '') for w in my_list_final]
my_list_final = [w.replace(',', '.') for w in my_list_final]
my_list_final = [w.replace('%', '') for w in my_list_final]
num_cpd = np.array(my_list_final[8:])
cpd_reshaped = num_cpd.reshape(len(rows),8)
cpd_final = pd.DataFrame(cpd_reshaped, columns=['Plazo', 'Fecha', 'Tasa_Min', 'Tasa_Max', 'Tasa_Prom', 
                                                          'Monto_Nom', 'Monto_Liq', 'Cheques'])

cpd_final[['Plazo', 'Monto_Nom', 'Monto_Liq','Cheques',
           'Tasa_Prom','Tasa_Min','Tasa_Max']] = cpd_final[['Plazo', 'Monto_Nom', 'Monto_Liq',
                                                               'Cheques','Tasa_Prom','Tasa_Min','Tasa_Max']].apply(pd.to_numeric)
volumen_total = cpd_final['Monto_Nom'].sum()
cheques_totales = cpd_final['Cheques'].sum()

cpd_final['Es30'] = np.where(cpd_final['Plazo']<=30, 1,0)
cpd_final['Tasa30'] = (cpd_final.Monto_Nom * cpd_final.Tasa_Prom * cpd_final.Es30)
cpd_final['Monto30'] = (cpd_final.Monto_Nom * cpd_final.Es30)
tasa_final_30 = cpd_final['Tasa30'].sum() / cpd_final['Monto30'].sum() /100

cpd_final['Es60'] = np.where((cpd_final['Plazo']<=60) & (cpd_final['Plazo']>30),1,0)
cpd_final['Tasa60'] = (cpd_final.Monto_Nom * cpd_final.Tasa_Prom * cpd_final.Es60)
cpd_final['Monto60'] = (cpd_final.Monto_Nom * cpd_final.Es60)
tasa_final_60 = cpd_final['Tasa60'].sum() / cpd_final['Monto60'].sum() /100

cpd_final['Es180'] = np.where((cpd_final['Plazo']<=180) & (cpd_final['Plazo']>60),1,0)
cpd_final['Tasa180'] = (cpd_final.Monto_Nom * cpd_final.Tasa_Prom * cpd_final.Es180)
cpd_final['Monto180'] = (cpd_final.Monto_Nom * cpd_final.Es180)
tasa_final_180 = cpd_final['Tasa180'].sum() / cpd_final['Monto180'].sum() /100

cpd_final['Es360'] = np.where((cpd_final['Plazo']<=360) & (cpd_final['Plazo']>180),1,0)
cpd_final['Tasa360'] = (cpd_final.Monto_Nom * cpd_final.Tasa_Prom * cpd_final.Es360)
cpd_final['Monto360'] = (cpd_final.Monto_Nom * cpd_final.Es360)
tasa_final_360 = cpd_final['Tasa360'].sum() / cpd_final['Monto360'].sum() /100

cpd_final['Mayor360'] = np.where(cpd_final['Plazo']>360, 1,0)
cpd_final['TasaMayor360'] = (cpd_final.Monto_Nom * cpd_final.Tasa_Prom * cpd_final.Mayor360)
cpd_final['MontoMayor360'] = (cpd_final.Monto_Nom * cpd_final.Mayor360)
tasa_final_mayor_360 = cpd_final['TasaMayor360'].sum() / cpd_final['MontoMayor360'].sum() /100

if str(tasa_final_30) == "nan":
    tasa_final_30 = ""
if str(tasa_final_60) == "nan":
    tasa_final_60 = ""
if str(tasa_final_180) == "nan":
    tasa_final_180 = ""
if str(tasa_final_360) == "nan":
    tasa_final_360 = ""
if str(tasa_final_mayor_360) == "nan":
    tasa_final_mayor_360 = ""
if str(volumen_total) == "nan":
    volumen_total = "0"
if str(cheques_totales) == "nan":
    cheques_totales = "0"

print ("CPD hasta 30:",tasa_final_30)
print("CPD hasta 60:",tasa_final_60)
print("CPD hasta 180:",tasa_final_180)
print("CPD hasta 360:",tasa_final_360)
print("CPD mayor 360:",tasa_final_mayor_360)
print ("Volumen total:",volumen_total)
print ("Cheques totales:",cheques_totales)

# Date

import datetime
now = datetime.datetime.now()
today_date = (str(now.year),"-",str(now.month),"-",str(now.day))

# Google Sheets

import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('creds02.json', scope)
client = gspread.authorize(creds)
    
tabla = soup_mav.find_all('table')[0]
headings = tabla.find_all('th')
rows = tabla.find_all('tr')[1:]

def parse_table(table):
    return [
        [cell.get_text().strip() for cell in row.find_all(['th', 'td'])]
           for row in table.find_all('tr')
    ]

my_list = parse_table(tabla)
sht4 = client.open("Info Macro")
worksheet4 = sht4.get_worksheet(4)



def job():
    sheet = client.open("Info Macro").sheet1
    sheet.update_cell(2, 5, bcra_base)
    sheet.update_cell(3, 5, bcra_reservas)
    sheet.update_cell(4, 5, bcra_badlar)
    sheet.update_cell(5, 5, bcra_leliq)
    sheet.update_cell(7, 5, dolar_compra)
    sheet.update_cell(8, 5, dolar_venta)
    sheet.update_cell (12, 6, rofex_01_fecha2)
    sheet.update_cell (13, 6, rofex_02_fecha2)
    sheet.update_cell (14, 6, rofex_03_fecha2)
    sheet.update_cell (15, 6, rofex_04_fecha2)
    sheet.update_cell (16, 6, rofex_05_fecha2)
    sheet.update_cell (17, 6, rofex_06_fecha2)
    sheet.update_cell (18, 6, rofex_07_fecha2)
    sheet.update_cell (19, 6, rofex_08_fecha2)
    sheet.update_cell (20, 6, rofex_09_fecha2)
    sheet.update_cell (21, 6, rofex_10_fecha2)
    sheet.update_cell (22, 6, rofex_11_fecha2)
    sheet.update_cell (23, 6, rofex_12_fecha2)
    sheet.update_cell (12, 5, rofex_01_value)
    sheet.update_cell (13, 5, rofex_02_value)
    sheet.update_cell (14, 5, rofex_03_value)
    sheet.update_cell (15, 5, rofex_04_value)
    sheet.update_cell (16, 5, rofex_05_value)
    sheet.update_cell (17, 5, rofex_06_value)
    sheet.update_cell (18, 5, rofex_07_value)
    sheet.update_cell (19, 5, rofex_08_value)
    sheet.update_cell (20, 5, rofex_09_value)
    sheet.update_cell (21, 5, rofex_10_value)
    sheet.update_cell (22, 5, rofex_11_value)
    sheet.update_cell (23, 5, rofex_12_value)
    sheet.update_cell (26, 5, ipc_3)
    sheet.update_cell (27, 5, deso_4)
    sheet.update_cell (28, 5, acti_4)
    sheet.update_cell (29, 5, pbi_4)
    sheet.update_cell (30, 5, pob_4)
    
    sht1 = client.open("Info Macro")
    worksheet1 = sht1.get_worksheet(1)
    worksheet1.insert_row([""],3)
    worksheet1.update_cell(3, 2, str(now.strftime("%Y-%m-%d")))
    worksheet1.update_cell(3, 3, dolar_compra)
    worksheet1.update_cell(3, 4, dolar_venta)
    formula0 = """=SI($B3>'02. BCRA'!$E$1;"";SI.ERROR(BUSCARV($B3;'02. BCRA'!$D:$M;2;0);F4))"""
    formula1 = """=SI($B3>'02. BCRA'!$C$1;"";SI.ERROR(BUSCARV($B3;'02. BCRA'!$B:$M;2;0);G4))"""
    formula2 = """=SI($B3>'02. BCRA'!$G$1;"";SI.ERROR(BUSCARV($B3;'02. BCRA'!$F:$M;2;0);H4))"""
    formula3 = """=SI($B3>'02. BCRA'!$I$1;"";SI.ERROR(BUSCARV($B3;'02. BCRA'!$H:$M;2;0);I4))"""
    formula4 = """=SI($B3>'02. BCRA'!$K$1;"";SI.ERROR(BUSCARV($B3;'02. BCRA'!$J:$M;2;0);J4))"""
    formula5 = """=SI($B3>'02. BCRA'!$M$1;"";SI.ERROR(BUSCARV($B3;'02. BCRA'!$L:$M;2;0);K4))"""
    worksheet1.update_acell('F3', formula0)
    worksheet1.update_acell('G3', formula1)
    worksheet1.update_acell('H3', formula2)
    worksheet1.update_acell('I3', formula3)
    worksheet1.update_acell('J3', formula4)
    worksheet1.update_acell('K3', formula5)

    sht2 = client.open("Info Macro")
    worksheet2 = sht2.get_worksheet(2)
    worksheet2.insert_row([""],3)
    worksheet2.update_cell(3, 4, bcra_leliq_fecha)
    worksheet2.update_cell(3, 5, bcra_leliq)
    worksheet2.update_cell(3, 6, bcra_badlar_fecha)
    worksheet2.update_cell(3, 7, bcra_badlar)
    worksheet2.update_cell(3, 8, bcra_base_fecha)
    worksheet2.update_cell(3, 9, bcra_base)
    worksheet2.update_cell(3, 10, bcra_reservas_fecha)
    worksheet2.update_cell(3, 11, bcra_reservas)
    worksheet2.update_cell(3, 12, bcra_depositos_fecha)
    worksheet2.update_cell(3, 13, bcra_depositos)
    worksheet2.update_cell(3, 14, fecha_riesgo)
    worksheet2.update_cell(3, 15, riesgo)
    
    sht3 = client.open("Info Macro")
    worksheet3 = sht3.get_worksheet(3)
    worksheet3.update_cell(3, 3, bind)
    worksheet3.update_cell(4, 3, text_ciudad_TNASGR)
    worksheet3.update_cell(5, 3, tasas_prov_03)
    worksheet3.update_cell(6, 3, rio_amortizable_promedio)
    worksheet3.update_cell(7, 3, rio_acuerdo_promedio)
    worksheet3.update_cell(8, 3, nacion_acuerdo)
    worksheet3.update_cell(9, 3, nacion_descubierto)
   
    sht4 = client.open("Info Macro")
    worksheet4 = sht4.get_worksheet(4)
    worksheet4.insert_row([""],3)
    worksheet4.update_cell(3, 2, str(now.strftime("%Y-%m-%d")))
    worksheet4.update_cell(3, 3, bind)
    #worksheet4.update_cell(3, 5, tna_ciudad2)
    #worksheet4.update_cell(3, 6, tna_ciudad3)
    #worksheet4.update_cell(3, 7, tna_ciudad4)
    worksheet4.update_cell(3, 9, tasas_prov_03)
    worksheet4.update_cell(3, 10, tasas_prov_02)
    worksheet4.update_cell(3, 11, tasas_prov_01)    
    worksheet4.update_cell(3, 13, tasa_final_30)
    worksheet4.update_cell(3, 14, tasa_final_60)
    worksheet4.update_cell(3, 15, tasa_final_180)
    worksheet4.update_cell(3, 16, tasa_final_360)
    worksheet4.update_cell(3, 17, tasa_final_mayor_360)
    worksheet4.update_cell(3, 18, volumen_total)
    worksheet4.update_cell(3, 19, float(cheques_totales))    
    #worksheet4.update_cell(3, 21, santander_prestamo_amortizable_12meses_min_tna)
    #worksheet4.update_cell(3, 22, santander_prestamo_amortizable_12meses_max_tna)
    #worksheet4.update_cell(3, 23, santander_acuerdo_comun_min_tna)
    #worksheet4.update_cell(3, 24, santander_acuerdo_comun_max_tna)
    #worksheet4.update_cell(3, 26, nacion_acuerdo)
    worksheet4.update_cell(3, 27, nacion_descubierto)
    worksheet4.update_cell(3, 29, text_ciudad_TNA36)
    worksheet4.update_cell(3, 30, text_ciudad_TNA12)
    worksheet4.update_cell(3, 31, text_ciudad_TNASGR)
    
import schedule  
import time 
schedule.every().day.at("17:27").do(job)

while True:  
   schedule.run_pending()
   time.sleep(1)
