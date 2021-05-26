import sys

# 导入you-get库
from you_get import common as you_get

directory = r'C:\Windows\System32\cmd.exe'

url = r'https://www.bilibili.com/video/av95978305/'

sys.argv = ['you_get', '-o', directory, url]

if __name__ == '__main__':

    # you_get

    try:
        you_get
    except Exception as e:
        print(e)
    finally:
        print('try 已做完')
