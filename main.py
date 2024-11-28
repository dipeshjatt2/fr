import requests
from urllib.parse import urlparse, parse_qs
import hashlib
import random
import time
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'authorization': '',
    'x-requested-with': 'org.telegram.messenger',
}
def compute_md5(amount ,seq):
    prefix = str(amount) + str(seq) + "7be2a16a82054ee58398c5edb7ac4a5a"
    return hashlib.md5(prefix.encode()).hexdigest()
  
def auth(url:str ) -> dict:
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.fragment)
    init = query_params.get('tgWebAppData', [None])[0]
    params = {'invitationCode': '',  'initData':init}
    data = {'invitationCode': '', 'initData':init,}
    response = requests.post('https://api.freedogs.bot/miniapps/api/user/telegram_auth', params=params, headers=headers, data=data)
    return response.json()


def do_click(init):
    headers['authorization'] = 'Bearer ' + auth(init)['data']['token']
    params = ''
    response = requests.get('https://api.freedogs.bot/miniapps/api/user_game_level/GetGameInfo', params=params, headers=headers)
    Seq = response.json()['data']['collectSeqNo']
    hsh = compute_md5('100000',Seq)
    params = {
        'collectAmount':'100000' ,
        'hashCode': hsh,
        'collectSeqNo': str(Seq),
    }
    response = requests.post('https://api.freedogs.bot/miniapps/api/user_game/collectCoin', params=params, headers=headers, data=params)
    return response.json()  

if __name__== '__main__':   
    #replace it with your own tgwebappdata
   while True : 
    result = do_click('https://app.freedogs.bot/#tgWebAppData=query_id%3DAAEO_is2AgAAAA7-KzaPPc1y%26user%3D%257B%2522id%2522%253A5203820046%252C%2522first_name%2522%253A%2522Ymx%2520haxor%2522%252C%2522last_name%2522%253A%2522%2522%252C%2522username%2522%253A%2522Ymxhaxor%2522%252C%2522language_code%2522%253A%2522en%2522%252C%2522allows_write_to_pm%2522%253Atrue%252C%2522photo_url%2522%253A%2522https%253A%255C%252F%255C%252Ft.me%255C%252Fi%255C%252Fuserpic%255C%252F320%255C%252Fz7MApv-o-JLTHEsup7BsTe7u-hdH1OpRJqHqKSJZE3mzUDptYO58qUNe0NJheL5A.svg%2522%257D%26auth_date%3D1732762814%26signature%3D3EXTS28pibp-PSdDLOH06cwNJ8K-bml90JH3q1G_XiLv6pY8w_36RzhNMuBo5DDh3-Cb70c7drmoDkxnQYnxDA%26hash%3D7509c11accf57e7250f1c5273660c1b881a808d8837c4e8adbe40aea6de68202&tgWebAppVersion=7.8&tgWebAppPlatform=android&tgWebAppThemeParams=%7B%22bg_color%22%3A%22%23ffffff%22%2C%22section_bg_color%22%3A%22%23ffffff%22%2C%22secondary_bg_color%22%3A%22%23f0f0f0%22%2C%22text_color%22%3A%22%23222222%22%2C%22hint_color%22%3A%22%23a8a8a8%22%2C%22link_color%22%3A%22%23b050ca%22%2C%22button_color%22%3A%22%23d476ed%22%2C%22button_text_color%22%3A%22%23ffffff%22%2C%22header_bg_color%22%3A%22%239a66a5%22%2C%22accent_text_color%22%3A%22%23c04ce5%22%2C%22section_header_text_color%22%3A%22%23b44fd8%22%2C%22subtitle_text_color%22%3A%22%23908d91%22%2C%22destructive_text_color%22%3A%22%23cc2929%22%2C%22section_separator_color%22%3A%22%23d9d9d9%22%7D')
    time.sleep(random.randint(20,100))
    print(result)


