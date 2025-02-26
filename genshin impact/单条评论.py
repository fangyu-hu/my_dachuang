import csv
import json
import time

import pandas
import requests
import re
def zifuchuangchuli(a):#处理掉抖音文字里的特殊字符
    m=''
    f1=open('特殊.csv','w',encoding='UTF-8')
    wf=csv.writer(f1)
    for i in list(a):
        try:
            if i=='\n' or i=='\\' or i=='n'or i=='/':
                continue
            wf.writerow([i])
            m=m+i
        except UnicodeEncodeError:
            continue
    f1.close()
    return m

def getpinglun(url):
    alldata=[]
    shipinurl=url
    wenjianid=shipinurl.split('=')[-1]
    proxies=None
    headers = {
        'x-youtube-client-name': '1',
        'x-goog-visitor-id': 'CgtpWjFfTU9xUC0wVSi27oqLBg%3D%3D',
        'referer': 'https://www.youtube.com/watch?v=ZPbKCHFaHfk',
        'origin': 'https://www.youtube.com',
        'accept': '*/*',
        'content-type': 'application/json',
        'authorization': 'SAPISIDHASH 1633859390_1544d7e66026adab37efb182d7a7a2a452d2e230',
        'cookie': 'VISITOR_INFO1_LIVE=iZ1_MOqP-0U; PREF=tz=Asia.Shanghai; __Secure-3PSID=AQiQp9tQBTmM78ZljHNTkmXfXYDGLxFAjP-5-vTCDIEFVbniQsaKNY53dlu7WMWRaiXWlA.; __Secure-3PAPISID=DyQInHHi4huadrnH/Azp9OgV4tuEQ4x-Td; LOGIN_INFO=AFmmF2swRgIhAP0ZD3uotK-EDbV-r7MBe1brUUFy1zItpV-Vhljz-LsJAiEAp2nBhTP0mB7j3Z0W_aVjMbV2fYdqJLHQRg_u7emeZvw:QUQ3MjNmeFJxTGFjSTZVTk9nYnBycXl0Q29yRC00dDhLQzI1dHEyNVJ5MnBYdHJZLXZyZlh4Q2tuTUNXeGJpVVhYbnBYRlFvN2NyU1Vlb0h3di1nLTNFbTVQaGpkcHpUTEo4Qi1vcHFTRkllb1JNa08taGpCNmVfdnJtM2ZQTWQ4amNDSW5QNTNkMXBRSUFjQWNCV3FMRk1RdldUcV9HT1ln; YSC=LM00KCQk5-k; __Secure-3PSIDCC=AJi4QfEVDgqA1hKZgglBFbXJWamNx0GxEydg7b2JcVD9kPHGz9ZfQA4EG7YvjjzjQ51XDGkP9g; ST-xhfma0=itct=CK8CENwwIhMIkNHTwMi_8wIVtkwPAh0KsQchMgpnLWhpZ2gtcmVjWg9GRXdoYXRfdG9fd2F0Y2iaAQYQjh4YngE%3D&csn=MC4zMTA1NjQxNTc4OTg5NjY0&endpoint=%7B%22clickTrackingParams%22%3A%22CK8CENwwIhMIkNHTwMi_8wIVtkwPAh0KsQchMgpnLWhpZ2gtcmVjWg9GRXdoYXRfdG9fd2F0Y2iaAQYQjh4YngE%3D%22%2C%22commandMetadata%22%3A%7B%22webCommandMetadata%22%3A%7B%22url%22%3A%22%2Fwatch%3Fv%3DZPbKCHFaHfk%22%2C%22webPageType%22%3A%22WEB_PAGE_TYPE_WATCH%22%2C%22rootVe%22%3A3832%7D%7D%2C%22watchEndpoint%22%3A%7B%22videoId%22%3A%22ZPbKCHFaHfk%22%2C%22watchEndpointSupportedOnesieConfig%22%3A%7B%22html5PlaybackOnesieConfig%22%3A%7B%22commonConfig%22%3A%7B%22url%22%3A%22https%3A%2F%2Fr4---sn-ouu2j-ioqz.googlevideo.com%2Finitplayback%3Fsource%3Dyoutube%26orc%3D1%26oeis%3D1%26c%3DWEB%26oad%3D3200%26ovd%3D3200%26oaad%3D11000%26oavd%3D11000%26ocs%3D700%26oewis%3D1%26oputc%3D1%26ofpcc%3D1%26msp%3D1%26odeak%3D1%26odepv%3D1%26osfc%3D1%26ip%3D164.70.90.213%26id%3D64f6ca08715a1df9%26initcwndbps%3D865000%26mt%3D1633859094%26oweuc%3D%26pxtags%3DCg4KAnR4EggyNDAwODEwOA%26rxtags%3DCg4KAnR4EggyMzk5Nzk3MA%252CCg4KAnR4EggyNDAwODEwOA%22%7D%7D%7D%7D%7D',
        'x-youtube-device': 'cbr=Edge+Chromium&cbrver=91.0.864.59&ceng=WebKit&cengver=537.36&cos=Windows&cosver=10.0&cplatform=DESKTOP&cyear=2011',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.59'}
    print(url)
    response = requests.get(url=url, headers=headers,proxies=proxies).text
    #print(response)
    item = re.findall('<script nonce=".*?">var ytInitialData = (.*?);</script>', response)[0]
    item = json.loads(item)
    num = 0
    try:
        token = \
        item['contents']['twoColumnWatchNextResults']['results']['results']['contents'][3]['itemSectionRenderer'][
            'contents'][0]['continuationItemRenderer']['continuationEndpoint']['continuationCommand']['token']
        print(token)
        id = url.split('?')[-1]


        headers={
            'x-youtube-client-name': '1',
            'x-goog-visitor-id': 'CgtpWjFfTU9xUC0wVSi27oqLBg%3D%3D',
            'referer': 'https://www.youtube.com/watch?v=ZPbKCHFaHfk',
            'origin': 'https://www.youtube.com',
            'accept': '*/*',
            'content-type': 'application/json',
            'authorization': 'SAPISIDHASH 1633859390_1544d7e66026adab37efb182d7a7a2a452d2e230',
            'cookie':'VISITOR_INFO1_LIVE=iZ1_MOqP-0U; PREF=tz=Asia.Shanghai; __Secure-3PSID=AQiQp9tQBTmM78ZljHNTkmXfXYDGLxFAjP-5-vTCDIEFVbniQsaKNY53dlu7WMWRaiXWlA.; __Secure-3PAPISID=DyQInHHi4huadrnH/Azp9OgV4tuEQ4x-Td; LOGIN_INFO=AFmmF2swRgIhAP0ZD3uotK-EDbV-r7MBe1brUUFy1zItpV-Vhljz-LsJAiEAp2nBhTP0mB7j3Z0W_aVjMbV2fYdqJLHQRg_u7emeZvw:QUQ3MjNmeFJxTGFjSTZVTk9nYnBycXl0Q29yRC00dDhLQzI1dHEyNVJ5MnBYdHJZLXZyZlh4Q2tuTUNXeGJpVVhYbnBYRlFvN2NyU1Vlb0h3di1nLTNFbTVQaGpkcHpUTEo4Qi1vcHFTRkllb1JNa08taGpCNmVfdnJtM2ZQTWQ4amNDSW5QNTNkMXBRSUFjQWNCV3FMRk1RdldUcV9HT1ln; YSC=LM00KCQk5-k; __Secure-3PSIDCC=AJi4QfEVDgqA1hKZgglBFbXJWamNx0GxEydg7b2JcVD9kPHGz9ZfQA4EG7YvjjzjQ51XDGkP9g; ST-xhfma0=itct=CK8CENwwIhMIkNHTwMi_8wIVtkwPAh0KsQchMgpnLWhpZ2gtcmVjWg9GRXdoYXRfdG9fd2F0Y2iaAQYQjh4YngE%3D&csn=MC4zMTA1NjQxNTc4OTg5NjY0&endpoint=%7B%22clickTrackingParams%22%3A%22CK8CENwwIhMIkNHTwMi_8wIVtkwPAh0KsQchMgpnLWhpZ2gtcmVjWg9GRXdoYXRfdG9fd2F0Y2iaAQYQjh4YngE%3D%22%2C%22commandMetadata%22%3A%7B%22webCommandMetadata%22%3A%7B%22url%22%3A%22%2Fwatch%3Fv%3DZPbKCHFaHfk%22%2C%22webPageType%22%3A%22WEB_PAGE_TYPE_WATCH%22%2C%22rootVe%22%3A3832%7D%7D%2C%22watchEndpoint%22%3A%7B%22videoId%22%3A%22ZPbKCHFaHfk%22%2C%22watchEndpointSupportedOnesieConfig%22%3A%7B%22html5PlaybackOnesieConfig%22%3A%7B%22commonConfig%22%3A%7B%22url%22%3A%22https%3A%2F%2Fr4---sn-ouu2j-ioqz.googlevideo.com%2Finitplayback%3Fsource%3Dyoutube%26orc%3D1%26oeis%3D1%26c%3DWEB%26oad%3D3200%26ovd%3D3200%26oaad%3D11000%26oavd%3D11000%26ocs%3D700%26oewis%3D1%26oputc%3D1%26ofpcc%3D1%26msp%3D1%26odeak%3D1%26odepv%3D1%26osfc%3D1%26ip%3D164.70.90.213%26id%3D64f6ca08715a1df9%26initcwndbps%3D865000%26mt%3D1633859094%26oweuc%3D%26pxtags%3DCg4KAnR4EggyNDAwODEwOA%26rxtags%3DCg4KAnR4EggyMzk5Nzk3MA%252CCg4KAnR4EggyNDAwODEwOA%22%7D%7D%7D%7D%7D',
            'x-youtube-device': 'cbr=Edge+Chromium&cbrver=91.0.864.59&ceng=WebKit&cengver=537.36&cos=Windows&cosver=10.0&cplatform=DESKTOP&cyear=2011',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.59'}

        url = 'https://www.youtube.com/youtubei/v1/next?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'
        while True:
            # shipinurl = 'https://www.youtube.com/watch?v=I_J4p2ToXN0'
            data = {"context": {
                "client": {"hl": "zh-CN", "gl": "US", "remoteHost": "164.70.90.213", "deviceMake": "",
                           "deviceModel": "",
                           "visitorData": "CgtpWjFfTU9xUC0wVSi27oqLBg%3D%3D",
                           "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38,gzip(gfe)",
                           "clientName": "WEB", "clientVersion": "2.20211008.01.00", "osName": "Windows",
                           "osVersion": "10.0",
                           "originalUrl": "https://www.youtube.com/", "platform": "DESKTOP",
                           "clientFormFactor": "UNKNOWN_FORM_FACTOR",
                           "configInfo": {"appInstallData": "CLbuiosGEO_XrQUQktWtBRC3y60FELu6_RIQ2L6tBRCR-PwS"},
                           "timeZone": "Asia/Shanghai", "browserName": "Edge Chromium", "browserVersion": "94.0.992.38",
                           "screenWidthPoints": 867, "screenHeightPoints": 969, "screenPixelDensity": 1,
                           "screenDensityFloat": 1, "utcOffsetMinutes": 480,
                           "userInterfaceTheme": "USER_INTERFACE_THEME_LIGHT",
                           "connectionType": "CONN_CELLULAR_4G",
                           "mainAppWebInfo": {"graftUrl": shipinurl, "webDisplayMode": "WEB_DISPLAY_MODE_BROWSER",
                                              "isWebNativeShareAvailable": True}}, "user": {"lockedSafetyMode": False},
                "request": {"useSsl": True, "internalExperimentFlags": [], "consistencyTokenJars": []},
                "clickTracking": {"clickTrackingParams": ''}, "adSignalsInfo": {
                    "params": [{"key": "dt", "value": "1633859385305"}, {"key": "flash", "value": "0"},
                               {"key": "frm", "value": "0"}, {"key": "u_tz", "value": "480"},
                               {"key": "u_his", "value": "9"},
                               {"key": "u_h", "value": "1080"}, {"key": "u_w", "value": "1920"},
                               {"key": "u_ah", "value": "1040"}, {"key": "u_aw", "value": "1920"},
                               {"key": "u_cd", "value": "24"}, {"key": "bc", "value": "31"},
                               {"key": "bih", "value": "969"},
                               {"key": "biw", "value": "851"},
                               {"key": "brdim", "value": "0,0,0,0,1920,0,1920,1040,867,969"},
                               {"key": "vis", "value": "1"}, {"key": "wgl", "value": "true"},
                               {"key": "ca_type", "value": "image"}],
                    "bid": "ANyPxKrMxR0FXq7IfTyu3dhMq_751ZPqFC3NzFkySvQwxfsVs8YSU7D2X0o0ESElZnuOmIGOXjRAoNw4yMwPqKFCKcV0A_ag9Q"}},
                "continuation": token}
            data = json.dumps(data)
            while True:
                try:
                    response = requests.post(url=url,headers=headers, data=data, verify=False,proxies=proxies).json()
                    break
                except:
                    time.sleep(2)
                    pass
            # print(response)
            try:
                for i in response['onResponseReceivedEndpoints'][1]['reloadContinuationItemsCommand'][
                    'continuationItems']:
                    try:
                        pinglunzuohe = i['commentThreadRenderer']['comment']['commentRenderer']['authorText'][
                            'simpleText']
                        pinglunshijian = \
                        i['commentThreadRenderer']['comment']['commentRenderer']['publishedTimeText']['runs'][0]['text']
                        text = ''.join([i0['text'] for i0 in i['commentThreadRenderer']['comment']['commentRenderer']['contentText']['runs']])
                        num += 1
                        print([pinglunzuohe,pinglunshijian,text])
                        alldata.append({'评论作者':pinglunzuohe,'评论时间':pinglunshijian,'评论内容':text})
                        token = i['commentThreadRenderer']['replies']['commentRepliesRenderer']['contents'][0][
                            'continuationItemRenderer']['continuationEndpoint']['continuationCommand']['token']
                        data = {"context": {
                            "client": {"hl": "zh-CN", "gl": "US", "remoteHost": "164.70.90.213", "deviceMake": "",
                                       "deviceModel": "",
                                       "visitorData": "CgtpWjFfTU9xUC0wVSi27oqLBg%3D%3D",
                                       "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38,gzip(gfe)",
                                       "clientName": "WEB", "clientVersion": "2.20211008.01.00", "osName": "Windows",
                                       "osVersion": "10.0",
                                       "originalUrl": "https://www.youtube.com/", "platform": "DESKTOP",
                                       "clientFormFactor": "UNKNOWN_FORM_FACTOR",
                                       "configInfo": {
                                           "appInstallData": "CLbuiosGEO_XrQUQktWtBRC3y60FELu6_RIQ2L6tBRCR-PwS"},
                                       "timeZone": "Asia/Shanghai", "browserName": "Edge Chromium",
                                       "browserVersion": "94.0.992.38",
                                       "screenWidthPoints": 867, "screenHeightPoints": 969, "screenPixelDensity": 1,
                                       "screenDensityFloat": 1, "utcOffsetMinutes": 480,
                                       "userInterfaceTheme": "USER_INTERFACE_THEME_LIGHT",
                                       "connectionType": "CONN_CELLULAR_4G",
                                       "mainAppWebInfo": {"graftUrl": shipinurl,
                                                          "webDisplayMode": "WEB_DISPLAY_MODE_BROWSER",
                                                          "isWebNativeShareAvailable": True}},
                            "user": {"lockedSafetyMode": False},
                            "request": {"useSsl": True, "internalExperimentFlags": [], "consistencyTokenJars": []},
                            "clickTracking": {"clickTrackingParams": ''}, "adSignalsInfo": {
                                "params": [{"key": "dt", "value": "1633859385305"}, {"key": "flash", "value": "0"},
                                           {"key": "frm", "value": "0"}, {"key": "u_tz", "value": "480"},
                                           {"key": "u_his", "value": "9"},
                                           {"key": "u_h", "value": "1080"}, {"key": "u_w", "value": "1920"},
                                           {"key": "u_ah", "value": "1040"}, {"key": "u_aw", "value": "1920"},
                                           {"key": "u_cd", "value": "24"}, {"key": "bc", "value": "31"},
                                           {"key": "bih", "value": "969"},
                                           {"key": "biw", "value": "851"},
                                           {"key": "brdim", "value": "0,0,0,0,1920,0,1920,1040,867,969"},
                                           {"key": "vis", "value": "1"}, {"key": "wgl", "value": "true"},
                                           {"key": "ca_type", "value": "image"}],
                                "bid": "ANyPxKrMxR0FXq7IfTyu3dhMq_751ZPqFC3NzFkySvQwxfsVs8YSU7D2X0o0ESElZnuOmIGOXjRAoNw4yMwPqKFCKcV0A_ag9Q"}},
                            "continuation": token}
                        data = json.dumps(data)
                        response2 = requests.post(url=url, data=data,headers=headers, verify=False,proxies=proxies).json()
                        # print(response2)
                        try:
                            for i in response2['onResponseReceivedEndpoints'][1]['reloadContinuationItemsCommand'][
                                'continuationItems']:
                                pinglunzuohe = i['commentRenderer']['authorText']['simpleText']
                                pinglunshijian = i['commentRenderer']['publishedTimeText']['runs'][0]['text']
                                try:
                                    huifutext=''.join([i00['text'] for i00 in i['commentRenderer']['contentText']['runs']])
                                    alldata.append(
                                        {'评论作者': pinglunzuohe, '评论时间': pinglunshijian, '评论内容': huifutext})
                                    print('回复', pinglunzuohe, pinglunshijian, huifutext)
                                except:
                                    pass
                        except:
                            try:
                                try:
                                    for i in \
                                            response2['onResponseReceivedEndpoints'][0][
                                                'appendContinuationItemsAction'][
                                                'continuationItems']:
                                        try:
                                            pinglunzuohe = i['commentRenderer']['authorText']['simpleText']
                                            pinglunshijian = i['commentRenderer']['publishedTimeText']['runs'][0][
                                                'text']
                                            try:
                                                huifutext = ''.join([i00['text'] for i00 in
                                                                     i['commentRenderer']['contentText']['runs']])
                                                alldata.append(
                                                    {'评论作者': pinglunzuohe, '评论时间': pinglunshijian,
                                                     '评论内容': huifutext})
                                                print('回复', pinglunzuohe, pinglunshijian, huifutext)
                                            except:
                                                pass
                                        except:
                                            print('回复跳过')
                                            pass
                                except:
                                    pass
                            except:
                                pass
                    except:
                        # print('跳过')
                        pass
            except:
                try:
                    for i in response['onResponseReceivedEndpoints'][0]['appendContinuationItemsAction'][
                        'continuationItems']:
                        try:
                            pinglunzuohe = i['commentThreadRenderer']['comment']['commentRenderer']['authorText'][
                                'simpleText']
                            pinglunshijian = \
                                i['commentThreadRenderer']['comment']['commentRenderer']['publishedTimeText']['runs'][
                                    0]['text']
                            text = ''.join([i0['text'] for i0 in i['commentThreadRenderer']['comment']['commentRenderer']['contentText']['runs']])
                            print([pinglunzuohe, pinglunshijian, text])
                            alldata.append({'评论作者':pinglunzuohe,'评论时间':pinglunshijian,'评论内容':text})
                            num += 1
                            # wf.write(zifuchuangchuli(text) + '\n')
                            token = i['commentThreadRenderer']['replies']['commentRepliesRenderer']['contents'][0][
                                'continuationItemRenderer']['continuationEndpoint']['continuationCommand']['token']
                            data = {"context": {
                                "client": {"hl": "zh-CN", "gl": "US", "remoteHost": "164.70.90.213", "deviceMake": "",
                                           "deviceModel": "",
                                           "visitorData": "CgtpWjFfTU9xUC0wVSi27oqLBg%3D%3D",
                                           "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38,gzip(gfe)",
                                           "clientName": "WEB", "clientVersion": "2.20211008.01.00",
                                           "osName": "Windows",
                                           "osVersion": "10.0",
                                           "originalUrl": "https://www.youtube.com/", "platform": "DESKTOP",
                                           "clientFormFactor": "UNKNOWN_FORM_FACTOR",
                                           "configInfo": {
                                               "appInstallData": "CLbuiosGEO_XrQUQktWtBRC3y60FELu6_RIQ2L6tBRCR-PwS"},
                                           "timeZone": "Asia/Shanghai", "browserName": "Edge Chromium",
                                           "browserVersion": "94.0.992.38",
                                           "screenWidthPoints": 867, "screenHeightPoints": 969, "screenPixelDensity": 1,
                                           "screenDensityFloat": 1, "utcOffsetMinutes": 480,
                                           "userInterfaceTheme": "USER_INTERFACE_THEME_LIGHT",
                                           "connectionType": "CONN_CELLULAR_4G",
                                           "mainAppWebInfo": {"graftUrl": shipinurl,
                                                              "webDisplayMode": "WEB_DISPLAY_MODE_BROWSER",
                                                              "isWebNativeShareAvailable": True}},
                                "user": {"lockedSafetyMode": False},
                                "request": {"useSsl": True, "internalExperimentFlags": [], "consistencyTokenJars": []},
                                "clickTracking": {"clickTrackingParams": ''}, "adSignalsInfo": {
                                    "params": [{"key": "dt", "value": "1633859385305"}, {"key": "flash", "value": "0"},
                                               {"key": "frm", "value": "0"}, {"key": "u_tz", "value": "480"},
                                               {"key": "u_his", "value": "9"},
                                               {"key": "u_h", "value": "1080"}, {"key": "u_w", "value": "1920"},
                                               {"key": "u_ah", "value": "1040"}, {"key": "u_aw", "value": "1920"},
                                               {"key": "u_cd", "value": "24"}, {"key": "bc", "value": "31"},
                                               {"key": "bih", "value": "969"},
                                               {"key": "biw", "value": "851"},
                                               {"key": "brdim", "value": "0,0,0,0,1920,0,1920,1040,867,969"},
                                               {"key": "vis", "value": "1"}, {"key": "wgl", "value": "true"},
                                               {"key": "ca_type", "value": "image"}],
                                    "bid": "ANyPxKrMxR0FXq7IfTyu3dhMq_751ZPqFC3NzFkySvQwxfsVs8YSU7D2X0o0ESElZnuOmIGOXjRAoNw4yMwPqKFCKcV0A_ag9Q"}},
                                "continuation": token}
                            data = json.dumps(data)
                            response2 = requests.post(url=url, data=data, verify=False,proxies=proxies).json()
                            # print(response2)
                            try:
                                for i in response2['onResponseReceivedEndpoints'][1]['reloadContinuationItemsCommand'][
                                    'continuationItems']:
                                    try:
                                        pinglunzuohe = i['commentRenderer']['authorText']['simpleText']
                                        pinglunshijian = i['commentRenderer']['publishedTimeText']['runs'][0]['text']
                                        try:
                                            huifutext = ''.join(
                                                [i00['text'] for i00 in i['commentRenderer']['contentText']['runs']])
                                            alldata.append(
                                                {'评论作者': pinglunzuohe, '评论时间': pinglunshijian,
                                                 '评论内容': huifutext})
                                            print('回复', pinglunzuohe, pinglunshijian, huifutext)
                                        except:
                                            pass
                                    except:
                                        pass
                            except:
                                try:
                                    try:
                                        for i in \
                                                response2['onResponseReceivedEndpoints'][0][
                                                    'appendContinuationItemsAction'][
                                                    'continuationItems']:
                                            try:
                                                pinglunzuohe = i['commentRenderer']['authorText']['simpleText']
                                                pinglunshijian = i['commentRenderer']['publishedTimeText']['runs'][0][
                                                    'text']
                                                try:
                                                    huifutext = ''.join([i00['text'] for i00 in
                                                                         i['commentRenderer']['contentText']['runs']])
                                                    alldata.append(
                                                        {'评论作者': pinglunzuohe, '评论时间': pinglunshijian,
                                                         '评论内容': huifutext})
                                                    print('回复', pinglunzuohe, pinglunshijian, huifutext)
                                                except:
                                                    pass
                                            except:
                                                print('回复跳过')
                                                pass
                                    except:
                                        pass
                                except:
                                    pass
                        except:
                            # print('跳过')
                            pass
                except:
                    pass
            try:
                token = \
                    response['onResponseReceivedEndpoints'][1]['reloadContinuationItemsCommand']['continuationItems'][
                        -1][
                        'continuationItemRenderer']['continuationEndpoint']['continuationCommand']['token']
            except:
                token = \
                    response['onResponseReceivedEndpoints'][0]['appendContinuationItemsAction']['continuationItems'][
                        -1][
                        'continuationItemRenderer']['continuationEndpoint']['continuationCommand']['token']
            print(token)
    except Exception as ex:
        print(response)
        pass
    shaixuanhoudata=[]
    dataframe=pandas.DataFrame(data=alldata,columns=list(alldata[0].keys()))
    dataframe.to_excel('{}.xlsx'.format(wenjianid),index=False)
url1='https://www.youtube.com/watch?v=e_F-KHVDOCo'

getpinglun('https://www.youtube.com/watch?v=EiAhMr6IJTQ')