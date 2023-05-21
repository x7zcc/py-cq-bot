from .http import BotHttp, Route


class API:
    """
    具体的httpAPI实现
    """
    def __init__(self, http: BotHttp):
        self._http = http

    async def get_login_info(self):
        """
        获取登录号信息.
        :return:
        """
        route = Route(end_point="/get_login_info")
        return self._http.request(route=route)

