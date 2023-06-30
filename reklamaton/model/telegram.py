from  telethon.sync import TelegramClient

from telethon.tl.functions.channels import GetFullChannelRequest
import json

# Set up your Telegram API credentials
api_id = '28981810'
api_hash = 'e3e51281f81ed774fd120900239f5cfd'


arr_channels = ['pravdadirty', 'NeRestorani', 'nemorgenshtern', 'kudago', 'bitkogan','asia_pekin_tokyo','ranarod','geografiyatg','lost_in_japan','slangeducation2_0','lawyermironova','nashturist','Architecture2021','outciv','itmolnia','skillboxru','matematikandrei','videoshocks','dvachannel','ludobreniya','PROgame_news','Slomai_sistemu_Potencial']


def get_channel(client, channel_entity):
    # Specify the channel username or entity
    #channel_entity = 'hackathons_in_russia'  # Replace with the channel username or entity

    # Get information about the channel
    channel = client.get_entity(channel_entity)

    ch_full = client(GetFullChannelRequest(channel=channel))
    channel_about = ch_full.full_chat.about 
    # Extract relevant information
                             
    channel_title = channel.title
    channel_username = channel.username
    channel_id = channel.id
    #channel_description = channel.description
    channel_participants_count = ch_full.full_chat.participants_count
    #channel_views = channel.views
    channel_restricted = channel.restricted
    channel_verified = channel.verified
    channel_has_link = channel.has_link

    # Print the extracted information
    #print("Channel:", channel)
    #print("ch_full:", ch_full)

    #print("Channel Title:", channel_title)
    #print("Channel Username:", channel_username)
    #print("Channel ID:", channel_id)
    #print("Channel about:", channel_about)


   # print("Channel Description:", channel_description)
    #print("Channel Participants Count:", channel_participants_count)
    #print("Channel Views:", channel_views)
    #print("Is Channel Restricted?:", channel_restricted)
    #print("Is Channel Verified?:", channel_verified)
    #print("Channel Has Link?:", channel_has_link)
    channel_data = {'channel': channel_id, 'channel_title': channel_title, 'participants_count':channel_participants_count,'messages': []}

    for message in client.iter_messages(channel, limit=100):
        #print(message.sender_id, ':', message.text)
        #print(message)
        if message.text == '': 
           continue
        if message.reactions is not None: 
           reactions = message.reactions.to_dict()
           simple_reactions = []
           for react in reactions['results']:
               simple_reactions.append({'emoticon':react['reaction']['emoticon'], 'count':react['count']})
           channel_data['messages'].append({ 'message':message.text, 'views': message.views, 'reactions':  simple_reactions})
        else:
           channel_data['messages'].append({ 'message':message.text, 'views': message.views,'reactions': None })
    return channel_data
# Connect to Telegram client
with TelegramClient('session_name', api_id, api_hash) as client:

   all_data = {'channels': []}
   for item in arr_channels:
       print('channel', item)
       all_data['channels'].append(get_channel(client, item))
   print('-----------------------------------')
   print('-------------FINISH----------------')
   #print('channel_data', all_data)
   with open('result.json', 'w') as fp:
       json.dump(all_data, fp)