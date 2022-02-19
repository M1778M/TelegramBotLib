from pyrogram import Client,filters
from pyrogram.types import Messge
from pyrogram.raw import functions


app = Client('robot',config_file='config.ini',phonenumber='+98900000000')

@app.on_message(filters.text and filters.chat('me'))
async def getm(client,msg:Messge):
    usertext = msg.text
    if 'chat_id' in usertext:
        try:
            iFound = usertext.find(':')
            chat_id = usertext[iFound:]
            try:
                await app.join_chat(chat_id)
            except:
                print('Invalid Channel')
            
            userlist = []
            for i in app.iter_chat_members(chat_id=chat_id):
                await userlist.append(i.user.id)
                
            print(userlist)
            channelName = '{}'
            await app.send(
                functions.channels.InviteToChannel(
                        channel = app.resolve_peer(f'@{channelName}'),
                        users = [app.resolve_peer(peer_id=j) for j in userlist]
                    )
            )
        except Exception as err:
            raise Exception (err)
    else:
        # Get Chat Id
        try:
            await app.join_chat(chat_id=usertext) # can send link or @namechat
        except:
            print('Invalid Channel')
        
        userlist = []
        for i in app.iter_chat_members(chat_id=usertext):
            await userlist.append(i.user.id)
            
        print(userlist)
        channelName = ''
        await app.send(
            functions.channels.InviteToChannel(
                    channel = app.resolve_peer(f'@{channelName}'),
                    users = [app.resolve_peer(peer_id=j) for j in userlist]
                )
        )
        
def chatlist():
    app.start()
    
    print(app.get_messages('me'))

    i = 0

    for i in app.get_dialogs():
        i += 1

        print(f'{i}- Type: {x.chat.type}- title: {x.chat.title}- Id: {x.chat.id}')

    app.stop()



app.run()
