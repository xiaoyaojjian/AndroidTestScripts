#!/usr/bin/evn python
# -*- coding:utf-8 -*-

# FileName RequestApi.py
# Author: HeyNiu
# Created Time: 20160729
"""
运行api测试总入口
"""


def launcher_api_test(app_type):
    """
    请求总入口
    :param app_type: 0 >> A; 1 >> B; 2 >> C; 3 >> D
    :return:
    1.获取接口列表
    2.与本地sessions对比
    3.差异化文件，是否继续
    3.1否 继续录制接口
    3.2是 开始跑接口

    """
    if app_type == 0:
        import sessions.DongDongRequests
        sessions.DongDongRequests.DongDongRequests(0).start()
    elif app_type == 1:
        import sessions.DongDongRequests
        sessions.DongDongRequests.DongDongRequests(1).start()
    elif app_type == 2:
        import sessions.JiaZaiRequests
        sessions.JiaZaiRequests.JiaZaiRequests().start()
    elif app_type == 3:
        import sessions.DecorationRequests
        sessions.DecorationRequests.DecorationRequests().start()


if __name__ == "__main__":
    print('接口回归测试启动...')
    launcher_api_test(0)
