#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/24 15:58
# @Author  : hzy
# @File    : send_email.py
# @Software: PyCharm
import pymongo
import logging
from datetime import datetime, timedelta
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib
import pymysql
import xlsxwriter

receivers = [
    'huzhenyu@aidigger.com',
    # 'jinqi@aidigger.com',
]

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


def send(html_data, title, filename):
    # title = '{}_{}'.format(title, q_date)
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


class Client(object):

    def __init__(self):
        self._client = None

    @property
    def params(self):
        return {
            'host': 'rm-bp1szaw50w7xu19m1.mysql.rds.aliyuncs.com',
            'port': 3306,
            'user': 'bees_platform',
            'password': 'E1RXCMQJUS02YX0',
            'database': 'bees_platform',
            'cursorclass': pymysql.cursors.DictCursor,
            'charset': 'utf8mb4'
        }

    def __get__(self, instance, owner):
        if self._client is None:
            self._client = pymysql.connect(**self.params)
        return self._client


class MongoCollection(object):
    def __init__(self):
        self._collection = None
        self._db_name = 'socrates_graph_car_prod'
        self._collection_name = 'article_statistics'
        self.mongo = None

    @property
    def params(self):
        return "mongodb://socrates_graph_car:socrates_graph_car_eigen123@dds-bp17fa78084b6c342.mongodb.rds.aliyuncs.com:3717/socrates_graph_car_prod?replicaSet=mgset-16493927"

    def __get__(self, instance, owner):
        if self._collection is None:
            self.mongo = pymongo.MongoClient(self.params)
            self._collection = self.mongo.get_database(self._db_name).get_collection(self._collection_name)
        return self._collection

    def __delete__(self, instance):
        if self.mongo is not None:
            self.mongo.close()


class ArticleStatistics(object):
    client = Client()
    collection = MongoCollection()

    def __init__(self, folder_id=None, folder_name=None):
        """

        :param folder_id: int or List[int]
        :param folder_name: str or List[str]
        """
        self._folder_id = folder_id
        self.folder_name = folder_name
        self._folder = None
        if self._folder_id is None and self.folder_name is None:
            raise ValueError('folder_id和folder_name不能同时为空')

    @property
    def folder(self):
        if self._folder is None:
            if not isinstance(self._folder_id, list):
                self._folder_id = [self._folder_id]
            if not isinstance(self.folder_name, list):
                self.folder_name = [self.folder_name]
            self._folder = self._execute(self.folder_sql, names=self.folder_name, ids=self._folder_id)
        return {x['id']: x for x in self._folder}

    @property
    def folder_sql(self):
        return 'SELECT * FROM folder WHERE is_deleted = FALSE AND (`name` IN %(names)s OR id IN %(ids)s)'

    @property
    def article_week_sql(self):
        return """SELECT DISTINCT folder_id,
                        'last_week' AS 'period',
                        COUNT( IF ( create_time BETWEEN %(begin_date)s AND %(end_date)s, 1, NULL ) ) AS 'create_count',
                        COUNT( IF ( last_publish_time BETWEEN %(begin_date)s AND %(end_date)s, 1, NULL ) ) AS 'publish_count'
                    FROM
                        user_article_model 
                    WHERE
                        folder_id IN %(ids)s
                    GROUP BY
                        folder_id;"""

    @property
    def article_month_sql(self):
        return """SELECT DISTINCT folder_id,
                        CONCAT(%(year)s,'年',%(month)s,'月') AS 'period',
                        COUNT( IF ( YEAR(create_time)=%(year)s AND MONTH(create_time)=%(month)s, 1, NULL ) ) AS 'create_count',
                        COUNT( IF ( YEAR(last_publish_time)=%(year)s AND MONTH(last_publish_time)=%(month)s, 1, NULL ) ) AS 'publish_count' 
                    FROM
                        user_article_model 
                    WHERE
                        folder_id IN %(ids)s
                    GROUP BY
                        folder_id;"""

    def get_last_week_period(self):
        last_week_end = self.get_previous_by_day(6)
        last_week_begin = self.get_previous_by_day(0, start_date=last_week_end)
        return last_week_begin, last_week_end

    def get_month_statistics(self, folder_id=None, year: int = None, month: int = None):
        folder_ids = [folder_id] if folder_id else list(self.folder.keys())
        year = year or datetime.today().year
        month = month or datetime.today().month
        return self._execute(self.article_month_sql, year=year, month=month, ids=folder_ids)

    def get_last_week_statistics(self, folder_id=None):
        folder_ids = [folder_id] if folder_id else list(self.folder.keys())
        week_begin, last_week_end = self.get_last_week_period()
        week_end = last_week_end + timedelta(days=1)
        return self._execute(self.article_week_sql, begin_date=week_begin, end_date=week_end,
                             ids=folder_ids)

    def get_folder_statistics_from_mongo(self, folder_id):
        res = self.collection.find_one({'folder_id': folder_id})
        if not res:
            data = {x['period']: x for x in self.get_folder_statistics_from_sql(folder_id)}
            self.write_to_mongo(folder_id, data)
        else:
            data = res['data']
            new_data = {x['period']: x for x in
                        self.get_folder_statistics_from_sql(folder_id, begin_date=datetime.today())}
            data.update(new_data)
            self.write_to_mongo(folder_id, new_data)

        # 组装数据
        last_week = data.pop('last_week')
        total_create = sum([x['create_count'] for x in data.values()])
        total_publish = sum([x['publish_count'] for x in data.values()])
        begin, end = self.get_last_week_period()
        # data[f'最近一周（{begin}-{end}）'] = last_week
        last_week['period'] = f'最近一周（{str(begin)[5:]}至{str(end)[5:]}）'
        folder_name = last_week['folder_name']
        result = [{
            'folder_name': folder_name,
            'period': '总量',
            'create_count': total_create,
            'publish_count': total_publish
        }, last_week]
        result.extend([data[x] for x in sorted(data, key=lambda x: (int(x[:4]), int(x[5:-1])), reverse=True)])
        return result

    def get_statistics(self):
        res = []
        for folder_id in self.folder:
            res.extend(self.get_folder_statistics_from_mongo(folder_id))
        return res

    def get_folder_statistics_from_sql(self, folder_id, begin_date: datetime.date = None):
        folder = self.folder[folder_id]
        # begin_date = folder['create_time'].date()
        begin_date = begin_date or datetime.today().replace(year=2020, month=9)
        res = []
        for year, month in self.get_year_month(begin_date):
            data = self.get_month_statistics(folder_id, year=year, month=month)
            res.extend(data)
        res.extend(self.get_last_week_statistics(folder_id))
        for x in res:
            x['folder_name'] = folder['name']
        return res

    @staticmethod
    def get_year_month(begin_date: datetime.date, end_date=None):
        end_date = end_date or datetime.today().date()
        year, month = begin_date.year, begin_date.month
        end_year, end_month = end_date.year, end_date.month
        while not (year >= end_year and month > end_month):
            yield year, month
            month = month + 1
            if month == 13:
                year += 1
                month = 1

    def write_to_mongo(self, folder_id, data: dict):
        self.collection.update_one({'folder_id': folder_id},
                                   {'$set': {'folder_id': folder_id, 'update_time': datetime.now(),
                                             **{'data.' + key: value for key, value in data.items()}}},
                                   upsert=True)

    @staticmethod
    def get_previous_by_day(index: int, start_date: datetime.date = None):
        """

        :param index: Monday 0 ~ Sunday 6
        :param start_date:
        :return:
        """
        if start_date is None:
            start_date = datetime.today().date()
        day_num = start_date.weekday()
        days_ago = (7 + day_num - index) % 7
        days_ago = 7 if days_ago == 0 else days_ago
        return start_date - timedelta(days=days_ago)

    def _execute(self, sql, **kwargs):
        with self.client.cursor() as cursor:
            cursor.execute(sql, kwargs)
        return cursor.fetchall()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()
        del self.collection


