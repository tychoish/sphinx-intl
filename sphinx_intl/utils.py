import os

from multiprocessing import cpu_count
from multiprocessing.pool import Pool

def expand_tree(path, extension='pot'):
    for root, sub_folders, files in os.walk(path):
        for file in files:
            if file.startswith('.#'):
                continue
            elif file.endswith('swp'):
                continue
            else:
                f = os.path.join(root, file)
                if extension != None:
                    if isinstance(extension, list):
                        if os.path.splitext(f)[1][1:] not in extension:
                            continue
                    else:
                        if not f.endswith(extension):
                            continue

                yield f

class WorkerPool(object):
    def __init__(self, size=None):
        if size is None:
            self.size = cpu_count()
        else:
            self.size = size

    def __exit__(self, *args):
        self.p.close()
        self.p.join()

class ProcessPool(WorkerPool):
    def __enter__(self):
        self.p = Pool(self.size)

        return self.p
