# -*- coding: utf-8 -*-
"""
Created on Fri May 19 15:28:43 2023

@author: goksel
"""
import math


"""""""TAHRİK MOMENT HESABI"""""""
Md = 680

k1 = 1.5

Ms = Md * k1



"""""""MİL ÇAP HESABI"""""""""

E1 = 3

tau_mil = 190

tau_mil_emniyet = tau_mil / E1

d_mil= ((Ms * (10 ** 3)) / (3.1415926535 * tau_mil_emniyet / 16)) ** (1/3)

" mil çapı min 43.45mm olarak hesaplanmış 45mm olarak belirlenmiştir"

d = 45

""""BALATA MERKEZCİL KUVVET HESABI"""""

Ca = 2.5

n =2

mu = 0.5

Rt = (129/2) * 10 ** (-3)    #tambur iç çap

Fn = Ms/( mu * Rt * n * Ca)



"""" KÜTLE MERKEZİ """

R1 = 74/2      #pabuçun başladığı yarıçap

R2 = 120/2     #pabuçun yarıçapı

R3 = 126/2     #balatanın bittiği yer

y1 = (2 * R1 * math.sin(60 * math.pi / 180)) / (3 * (60 * math.pi / 180))

y2 = (2 * R2 * math.sin(60 * math.pi / 180)) / (3 * (60 * math.pi / 180))

y3 = (2 * R3 * math.sin(60 * math.pi / 180)) / (3 * (60 * math.pi / 180))

y12 = (y2 * math.pi * (R2) ** 2 - y1 * math.pi * (R1) ** 2) / (math.pi * ((R2) ** 2 - (R1) ** 2))

y13 = (y3 * math.pi * (R3) ** 2 - y2 * math.pi * (R2) ** 2) / (math.pi * ((R3) ** 2 - (R2) ** 2))

y123 = (y13 * math.pi * (R3 ** 2 - R2 ** 2) + 1.7 * y12 * math.pi * (R2 ** 2 - R1 ** 2)) / (math.pi * (R3 ** 2 - R2 ** 2) + 1.7 * math.pi * (R2 ** 2 - R1 ** 2) )



"""m = d*V 'den bulunan kütleler"""

ro_st = 0.0077  #gr/mm^3

V_st = 116500  #mm^3

m_st = ro_st*V_st

ro_balata = 0.00452  #gr/mm^3

V_balata = 19080  #mm^3

m_balata = ro_balata*V_balata

m_toplam2 = (m_balata+m_st)*(10**(-3))

"görüldüğü üzere çizim ile belirlenen hacim ve yoğunluktan bulduğumuz kütle değerleriyle ağırlık merkeziyle bulduğumuz kütle değeri örtüşmektedir"




"""""AÇISAL HIZ MAX """""

W = 3800 * math.pi * 2 / 60

R_toplam = (y123) * 10 ** (-3)

m_toplam = Fn / (R_toplam * W * W)



""""" İLK TEMAS """""

W2  =  1000 * math.pi * 2 / 60

R_toplam = (y123) * 10 ** (-3) 

Fyay_toplam = m_toplam * ((W2) ** 2) * R_toplam



"""  YAY HESAPLARI  """

""" Fn_yay/8 = K * (X1 + ön gerilme + aralık töleransı - X1)"""

""""X1 + ön gerilme + aralık töleransı(5.1) = 44.6mm"""

"""Kanca uzunluğu 10mm (tanesi) """

k = 7811 * (10 ** -3)

X1 = 28.702

tolerans = 2 * 2.55

ön_gerilme = (Fyay_toplam/(8*k))-tolerans    # 4 er yay kullanıldı toplam 8 yay



"""  DİNAMİK EMNİYET HESABI  """


Fn2 = Fn - Fyay_toplam

mu_dinamik = 0.45    

"Değer balata dinamik sürütnme tablosundan çekildi"

M_dinamik = Fn2 * Rt * n * Ca * mu_dinamik

E_dinamik = M_dinamik / Md

"""BU TARZ SİSTEMLER HER ZAMAN STATİK SÜRTÜNME ALTINDA İNCELENMEZ. ÇÜNKÜ YÜKSEK YÜK ALTINDA KALKIŞ SAĞLANDIĞINDA SİSTEM GEREKLİ MOMENTİ ÜRETEMEYECEĞİ İÇİN KAVRAMA SÜRTMEYE DEVAM EDECEKTİR. TAA Kİ SİSTEM MAKS MOMENT DEĞERİNE ULAŞIP KİTLENENE KADAR"""



"""  STATİK EMNİYET HESABI  """

M_statik = Fn2 * Rt * n * Ca * mu

E_statik = M_statik / Md



"""  KOMPONENT EMNİYETLERİ """

"TAMBUR"
Tambur_içap = 129

Tambur_dçap = 139

Tambur_yükseklik = 50

Burulma_tambur = 32 * (Tambur_dçap/2) * M_statik * (10 ** 3) / ( math.pi * (Tambur_dçap ** 4 - Tambur_içap ** 4))

Kesilme_tambur = (M_statik * (10 ** 3) / Tambur_içap) / (math.pi * Tambur_içap * Tambur_yükseklik)

"KAMA"
"Emniyet basıncı St70 çekme dayanımına yakın olarak alınmıştır."

Pem = 250

t1 = 5

t2 = 5

b = 8

"milin ezilmesi"

l1 = (2 * (Ms) * (10 ** 3)) / (Pem * d * t1) 

"göbeğin ezilmesi"

l2 = (2 * (Ms) * (10 ** 3)) / (Pem * d * t2) 

"kamanın kesilmesi"

l3 = (2 * (Ms) * (10 ** 3)) / (tau_mil * d * b)

"sacın kopması"

sac_kalınlık = 1

sac_genişlik = 50

delik_çapı = 3

sac_kopması = (Fyay_toplam/2)/((sac_genişlik - 4 * delik_çapı) * sac_kalınlık)

"sacın yırtılması"

s = 4        #delik kenar mesafesi

sacın_yırtılması = (Fyay_toplam/8) / (sac_kalınlık * s) 

"yayın kesilmesi"

tel_kalınlığı = 1

yayın_kesilmesi = (Fyay_toplam/8)/((math.pi * tel_kalınlığı ** 2 )/4)

"yayın kesme mukavemeti 1470 mpa"

"balata pabuç bağlantısı"

F_bağlantı = ((Ms*(10**3))/2)/(118/2)

bağlantı_şekilbağlı = F_bağlantı/(50*2)


"yapıştırma mukavemeti"

F_kesme = (M_statik*(10**3)/120)

Alan_yapıştırma = (2/3)*math.pi*50*60

gerilme_yapıştırma = F_kesme/Alan_yapıştırma

"çıkış mili burulma"

çıkışmili_dçap = 55

çıkışmili_iççap = 45

Burulma_çıkımili = 32 * (çıkışmili_dçap/2) * M_statik * (10 ** 3) / ( math.pi * (çıkışmili_dçap** 4 - çıkışmili_iççap ** 4))


"""////////////////////////////////////////////////////////SONUÇ/////////////////////////////////////////////"""









