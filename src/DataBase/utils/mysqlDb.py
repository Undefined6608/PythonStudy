import pymysql

""" 常用模块：读写MySQL """

def get_conn():
    """
    获取 MySQL 的连接
    :return: Mysql Connection
    """
    return pymysql.connect(
        host="127.0.0.1",
        port= 3306,
        user="root",
        password="071b956d-9b14-4bc3-8a59-a78ed16eb153",
        db="py_study_mysql",
        charset="utf8"
    )

def query_data(sql:str) -> dict:
    """
    根据 SQL 查询数据并返回
    :param sql: SQL 语句
    :return: list[dict]
    """
    
    conn = get_conn()
    
    try:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        ## 关闭链接
        conn.close()

def insert_or_update_data(sql:str) -> None:
    """
    执行新增 insert 或者 update 的 SQL
    :param sql: insert or update sql
    :return: 不返回内容
    """
    conn = get_conn()
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        ## 注意，要 commit 才可以生效
        conn.commit()
    finally:
        ## 关闭链接
        conn.close()