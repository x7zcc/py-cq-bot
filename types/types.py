class GroupInfo:
    id: int
    create_time: int
    level: int
    name: str
    member: int
    max_member: int


class Member:
    group: int
    uin: int
    nick: str
    card: str
    title: str
    sex: str
    age: int
    area: str
    level: str
    join_time: int
    last_time: int
    title_expire_time: int
    ban_free_time: int
    role: str
    unfriendly: bool
    card_changeable: bool


class Sender:
    uin: int
    nick: str
    sex: str
    age: int
    card: str
    area: str
    level: str
    role: str
    title: str


class Anonymous:
    id: int
    name: str
    flag: str


class Reply:
    id: int


class Message:
    type: str
    me: int
    uin: int
    id: int
    group: int
    time: int
    text: str
    content: list[dict]
    at: list
    reply: Reply
    anonymous: Anonymous
    font: str
    sender: Sender


class Friend:
    uin: int
    nick: str
    mark: str


class Device:
    appid: int
    name: str
    type: str


class ForwardMessage:
    content: str
    sender: Sender
    time: int


class Image:
    size: int
    file_name: str
    url: str


class File:
    group: int
    file_id: str
    file_name: str
    busid: int
    size: int
    upload_time: int
    dead_time: int
    modify_time: int
    download_times: int
    uploader: int
    uploader_name: str


class Folder:
    group: int
    folder_id: str
    folder_name: str
    create_time: int
    creator: int
    creator_name: str
    file_count: int
