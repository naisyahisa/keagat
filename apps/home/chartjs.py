from ast import Or
from collections import OrderedDict


class processData:
    def firstChart(vaksin):
        # ser = VacSerializer(vac, many=True)
        print("#########masuk process data db")
        #[{"id": 1, "district": "Baling"}, {"id": 2, "district": "Sik"}...]

        # district = []
        # year = []
        # vacAble = []
        # vacDone = []
        # percent = []
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
            if x.year == 2018:
                # num += 1
                # no = [num]
                # dataNum.append(no) 
                dataList.append(context)

        vaksin2018 = dict.fromkeys(data, dataList)

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
            # district.append(x.district)
            # year.append(x.year)
            # vacDone.append(x.vac_done)
            # vacAble.append(x.vac_able)
            # percent.append(perc)
        # print(percent)
        #before jadi lable data kenaa classify ikut tahun
        # labellist = []
        # labeldata = []
        # labelyear = []
        # for i in range(len(year)):
        #     if year[i] == 2018:
        #         labellist.append(district[i])
        #         labeldata.append(percent[i])
        #         labelyear.append(year[i])
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
        return vaksin2018