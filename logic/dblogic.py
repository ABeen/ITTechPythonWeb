# -*- coding:utf-8 -*-

""" 数据表基本操作通用逻辑

    作者: ABeen
"""

from bson import ObjectId
from pymongo import MongoClient

DMONGODB_HOST='localhost'
BNAME = 'dbname'


class DBLogic(object):
    """ pymongo DB logic
    """
    def __init__(self, table='test', dbname=DBNAME):
        self.db = self.init_db()
        self.table = table

    def init_db(self):
        mongoclient = MongoClient(host=MONGODB_HOST or "localhost", port=27017,
                                  connect=False)
        return mongoclient[DBNAME]

    def find_count(self, **kwargs):
        return self.db[self.table].find(kwargs).count()

    def add(self, **kwargs):
        return str(self.db[self.table].insert(kwargs))

    def insert_one(self, **kwargs):
        return self.db[self.table].insert_one(**kwargs)

    def findbyid(self, sid):
        return mongo_conv(self.db[self.table].find_one({'_id': ObjectId(sid)}))

    def findone(self, **kwargs):
        return mongo_conv(self.db[self.table].find_one(kwargs))

    def find(self, page_index=1, page_size=10, **kwargs):
        """ 查找
            1. 提取Dict参数说明:
                cond    :  查询条件
                values  :  返回数据字段

            2. 返回Dict数据说明:
                count   :  数据总条件
                data    :  当前返回数据列表
        """
        page_index -= 1
        cond = kwargs.get('cond', None)
        msort = kwargs.get('msort', [('addon', -1)])
        if not msort:
            msort = [('addon', -1)]
        values = kwargs.get('values', None)

        result = {}
        result['count'] = self.db[self.table].find(cond).count()
        if result['count'] <= 0:
            result['data'] = []
            return result

        cursor = self.db[self.table].find(cond, values).sort(msort)
        cursor = cursor.skip(page_index * page_size).limit(page_size)
        result['data'] = mongo_conv(list(cursor))
        return result

    def find_nopage(self, **kwargs):
        """
            1. 提取Dict参数说明:
                cond    :  查询条件
                values  :  返回数据字段

            2. 返回Dict数据说明:
                count   :  数据总条件
                data    :  当前返回数据列表
        """
        values = kwargs.get('values', None)
        cond = kwargs.get('cond', None)
        msort = kwargs.get('msort', [('addon', -1)])

        result = {}
        result['count'] = self.db[self.table].find(cond).count()
        if result['count'] <= 0:
            result['data'] = []
            return result

        cursor = self.db[self.table].find(cond, values).sort(msort)
        result['data'] = mongo_conv(list(cursor))
        return result

    def cursor(self, **kwargs):
        """
            1. 提取Dict参数说明:
                cond    :  查询条件
                values  :  返回数据字段

            2. 返回Dict数据说明:
                count   :  数据总条件
                data    :  当前返回数据列表
        """
        values = kwargs.get('values', None)
        cond = kwargs.get('cond', None)
        return self.db[self.table].find(cond, values)

    def find_aggregate(self, pipeline, **kwargs):
        """ 聚合管道查询
        """
        return self.db[self.table].aggregate(pipeline, **kwargs)

    def exist(self, **kwargs):
        return self.db[self.table].find_one(kwargs)

    def update(self, cond, setdata):
        setdata = {"$set": setdata}
        return str(self.db[self.table].update(cond, setdata, multi=True))

    def updatebyid(self, sid, setdata):
        cond = {'_id': ObjectId(sid)}
        setdata = {"$set": setdata}
        return str(self.db[self.table].update(cond, setdata))

    def update_inc(self, sid, key, count):
        cond = {'_id': ObjectId(sid)}
        incdata = {"$inc": {key: count}}
        return str(self.db[self.table].update(cond, incdata, multi=False))

    def remove(self, **kwargs):
        return str(self.db[self.table].remove(kwargs, multi=True))

    def find_one_and_replace(self, lfilter, replace_doc, upsert=False):
        # returnDocument.BEFORE = False  returnDocument.AFTER = True
        return self.db[self.table].find_one_and_replace(lfilter, replace_doc,
                                                        upsert=upsert,
                                                        return_document=True)

    def find_one_and_update(self, lfilter, setdata, upsert=False):
        # returnDocument.BEFORE = False  returnDocument.AFTER = True
        setdata = {"$set": setdata}
        return self.db[self.table].find_one_and_update(lfilter, setdata,
                                                       upsert=upsert,
                                                       return_document=True)

    def find_one_and_update_byid(self, sid, setdata, upsert=False):
        lfilter = {'_id': ObjectId(sid)}
        setdata = {"$set": setdata}
        return self.db[self.table].find_one_and_update(lfilter, setdata,
                                                       upsert=upsert,
                                                       return_document=True)


def mongo_conv(d):
    """ 将 MongoDB 返回结果中的:
            (1) Unicode 还原为 str。
            (2) ObjectId 还原为 str。
    """
    if isinstance(d, (str, ObjectId)):
        return str(d)
    elif isinstance(d, (list, tuple)):
        return [mongo_conv(x) for x in d]
    elif isinstance(d, dict):
        return dict([(mongo_conv(k), mongo_conv(v)) for k, v in d.items()])
    else:
        return d


__all__ = ['DBLogic']
