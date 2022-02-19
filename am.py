# This is a sample Python script.
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.raw import functions
from pyrogram import filters
from lib import Analize
import time
app = Client("AddMember", config_file="config.ini")

channelLink = "https://t.me/{}"
channelName = "{}"


def Add_MB(username:str):
    with app:
        i = 0

        i += 1
        print(app.get_chat(chat_id))
        channelName = '{}'
        try:
            app.send(
            functions.channels.InviteToChannel(
                channel = app.resolve_peer(f'@{channelName}'),
                users = []
                )
            )
            time.sleep(10)
        except Exception as err:
            raise Exception(err)
            time.sleep(3)
            
def GetMemberFromChannel(chat_id:int):
    app.start()
    listMembers = []

    for i in app.iter_chat_members(chat_id=chat_id):
    	listMembers.append(i)
    app.stop()
    return listMembers





def chatlist():
    app.start()
    x = app.get_dialogs()
    #print(app.get_messages('me'))
    ot = []
    #print(f'{i}- Type: {x.chat.type}- title: {x.chat.title}- Id: {x.chat.id}')
    for i in x:
        try:
            if i.chat.type == 'supergroup':
                ot.append([i.chat.id,i.chat.username,i.chat.type])
            else:
                print(f'Cant Added[{i}]')
        except Exception as err:
            print(err)
    app.stop()
    return ot


def GetAllIds():
    obj = chatlist()
    ot = []
    e = 0
    out = []
    for i in obj:
        ot.append(GetMemberFromChannel(i[0]))
        e += 1

    for i in range(len(ot)):
        for j in range(len(ot[i])):
            out.append(ot[i][j].user)
    return out



def send_msg(chat_id,text:str):
    app.start()
    try:
        app.send_message(chat_id,text)
    except Exception as err:
        print(err)
    app.stop()


import json


if __name__ == '__main__':
    print("Start...")
    
    # sendmessage("Hi")
    # sendphoto()
    # rdMessage
    #s = chatlist()
    # getmembers()
    # gethistory()
    # gethistorymember()
    #obj = chatlist()
    #GetMemberFromChannel()
    #for i in ids:
    #    print(i)
    #    Add_MB(i)
    #    time.sleep(0)
    print(GetAllIds())
