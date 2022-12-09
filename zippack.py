import os
import zipfile

def creating_arch():
    root = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(root, 'resources')
    file_dir = os.listdir(path)
    arch_path = os.path.join(path,'archive.zip')

    with zipfile.ZipFile(arch_path, mode='w', \
                     compression=zipfile.ZIP_DEFLATED) as zf:
        for file in file_dir:
            add_file = os.path.join(path, file)
            zf.write(add_file)

    return zf