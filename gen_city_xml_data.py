# -*- coding: utf-8 -*-

import json
import xmltodict
import china_region

jsfile= open('./area_code_2019.json')
xmlfile=open('./zipcode.csv')

d= json.loads(jsfile.read())
zipcodes={}
i=0
for x in xmlfile.readlines():
    if i==0:
        i=i+1
        continue
    
    xx=x.split('"')
#     print('xx',xx)
    addr=xx[1].split(',')
#     print('addr',addr)

    
    zcode=xx[-1].split(',')[1].split('\n')[0]
    co=addr[0]
    st=addr[1]
    key=city=cot =False
    if len(addr)>2:
        city=addr[2]
    if len(addr)>3:
        cot=addr[3]
    if cot and city:
        key='%s%s'%(city,cot)
#         print(co,st,city,cot)
    elif city:
        key='%s'%(city)
#         print(co,st,city)
#     print(zcode)
    i=i+1
    if key:
        zipcodes.update({
            key:zcode
        })
    
# print(zipcode)
    

    
state_map ={
"上海市": "state_cn_SH",
"浙江省": "state_cn_ZJ",
"天津市": "state_cn_TJ",
"安徽省": "state_cn_AH",
"福建省": "state_cn_FJ",
"重庆市": "state_cn_CQ",
"北京市": "state_cn_BJ",
"江西省": "state_cn_JX",
"山东省": "state_cn_SD",
"河南省": "state_cn_HA",
"内蒙古自治区": "state_cn_NM",
"湖北省": "state_cn_HB",
"新疆维吾尔自治区": "state_cn_XJ",
"湖南省": "state_cn_HN",
"宁夏回族自治区": "state_cn_NX",
"广东省": "state_cn_GD",
"西藏自治区": "state_cn_XZ",
"海南省": "state_cn_HI",
"广西壮族自治区": "state_cn_GX",
"四川省": "state_cn_SC",
"河北省": "state_cn_HE",
"贵州省": "state_cn_GZ",
"山西省": "state_cn_SX",
"云南省": "state_cn_YN",
"辽宁省": "state_cn_LN",
"陕西省": "state_cn_SN",
"吉林省": "state_cn_JL",
"甘肃省": "state_cn_GS",
"黑龙江省": "state_cn_HL",
"青海省": "state_cn_QH",
"江苏省": "state_cn_JS",
"台湾省": "state_cn_TW",
"香港特别行政区": "state_cn_HK",
"澳门特别行政区": "state_cn_MO",


    
}


#         <record id="china_city_510802" model="res.city">
#             <field name="state_id" ref="base.state_cn_SC" />
#             <field name="country_id" ref="base.cn" />
#             <field name="zipcode">510802</field>
#             <field name="name">广元市利州区</field>
#         </record>

for x in d:

    state=x['name']
    for c in x['children']:

        city=c['name']
        for z in c['children']:


            code='%s'%(z['code'])
            zipcode=code[:6]
            stateid=state_map.get(state,'')
            
            county=z['name']
            if c['name'] == '市辖区':
                ctname= z['name']
            else:
                if z['name'] =='市辖区':
                    ctname=c['name']
                else:
                    ctname=c['name']+z['name']

            
            xmlid= 'china_city_%s'%(zipcode)
 
            if city=='市辖区':
                city = state
            
            ct=True
            if county=='市辖区':
                county=city
                ct=False
#             print(state)
#             print(city)
#             print(county)
#             xx=china_region.search(province=state,city=city,county=county)


#             if xx:
#                 zip=xx[0]['zipCode']
            if ct:
                ctname= city+county
            else:
                ctname= city
#             print(ctname)
#             print(type(zipcode))
            zip=zipcodes.get(ctname,'')
            print(  '''                  
            <record id="%s" model="res.city">
                <field name="state_id" ref="base.%s" />
                <field name="country_id" ref="base.cn" />
                <field name="zipcode">%s</field>
                <field name="name">%s</field>
            </record>   
               '''%(xmlid,stateid,zip,ctname  ) )

