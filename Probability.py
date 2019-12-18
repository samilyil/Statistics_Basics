{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.0064\n"
     ]
    }
   ],
   "source": [
    "oranA = 0.4\n",
    "oranB = 0.4 \n",
    "oranC = 0.2\n",
    "# Üretilen her 10 bilgisayardan 4 tanesi A şirketi tarafından, \n",
    "# 4 tanesi B şirketi tarafından ve 2 tanesi C şirketi tarafından üretiliyormuş.\n",
    "\n",
    "hata_A = 0.015 \n",
    "hata_B = 0.020\n",
    "hata_C = 0.010\n",
    "\n",
    "# A şirketi her 1000 bilgisayarda 15 adet hatalı üretim yapıyor.\n",
    "# B şirketi her 1000 bilgisayarda 20 adet hatalı üretim yapıyor.\n",
    "# C şirketi her 1000 bilgisayarda 10 adet hatalı üretim yapıyor.\n",
    "\n",
    "#Rastgele seçilen bozuk bir bilgisayarın B şirketi tarafından üretilmiş olma olasılığı nedir?\n",
    "\n",
    "# Toplam 1000 tane bilgisayarımız olduğunu var sayıyorum. \n",
    "# Bunun 400 tanesi A şirketi tarafından üretilmiştir. \n",
    "# 400 tanesi B şirketi tarafından \n",
    "# 200 tanesi C şirketi tarafından\n",
    "\n",
    "#Yapılması gereken ilk iş hata oranlarını bu sayılara göre tekrar hesaplamak.\n",
    "\n",
    "hata_Ason = hata_A*(oranA*1000)\n",
    "hata_Bson = hata_B*(oranB*1000)\n",
    "hata_Cson = hata_C*(oranC*1000)\n",
    "\n",
    "#Seçilen bilgisayarın bozuk olma olasılığı\n",
    "toplam = (oranA+oranB+oranC)*1000\n",
    "pHata = (hata_Ason + hata_Bson + hata_Cson)/toplam\n",
    "\n",
    "#Seçilen bilgisayarın B şirketi tarafından üretilmiş olma olasılığı\n",
    "oranB\n",
    "\n",
    "#Rastgele seçilen bozuk bir bilgisayarın B şirketi tarafından üretilmiş olma olasılığı\n",
    "\n",
    "pB = pHata*oranB\n",
    "print(pB)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