def statistics_data(info):
    data_items = []
    for item in info:
        data_items.append(
            {
                '时间': item['period'],
                '文件夹': item['folder_name'],
                '已发布文章数量': item['publish_count'],
                '生产文章数量': item['create_count']
            }
        )
    d_map = {}
    df1_c_list = ['文件夹', '时间', '已发布文章数量', '生产文章数量']
    for k in df1_c_list:
        d_map[k] = []
    for item in data_items:
        for key in df1_c_list:
            d_map[key].append(item[key])
    return d_map, df1_c_list


def get_yesterday():
    d = datetime.now()
    at = (d - timedelta(1)).strftime('%Y-%m-%d')
    return at


def parse_to_html(df):
    global head, body
    pd.set_option('display.max_colwidth', -1)  # 设置表格数据完全显示（不出现省略号）
    df_html = df.to_html(escape=False)  # DataFrame数据转化为HTML表格形式
    this_body = body.format(yesterday=get_yesterday(), df_html=df_html)
    html_data = "<html>" + head + this_body + "</html>"
    html_data = html_data.replace('\n', '').encode("utf-8")
    return html_data


def retxls(df1, df1_c_list, title):
    filename = './{}_{}_1.xlsx'.format(title, get_yesterday())
    out_df = pd.DataFrame(df1, columns=df1_c_list)
    writer = pd.ExcelWriter(filename, engine="xlsxwriter")
    out_df.to_excel(writer, sheet_name="Sheet1", index=False)
    merge_cells(out_df, writer)
    print(filename)
    return filename


def merge_cells(df, writer):
    start_cells = [1]
    for row in range(2, len(df) + 1):
        if df.loc[row - 1, '文件夹'] != df.loc[row - 2, '文件夹']:
            start_cells.append(row)
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    merge_format = workbook.add_format({'align': 'center', 'valign': 'vcenter', 'border': 2})

    lastRow = len(df)

    for row in start_cells:
        try:
            endRow = start_cells[start_cells.index(row) + 1] - 1
            if row == endRow:
                worksheet.write(row, 0, df.loc[row - 1, '文件夹'], merge_format)
            else:
                worksheet.merge_range(row, 0, endRow, 0, df.loc[row - 1, '文件夹'], merge_format)
        except IndexError:
            if row == lastRow:
                worksheet.write(row, 0, df.loc[row - 1, '文件夹'], merge_format)
            else:
                worksheet.merge_range(row, 0, lastRow, 0, df.loc[row - 1, '文件夹'], merge_format)

    writer.save()


if __name__ == '__main__':
    with ArticleStatistics(folder_id=[257, 259, 256, 326, 323, 389]) as arts:
        data = arts.get_statistics()
    d_map, d_list = statistics_data(data)
    logging.info("parse_to_df")
    df = pd.DataFrame(d_map)
    html_data = parse_to_html(df)
    logging.info("parse_to_html")
    filename = retxls(df, d_list, '太平洋稿件统计')
    df = pd.read_excel(filename)
    # send(html_data, '太平洋稿件统计', filename)
