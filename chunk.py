import io


def split_f(message, file: bytes, bot):
    chunk_size = 1024 * 100  # Bytes, 100kb
    chunk = 0
    array_of_chunks = []

    file_name = message.document.file_name
    file = io.BytesIO(file)
    byte = file.read(chunk_size)

    while byte:
        chunk_name = ''.join(file_name.split('.')[:-1]) + '_chunk_' + str(chunk) + '.txt'
        id_ms = bot.send_document(message.chat.id, byte, visible_file_name=chunk_name)
        chunk += 1
        byte = file.read(chunk_size)
        array_of_chunks.append(str(id_ms.message_id))
    chunks = " ".join(array_of_chunks)  # Convert array to string

    return (
        {
            'id_message': chunks,
            'name': file_name
        })


def merge_f(message, file_info: dict, bot):
    id_messages = file_info['id_message'].split()  # Convert string to array

    file_name = file_info['name']
    buf_file = b''
    for data in id_messages:
        ms = bot.forward_message(chat_id=message.chat.id, from_chat_id=message.chat.id, message_id=data)
        file_id = ms.document.file_id
        file = bot.get_file(file_id)
        file = io.BytesIO(bot.download_file(file.file_path))
        byte = file.read()
        buf_file = buf_file+byte
    info = bot.send_document(message.chat.id, buf_file, visible_file_name=file_name, caption='Mergen file: '+file_name)
    print(file_name, str(info.document.file_size)+' bytes')



