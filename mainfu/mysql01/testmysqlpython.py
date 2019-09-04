from mysqlpython import mysqlpython


sqlh = mysqlpython('localhost',3306,'liuyandb','root','123456')
sql_update = 'update sheng set s_id=300000 where s_name="湖北省";'

sqlh.zhixing(sql_update)