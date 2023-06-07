from abc import ABC, abstractmethod


class BaseFileManager(ABC):

    # template method
    def record_request(self, request_body):
        self._actual_record(request_body)
        self._after_record(request_body)

    @abstractmethod
    def _actual_record(self, request_body):
        pass

    @abstractmethod
    def _after_record(self, request_body):
        pass