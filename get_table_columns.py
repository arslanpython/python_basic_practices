# import mysql.connector
#
#
# def get_table_colums(table_name):
#     try:
#         print 'Making Connection...'
#         sql_connection = mysql.connector.connect(
#             host="192.169.189.67",
#             user="scraper_dev",
#             passwd="password123",
#             database="ScraperSandboxDatabase"
#         )
#
#         sql_conn_cursor = sql_connection.cursor()
#         print 'Connected.'
#
#         query = "SHOW COLUMNS FROM " + table_name
#         print query
#
#         sql_conn_cursor.execute(query)
#         columns = sql_conn_cursor.fetchall()
#         columns = [col[0] for col in columns]
#         columns = {i: v for i, v in enumerate(columns)}
#         print columns
#
#     except Exception as e:
#         print e
#
# get_table_colums("T_People")