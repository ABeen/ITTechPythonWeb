# -*- coding:utf-8 -*-

""" 实用程序

    作者: ABeen
    创建: 2018-07-28
"""


def count_page(page_index=1, page_size=10, page_page_count=10, count=0):
    """ 分屏分页算法
            每屏显示page_page_count个页码，每页显示page_size条。

        Args:
            page_index  :  当前页码
            page_size   :  每页显示条数
            page_preview:  前一页
            page_next   :  后一页
            page_count  :  总页数
            page_links  :  页码列表
            count       :  总记录数
            page_page_count : 每页显示页码数

        Return:
            return dict(
                    page_index=page_index,
                    page_size=page_size,
                    page_preview=page_preview,
                    page_next=page_next,
                    page_count=page_count,
                    page_links=page_links,
                    count=count,
                    page_page_count=page_page_count)
    """
    # 计算总页数
    page_count, remainder = divmod(count, page_size)
    if remainder > 0:
        page_count += 1

    # 计算前页
    page_preview = page_index - page_page_count
    if page_index <= page_page_count:
        page_preview = page_index

    # 计算后页
    page_next = page_index + page_page_count
    if page_index > page_count - page_page_count:
        page_next = page_count

    # 计算每页页码数
    start = (page_index - 1)/page_page_count * page_page_count + 1
    end = (page_index - 1)/page_page_count * page_page_count + page_page_count
    if end > page_count:
        end = page_count
    page_links = range(int(start), int(end) + 1)

    return dict(
        page_index=page_index,
        page_size=page_size,
        page_preview=page_preview,
        page_next=page_next,
        page_count=page_count,
        page_links=page_links,
        count=count,
        page_page_count=page_page_count)


def set_default_value(source_dict, list_key, default_value):
    """ 设置默认值

        给 source_dict 字典在无值的时候，设置 list_key 里的默认 default_value
    """
    for key in list_key:
        source_dict[key] = source_dict.get(key, default_value)
    return source_dict


__all__ = ["count_page", "set_default_value"]
