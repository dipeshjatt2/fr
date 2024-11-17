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
    result = do_click('https://app.freedogs.bot/#tgWebAppData=query_id%3DAAEO_is2AgAAAA7-Kzb9gtKe%26user%3D%257B%2522id%2522%253A5203820046%252C%2522first_name%2522%253A%2522Ymx%2520haxor%2522%252C%2522last_name%2522%253A%2522%2522%252C%2522username%2522%253A%2522Ymxhaxor%2522%252C%2522language_code%2522%253A%2522en%2522%252C%2522allows_write_to_pm%2522%253Atrue%252C%2522photo_url%2522%253A%2522https%253A%255C%252F%255C%252Ft.me%255C%252Fi%255C%252Fuserpic%255C%252F320%255C%252Fz7MApv-o-JLTHEsup7BsTe7u-hdH1OpRJqHqKSJZE3mzUDptYO58qUNe0NJheL5A.svg%2522%257D%26auth_date%3D1731858539%26signature%3DNPba6wGS0kfXkQNdm3X3EkYZy1kpB4xPusyyM-ZtjRbMWqY2hkhXD5GVKmVEn-QDuKPK_cqmpIn4_L4ikxL1Bw%26hash%3Df0ddd4d1f9e5f9dafd10e7008be86d12eef7f7c6176972b5634078f004e1896d&tgWebAppVersion=7.10&tgWebAppPlatform=android&tgWebAppThemeParams=%7B%22bg_color%22%3A%22%23ffffff%22%2C%22section_bg_color%22%3A%22%23ffffff%22%2C%22secondary_bg_color%22%3A%22%23f0f0f0%22%2C%22text_color%22%3A%22%23222222%22%2C%22hint_color%22%3A%22%23a8a8a8%22%2C%22link_color%22%3A%22%232678b6%22%2C%22button_color%22%3A%22%2350a8eb%22%2C%22button_text_color%22%3A%22%23ffffff%22%2C%22header_bg_color%22%3A%22%23527da3%22%2C%22accent_text_color%22%3A%22%231c93e3%22%2C%22section_header_text_color%22%3A%22%233a95d5%22%2C%22subtitle_text_color%22%3A%22%2382868a%22%2C%22destructive_text_color%22%3A%22%23cc2929%22%2C%22section_separator_color%22%3A%22%23d9d9d9%22%2C%22bottom_bar_bg_color%22%3A%22%23f0f0f0%22%7D')
    time.sleep(2)
    print(result)

while True:
    result = do_click('https://app.freedogs.bot/#tgWebAppData=query_id%3DAAEO_is2AgAAAA7-Kzb9gtKe%26user%3D%257B%2522id%2522%253A5203820046%252C%2522first_name%2522%253A%2522Ymx%2520haxor%2522%252C%2522last_name%2522%253A%2522%2522%252C%2522username%2522%253A%2522Ymxhaxor%2522%252C%2522language_code%2522%253A%2522en%2522%252C%2522allows_write_to_pm%2522%253Atrue%252C%2522photo_url%2522%253A%2522https%253A%255C%252F%255C%252Ft.me%255C%252Fi%255C%252Fuserpic%255C%252F320%255C%252Fz7MApv-o-JLTHEsup7BsTe7u-hdH1OpRJqHqKSJZE3mzUDptYO58qUNe0NJheL5A.svg%2522%257D%26auth_date%3D1731858539%26signature%3DNPba6wGS0kfXkQNdm3X3EkYZy1kpB4xPusyyM-ZtjRbMWqY2hkhXD5GVKmVEn-QDuKPK_cqmpIn4_L4ikxL1Bw%26hash%3Df0ddd4d1f9e5f9dafd10e7008be86d12eef7f7c6176972b5634078f004e1896d&tgWebAppVersion=7.10&tgWebAppPlatform=android&tgWebAppThemeParams=%7B%22bg_color%22%3A%22%23ffffff%22%2C%22section_bg_color%22%3A%22%23ffffff%22%2C%22secondary_bg_color%22%3A%22%23f0f0f0%22%2C%22text_color%22%3A%22%23222222%22%2C%22hint_color%22%3A%22%23a8a8a8%22%2C%22link_color%22%3A%22%232678b6%22%2C%22button_color%22%3A%22%2350a8eb%22%2C%22button_text_color%22%3A%22%23ffffff%22%2C%22header_bg_color%22%3A%22%23527da3%22%2C%22accent_text_color%22%3A%22%231c93e3%22%2C%22section_header_text_color%22%3A%22%233a95d5%22%2C%22subtitle_text_color%22%3A%22%2382868a%22%2C%22destructive_text_color%22%3A%22%23cc2929%22%2C%22section_separator_color%22%3A%22%23d9d9d9%22%2C%22bottom_bar_bg_color%22%3A%22%23f0f0f0%22%7D')
    print(result)
    time.sleep(3)
    result = do_click('https://app.freedogs.bot/#tgWebAppData=query_id%3DAAEaEuBjAwAAABoS4GOiTKxl%26user%3D%257B%2522id%2522%253A8118080026%252C%2522first_name%2522%253A%2522%25E0%25A6%25B9%25201%25F0%259F%2590%25BE%2522%252C%2522last_name%2522%253A%2522%2522%252C%2522language_code%2522%253A%2522en%2522%252C%2522allows_write_to_pm%2522%253Atrue%252C%2522photo_url%2522%253A%2522https%253A%255C%252F%255C%252Ft.me%255C%252Fi%255C%252Fuserpic%255C%252F320%255C%252FNPkIQRym7EWS-DGSflpT2jckB4a9gH5kJcVp68OxinB7HS34KcsCjNuN0xf62y7b.svg%2522%257D%26auth_date%3D1731858578%26signature%3DxbebMig8ASUpgmzZQCD3ovHTWEwWDsjvRk7YDINKLvqxjOCsEtFNuNZiRifNZTUOto0imRAm5Jttmw3_VjNoCA%26hash%3Dc65e6494cce8393b78b5bca48a677c902a75b9dfcf9c4287e628e6f8a743a398&tgWebAppVersion=7.10&tgWebAppPlatform=android&tgWebAppThemeParams=%7B%22bg_color%22%3A%22%23ffffff%22%2C%22section_bg_color%22%3A%22%23ffffff%22%2C%22secondary_bg_color%22%3A%22%23f0f0f0%22%2C%22text_color%22%3A%22%23222222%22%2C%22hint_color%22%3A%22%23a8a8a8%22%2C%22link_color%22%3A%22%232678b6%22%2C%22button_color%22%3A%22%2350a8eb%22%2C%22button_text_color%22%3A%22%23ffffff%22%2C%22header_bg_color%22%3A%22%23527da3%22%2C%22accent_text_color%22%3A%22%231c93e3%22%2C%22section_header_text_color%22%3A%22%233a95d5%22%2C%22subtitle_text_color%22%3A%22%2382868a%22%2C%22destructive_text_color%22%3A%22%23cc2929%22%2C%22section_separator_color%22%3A%22%23d9d9d9%22%2C%22bottom_bar_bg_color%22%3A%22%23f0f0f0%22%7D ')
    print(result)
    time.sleep(20)
