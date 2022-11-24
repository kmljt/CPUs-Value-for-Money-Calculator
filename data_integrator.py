# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 10:11:03 2019

@author: KamalPC
"""

def integrate():
    ubm=open('ubm-data.txt')
    amazon=open('amazon-data.txt')
    mdcomputers=open('mdcomputers-data.txt')
    gamesncomps=open('gamesncomps-data.txt')
    primeabgb=open('primeabgb-data.txt')
    tanotis=open('tanotis-data.txt')
    assoc=open('associations.txt', 'w')
    integ=open('integrated-data.txt', 'w')

    for cpu in ubm:
        integ.write(cpu[:-1])
        #=====  decluterring names  =======

        count, brand, name=cpu.split('\t')[:3]
        
        if 'Six Core' in name:
            name=name[:-9]
        elif 'Triple Core' in name:
            name=name[:-12]
        elif 'Quad Core' in name:
            name=name[:-10]
        elif 'APU R3' in name:
            name=name[:-7]
        elif 'APU (' in name or 'APU R3 Graphics' in name or 'APU R5 Graphics' in name:
            name=name[:-16]
        elif 'APU' in name:
            name=name[:-4]
        elif (name[-2:]=='v2' or
              name[-2:]=='V2' or
              name[-2:]=='v3' or
              name[-2:]=='v4' or
              name[-2:]=='v5' or
              name[-2:]=='v6'):
            name=name[:-3]
        elif name[-2:]==' 0':
            name=name[:-2]

        #=====  extracting information from names  =======

        model=name.split()[-1]
        num=presuf=''
        for char in model:
            if char.isnumeric():
                num+=char
            else:
                presuf+=char

        print(count, brand, name, num, presuf)
        assoc.write(f'{count} {brand} {name} {num} {presuf}\n')
        
        #=====  mapping results with cpu names  =======
        
        for vendor in (amazon, mdcomputers, gamesncomps, primeabgb, tanotis):
            prices=[]
            for result in vendor:
                is_a_valid_result=False   #flag
                product, price = result.split('\t')
                
                if ('Lenovo' not in product and
                    'Supermicro' not in product and
                    'Delid' not in product and
                    'Assembled' not in product and
                    'Keyboard' not in product and
                    presuf!='U' and
                    'Inspiron' not in product and
                    'TOSHIBA' not in product and
                    'Acer' not in product):
        
                    if '2600X' in name and product=='AMD 4.2GHz Socket AM4 Processor':
                        is_a_valid_result=True
                    elif '7940X' in name and product=='Intel Core Processor Set':
                        is_a_valid_result=True
        
                    if 'Ryzen' in name:
                        if 'Core i' not in product:
                            if presuf=='G':
                                if num+presuf in product or num+'C' in product:
                                    is_a_valid_result=True
                            elif presuf=='':
                                if num+' ' in product or num+'B' in product:
                                    is_a_valid_result=True
                                elif num==product[-4:]:
                                    is_a_valid_result=True
                            else:
                                if num+presuf in product or num[:-1]+presuf in product:
                                    is_a_valid_result=True
                                    
                    elif 'Core i' in name:
                        if ('Xeon' not in product and
                            'SLACR' not in product and
                            'Duo' not in product and
                            'AMD' not in product and
                            'Amd' not in product and
                            'Optane' not in product and
                            'PENTIUM' not in product and
                            'Celeron' not in product and
                            'Pentium' not in product and
                            'DUO' not in product and
                            'Pemtium' not in product and
                            #'Core 2' not in product and
                            'Circle' not in product and
                            'P4' not in product):
                            
                            if 'HD Graphics' in product and num in product and product.index('HD Graphics')<product.index(num): continue
                            
                            if presuf=='':
                                if name.split()[-2][0]=='i':
                                    if num+' ' in product and product[product.index(num)-1]!='I':
                                        is_a_valid_result=True
                                    elif num==product[-4:] and product[-5]!='I':
                                        is_a_valid_result=True
                            elif presuf=='XE':
                                if num+'X' in product:
                                    is_a_valid_result=True
                            else:
                                if ((num+presuf in product) and 
                                    (num+presuf+'F' not in product) and
                                    (num+presuf+'f' not in product) and
                                    (num+presuf+'s' not in product) and
                                    (product[product.index(num)-1]!='I')):
                                    is_a_valid_result=True
                                    
                    elif 'Pentium' in name or 'Celeron' in name:
                        if ((num+presuf in product or presuf+num in product) and
                            presuf+num+'0' not in product and
                            'Core i' not in product and
                            'Core I' not in product and
                            'Core 2 ' not in product and
                            'AMD' not in product and
                            'Amd' not in product):
                            if product[product.index(num)-2]==' ':
                                is_a_valid_result=True
                                
                    elif 'FX' in name:
                        if presuf=='':
                            if ('FX' in product or 'FD' in product) and (num+' ' in product or num+'W' in product):
                                is_a_valid_result=True
                        else:
                            if num+presuf in product:
                                is_a_valid_result=True
                                
                    elif 'Athlon' in name:
                        if len(num)>2:
                            if ('Xeon' not in product and
                                'Ryzen' not in product and
                                'RYZEN' not in product and
                                'FX' not in product and
                                'Sempron' not in product and
                                'Opteron' not in product and
                                'Pentium' not in product and
                                'Celeron' not in product and
                                'Core i' not in product and
                                'Intel' not in product and
                                'MSI' not in product and
                                'Atom' not in product and
                                'AMD YD' not in product and
                                presuf+num+'0' not in product):
                                if num+presuf in product:
                                    if 'GE' not in name:
                                        if 'GE' not in product:
                                            is_a_valid_result=True
                                    else: is_a_valid_result=True
                                        
                    elif 'Xeon' in name:
                        if presuf+num in product:
                            is_a_valid_result=True
                            
                    elif 'Core2' in name:
                        if name[-4:]!='Quad':
                            if ('AMD' not in product and
                                'Core i' not in product and
                                'Core I' not in product and
                                'Pentium' not in product):
                                if presuf+num in product:
                                    is_a_valid_result=True
                                    
                    else: #A-series, Phenoms
                        if ('Intel' not in product and
                            'INTEL' not in product and
                            'ibm' not in product and
                            'Jack' not in product and
                            'Ryzen' not in product and
                            'RYZEN' not in product and
                            'Fx' not in product and
                            'Sempron' not in product and
                            'Opteron' not in product and
                            'FX' not in product):
                            if num+presuf in product:
                                if 'Phenom' in name and 'Phenom' in product:
                                    if len(num)>3:
                                        is_a_valid_result=True
            
                if is_a_valid_result:
                    print(f'{product}\t{price}')
                    assoc.write(f'{product}\t{price}')
                    prices.append(int(float(price)))
        
            if prices:
                integ.write('\t'+str(min(prices)))
            else:
                integ.write('\t'+str(1e7))
        integ.write('\n')
        amazon.seek(0)
        mdcomputers.seek(0)
        gamesncomps.seek(0)
        primeabgb.seek(0)
        tanotis.seek(0)
        assoc.write('\n\n')
        print()
            
    integ.close()
    assoc.close()
