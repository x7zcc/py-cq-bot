class Client:
    __slots__ = ["__uin", "data"]
    __uin: int
    data: dict

    # 计划保护client的属性，避免外部修改

    def __init__(self, uin, **kwargs):
        self.__uin = uin
        self.data = kwargs

    def __getattr__(self, item):
        # 找不到属性时调用
        if item in self.data:
            return self.data.get(item)
        return item

    @property
    def uin(self):
        return self.__uin