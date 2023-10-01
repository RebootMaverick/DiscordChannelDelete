import json
import requests as RebootMaverick
import time
import logging
from rich.logging import RichHandler

def channeldelete():
    with open('./config.json') as f:
        data = json.load(f)
    secret_key = data['Token']
    headers = {'authorization': secret_key}
    guild_id = int(input('Attack Guild ID :'))
    guild = guild_id
    try:
        RM = RebootMaverick.get(f"https://discord.com/api/v9/guilds/{guild}/channels",headers=headers)   
        R = RM.json()
        for channels in R:
            logging.basicConfig(
                level=logging.DEBUG,
                format="%(message)s",
                datefmt="[%X]",
                handlers=[RichHandler(rich_tracebacks=True)],
            )
            channels_delete = channels['id']
            K = RebootMaverick.delete(f'https://discord.com/api/v9/channels/{channels_delete}',headers=headers)
            if K.status_code == 200:
                log = logging.getLogger("rich")
                B = log.info(f"チャンネルの削除に成功しました : {channels_delete}")
                print(B)
            else:
                print('(#^.^#)')
    except Exception as e:
        print(e)
        print('正常な値を入れてください。')