import os
import shutil


def win_nt(path):
    content = []
    if path != '':
        if os.path.isfile(path):
            print('try open this')
        else:
            try:
                path_list = os.listdir(path)
            except Exception as e:
                print(e)
                return
            for sub_path in path_list:
                temp_path = os.path.join(path, sub_path)
                if os.path.isdir(temp_path):
                    temp = {
                        'path': temp_path,
                        'name': sub_path,
                        'type': 'file_folder',
                    }
                else:
                    extension = find_extension(temp_path).lower()
                    if extension in ['bmp', 'jpg', 'jpeg', 'png', 'gif']:
                        temp = {
                            'path': temp_path,
                            'name': sub_path,
                            'type': 'image',
                        }
                    elif extension in ['mp4', 'webm','ogg']:
                        temp = {
                            'path': temp_path,
                            'name': sub_path,
                            'type': 'video',
                        }
                    elif extension in ['mp3', 'wav', 'ogg']:
                        temp = {
                            'path': temp_path,
                            'name': sub_path,
                            'type': 'audio',
                        }
                    elif extension in ['txt', 'pdf', 'docx', 'doc']:
                        temp = {
                            'path': temp_path,
                            'name': sub_path,
                            'type': 'text',
                        }
                    else:
                        temp = {
                            'path': temp_path,
                            'name': sub_path,
                            'type': 'file',
                        }
                content.append(temp)
    else:
        for index in range(65, 91):
            volume = chr(index) + ':\\'
            if os. path.isdir(volume):
                temp = {
                    'path': volume,
                    'name': volume[:-1],
                    'type': 'drive',
                }
                content.append(temp)
    return content


def div_path(path):
    seg_path = []
    if path != '':
        segment = path.split('\\')
        temp_path = segment[0]+'\\'
        temp = {
            'path': temp_path,
            'name': segment[0]
        }
        seg_path.append(temp)
        for seg in segment[1:]:
            temp_path = temp_path + seg
            temp = {
                'path': temp_path,
                'name': seg
            }
            temp_path = temp_path + '\\'
            seg_path.append(temp)
    return seg_path


def find_extension(path):
    if path != '':
        extension = path.split('.')[-1:][0]
        return extension
    else:
        return 'ERROR'


def copy_file_to_cache(source_path):
    shutil.copy(source_path, 'static/cache')


def delete_cache():
    cache_dir = 'static/cache'
    del_list = os.listdir(cache_dir)
    for file in del_list:
        file_path = os.path.join(cache_dir, file)
        os.remove(file_path)


def get_filename(path):
    if isinstance(path,str):
        file_name = path.split('\\')[-1:][0]
        return file_name
    else:
        return 'Error'
