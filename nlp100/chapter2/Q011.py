# coding: utf-8

from util import util

def Q_011_0():
    """ 11. タブをスペースに置換
    タブ1文字につきスペース1文字に置換せよ．
    """

    data = []
    with open('data/hightemp.txt', 'r') as f:
        data = [line.strip().replace('\t', ' ') for line in f]

    return data

def Q_011_1():
    """ 11. タブをスペースに置換
    確認にはsedコマンドを用いよ．
    """

    ite = util.exe_cmd('sed "s/\t/ /g" data/hightemp.txt')
    return list(ite)

def Q_011_2():
    """ 11. タブをスペースに置換
    確認にはtrコマンドを用いよ．
    """

    ite = util.exe_cmd('tr "\t" " " < data/hightemp.txt')
    return list(ite)

def Q_011_3():
    """ 11. タブをスペースに置換
    確認にはexpandコマンドを用いよ．
    """

    ite = util.exe_cmd('expand -t 1 data/hightemp.txt')
    return list(ite)
