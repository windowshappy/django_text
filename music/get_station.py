import re
import requests
import os


class get(object):
    data = []
    type_data = []

    def get_station(self):
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                                 ' Chrome/81.0.4044.122 Safari/537.36'}
        url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9142'
        response = requests.get(url, verify=True, headers=headers)
        station = re.findall('([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
        station = str(dict(station))
        self.write(station)

    def write(self, text):
        f = open('station.text', 'w', encoding='utf_8_sig')
        f.write(text)
        f.close()

    def read(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        f = open(os.path.join(BASE_DIR, 'music\\station.text'), 'r', encoding='utf_8_sig')
        data = f.readline()
        f.close()
        return data

    def isStation(self):
        isStations = os.path.exists('station.text')
        if isStations:
            pass
        else:
            self.get_station()

    def query(self, date, form, to):
        # self.isStation()
        self.data.clear()
        self.type_data.clear()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                                 ' Chrome/81.0.4044.122 Safari/537.36',
                   'Cookie': 'JSESSIONID=278A0D89386DC862E71B0C9ED4337127; BIGipServerotn=334496266.64545.0000; RAIL_EXPIRATION=1588315756307; RAIL_DEVICEID=JYyaTGPzjfc_zVnVI3XidIxGZWDQw1OnVc6i8XSmy6gvGQpAR9ndgvS_DknXa8zKHcmE1LWB4xfdjASMEt_WguI783VQI2TP9tz8xP6xsgyywOwXX6rwnWJomvS_3uI1KI2X1wwkNO50NyuCT2v-7M1DvNxrEgip; BIGipServerpool_passport=267190794.50215.0000; route=6f50b51faa11b987e576cdb301e545c4; _jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_toStation=%u8861%u6C34%2CHSP; _jc_save_fromDate=2020-04-28; _jc_save_toDate=2020-04-28; _jc_save_wfdc_flag=dc'}
        url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(
            date, form, to)
        print(url)
        response = requests.get(url, headers=headers, verify=True).json()['data']['result']
        print(response)
        station = eval(self.read())
        if len(station) != 0:
            for i in response:
                tmp_list = i.split('|')
                form_station = list(station.keys())[list(station.values()).index(tmp_list[6])]
                to_station = list(station.keys())[list(station.values()).index(tmp_list[7])]
                seat = [tmp_list[3], form_station, to_station, tmp_list[8], tmp_list[9], tmp_list[10], tmp_list[32],
                        tmp_list[31], tmp_list[30], tmp_list[21], tmp_list[23], tmp_list[33], tmp_list[28],
                        tmp_list[24], tmp_list[29], tmp_list[26]]
                newSeat = []
                for s in seat:
                    if s == "":
                        s = "--"
                    else:
                        s = s
                    newSeat.append(s)
                self.data.append(newSeat)
        print(self.data)
        return self.data


# get().query('2020-04-29', 'BJP', 'HSP')
