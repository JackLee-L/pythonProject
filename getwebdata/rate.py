import re
import requests
import json
from bs4 import BeautifulSoup
from lxml import html


def getwebdata():
    URL = 'http://www.zhijinwang.com/boc/'
    # URL = 'http://www.zhijinwang.com/huilv/?from=USD&to=CNY&num=100'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/63.0.3239.132 Safari/537.36 '
    }
    res = requests.get(URL, headers=headers)
    # 更改网页编码--------不改会乱码
    res.encoding = "GB2312"
    soup = BeautifulSoup(res.text, "lxml")
    # div1 = soup.find(id='table18')
    # ret = re.findall("table18", soup)[0]
    tr = soup.find_all('tr', limit=2)[1]
    print(tr.content)
    # dict_ret = json.load(res.content.decode())
    # content_list = dict_ret["table18"]
    # with open("table18.test", 'W', encoding="utf-8") as f:
    #     for r in content_list:
    #         f.write(r)


def test():
    lines = '''<tr>

                    <th><b><a target="_blank" href="http://www.zhijinwang.com/huilv/?from=TWD&amp;to=CNY&amp;num=100"><font color="#FF0000">台币汇率</font></a></b></th>
                        <th>-</th>
                        <th>22.47</th>
                        <th>-</th>
                        <th>24.35</th>
                        <th>23.26</th>
                        <td class="pjrq">2020.03.03 18:06:47
                        </td><th>18:06:47</th>
                    </tr>
 
                    <tr>

                    <th><b><a target="_blank" href="http://www.zhijinwang.com/huilv/?from=USD&amp;to=CNY&amp;num=100"><font color="#FF0000">美元汇率</font></a></b></th>
                        <th>696.59</th>
                        <th>690.92</th>
                        <th>699.54</th>
                        <th>699.54</th>
                        <th>695.16</th>
                        <td class="pjrq">2020.03.03 18:06:47
                        </td><th>18:06:47</th>
                    </tr>'''
    res = re.findall(r'<th>(.*?)</th>', lines, re.I | re.M)
    for r in res:
        print(r)


if __name__ == '__main__':
    # print_test()
    getwebdata()
    # test()
