import requests
from bs4 import BeautifulSoup


class get:
    code = {}
    now_url = 'https://free-api.heweather.net/s6/weather/now?location={}&key=623e201a5d534180988b5fa929ef3b40'
    lifestyle_url = 'https://free-api.heweather.net/s6/weather/lifestyle?location={}&' \
                    'key=623e201a5d534180988b5fa929ef3b40 '
    """生活指数类型 comf：舒适度指数、cw：洗车指数、drsg：穿衣指数、flu：感冒指数、sport：运动指数、trav：旅游指数、
    uv：紫外线指数、air：空气污染扩散条件指数、ac：空调开启指数、ag：过敏指数、gl：太阳镜指数、mu：化妆指数、
    airc：晾晒指数、ptfc：交通指数、fsh：钓鱼指数、spi：防晒指数"""

    def get_now(self, name):
        response = requests.get(self.now_url.format(name)).json()['HeWeather6'][0]
        if response['status'] == 'ok':
            update = response['update']['loc']
            now = response['now']
            cloud = now['cloud']
            cond_txt = now['cond_txt']
            fl = now['fl'] + '摄氏度'
            hum = now['hum']
            pcpn = now['pcpn']
            pres = now['pres'] + '百帕'
            tmp = now['tmp'] + '摄氏度'
            vis = now['vis'] + '公里'
            wind_deg = now['wind_deg']
            wind_dir = now['wind_dir']
            wind_sc = now['wind_sc']
            wind_spd = now['wind_spd'] + '公里/小时'
            print(update)
            print(response)
        else:
            return '出现问题'

    def get_lifestyle(self):
        return None

    def get_code(self):
        self.code.clear()
        url = 'https://dev.heweather.com/docs/refer/condition'
        response = BeautifulSoup(requests.get(url).text, 'lxml').find_all('table')[0].find_all('tbody')[0].find_all('tr')
        for res in response:
            res = res.find_all('td')
            code = res[0].text
            zh = res[1].text
            self.code[code] = zh
        print(self.code)
        return self.code


# get().get_code()
get().get_now('北京')
