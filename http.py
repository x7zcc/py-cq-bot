class Route:
    _scheme: str = "http"
    _host: str = "localhost"
    _port: int = 5700

    def __init__(self, method: str = "GET", end_point: str = "/", **params):
        self._method = method
        self._endpoint = end_point
        self._params = params

    def __str__(self):
        return "{0._scheme}://{0._host}:{0._port}{0._endpoint}".format(self)

    @property
    def url(self):
        return self.__str__()


class BotHttp:
    """
    主要负责http通讯
    """

    def __init__(self, port: int = 5700):
        self._port = port

    def request(self, route: Route):
        pass
