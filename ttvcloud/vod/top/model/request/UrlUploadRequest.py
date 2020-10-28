import json


class UrlUploadRequest:
    def __init__(self, space_name):
        self.space_name = space_name
        self.url_sets = []

    def get_space_name(self):
        return self.space_name

    def set_space_name(self, space_name):
        self.space_name = space_name

    # def set_url_sets(self, url_sets):
    #     self.url_sets = url_sets
    #
    def get_url_sets(self):
        return self.url_sets

    def add_url_set(self, url_set):
        self.url_sets.append(url_set)

    def to_dict(self):
        params = []
        for u in self.url_sets:
            params.append(u.to_dict())
        return {
            'SpaceName': self.space_name,
            'URLSets': json.dumps(params)
        }


class UrlSet:
    def __init__(self, source_url):
        self.source_url = source_url
        self.callback_args = ""
        self.md5 = ""
        self.template_id = ""
        self.title = ""
        self.description = ""
        self.tags = ""
        self.category = ""

    def to_dict(self):
        return {
            'SourceUrl': self.source_url,
            'CallbackArgs': self.callback_args,
            'Md5': self.md5,
            'TemplateId': self.template_id,
            'Title': self.title,
            'Description': self.description,
            'Tags': self.tags,
            'Category': self.category
        }

    def set_source_url(self, source_url):
        self.source_url = source_url

    def get_source_url(self):
        return self.source_url

    def set_callback_args(self, callback_args):
        self.callback_args = callback_args

    def get_callback_args(self):
        return self.callback_args

    def set_md5(self, md5):
        self.md5 = md5

    def get_md5(self):
        return self.md5

    def set_template_id(self, template_id):
        self.template_id = template_id

    def get_template_id(self):
        return self.template_id

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def set_tags(self, tags):
        self.tags = tags

    def get_tags(self):
        return self.tags

    def set_category(self, category):
        self.category = category

    def get_category(self):
        return self.category
