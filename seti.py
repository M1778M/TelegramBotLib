from pyrogram import Client
import json

app = Client('test',config_file='config.ini')



def chatlist():
    app.start()
    x = app.get_dialogs()
    ot = []
    for i in x:
        try:
            if i.chat.type == 'supergroup':
                ot.append([i.chat.id,i.chat.username,i.chat.type])
            else:
                print(f"cant add [{i.chat.id}]")
        except Exception as err:
            print(err)
    app.stop()
    return ot


def GetMemberFromChannel(chat_id:int):
    app.start()
    listMembers = []
    for i in app.iter_chat_members(chat_id):
        listMembers.append(i)
    app.stop()
    return listMembers 





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
            out.append(ot[i][j].user.id)
    return out

