from .base_file_manager import BaseFileManager


class RemoteFileManager(BaseFileManager):

    def _actual_record(self, request_body):
        print("Recording request to remote DB...")

    def _after_record(self, request_body):
        print("Checking if something should be cleaned up")