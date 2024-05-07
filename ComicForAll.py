import requests

url = 'https://comic.mkzcdn.com/chapter/v1/?comic_id=207622'  # 总章节目录
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}
comic_id = '207622'  # 漫画的编号


def getChapterResponse():
    response = requests.get(url, headers=headers)
    jsonData = response.json()['data']

    # for item in jsonData:
    #     chapter_id = item['chapter_id']
    #     print(chapter_id)
    chapter_id_list = [item['chapter_id'] for item in jsonData]
    # 每个章节的id全部获取，每章节对应的url就是：https://www.mkzhan.com/漫画编号/章节id.html
    return chapter_id_list

chapter_url = getChapterResponse() # 获取章节编号
every_url = []
for item in chapter_url:
    data = f'https://comic.mkzcdn.com/chapter/content/v1/?chapter_id={item}&comic_id={comic_id}&format=1&quality=1&sign=99cdd1b0601302f9f67e94b34bd7c805&type=1&uid=72077855'
    every_url.append(data)

print(every_url)
