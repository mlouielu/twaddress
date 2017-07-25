# -*- coding: utf-8 -*-

import csv
import os
from collections import namedtuple


County = namedtuple('County', ['code', 'cht', 'eng'])


def __load(path):
    with open(path, newline='', encoding='utf-8') as f:
        return {row[0]: row[1] for row in csv.reader(f)}


def __load_county(path):
    with open(path, newline='', encoding='utf-8') as f:
        return {row[1]: County(*row) for row in csv.reader(f)}


city = {
    '臺北市': 'Taipei City',
    '基隆市': 'Keelung City',
    '新北市': 'New Taipei City',
    '連江縣': 'Lienchiang County',
    '宜蘭縣': 'Yilan County',
    '釣魚台': 'Diaoyutai',
    '新竹市': 'Hsinchu City',
    '新竹縣': 'Hsinchu County',
    '桃園市': 'Taoyuan City',
    '苗栗縣': 'Miaoli County',
    '臺中市': 'Taichung City',
    '彰化縣': 'Changhua City',
    '南投縣': 'Nantou County',
    '嘉義市': 'Chiayi City',
    '嘉義縣': 'Chiayi County',
    '雲林縣': 'Yunlin County',
    '臺南市': 'Tainan City',
    '高雄市': 'Kaohsiung City',
    '澎湖縣': 'Penghu County',
    '金門縣': 'Kinmen County',
    '屏東縣': 'Pingtung County',
    '臺東縣': 'Taitung County',
    '花蓮縣': 'Hualien County'
}


# Load all dataset
__basepath = os.path.dirname(__file__)

county = __load_county(os.path.join(__basepath, 'dataset/county10603.csv'))
road = __load(os.path.join(__basepath, 'dataset/road10603.csv'))
village = __load(os.path.join(__basepath, 'dataset/village10602.csv'))
