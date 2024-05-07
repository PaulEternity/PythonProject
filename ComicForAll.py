import requests
import os

comic_id = str(input('输入漫画编号'))  # 漫画的编号
url = f'https://comic.mkzcdn.com/chapter/v1/?comic_id={comic_id}'  # 总章节目录
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}


def getChapterResponse():
    response = requests.get(url, headers=headers)
    jsonData = response.json()['data']

    # for item in jsonData:
    #     chapter_id = item['chapter_id']
    #     print(chapter_id)
    chapter_id_list = [item['chapter_id'] for item in jsonData]
    # 每个章节的id全部获取，每章节对应的url就是：https://www.mkzhan.com/漫画编号/章节id.html
    return chapter_id_list


def getImgResponse():
    chapter_url = getChapterResponse()  # 获取章节编号
    every_url = []
    for item in chapter_url:
        data = f'https://comic.mkzcdn.com/chapter/content/v1/?chapter_id={item}&comic_id={comic_id}&format=1&quality=1&sign=99cdd1b0601302f9f67e94b34bd7c805&type=1&uid=72077855'
        every_url.append(data)

    return every_url  # 获取到每个章节存储图片的总地址


# 把每个章节的图片拿出来
# def getResponse():  # 获取每个章节图片的响应对象
#     # every_img_url = getImgResponse()
#     # img_list = []
#     # for item in every_img_url:
#     #     data = requests.get(url=item, headers=headers)
#     #     img_list.append(data)
#     # return img_list
#     every_img_url = getImgResponse()
#     img_list = []
#     for item in every_img_url:
#         response = requests.get(url=item, headers=headers)
#         if response.status_code == 200:
#             img_list.append(response.json())
#     return img_list
#
#
# def getImg():
#     # img_content_list = getResponse()
#     # img_list_all = []
#     # for item in img_content_list:
#     #     information = item.json()
#     #     pages = information['data']['page']
#     #     img_list = [page['image'] for page in pages]
#     #     img_list_all.append(img_list)
#     # return img_list_all
#     img_content_list = getResponse()
#     img_list_all = []
#     for item in img_content_list:
#         pages = item['data']['page']
#         img_list = [page['image'] for page in pages]
#         img_list_all.append(img_list)
#     return img_list_all
def getImg():
    img_url_list = getImgResponse()
    img_list_all = []
    for item in img_url_list:
        response = requests.get(url=item, headers=headers)
        if response.status_code == 200:
            information = response.json()
            pages = information['data']['page']
            img_list = [page['image'] for page in pages]
            img_list_all.append(img_list)
    return img_list_all

def Save(imgs, chapter_num):
    if not os.path.exists('comic_images'):  # 检查保存目录是否存在，如果不存在则创建
        os.makedirs('comic_images')

    chapter_dir = f'Chapter_{chapter_num}'
    chapter_path = os.path.join('comic_images', chapter_dir)
    os.makedirs(chapter_path, exist_ok=True)

    for idx, img_url in enumerate(imgs):
        response = requests.get(img_url, headers=headers)
        if response.status_code == 200:
            image_name = f'image_{idx+1}.jpg'
            image_path = os.path.join(chapter_path, image_name)
            with open(image_path, 'wb') as f:
                f.write(response.content)
            print(f'Saved image: {image_name} in {chapter_dir}')
        else:
            print(f'Failed to download image {img_url}')

if __name__ == '__main__':
    img_list_all = getImg()
    for chapter_num, imgs in enumerate(img_list_all, start=1):
        Save(imgs, chapter_num)


