from mysql.connector import connect
from shutil import copy2

connection=connect(host='localhost', user='root', passwd='root')
cursor=connection.cursor()

def add_data(dbname='UserBench', tblname='CPUs', filename='integrated-data.txt'):
    cursor.execute(f'create database {dbname}')
    copy2(f'{filename}', f'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Data\\{dbname}\\{filename}')
    cursor.execute(f'use {dbname}')
    #cursor.execute(f'drop table {tblname}') 
    
    cursor.execute(f'create table {tblname}(SNo int(4) primary key, Brand varchar(10), Model varchar(50), UsrRt int(3), AvgBn float(5, 2), SCr float(6, 2), DCr float(6, 2), QCr float(6, 2), OCr float(6, 2), MCr float(6, 2), Mkt float(4, 2), Age int(3), Amazon int(8), MDComp int(8), GmsnCmps int(8), PrmABGB int(8), Tanotis int(8))')
    cursor.execute(f'load data infile "{filename}" into table {tblname} fields terminated by "\t"')

    cursor.execute(f'select max(scr) from {tblname}')
    cursor.execute(f'update {tblname} set scr=scr*(100/{cursor.fetchone()[0]})')
    cursor.execute(f'select max(dcr) from {tblname}')
    cursor.execute(f'update {tblname} set dcr=dcr*(100/{cursor.fetchone()[0]})')
    cursor.execute(f'select max(qcr) from {tblname}')
    cursor.execute(f'update {tblname} set qcr=qcr*(100/{cursor.fetchone()[0]})')
    cursor.execute(f'select max(ocr) from {tblname}')
    cursor.execute(f'update {tblname} set ocr=ocr*(100/{cursor.fetchone()[0]})')
    cursor.execute(f'select max(mcr) from {tblname}')
    cursor.execute(f'update {tblname} set mcr=mcr*(100/{cursor.fetchone()[0]})')
        
    cursor.execute(f'alter table {tblname} add column Minimum int(8) as (least(Amazon, MDComp, GmsnCmps, PrmABGB, Tanotis))')
    
    cursor.execute(f'alter table {tblname} add column EffPerf float(6, 2) as ((0.5*scr)+(0.05*dcr)+(0.4*qcr)+(0.04*ocr)+(0.01*mcr))')
    cursor.execute(f'alter table {tblname} add column Value float(10, 6) as (effperf/minimum)')
    cursor.execute(f'select Value from {tblname} where model like "%3500"')
    bestval=cursor.fetchone()[0]
    cursor.execute(f'alter table {tblname} drop column Value')
    cursor.execute(f'alter table {tblname} add column Value float(6, 2) as ((100/{bestval})*(effperf/minimum))')
    
    cursor.execute(f'alter table {tblname} add column EqPerf float(6, 2) as (.2*scr+.2*dcr+.2*qcr+.2*ocr+.2*mcr)')
    cursor.execute(f'alter table {tblname} add column EqVal float(10, 6) as (eqperf/sqrt(minimum))')
    cursor.execute(f'select eqval from {tblname} where model like "%3500"')
    bestval=cursor.fetchone()[0]
    cursor.execute(f'alter table {tblname} drop column eqval')
    cursor.execute(f'alter table {tblname} add column EqVal float(6, 2) as ((100/{bestval})*(eqperf/sqrt(minimum)))')

    
