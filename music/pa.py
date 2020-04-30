"""
https://songsearch.kugou.com/song_search_v2?callback=jQuery112403208541746345319_1587769142930&keyword=l&page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=1587769142932
"""
import requests
from bs4 import BeautifulSoup
import json
import re
import urllib.request as request


class music(object):
    def get(self, music_name):
        url = 'https://songsearch.kugou.com/song_search_v2?callback=jQuery112403208541746345319_1587769142930&keyword={}&page={}&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=1587769142932'.format(
            music_name, '1')
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
            'referer': 'https://www.kugou.com/yy/html/search.html'
        }
        r = requests.get(url=url, headers=headers)
        req = re.search("jQuery\d+_\d+\(?", r.text)
        data = json.loads(r.text.strip().lstrip(req.group()).rstrip(")"))
        text = data['data']['lists']
        print(text)
        te = []
        for t in text:
            music_id = t['AlbumID']
            FileHash = t['FileHash']
            # https://wwwapi.kugou.com/yy/index.php?r=play/getdata&callback=jQuery1910048948491205964784_1587783698224&hash=EF5B3B50F9D5FE0E418A03CC8ED2AD0B&album_id=0&dfid=0hb5QI0yFrCJ0nxuNh16sVE4&mid=01f4f62f7988d4835e7c6396744aa299&platid=4&_=1587783698226
            i_url = 'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&callback=jQuery191013860146079482383_1587772818754&hash={}&album_id={}&dfid=0hb5QI0yFrCJ0nxuNh16sVE4&mid=01f4f62f7988d4835e7c6396744aa299&platid=4&_=1587772818755'.format(
                FileHash, music_id)
            item_url = 'https://www.kugou.com/song/#hash={}&album_id={}'.format(FileHash, music_id)
            # i=request.urlopen(i_url).read()
            # print(i)
            h = {
                'cookie': 'kg_mid=01f4f62f7988d4835e7c6396744aa299; kg_dfid=0hb5QI0yFrCJ0nxuNh16sVE4; '
                          'kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; '
                          'kg_mid_temp=01f4f62f7988d4835e7c6396744aa299',
                'referer': 'https://www.kugou.com/song/',
                'sec-fetch-dest': 'script',
                'sec-fetch-mode': 'no-cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/81.0.4044.122 Safari/537.36 '
            }
            # pro = {
            #     'http': '27.43.188.27:808',
            #     'https': '27.43.188.27:8080'
            # }
            cookies = {'cookies': 'kg_mid=01f4f62f7988d4835e7c6396744aa299; kg_dfid=0hb5QI0yFrCJ0nxuNh16sVE4; '
                                  'kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; '
                                  'kg_mid_temp=01f4f62f7988d4835e7c6396744aa299'}
            # , proxies=pro
            item = requests.get(i_url, headers=h)
            # item = re.search("jQuery\d+_\d+\(?", item.text)
            # print(mp3_url.get('src'))
            # print(len('jQuery191013860146079482383_1587772818754'))
            print(item.text[42:][:-2])
            # te.append(music_id)
        # print(te)
        # print(data)


music().get('l')

# 在这里，为了分步演示，直接用刚才第一步搜索时开发者模式获取到的搜索列表第一条的id和hash
# 文章最后有整个连贯的代码

# id = '557512' #单曲id
# hash = '41C2E4AB5660EAE04021C5893E055F50' #单曲hash值
# url = 'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&callback=jQuery19107465224671418371_1555932632517&hash=%s&album_id=%s&_=1555932632518'.format(hash,id)
# h = {
#                 'referer': 'https://www.kugou.com/song/',
#                 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
#                 }
# res = requests.get(url, headers=h)
#
# print(res.text)
