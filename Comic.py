import requests
import os  # 文件操作

url = 'https://comic.mkzcdn.com/chapter/content/v1/?chapter_id=962617&comic_id=208643&format=1&quality=1&sign=99cdd1b0601302f9f67e94b34bd7c805&type=1&uid=72077855'

# 找到存放整个章节图片的位置 CV某个图片.jpg前的部分进行搜索，查找与该章节图片数一致的链接，就是url


def GetResponse(urls):  # 发送请求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    response = requests.get(url=urls, headers=headers)
    return response


# 获取数据方式
# response.text 获取响应文本 html的网页内容 网页源代码
# response.json() 获取json数据 字典，列表
# response.content 获取响应二进制数据 图片，视频，音频，特定格式文件
def GetImg():
    information = GetResponse(url).json()
    img_list = []
    # print(information)
    pages = information['data']['page']  # 根据键值对取值，基本语法规则，取字典里data对应的page的内容 忘了就把上一行取消注释，运行看看
    # for page in pages:
    #     img = page['image']
    #     img_list.append(img)

    img_list = [page['image'] for page in pages]  # 上三行代码简化版
    return img_list


def Save(imgs, title):  # 保存图片内容
    ImgContent = GetResponse(imgs).content
    if not os.path.exists('img'):  # 判断img文件夹是否存在，如果不存在就自动创建
        os.mkdir('img')
    with open(f'img\\{title}.jpg', mode='wb') as f:
        f.write(ImgContent)


if __name__ == '__main__':
    imgList = GetImg()
    num = 1
    for img in imgList:
        Save(img, num)
        num += 1

# 只能爬取某个章节已经改良