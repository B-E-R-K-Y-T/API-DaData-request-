from src.service.client.request import AsyncRequest, BaseRequest


class AsyncAPIWorker:
    def __init__(self, request: BaseRequest = AsyncRequest()):
        self.__request = request

