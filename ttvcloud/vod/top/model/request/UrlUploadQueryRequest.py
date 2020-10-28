
class UrlUploadQueryRequest:
    def __init__(self, job_ids):
        self.job_ids = job_ids

    def set_job_ids(self, job_ids):
        self.job_ids = job_ids

    def to_dict(self):
        return {
            "JobIds": self.job_ids
        }
