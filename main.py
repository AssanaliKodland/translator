def is_api_group(chat_id):
    return chat_id == GROUP_CHAT_ID


@bot.message_handler(func=lambda m: True, content_types=['new_chat_participant'])
def on_user_joins(message):
    if not is_api_group(message.chat.id):
        return
