#!/usr/bin/python3

#Openload Downloader 


import os
import sys
import urllib
import time
from selenium import webdriver
from pyvirtualdisplay import Display


url=sys.argv[1]
filename=url.split('/')[-1]


print("Estrazione link download")


#Creo un display virtuale per il browser
display = Display(visible=0, size=(800, 600))
display.start()

browser=webdriver.Firefox()
browser.get(url)

#Cerco il bottone che devo cliccare
button=browser.find_element_by_css_selector('#btnDl')
button.click()

#Clicco e chiudo la finestra popup che si apre
button.click()
browser.switch_to.window(browser.window_handles[-1])
browser.close()
browser.switch_to.window(browser.window_handles[0])

#Aspetto i 5 secondi per il download
time.sleep(6)


#Cerco il prossimo bottone
button=browser.find_element_by_css_selector('#downloadTimer > a:nth-child(1)')


#Clicco e chiudo i popup (Adesso sono 2 )
button.click()
browser.switch_to.window(browser.window_handles[-1])
browser.close()
browser.switch_to.window(browser.window_handles[-1])
browser.close()
browser.switch_to.window(browser.window_handles[0])


#Prendo l'url per il download e chiudo il browser
button=browser.find_element_by_css_selector('#realdl > a:nth-child(1)')
downloadurl=button.get_attribute('href')
browser.quit()
display.stop()



print('Download di '+filename+' in corso...')
out=urllib.request.urlretrieve(downloadurl,filename)
print('Download di '+filename+' completato!')




os.remove('geckodriver.log')

