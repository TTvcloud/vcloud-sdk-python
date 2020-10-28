class UploadVideoRequest:
    def __init__(self):
        self.space_name = ""
        self.file_path = ""
        self.function_list = []
        self.callback_args = ""

    def set_space_name(self, space_name):
        self.space_name = space_name

    def set_file_path(self, file_path):
        self.file_path = file_path

    def add_function(self, function):
        self.function_list.append(function)

    def set_callback_args(self, callback_args):
        self.callback_args = callback_args
