import itchat
import threading
import time

def send_group_message(message, group_name):
    """向指定的群发送一条消息"""
    group = itchat.search_chatrooms(name=group_name)
    if group:
        itchat.send_msg(msg=message, toUserName=group[0]['UserName'])
    else:
        print(f"未找到群：{group_name}")

def schedule_message(message, group_name, interval):
    """定时发送消息"""
    
    send_group_message(message, group_name)
    threading.Timer(interval, schedule_message, args=(message, group_name, interval)).start()

# 每5分钟（300秒）向名为"Group Name"的群发送一条消息
schedule_message("这是一条定时消息", "Group Name", 300)

# 防止程序立即退出
while True:
    time.sleep(1000)
