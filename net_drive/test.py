def get_filename(path):
    if isinstance(path,str):
        file_name = path.split('\\')[-1:][0]
        return file_name
    else:
        return 'Error'


print(get_filename('D:\PythonWorkshop\\net_drive\\templates\\audio.html'))
