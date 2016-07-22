from channels import Group

group_name = 'default-group'


def ws_connect(message):
    Group(group_name).add(message.reply_channel)


def ws_receive(message):
    msg_content = message.content['text']

    Group(group_name).send({
        'text': msg_content,
    })


def ws_disconnect(message):
    Group(group_name).discard(message.reply_channel)
