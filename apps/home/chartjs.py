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
        # print("Labellist:")
        # print(labellist)
        # print("Labeldata:")
        # print(labeldata)
        # print("Labelyear:")
        # print(labelyear)
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
    
    def get_vac_done_able(vaksin,tahun):
        data_done =[]
        data_able =[]
        for i in vaksin:
            if i.year == tahun:
                data_able.append(i.vac_able)
                data_done.append(i.vac_done)
            
        return data_able, data_done

    def get_vac_perc(vaksin,tahun):
        data=[]
        for i in vaksin:
            if i.year == tahun:
                perc = round((i.vac_done/i.vac_able)*100,2)
                data.append(perc)
        return data

    def sorted_data(key, value):
        dict = {}
        for i in key:
            for j in value:
                dict[i] = j
                value.remove(j)
                break

        # print('dict', dict)
        sorted_dict = sorted(dict.items(),key = lambda kv:(kv[1], kv[0]))

        daerah=[]
        percentage=[]
        for i in range(len(sorted_dict)):
            daerah.append(sorted_dict[i][0])
            percentage.append(sorted_dict[i][1])
        # print(daerah)
        # print(percentage)
        # pass back to view as sorted list
        # percentage=[]
        # for k in daerah:
        #     for key in dict:
        #         for value in dict:
        #             if key == k:   
        #                 percentage.append(dict[value])

        return daerah, percentage

    def sorted_not20(daerah, perc_year, sorted_list20):
        dict = {}
        for i in daerah:
            for j in perc_year:
                dict[i] = j
                perc_year.remove(j)
                break
        # print(dict)
        sorted_daerah = sorted_list20[0]
        # print(sorted_daerah)
        # print('sorted daerah',sorted_daerah) 
        sorted_percentage=[]
        for k in range(len(sorted_daerah)):
            for key in dict:
                if key == sorted_daerah[k]:
                    sorted_percentage.append(dict[key])

        # print('sorted perce', sorted_percentage)
        # print(len(sorted_percentage))
        return sorted_percentage
        
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
    
   
    def calc_whole_perc(distinct_year, vaksin):
        sum_able_year = []
        sum_done_year = []
        sum_able = 0
        sum_done = 0
        limit = 0
        for i in vaksin:
            print('i',i)
            for j in distinct_year:
                print('j',j)
                if j == i.year:
                    limit = limit +1
                    print('limit:', limit)
                    if limit == 13:
                        sum_able_year.append(sum_able)
                        sum_done_year.append(sum_done)
                        sum_able = 0 
                        sum_done = 0
                        break
                    else:
                        print("tambah")
                        sum_able += i.vac_able
                        sum_done += i.vac_done
        print(sum_able)
        print(sum_done)
        whole_perc = round((sum_done/sum_able)*100,2)
        print(whole_perc)
        return whole_perc



    def dataforpredict(vaksin):
        df = pd.DataFrame(list(vaksin.objects.all().values()))
        return df
        