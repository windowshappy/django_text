import requests
import re
from bs4 import BeautifulSoup
from lxml import etree
import time
import random
from selenium import webdriver
import json


class get(object):
    def get_jd(self, name):
        url = 'https://search.jd.com/Search?keyword={}&enc=utf-8&suggest=1.his.0.0&wq={}'.format(name, name)
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                                 ' Chrome/81.0.4044.122 Safari/537.36',
                   'referer': 'https://search.jd.com/Search?keyword={}&enc=utf-8&wq={}'.format(name, name)}
        response = requests.get(url, headers=headers)
        response = BeautifulSoup(response.text, 'lxml')
        page = response.find('span', {'class', 'fp-text'}).find_all('i')[0].text
        print('page', page)
        ul = response.find('ul', {'class', 'gl-warp clearfix'})
        p = 10
        if p > page:
            p = page
        for pa in range(1, p+1):
            url = 'https://search.jd.com/Search?keyword={}&enc=utf-8&suggest=1.his.0.0&wq={}&page={}'.format(name, name, (pa-1)*2+1)
            response = requests.get(url, headers=headers)
            response = BeautifulSoup(response.text, 'lxml')
            page = response.find('span', {'class', 'fp-text'}).find_all('i')[0].text
            print('page', page)
            ul = response.find('ul', {'class', 'gl-warp clearfix'})
            for li in ul.find_all('li'):
                jd_id = li.get('data-sku')
                img_url = 'https:' + li.find_all('img')[0].get('src')
                book_name = li.find('div', {'class', 'p-name p-name-type-2'}).find_all('em')[0].text
                item_url = 'https://item.jd.com/' + jd_id
                shop_url = 'https://chat1.jd.com/api/checkChat?pid={}&returnCharset=utf-8&_=1587971939655'.format(jd_id)
                shop = json.loads(requests.get(shop_url, headers=headers).text[5:][:-2])
                shop_item = shop['seller']
                shop_id = shop['shopId']
                venderId = shop['venderId']
                price_url = 'https://p.3.cn/prices/mgets?type=1&area=5_275_41510_0&pdtk=&pduid=15866927693761919476382&pdpin=&pdbp=0&skuIds={}&ext=11100000&_=1587971940149'.format(
                    'J_' + jd_id)
                price_item = json.loads(requests.get(price_url, headers=headers).text[1:][:-2])
                Original_price = price_item['m']
                jd_price = price_item['op']
                promotion_url = 'https://cd.jd.com/promotion/v2?skuId={}&area=5_275_41510_0&shopId={}&venderId={}&cat=1713%2C3287%2C3800&isCanUseDQ=1&isCanUseJQ=1&appid=1&_=1587971939962'.format(
                    jd_id, shop_id, venderId)
                promotion = requests.get(promotion_url, headers=headers)
                promotion_1 = promotion.json()['prom']
                promotion_2 = promotion_1['pickOneTag']
                promotion_3 = promotion_1['tags']
                if len(promotion_2) == 0 and len(promotion_3) == 0:
                    content = '无优惠'
                for p in promotion_2:
                    content = p['name'] + ': ' + p['content']
                for p1 in promotion_3:
                    content = p1['name'] + ': ' + p1['content']
                # print(content)
            new_url = 'https://search.jd.com/s_new.php?keyword={}' \
                      '&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&cid2=653&cid3=655' \
                      '&page=8&s=204&scrolling=y&log_id=1530006198.15672'.format(name)
            new_response = BeautifulSoup(requests.get(new_url, headers=headers).text, 'lxml')
            new_li_list = new_response.find_all('li')
            for new_li in new_li_list:
                new_jd_id = new_li.get('data-sku')
                new_img_url = 'https:' + new_li.find_all('img')[0].get('src')
                new_book_name = new_li.find('div', {'class', 'p-name p-name-type-2'}).find_all('em')[0].text
                new_item_url = 'https://item.jd.com/' + new_jd_id
                new_shop_url = 'https://chat1.jd.com/api/checkChat?pid={}&returnCharset=utf-8&_=1587971939655'.format(new_jd_id)
                new_shop = json.loads(requests.get(new_shop_url, headers=headers).text[5:][:-2])
                new_shop_item = new_shop['seller']
                new_shop_id = new_shop['shopId']
                new_venderId = new_shop['venderId']
                new_price_url = 'https://p.3.cn/prices/mgets?type=1&area=5_275_41510_0&pdtk=&pduid=15866927693761919476382&pdpin=&pdbp=0&skuIds={}&ext=11100000&_=1587971940149'.format(
                    'J_' + new_jd_id)
                new_price_item = json.loads(requests.get(new_price_url, headers=headers).text[1:][:-2])
                new_Original_price = new_price_item['m']
                new_jd_price = new_price_item['op']
                new_promotion_url = 'https://cd.jd.com/promotion/v2?skuId={}&area=5_275_41510_0&shopId={}&venderId={}&cat=1713%2C3287%2C3800&isCanUseDQ=1&isCanUseJQ=1&appid=1&_=1587971939962'.format(
                    new_jd_id, new_shop_id, new_venderId)
                new_promotion = requests.get(new_promotion_url, headers=headers)
                new_promotion_1 = new_promotion.json()['prom']
                new_promotion_2 = new_promotion_1['pickOneTag']
                new_promotion_3 = new_promotion_1['tags']
                if len(new_promotion_2) == 0 and len(new_promotion_3) == 0:
                    new_content = '无优惠'
                for p in new_promotion_2:
                    new_content = p['name'] + ': ' + p['content']
                for p1 in new_promotion_3:
                    new_content = p1['name'] + ': ' + p1['content']
                # print(new_content)


get().get_jd('windows')
