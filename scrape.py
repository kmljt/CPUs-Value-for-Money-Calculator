# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 23:14:08 2019

@author: KamalPC
"""

from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from os import chdir, mkdir, getcwd
from time import sleep

cwd=getcwd()

def Amazon(images_wanted=False):
    chdir(cwd)
    file=open('amazon-data.txt', 'w')

    if images_wanted:
        try:
            mkdir('amazon-images')
        except: pass
        
        chdir('amazon-images')
        
    # search_query='https://www.amazon.in/s?i=computers&rh=n%3A976392031%2Cn%3A976393031%2Cn%3A1375344031%2Cn%3A1375391031&s=review-rank'
    search_query='https://www.amazon.in/s?k=processor&ref=nb_sb_noss_1'
    driver=Chrome(r'C:\Users\KamalPC\Downloads\chromedriver_win32\chromedriver.exe')
    driver.get(search_query)
    pages=int(driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[8]/div/span/div/div/ul/li[6]').text)
    
    for page in range(pages):
        soup=BeautifulSoup(driver.page_source)#, 'lxml')
        results=soup.find_all('div', {'class': 'sg-col-20-of-24 s-result-item sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28'})
        
        for result in results:
            try:
                name=result.find('span', {'class': 'a-size-medium a-color-base a-text-normal'}).text
                if ('AMD' in name or
                    'Amd' in name or
                    'amd' in name or
                    'Intel' in name or
                    'INTEL' in name or
                    'intel' in name):
                    
                    try:
                        price=int(float(result.find('span', {'class': 'a-price-whole'}).text.replace(',', '')))
                    except:
                        price=int(float(result.find('span', {'class': 'a-color-price'}).text.replace(',', '').strip('₹')))

                    if images_wanted:
                        image=result.find('img', {'class': 's-image'})['src']
                        try:
                            urlretrieve(image, f'{name.replace("/", "")[:100]}.jpg')
                        except: pass
                        
                    sttr=f'{name}\t{price}'
                    file.write(sttr+'\n')
                    print(sttr)
            except: pass
        
        if page!=pages-1:
            # search_query=f'https://www.amazon.in/s?i=computers&rh=n%3A976392031%2Cn%3A976393031%2Cn%3A1375344031%2Cn%3A1375391031&s=review-rank&page={page+2}'
            search_query=f'https://www.amazon.in/s?k=processors&page={page+2}'
            driver.get(search_query)
        
    file.close()
    driver.close()

def MDComputers(images_wanted=False):
    chdir(cwd)
    file=open('mdcomputers-data.txt', 'w')

    if images_wanted:
        try:
            mkdir('mdcomputers-images')
        except: pass
        
        chdir('mdcomputers-images')
        
    search_query='https://mdcomputers.in/processor?limit=100'
    driver=Chrome(r'C:\Users\KamalPC\Downloads\chromedriver_win32\chromedriver.exe')
    driver.get(search_query)
    
    soup=BeautifulSoup(driver.page_source)#, 'lxml')
    results=soup.find_all('div', {'class': 'product-layout product-grid product-grid-4 col-lg-3 col-md-4 col-sm-6 col-xs-12'})
    
    for result in results:
        name=result.find('h4').text
        price=result.find('span', {'class': 'price-new'}).text.strip().lstrip('₹').replace(',', '')

        if images_wanted:
            image='https:'+result.find('img')['data-src'].replace('75x75.jpg', '600x600.jpg')
            urlretrieve(image, f'{name}.jpg')
            
        sttr=f'{name}\t{price}'
        file.write(sttr+'\n')
        print(sttr)
        
    file.close()
    driver.close()
    
def GamesNComps(images_wanted=False):
    chdir(cwd)
    file=open('gamesncomps-data.txt', 'w')

    if images_wanted:
        try:
            mkdir('gamesncomps-images')
        except: pass
        
        chdir('gamesncomps-images')
        
    driver=Chrome(r'C:\Users\KamalPC\Downloads\chromedriver_win32\chromedriver.exe')
    
    for query in ('amd', 'intel'):
        search_query=f'https://gamesncomps.com/?s={query}&product_cat=0&post_type=product'
        driver.get(search_query)
        
        while True:
            soup=BeautifulSoup(driver.page_source, features="html.parser")
            # results=soup.find_all('div', {'class': 'grid__item search-result post-large--one-quarter medium--one-third small--one-half'})
            results=soup.find_all('div', {'class': 'product-inner product-item__inner'})
            
            for result in results:
                try:
                    name=result.find('h2').text.title()
                    if (('Amd' in name or 
                         'Intel' in name or
                         'I9' in name) and
                        ('Motherboard' not in name and 
                         'Corsair' not in name and 
                         'Ssd' not in name)):
                        # price=result.find('span', {'itemprop': 'price'}).text.strip()[4:-3].replace(',', '')
                        price=result.find('span', {'class': 'woocommerce-Price-amount amount'}).contents[-1][:-3].replace(',', '')

                        if images_wanted:
                            image='https:'+result.find('img')['srcset'].split(', ')[0][:-17].replace('_40x', '')
                            urlretrieve(image, f'{name}.jpg')

                        sttr=f'{name}\t{price}'
                        file.write(sttr+'\n')
                        print(sttr)
                except: pass
            try:
                driver.find_element_by_link_text('→').click()
                sleep(2)
            except: break
    
    file.close()
    driver.close()
    
def PrimeABGB(images_wanted=False):
    chdir(cwd)
    file=open('primeabgb-data.txt', 'w')

    if images_wanted:
        try:
            mkdir('primeabgb-images')
        except: pass
        
        chdir('primeabgb-images')
        
    driver=Chrome(r'C:\Users\KamalPC\Downloads\chromedriver_win32\chromedriver.exe')
    
    for page in range(3):
        search_query=f'https://www.primeabgb.com/buy-online-price-india/cpu-processor/page/{page+1}/'
        driver.get(search_query)
        sleep(2)
        soup=BeautifulSoup(driver.page_source)#, 'lxml')
        results=soup.find_all('div', {'class': 'product-inner equal-elem'})
        
        for result in results:
            name=result.find('h3', {'class': 'product-name short'}).text

            if images_wanted:
                image=result.find('img')['src'].replace('-300x300', '')
                urlretrieve(image, f'{name}.jpg')
                
            try:
                price=result.find_all('span', {'class': 'woocommerce-Price-amount amount'})[-1].contents[-1].replace(',', '')
            except:
                continue
            
            sttr=f'{name}\t{price}'
            file.write(sttr+'\n')
            print(sttr)
    file.close()
    driver.close()

def Tanotis(images_wanted=False):
    chdir(cwd)
    file=open('tanotis-data.txt', 'w')

    if images_wanted:
        try:
            mkdir('tanotis-images')
        except: pass
        
        chdir('tanotis-images')
        
    search_query='https://www.tanotis.com/search?q=processor'
    driver=Chrome(r'C:\Users\KamalPC\Downloads\chromedriver_win32\chromedriver.exe')
    driver.get(search_query)
    sleep(2)
    no_of_results=int(driver.find_element_by_xpath('//*[@id="searchModal"]/div[1]/div[3]/div/div[2]/div[1]/div[2]/span/span/span[2]').text)
    
    for page in range(no_of_results//60+1):
        
        soup=BeautifulSoup(driver.page_source)#, 'lxml')
        results=soup.find_all('div', {'class': 'pd-bd product-inner'})
        
        for result in results:
            try:
                name=result.find('h3', {'class': 'product-title'}).text
                if name.split()[0] in ('AMD', 'Intel'):
                    price=int(float(result.find('span', {'class': 'red'}).text[2:]))

                    if images_wanted:
                        try:
                            image=result.find('img')['src'].replace('_250x250', '')
                            urlretrieve(image, f'{name}.jpg')
                        except: pass
                        
                    sttr=f'{name}\t{price}'
                    file.write(sttr+'\n')
                    print(sttr)
            except: pass
        
        if page!=no_of_results//60:
            driver.find_element_by_link_text('>').click()
            sleep(2)
    file.close()
    driver.close()
