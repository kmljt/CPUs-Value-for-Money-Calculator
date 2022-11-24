# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 21:17:46 2019

@author: KamalPC
"""

from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
from time import sleep

def scrape():
    file=open('ubm-data.txt', 'w')
    driver=Chrome(r'C:\Users\KamalPC\Downloads\chromedriver_win32\chromedriver.exe')
    driver.get('https://cpu.userbenchmark.com/')

    for i in range(3):
        driver.find_element_by_xpath(f'//*[@id="tableDataForm:mhtddyntac"]/table/thead/tr/th[{i+11}]/a').click()
        sleep(1)
        driver.find_element_by_xpath(f'//*[@id="columnsDialog"]/div/div/div[2]/div/a[{3-i}]').click()
        sleep(3)

    number_of_cpus=int(driver.find_element_by_xpath('//*[@id="tableDataForm:mhtddynsbc"]/div[1]').text[:-5].replace(',', ''))

    for page_number in range(1, number_of_cpus//50+2):
        sleep(5)
        
        soup=BeautifulSoup(driver.page_source)#, 'lxml')
        cpus=soup.find_all('tr', {'class': 'hovertarget'})
        
        for cpu in cpus:
            srno=int(cpu.contents[1].contents[3].contents[0])
            # link=cpu.contents[3].contents[1].contents[1].contents[0]['href']
            # image=cpu.contents[3].contents[1].contents[1].contents[0].contents[0]['src']
            brand=cpu.contents[3].contents[1].contents[3].contents[1].contents[2].strip()
            name=cpu.contents[3].contents[1].contents[3].contents[1].contents[3].contents[0].replace('-', ' ')
            # samples=int(eval(cpu.contents[3].contents[1].contents[3].contents[3].contents[0].lstrip('Samples ').replace('k', '*1000')))
            dualcore=float(cpu.contents[5].contents[0].contents[0])
            quadcore=float(cpu.contents[7].contents[0].contents[0])
            _64_core=float(cpu.contents[9].contents[0].contents[0])
            usrrat=int(cpu.contents[11].contents[0].contents[1])
            avgbench=float(cpu.contents[15].contents[0].contents[0].contents[0])
            singlecore=float(cpu.contents[17].contents[0].contents[0])
            octacore=float(cpu.contents[19].contents[0].contents[0])
            try: mktshare=float(cpu.contents[21].contents[0].contents[0])
            except: mktshare=0
            age=int(cpu.contents[23].contents[0].contents[0].rstrip('+'))
            
            sttr=f'{srno}\t{brand}\t{name}\t{usrrat}\t{avgbench}\t{singlecore}\t{dualcore}\t{quadcore}\t{octacore}\t{_64_core}\t{mktshare}\t{age}'
            print(sttr)
            file.write(sttr+'\n')
            
        if page_number!=number_of_cpus//50+1:
            driver.find_element_by_link_text('Next »').click()

    file.close()
    driver.close()
