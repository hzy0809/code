#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/24 15:26
# @Author  : hzy
# @File    : sendemail.py
# @Software: PyCharm

from openpyxl import Workbook
import logging
import unittest
from datetime import datetime, timedelta
from avalon.material import Material
from saber_sdk.op.pyscript.v2.src.core import func

import requests
from requests.auth import HTTPBasicAuth
import poplib
import pandas as pd
import urllib.parse
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.header import Header
import smtplib

receivers = [
    'jinqi@aidigger.com',
    'wuna@aidigger.com',
    'liyunjiao@aidigger.com',
    'xinglu@aidigger.com',
    'fanshaohui@aidigger.com',
    'yinyi@aidigger.com'
]
# receivers = [
#     # 'chen.chen@aidigger.com',
#     'jinqi@aidigger.com'
# ]

head = """
        <head>
            <meta charset="utf-8">
            <STYLE TYPE="text/css" MEDIA=screen>

                table.dataframe {
                    border-collapse: collapse;
                    border: 2px solid #a19da2;
                    /*居中显示整个表格*/
                    margin: auto;
                }

                table.dataframe thead {
                    border: 2px solid #91c6e1;
                    background: #f1f1f1;
                    padding: 10px 10px 10px 10px;
                    color: #333333;
                }

                table.dataframe tbody {
                    border: 2px solid #91c6e1;
                    padding: 10px 10px 10px 10px;
                }

                table.dataframe tr {

                }

                table.dataframe th {
                    vertical-align: top;
                    font-size: 14px;
                    padding: 10px 10px 10px 10px;
                    color: #105de3;
                    font-family: arial;
                    text-align: center;
                }

                table.dataframe td {
                    text-align: center;
                    padding: 10px 10px 10px 10px;
                }

                body {
                    font-family: 宋体;
                }

                h1 {
                    color: #5db446
                }

                div.header h2 {
                    color: #0002e3;
                    font-family: 黑体;
                }

                div.content h2 {
                    text-align: center;
                    font-size: 28px;
                    text-shadow: 2px 2px 1px #de4040;
                    color: #fff;
                    font-weight: bold;
                    background-color: #008eb7;
                    line-height: 1.5;
                    margin: 20px 0;
                    box-shadow: 10px 10px 5px #888888;
                    border-radius: 5px;
                }

                h3 {
                    font-size: 22px;
                    background-color: rgba(0, 2, 227, 0.71);
                    text-shadow: 2px 2px 1px #de4040;
                    color: rgba(239, 241, 234, 0.99);
                    line-height: 1.5;
                }

                h4 {
                    color: #e10092;
                    font-family: 楷体;
                    font-size: 20px;
                    text-align: center;
                }

                td{
                    /*width: 60px;*/
                    min-width: 60px;
                    max-width: 80px;
                    max-height: 300px;
                }

            </STYLE>
        </head>
        """

body = """
        <body>

        <div align="center" class="header">
            <!--标题部分的信息-->
            <h1 align="center">截止昨天结束的数据</h1>
            <h2 align="center">{yesterday}</h2>
        </div>

        <hr>

        <div class="content">
            <!--正文内容-->
            <h2> </h2>

            <div>
                {df_html}

            </div>
            <hr>

            <p style="text-align: center">

            </p>
        </div>
        </body>
        """

account_url = 'https://owl.aizao.com/api/v4/organization/3461/accounts?page=1&size=10000'
data_url = "https://video-api.aizao.com/api/v1/third_accounts/{}/video_statistics?&date={}&page=1&page_size=10000"
daily_url = "https://video-api.aizao.com/api/v1/third_accounts/{}/daily_statistics"
bs_header = {
    "content-type": "application/json;charset=UTF-8"
}


def get_yesterday():
    d = datetime.now()
    at = (d - timedelta(1)).strftime('%Y-%m-%d')
    return at


q_date = get_yesterday()


def parse_to_html(df):
    global head, body
    pd.set_option('display.max_colwidth', -1)  # 设置表格数据完全显示（不出现省略号）
    df_html = df.to_html(escape=False)  # DataFrame数据转化为HTML表格形式
    this_body = body.format(yesterday=get_yesterday(), df_html=df_html)
    html_data = "<html>" + head + this_body + "</html>"
    html_data = html_data.replace('\n', '').encode("utf-8")
    return html_data


def send(html_data, title, filename):
    title = '{}_{}'.format(title, q_date)
    global receivers
    mail_host = 'smtpdm.aliyun.com'
    mail_user = 'socrates_editor@aidigger.com'
    mail_pass = 'socrates_editor2333'
    mail_host = 'smtp.163.com'
    mail_user = 'tools_jq@163.com'
    mail_pass = '@fFKqt*852YU/t6'
    mail_pass = 'BYGASULOBASTHXYW'  # 授权密码
    try:
        me = mail_user
        msg = MIMEMultipart()
        attach_table = MIMEApplication(open(filename, 'rb').read())
        # 给附件增加标题
        attach_table.add_header('Content-Disposition', 'attachment', filename='{}.xlsx'.format(title))
        #  这样的话，附件名称就可以是中文的了，不会出现乱码
        attach_table.set_charset('utf-8')
        msg.attach(attach_table)

        msg['Subject'] = title
        msg['From'] = me
        msg['To'] = ",".join(receivers)
        handle = smtplib.SMTP(mail_host, 25)
        logging.info('smtp success')
        # handle = smtplib.SMTP()
        # handle.connect(mail_host, 465)
        handle.login(mail_user, mail_pass)
        logging.info('login success')
        # msg = "To: 281742852@qq.com\r\nFrom: jinqi_601@163.com\r\nSubject: 电脑已开机 \r\n\r\nsomeone open you computer...do you want shutdown\r\n"

        context = MIMEText(html_data, _subtype='html', _charset='utf-8')  # 解决乱码

        # msg.attach(att)
        msg.attach(context)
        # print(msg)
        handle.sendmail(mail_user, receivers, msg.as_string())
        logging.info('send 完成')
        handle.close()

        return True
    except Exception as e:
        print(e)
        return False


