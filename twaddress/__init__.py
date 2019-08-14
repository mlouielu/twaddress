# -*- coding: utf-8 -*-


from twaddress import algo


def _to_eng(cut_result):
    code, city, road, village, address = cut_result

    result = [road, village, '%s %s' % (city, code), 'Taiwan']
    if address['巷']:
        result.insert(0, 'Ln. ' + address['巷'])
    if address['弄']:
        result.insert(0, 'Aly. ' + address['弄'])
    if address['號']:
        result.insert(0, 'No.' + address['號'])
    if address['樓']:
        result.insert(0, address['樓'])
    if address['室']:
        result.insert(0, address['室'])

    return ', '.join(filter(lambda x: x, result))


def get(address):
    return _to_eng(cut(address))


def cut(address):
    return algo.mms_cut(address)
