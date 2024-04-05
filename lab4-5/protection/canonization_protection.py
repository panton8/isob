import os


class CanonizationProtection:
    @staticmethod
    def is_valid_file_path(file_path):
        path_components = file_path.split(os.path.sep)
        for component in path_components:
            if '..' in component:
                return False

        return True

