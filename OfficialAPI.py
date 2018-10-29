import requests
import json
import csv
import sys
import time
import os

## change this to the folder where this script lives
## you need this so you can double click on the script anywhere
os.chdir("C:\\Users\\Tech\\Desktop\\walmart api\\")

##      OfficialAPI.py
##      by Friday

##      this is a very simple script for testing the official Walmart API (walmart labs)
##      you need an API key - you can get one for free on the walmartlabs website


##
## single item:
## url = http://api.walmartlabs.com/v1/items/12417832?apiKey={apiKey}
##
## multiple items:
## http://api.walmartlabs.com/v1/items?ids=12417832,19336123&apiKey={apiKey}
##
## limited to 5,000 queries/day
##
## doc - https://developer.walmartlabs.com/docs/read/Home



apikey = "xxxxxxxxxxxxxxxxxx"    #put your api key here

print("")
print("Starting search at %s " % time.ctime())
print("")

data = []
skulist = ['15213261377','15213261223','15213261117','15213261193','15213261643','15213261735','56112076','557187544','994342377','226303597','122149773','444645020','744600968','811829813','828150107','617089098','778983483','148722715','50884205','439811107','24246728','9605536','129407621','16922920','842898046','46252282','865234574','535554960','298536498','924892255','284770673','9252523','631599146','298162419','110963478','44365002','827272022','974985840','581583863','54518167','448134617','55528638','108295087','55556430','404235285','673878344','717211702','54518166','737324985','743971586','597549840','827272022','314572057','752686817','895341040','564883313','55556429','556391094','392713124','54371978','796187411','903169162','906411946','139081640','158980002','666694722','572118225','788641296','636479157','576103107','939622535','713156836','180107746','312093778','44664721','27943324','9252523','190483931','9189491','5359083','25862849','19598766','23752171','55392362','33963166','46514593','170247386','55126141','827935168','55426080','443800295','412627364','885148922','279997977','136838715','407164200','45799822','17126458','44997871','103776449','624446583','452170213','13224381','55126258','305646808','148506813','866533791','101948702','782467792?','657136655','163329791','768447743','55126259','55126218','55126255','123040621','705596439','822603574','794437422','821527659','55126212','55126223','401645095','754096201','951814057','498907341','595339080','499543430','773934509','310602842','884810056','293187372','354627536','353256894','56243817','116248698','195196501','415310380','370381617','50799043','112552726','968734811','434913270','170596927','521594979','791699736','596982685','349601714','611555398','613705821','682645801','734984960','349601714','878692549','921402438','860011361','871888919','42910921','42911230','768424931','851521275','273528108','54595517','928852236','355220444','586819864','55141844','814723888','931145975','848196821','770827823','541823550','474397515','52612986','42666034241','54595519','54595520','101948702','935015835','785067498','51676249','461794735','405229858','949096738','50154874','482181915','677157701','958864885','895572550','45717692','182802872','453305542','190555839','224584101','54595518','481520932']

for SKU in skulist:
    os.system("title walmart API searching SKU " + str(SKU))
    ##time.sleep(1)
    url = "http://api.walmartlabs.com/v1/items/{}?apiKey={}".format(SKU,apikey)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, timeout=30, headers=headers)

    if response.status_code == 404:
        print("Error 404 - SKU " + str(SKU) + " not found. Please check your SKU and try again.")
        continue
    elif response.status_code == 200:
        ## we get a valid response, continue
        pass

    try:
        current_data = response.json()
    except:
        continue
    
    temp_dict = {'SKU': SKU}

    

    try:
        temp_dict['name'] = current_data['name']
        temp_dict['name'] = temp_dict['name'].replace('™', ' ')
        temp_dict['name'] = temp_dict['name'].replace('©', ' ')
        temp_dict['name'] = temp_dict['name'].replace(',', ' ')
        temp_dict['name'] = temp_dict['name'].replace('&', ' ')
        temp_dict['name'] = temp_dict['name'].replace('"', ' ')
        temp_dict['name'] = temp_dict['name'].replace('-', ' ')
        temp_dict['name'] = temp_dict['name'].replace('<', ' ')
        temp_dict['name'] = temp_dict['name'].replace('>', ' ')
        temp_dict['name'] = temp_dict['name'].replace('*', ' ')
        temp_dict['name'] = temp_dict['name'].replace('?', ' ')
        temp_dict['name'] = temp_dict['name'].replace(':', ' ')
        temp_dict['name'] = temp_dict['name'][:50]  ##limit to 50 characters
    except KeyError:
        temp_dict['name'] = ''
                    

    try:
        temp_dict['UPC'] = current_data['upc']
    except KeyError:
        temp_dict['UPC'] = ''

    try:
        temp_dict['OnlinePrice'] = current_data['salePrice']
        temp_dict['OnlinePrice'] = "$" + str(temp_dict['OnlinePrice'])
    except KeyError:
        temp_dict['OnlinePrice'] = ''
                    
    try:
        temp_dict['OnlineInStock'] = current_data['availableOnline']
    except KeyError:
        temp_dict['OnlineInStock'] = ''
                    




    print(temp_dict.items()) 	
    data.append(temp_dict)
            

## you need a subfolder called 'searches' or this will fail
with open('searches' + '/' + 'OfficialAPI-results.csv', 'w', encoding='utf-8') as outfile:
    f = csv.DictWriter(outfile, ['name', 'SKU', 'UPC', 'OnlinePrice', 'OnlineInStock'],
                       delimiter=',', lineterminator='\n')
    f.writeheader()
    f.writerows(data)

	

