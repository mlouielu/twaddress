# -*- coding: utf-8 -*-

import re
from twaddress import data


def _normalize_address(s):
    REPLACE_MAP = {
        '之': '-', '樓': 'F',
        '１': '1', '２': '2', '３': '3', '４': '4', '５': '5',
        '６': '6', '７': '7', '８': '8', '９': '9', '０': '0',
        '一': '1', '二': '2', '三': '3', '四': '4', '五': '5',
        '六': '6', '七': '7', '八': '8', '九': '9',
    }

    for key in REPLACE_MAP:
        s = s.replace(key, REPLACE_MAP[key])
    return s


def parse(s):
    result = {'巷': '', '弄': '', '號': '', '樓': '', '室': ''}

    s = _normalize_address(s)

    # Match 巷號弄室
    pattern = '(\d+[巷號弄室])'
    match = re.findall(pattern, s)
    left = re.sub(pattern, '', s)
    for i in match:
        result[i[-1]] = str(i[:-1]).strip()
    if left:
        result['樓'] = left

    return result


def _maximum_match_segment(s, maxlen, d):
    for i in range(maxlen, 0, -1):
        if s[:i] in d:
            return (d[s[:i]], s[i:])
    return '', s


def mms_cut(s):
    # Maximum match segment cut
    # Assumpt input is a correct address

    city, s = _maximum_match_segment(s, 7, data.county)
    if not city:
        city, s = _maximum_match_segment(s, 7, data.city)
        code = ''
    if isinstance(city, data.County):
        code = city.code
        city = city.eng
    road, s = _maximum_match_segment(s, 14, data.road)
    village, s = _maximum_match_segment(s, 7, data.village)
    address = parse(s)

    return code, city, road, village, address
