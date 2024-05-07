# 爬取B站视频
import re
import json
from pprint import pprint  # 格式化输出

import requests

# 找m4s的存储方式
url = 'https://www.bilibili.com/video/BV1ZJ4m1E7Q6/?spm_id_from=333.1007.tianma.1-1-1.click&vd_source=af4d6400d422198f4c38cb1f382f3ac2'
headers = {
    'Cookie': 'buvid3=1281953E-6C8B-74B9-23F6-12FFD57090C139945infoc; b_nut=1696850339; i-wanna-go-back=-1; b_ut=7; _uuid=E67DB5FC-59AA-E7A9-F892-FA95C7E2888240588infoc; buvid4=9ED87111-FD06-86A9-20E5-E5472F6684CF41057-023100919-dd0vAJ%2Bkw%2BRVXvql4x929p15Npg61yCIfFzCdlDKY8Za4qOJcD0UXA%3D%3D; CURRENT_BLACKGAP=0; DedeUserID=477971386; DedeUserID__ckMd5=74daff4d62a5dd8a; rpdid=0zbfAGUO0Z|8l2byXNO|G9d|3w1QPOki; CURRENT_FNVAL=4048; PVID=1; enable_web_push=DISABLE; FEED_LIVE_VERSION=V_WATCHLATER_PIP_WINDOW3; header_theme_version=CLOSE; home_feed_column=5; b_lsid=CFBC4BFD_18F52EFF364; bsource=search_google; bmg_af_switch=1; bmg_src_def_domain=i0.hdslb.com; browser_resolution=1421-785; SESSDATA=f6871650%2C1730635410%2Ca66c2%2A52CjBPlvo0GAozinhuoynwPsOSxgJuQNPBPObTb8ko4Z8qo8dQU7OJTru1z-CxuCzD6tISVlVuZ285bTJ6dlVmY3VIX3BTR0FJWFpZSDNHbGlaY1hpM1E3cGlCQk1aYUhRVU42dmo5ZDNXWlp3blpKNk9mV2lNNW5pYVB2VThwUzdTUEhVX3c5S3N3IIEC; bili_jct=505f05704ceba4e01fc83fd004b3d7c5; sid=5s1hz4fi; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTUzNDI2MjEsImlhdCI6MTcxNTA4MzM2MSwicGx0IjotMX0.b_S1MMbMyqv87I5dpq4H5krMewtdtfZibzXL62BJmPA; bili_ticket_expires=1715342561; fingerprint=ef810ddfcf3a3d857d3a4c2e2ed0b3fc; buvid_fp=1281953E-6C8B-74B9-23F6-12FFD57090C139945infoc; buvid_fp_plain=undefined',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}


def getResponse(urls):  # 请求响应
    response = requests.get(urls, headers=headers)
    return response


def getVideoInfo():
    response = getResponse(url)
    html = response.text
    # info = re.findall('<script>window.__playinfo__ = (.*?)</script>', html)[0]  # 匹配window.__playinfo__内的所有内容
    # json_data = json.loads(info)  # 转换为JSON格式存储

    print(html)


getVideoInfo()


