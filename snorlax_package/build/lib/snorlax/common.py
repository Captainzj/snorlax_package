import os


def is_exists_ds_store(path):
    if '.DS_Store' in os.listdir(path):
        os.remove(os.path.join(path, '.DS_Store'))
        print(".DS_Store exists, and removed.")