def get_account():
    res = requests.get(account_url, headers=bs_header, auth=HTTPBasicAuth("19999999999", "AI2021@lp0517"))
    res = res.json()
    return res


def get_video_play_url(video, account_type):
    if not video['share_url']:
        return '暂无'
    if account_type == 'douyin':
        return video['share_url']
    elif account_type == 'kuaishou':
        return "https://video.kuaishou.com/short-video/{}".format(video['item_id'])
    else:
        return '暂无'


def video_data(account_info):
    data_items = []
    for item in account_info['data']:
        idf = item['identifier']
        if item['account_type'] not in ['kuaishou', 'douyin']:
            print("continue")
            continue
        res = requests.get(data_url.format(idf, q_date), headers=bs_header)
        res = res.json()
        item_data = res['results']
        for video in item_data:
            data_items.append({
                "账户名称": item['account_info'].get('name', item['account_info'].get('nickname', '')),
                "时间": q_date,
                "渠道类型": item['account_type'],
                "视频名称": video['title'],
                "视频链接": get_video_play_url(video, item['account_type']),
                # "https://video.kuaishou.com/short-video/{}".format(video['item_id']) if item['account_type'] == 'kuaishou' else "暂无",
                "播放": video['total_play'],
                "点赞": video['total_like'],
                "评论": video['total_comment'],
                "转发": video['total_share'],
                "视频发布时间": video['create_time'],
                "更新时间": video['update_time'],
                "原始meta": video,
                "账户meta": item
            })
    d_map = {}
    df1_c_list = ["账户名称", "时间", "渠道类型", "视频名称", "视频链接", "播放", "点赞", "评论", "转发", "视频发布时间"]
    for k in df1_c_list:
        d_map[k] = []
    for item in data_items:
        for key in df1_c_list:
            d_map[key].append(item[key])
    return d_map, df1_c_list


def account_data(account_info):
    """
    total_comment: 3
    total_fans: 24
    total_issue: 17
    total_like: 67
    total_play: 6216
    total_share: 10
    """
    data_items = []
    for item in account_info['data']:
        idf = item['identifier']
        if item['account_type'] not in ['kuaishou', 'douyin']:
            print("continue")
            continue
        res = requests.get(daily_url.format(idf), headers=bs_header)
        res = res.json()
        item_data = res['results']
        if len(item_data) == 0 or item_data[0]['date'] != q_date:
            print(item['account_info'].get('name', item['account_info'].get('nickname', '')))
            data_items.append({
                "账户名称": item['account_info'].get('name', item['account_info'].get('nickname', '')),
                "时间": "数据获取异常，请检查账户授权",
                "渠道类型": item['account_type'],
                "累积播放": 0,
                "累积点赞": 0,
                "累积评论": 0,
                "累积转发": 0,
                "累积粉丝": 0,
                "累积作品": 0,
                "新增播放": 0,
                "新增点赞": 0,
                "新增评论": 0,
                "新增转发": 0,
                "新增粉丝": 0,
                "新增作品": 0,
            })
        else:
            video = item_data[0]
            data_items.append({
                "账户名称": item['account_info'].get('name', item['account_info'].get('nickname', '')),
                "时间": video['date'],
                "渠道类型": item['account_type'],
                "累积播放": video['total_play'],
                "累积点赞": video['total_like'],
                "累积评论": video['total_comment'],
                "累积转发": video['total_share'],
                "累积粉丝": video['total_fans'],
                "累积作品": video['total_issue'],
                "新增播放": video['new_play'],
                "新增点赞": video['new_like'],
                "新增评论": video['new_comment'],
                "新增转发": video['new_share'],
                "新增粉丝": video['new_fans'],
                "新增作品": video['new_issue'],
                "原始meta": video,
                "账户meta": item
            })
    df1_c_list = ["账户名称", "时间", "渠道类型", "累积播放", "累积点赞", "累积评论", "累积转发", "累积粉丝", "累积作品", "新增播放", "新增点赞", "新增评论", "新增转发",
                  "新增粉丝", "新增作品"]
    d_map = {}
    for k in df1_c_list:
        d_map[k] = []
    for item in data_items:
        for key in df1_c_list:
            d_map[key].append(item[key])
    return d_map, df1_c_list


def retxls(df1, df1_c_list, title):
    filename = './{}_{}.xlsx'.format(title, get_yesterday())
    out_df = pd.DataFrame(df1, columns=df1_c_list)
    out_df.to_excel(filename, "Sheet1", engine="openpyxl")
    print(filename)
    return filename


@func.register()
def main(material: Material, config: dict, context: dict) -> Material:
    acc = get_account()
    # 单视频累积
    d_map, d_list = video_data(acc)
    logging.info("parse_to_df")
    df = pd.DataFrame(d_map)
    html_data = parse_to_html(df)
    logging.info("parse_to_html")
    filename = retxls(df, d_list, '单视频数据')
    send(html_data, '单视频数据', filename)

    # 账户部分
    d_map, d_list = account_data(acc)
    logging.info("parse_to_df")
    df = pd.DataFrame(d_map)
    html_data = parse_to_html(df)
    logging.info("parse_to_html")
    filename = retxls(df, d_list, '分账户数据')
    send(html_data, '分账户数据', filename)

    return material


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.DEBUG)

    raw_dict = {}
    config = {}
    context = {}

    logging.info("start testing...")
    print(main(Material.from_raw_dict(raw_dict), config, context))
