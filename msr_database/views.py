from .models import CalendaData

class Msr_Calculator():
    def __init__(self):
        pass

    def getAll(self, year, month, day, time, sl, gen):
        if int(sl) == 1:
            birthdata = CalendaData.objects.using('msdb').filter(cd_sy=year,cd_sm=month,cd_sd=day)
        else:
            birthdata = CalendaData.objects.using('msdb').filter(cd_ly=year,cd_lm=month,cd_ld=day)
        outdata = birthdata[0]
        outdata = {
            "s_year" : birthdata[0].cd_sy,
            "s_month" : birthdata[0].cd_sm,
            "s_day" : birthdata[0].cd_sd,
            "l_year" : birthdata[0].cd_ly,
            "l_month" : birthdata[0].cd_lm,
            "l_day" : birthdata[0].cd_ld,
            "year_gan_ch" : birthdata[0].cd_hyganjee[0],
            "year_ji_ch" : birthdata[0].cd_hyganjee[1],
            "year_gan_kr" : birthdata[0].cd_kyganjee[0],
            "year_ji_kr" : birthdata[0].cd_kyganjee[1],
            "month_gan_ch" : birthdata[0].cd_hmganjee[0],
            "month_ji_ch" : birthdata[0].cd_hmganjee[1],
            "month_gan_kr" : birthdata[0].cd_kmganjee[0],
            "month_ji_kr" : birthdata[0].cd_kmganjee[1],            
            "day_gan_ch" : birthdata[0].cd_hdganjee[0],
            "day_ji_ch" : birthdata[0].cd_hdganjee[1],
            "day_gan_kr" : birthdata[0].cd_kdganjee[0],
            "day_ji_kr" : birthdata[0].cd_kdganjee[1],
            "ddi_kor" : birthdata[0].cd_ddi,
            "sol_plan" : birthdata[0].cd_sol_plan,
            "lunar_plan" : birthdata[0].cd_lun_plan,
        }
        outdata["time_ji_kr"] = time
        outdata["time_gan_kr"] = self.get_time_gan(outdata["day_gan_kr"],outdata["time_ji_kr"])
        outdata["time_gan_ch"] = self.gankr_to_ch(outdata["time_gan_kr"])
        outdata["time_ji_ch"] = self.jikr_to_ch(outdata["time_ji_kr"])
        outdata["gender"] = gen
        outdata["daewoon"] = self.getDaewoon(outdata["gender"],outdata["year_gan_kr"],outdata["month_gan_kr"],outdata["month_ji_kr"])
        outdata["daewoon_num"] = self.daewoonNum(year,month,day,sl,outdata["daewoon"][0])
        return outdata

    def getDaewoon(self,gen,ygan,mgan,mji):
        YANGGAN = ["???","???","???","???","???"]
        EUMGAN = ["???","???","???","???","???"]
        CHEONGAN = ["???","???","???","???","???","???","???","???","???","???"]
        JIJI = ["???","???","???","???","???","???","???","???","???","???","???","???"]

        if (gen == "???" and ygan in YANGGAN) or (gen == "???" and ygan in EUMGAN):
            data = ["??????"]
            data_gan = []
            data_ji = []
            for i in range(len(CHEONGAN)):
                if CHEONGAN[i] == mgan:
                    start = i + 1
        
            for i in range(10):
                data_gan.append(CHEONGAN[start%10])
                start += 1

            for i in range(len(JIJI)):
                if JIJI[i] == mji:
                    start = i + 1
        
            for i in range(10):
                data_ji.append(JIJI[start%12])
                start += 1
            
            data.append(data_gan)
            data.append(data_ji)

            return data

        elif (gen == "???" and ygan in EUMGAN) or (gen == "???" and ygan in YANGGAN):
            data = ["??????"]
            data_gan = []
            data_ji = []
            for i in range(len(CHEONGAN)):
                if CHEONGAN[i] == mgan:
                    start = i - 1
        
            for i in range(10):
                data_gan.append(CHEONGAN[start%10])
                start -= 1

            for i in range(len(JIJI)):
                if JIJI[i] == mji:
                    start = i - 1
        
            for i in range(10):
                data_ji.append(JIJI[start%12])
                start -= 1
            
            data.append(data_gan)
            data.append(data_ji)

            return data
    
    def daewoonNum(self,year,month,day,sl,way):
        JEOLGI = ["??????","??????","??????","??????","??????","??????","??????","??????","??????","??????","??????","??????"]
        if int(sl) == 1:
            birthdata = CalendaData.objects.using('msdb').filter(cd_sy=year,cd_sm=month,cd_sd=day)
        else:
            birthdata = CalendaData.objects.using('msdb').filter(cd_ly=year,cd_lm=month,cd_ld=day)
        start_spot = birthdata[0].cd_no - 35
        temp_data_list = CalendaData.objects.using('msdb').filter(cd_no__gt=start_spot,cd_no__lt=start_spot+70)  
        temp_data = []
        for i in range(len(temp_data_list)):
            if temp_data_list[i].cd_kterms in JEOLGI:
                temp_data.append(temp_data_list[i])
        if way == "??????":
            for i in range(len(temp_data)):
                if birthdata[0].cd_no < temp_data[i].cd_no:
                    daewoon_num = round((temp_data[i].cd_no - birthdata[0].cd_no) / 3, 1)
                    return daewoon_num
        else:
            for i in range(len(temp_data)):
                if birthdata[0].cd_no > temp_data[len(temp_data)-1-i].cd_no:
                    daewoon_num = round((birthdata[0].cd_no - temp_data[len(temp_data)-1-i].cd_no) / 3, 1)
                    return daewoon_num

    def get_time_gan(self,day_gan_kr,time_ji):
        CHEONGAN = ["???","???","???","???","???","???","???","???","???","???"]
        JIJI = ["???","???","???","???","???","???","???","???","???","???","???","???"]
        for i in range(len(JIJI)):
            if JIJI[i] == time_ji:
                time_ji_num = i

        if day_gan_kr == "???" or day_gan_kr == "???":
            return CHEONGAN[time_ji_num % 10] 
        if day_gan_kr == "???" or day_gan_kr == "???":
            return CHEONGAN[(time_ji_num + 2) % 10]
        if day_gan_kr == "???" or day_gan_kr == "???" :
            return CHEONGAN[(time_ji_num + 4) % 10]
        if day_gan_kr == "???" or day_gan_kr == "???" :
            return CHEONGAN[(time_ji_num + 6) % 10]
        if day_gan_kr == "???" or day_gan_kr == "???" :
            return CHEONGAN[(time_ji_num + 8) % 10]

    def gankr_to_ch(self,gankr):
        CHEONGAN = ["???","???","???","???","???","???","???","???","???","???"]
        CHEONGAN_CH = ["???","???","???","???","???","???","???","???","???","???"]
        for i in range(len(CHEONGAN)):
            if CHEONGAN[i] == gankr:
                return CHEONGAN_CH[i]

    def jikr_to_ch(self,jikr):
        JIJI = ["???","???","???","???","???","???","???","???","???","???","???","???"]
        JIJI_CH = ["???","???","???","???","???","???","???","???","???","???","???","???"]
        for i in range(len(JIJI)):
            if JIJI[i] == jikr:
                return JIJI_CH[i]

    