from telethon import TelegramClient
import os
import csv
import requests


#telegram api
api_id = '26161644'
api_hash = 'c4560ad11ff743648c861c127325f9de'
phone_number = '+25198 043 2130'

# Path to store images and documents
image_dir = (r'C:\Users\befekadum\Documents\10x acadamy\WEEK7\Ethiopian-medical-business-\data\images')
#doc_dir = './data'

client = TelegramClient('session_name', api_id, api_hash)

async def fetch_telegram_messages(channel_username):
    """
    Connects to a Telegram channel and fetches messages (including text, images, and documents).
    
    Parameters:
    channel_username (str): The username of the Telegram channel.
    
    Returns:
    List[dict]: List of messages containing text and media information.
    """
    await client.start(phone_number)
    
    # Join and fetch messages from the channel
    channel = await client.get_entity(channel_username)
    messages = []
    
    async for message in client.iter_messages(channel, limit=100000):
        msg_data = {
            'id': message.id,
            'sender': message.sender_id,
            'timestamp': message.date.strftime('%Y-%m-%d %H:%M:%S'),
            'text': message.message if message.message else '',
        }
        
        #Download images if present
        if message.photo:
            photo = await message.download_media(file=image_dir)
            msg_data['image'] = photo
        
        # Download documents if present
        #if message.document:
          #  document = await message.download_media(file=doc_dir)
         #   msg_data['document'] = document
        
        messages.append(msg_data)
    
    return messages

def save_messages_to_csv(messages, output_file='messages.csv'):
    """
    Saves a list of messages into a CSV file.
    
    Parameters:
    messages (List[dict]): The list of messages to save.
    output_file (str): The file path to save the CSV.
    
    Returns:
    None
    """
    # Define the columns for the CSV
    fieldnames = ['id', 'sender', 'timestamp', 'text', 'image', 'document']
    
    # Open the CSV file for writing
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        # Write the header row
        writer.writeheader()
        
        # Write each message as a row
        for message in messages:
            writer.writerow({
                'id': message['id'],
                'sender': message['sender'],
                'timestamp': message['timestamp'],
                'text': message['text'],
                'image': message.get('image', ''),  # Leave empty if no image
                'document': message.get('document', '')  # Leave empty if no document
            })

async def main():
    # Example list of channels
    channels = ['@lobelia4cosmetics','@EAHCI','@yetenaweg','@CheMed123','@DoctorsET' ]
    
    all_messages = []
    for channel in channels:
        print(f"Fetching messages from {channel}...")
        messages = await fetch_telegram_messages(channel)
        all_messages.extend(messages)
    
    # Save the fetched messages to a CSV file
    save_messages_to_csv(all_messages, output_file='messages_new1.csv' )
    
    print("Messages have been saved to CSV.")

# Start the event loop to run the main function
with client:
    client.loop.run_until_complete(main())