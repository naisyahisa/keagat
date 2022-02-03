from ast import Or
from collections import OrderedDict
import collections, json
import pandas as pd

class processData:
    def firstChart(vaksin):
        # ser = VacSerializer(vac, many=True)
        print("#########masuk process data db")
        #[{"id": 1, "district": "Baling"}, {"id": 2, "district": "Sik"}...]

        district = []
        year = []
        vacAble = []
        vacDone = []
        percent = []
        #iterate objects.all
        vaksin2018 = OrderedDict()
        num = 0
        data = ["data"]
        dataList = []
        for x in vaksin:
            perc = round((x.vac_done/x.vac_able)*100,2)
            context = {
                'id':x.id,
                'district':x.district,
                'year':x.year,
                'vac_able':x.vac_able,
                'vac_done':x.vac_done,
                'percentage': perc
            }
            # print (context)
            # if x.year == 2018:
                # num += 1
                # no = [num]
                # dataNum.append(no) 
                # dataList.append(context)

        # vaksin2018 = dict.fromkeys(data, dataList)

        # print("vaksin2018")
        # print(vaksin2018)
        # print(list(vaksin2018))
        # print(len(vaksin2018))
            # dataSource = OrderedDict()
        
            # for key, value in singlebardict.items():
            #     data = {}
            #     data["label"] = key
            #     data["value"] = value
            #     dataSource["data"].append(data)
            
            #main lists
            district.append(x.district)
            year.append(x.year)
            vacDone.append(x.vac_done)
            vacAble.append(x.vac_able)
            percent.append(perc)
        print(percent)    
        # print(percent)
        #before jadi lable data kenaa classify ikut tahun
        labellist = []
        labeldata = []
        labelyear = []
        for i in range(len(year)):
            if year[i] == 2018:
                labellist.append(district[i])
                labeldata.append(percent[i])
                labelyear.append(year[i])
        print("Labellist:")
        print(labellist)
        print("Labeldata:")
        print(labeldata)
        print("Labelyear:")
        print(labelyear)
        # districtDict = {}
        # for key in labellist:
        # #    labeldata untuk data yg disimpan
        #     for value in labeldata:
        #         districtDict[key] = value
        #         labeldata.remove(value)
        #         break
        # print("##############")
        # print(districtDict)    
        return labellist, labeldata, labelyear
    
    def thirdChart(vaksin):

        # data: {
        #     datasets: [{
        #             data: [{district: 'Alor Setar', 2018: {vac_able: 318,vac_done:210}}, {district: 'Baling', 2018: {vac_able: 157,vac_done:100}}]
        #                 }]
        #     },
        #     options: {
        #         parsing: {
        #             xAxisKey: 'district',
        #             yAxisKey: '2018.value'
        #                 }
        #             }   

        return vaksin
    
    def get_label(vaksin):
        lbl = []
        for i in vaksin:
            if i.district not in lbl:
                lbl.append(i.district)

        return lbl
    
    def get_vac_done(vaksin,tahun=2018):
        data =[]
        for i in vaksin:
            if i.year==tahun:
                data.append(i.vac_done)
            
        return data

    def get_json(vaksin,tahun):
        data=[]
        # for feature in vaksin:
        #     item = {"daerah": feature.district}
        item = {}
        for attribute in vaksin:
            
            if attribute.year==tahun:
                item = {'daerah':attribute.district,'bilangan':{'vac_able':attribute.vac_able,'vac_done':attribute.vac_done}}
                data.append(item)

        jsonData=json.dumps(data)
        return jsonData
    
   
    def dataforpredict(vaksin):
        df = pd.DataFrame(list(vaksin.objects.all().values()))
        return df
        