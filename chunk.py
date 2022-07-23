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
        print(id_ms)
        chunk += 1
        byte = file.read(chunk_size)
        # array_of_chunks.append(str(file_chunk.name))

    chunks = " ".join(array_of_chunks)  # Convert array to string

    return (
        {
            'chunks': chunks,
            'name': file_name
        })


def merge_f(file_info: dict):
    array_of_chunks = file_info.get('chunks').split()  # Convert string to array
    with open('copy_' + file_info.get('name'), 'wb') as return_file:
        for chunk in array_of_chunks:
            with open(chunk, 'rb') as chunk:
                return_file.write(chunk.read())

    print('Файл')
