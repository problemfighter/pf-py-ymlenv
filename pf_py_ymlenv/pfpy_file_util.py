import os
from functools import reduce
from os.path import exists, join


class PFPYFileUtil:
    PROJECT_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

    @staticmethod
    def concat_path(first, last, *more_path):
        path = join(first, last)
        if len(more_path) > 0:
            path = os.path.join(path, reduce(os.path.join, more_path))
        return path

    @staticmethod
    def is_exists_path(path):
        return exists(path)

    @staticmethod
    def delete_file(path):
        if PFPYFileUtil.is_exists_path(path):
            os.remove(path)

    def concat_with_root(self, *paths):
        if paths:
            return os.path.join(self.PROJECT_ROOT_DIR, reduce(os.path.join, paths))
