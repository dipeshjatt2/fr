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
    result = do_click('https://app.freedogs.bot/#tgWebAppData=query_id%3DAAEO_is2AgAAAA7-KzZU9nCj%26user%3D%257B%2522id%2522%253A5203820046%252C%2522first_name%2522%253A%2522Ymx%2520haxor%2522%252C%2522last_name%2522%253A%2522%2522%252C%2522username%2522%253A%2522Ymxhaxor%2522%252C%2522language_code%2522%253A%2522en%2522%252C%2522allows_write_to_pm%2522%253Atrue%257D%26auth_date%3D1731290589%26hash%3D830adca22ed2d6b2c8f85a0eb23a90e417374a207f9e36fa38379a48113d4dee&tgWebAppVersion=7.10&tgWebAppPlatform=android&tgWebAppThemeParams=%7B%22bg_color%22%3A%22%23ffffff%22%2C%22section_bg_color%22%3A%22%23ffffff%22%2C%22secondary_bg_color%22%3A%22%23f0f0f0%22%2C%22text_color%22%3A%22%23222222%22%2C%22hint_color%22%3A%22%23a8a8a8%22%2C%22link_color%22%3A%22%232678b6%22%2C%22button_color%22%3A%22%2350a8eb%22%2C%22button_text_color%22%3A%22%23ffffff%22%2C%22header_bg_color%22%3A%22%23527da3%22%2C%22accent_text_color%22%3A%22%231c93e3%22%2C%22section_header_text_color%22%3A%22%233a95d5%22%2C%22subtitle_text_color%22%3A%22%2382868a%22%2C%22destructive_text_color%22%3A%22%23cc2929%22%2C%22section_separator_color%22%3A%22%23d9d9d9%22%2C%22bottom_bar_bg_color%22%3A%22%23f0f0f0%22%7D ')
    time.sleep(2)
    print(result)

while True:
    result = do_click('https://app.freedogs.bot/#tgWebAppData=query_id%3DAAEO_is2AgAAAA7-KzZU9nCj%26user%3D%257B%2522id%2522%253A5203820046%252C%2522first_name%2522%253A%2522Ymx%2520haxor%2522%252C%2522last_name%2522%253A%2522%2522%252C%2522username%2522%253A%2522Ymxhaxor%2522%252C%2522language_code%2522%253A%2522en%2522%252C%2522allows_write_to_pm%2522%253Atrue%257D%26auth_date%3D1731290589%26hash%3D830adca22ed2d6b2c8f85a0eb23a90e417374a207f9e36fa38379a48113d4dee&tgWebAppVersion=7.10&tgWebAppPlatform=android&tgWebAppThemeParams=%7B%22bg_color%22%3A%22%23ffffff%22%2C%22section_bg_color%22%3A%22%23ffffff%22%2C%22secondary_bg_color%22%3A%22%23f0f0f0%22%2C%22text_color%22%3A%22%23222222%22%2C%22hint_color%22%3A%22%23a8a8a8%22%2C%22link_color%22%3A%22%232678b6%22%2C%22button_color%22%3A%22%2350a8eb%22%2C%22button_text_color%22%3A%22%23ffffff%22%2C%22header_bg_color%22%3A%22%23527da3%22%2C%22accent_text_color%22%3A%22%231c93e3%22%2C%22section_header_text_color%22%3A%22%233a95d5%22%2C%22subtitle_text_color%22%3A%22%2382868a%22%2C%22destructive_text_color%22%3A%22%23cc2929%22%2C%22section_separator_color%22%3A%22%23d9d9d9%22%2C%22bottom_bar_bg_color%22%3A%22%23f0f0f0%22%7D ')
    print(result)
    time.sleep(3)
    result = do_click('https://app.freedogs.bot/#tgWebAppData=user%3D%257B%2522id%2522%253A8118080026%252C%2522first_name%2522%253A%2522%25E0%25A6%25B9%25201%25F0%259F%2590%25BE%2522%252C%2522last_name%2522%253A%2522%2522%252C%2522language_code%2522%253A%2522en%2522%252C%2522allows_write_to_pm%2522%253Atrue%257D%26chat_instance%3D-235759697544074475%26chat_type%3Dsender%26auth_date%3D1731291138%26hash%3D8f901e7b62be18a03e4318342eaf0f426d4d9a3ce334ad9649a05b3371121130&tgWebAppVersion=7.10&tgWebAppPlatform=android&tgWebAppThemeParams=%7B%22bg_color%22%3A%22%23ffffff%22%2C%22section_bg_color%22%3A%22%23ffffff%22%2C%22secondary_bg_color%22%3A%22%23f0f0f0%22%2C%22text_color%22%3A%22%23222222%22%2C%22hint_color%22%3A%22%23a8a8a8%22%2C%22link_color%22%3A%22%232678b6%22%2C%22button_color%22%3A%22%2350a8eb%22%2C%22button_text_color%22%3A%22%23ffffff%22%2C%22header_bg_color%22%3A%22%23527da3%22%2C%22accent_text_color%22%3A%22%231c93e3%22%2C%22section_header_text_color%22%3A%22%233a95d5%22%2C%22subtitle_text_color%22%3A%22%2382868a%22%2C%22destructive_text_color%22%3A%22%23cc2929%22%2C%22section_separator_color%22%3A%22%23d9d9d9%22%2C%22bottom_bar_bg_color%22%3A%22%23f0f0f0%22%7D ')
    print(result)
    time.sleep(50)
