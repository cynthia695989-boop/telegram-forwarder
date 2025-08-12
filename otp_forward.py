from telethon import TelegramClient, events

api_id = 24421692
api_hash = "37cf8f20068e77728225880f2e9cc65d"

source_chats = [-1002044564008, -1002575654842]
target_chat = -1002833425394

session_name = "otp_forward"

client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage(chats=source_chats))
async def forward_otp(event):
    try:
        await client.send_message(target_chat, event.message)
        print(f"Message forwarded from {event.chat_id} to {target_chat}")
    except Exception as e:
        print(f"Error: {e}")

client.start()
client.run_until_disconnected()
