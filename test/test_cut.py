# -*- coding: utf-8 -*-

import unittest
import twaddress

@unittest.skip('Just skip...')
class CutTest(unittest.TestCase):
    def test_short_address(self):
        expect = ['高雄市', '三民區', '建工路', '415號']
        self.assertEqual(twaddress.cut('高雄市三民區建工路415號'), expect)

    def test_normal_address(self):
        expect = ['高雄市', '前鎮區', '成功二路', '25號', '5樓之1']
        self.assertEqual(twaddress.cut('高雄市前鎮區成功二路25號5樓之1'), expect)

    def test_hard_address(self):
        expect = []
        self.assertEqual(twaddress.cut('嘉義市溪興街153巷12弄25號5樓3室'), expect)


class GetTest(unittest.TestCase):
    def test_hard_address(self):
        expect = ('50F-60, No.30, Aly. 20, Ln. 10, Qixian 1st Rd., '
                  'Xinxing Dist., Kaohsiung City 800, Taiwan')
        self.assertEqual(twaddress.get('高雄市新興區七賢一路10巷20弄30號50樓之60'), expect)
