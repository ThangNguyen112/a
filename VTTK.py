import time,requests,random,json

tap_url = "https://vuongtrieu.ecoresort.online/api/tap"
sell_url = "https://vuongtrieu.ecoresort.online/api/market/sell"
user_url = "https://vuongtrieu.ecoresort.online/api/user"
list_url = "https://vuongtrieu.ecoresort.online/api/market/private/list"

profile_data = {
            "telegram_id":"1225233239",
            "first_name":"No",
            "hide_avatar":0,
            "initData":"query_id=AAFXkwdJAAAAAFeTB0kj2Lke&user=%7B%22id%22%3A1225233239%2C%22first_name%22%3A%22No%22%2C%22last_name%22%3A%22Mar%22%2C%22username%22%3A%22ThangNG2303%22%2C%22language_code%22%3A%22vi%22%2C%22allows_write_to_pm%22%3Atrue%2C%22photo_url%22%3A%22https%3A%5C%2F%5C%2Ft.me%5C%2Fi%5C%2Fuserpic%5C%2F320%5C%2FjItcs-C6BKkzSfm_5ilr_gv3zjuy9Bw6EwMDLAozHq4.svg%22%7D&auth_date=1778167150&signature=J3Gs51a0eLeUMewiVX5KUzEjcQRHRJ48efNfzwgiwZ2io7XS6AT8SANNGtpv18NR_hr2fCVru17Dyd6qtJoADw&hash=e843927a9567d94d7adcec8f93182f5b95ab7ae616d3ac7f8860cfeb90772bb2",
}
def sell(resource, amount, price):
        sell_data = {
                    "resource_type":resource,
                    "amount":amount,
                    "price_gold":price
        }
        sell_data.update(profile_data)
        post_sell = requests.post(sell_url, json=sell_data) 
        return post_sell
user_data = {
            "start_param":"6118757082",
            "device_code":"DEV_4t7mdrv9x_1778063410279"
}
user_data.update(profile_data)
    
print('Tỉ lệ nguyên liệu gỗ, đá: ')
ratio = input()
energy = 0
i = 0
t = 0

while True:
    post_user = requests.post(user_url, json=user_data)
    try: 
        energy = post_user.json()['user']['energy']
        taps = round(energy/2 -10)
    except: 
        print(post_user.text)
        
    if ratio == '': 
        wood_taps = random.randint(round(taps/2.5), round(taps/1.5))
        stone_taps = taps - wood_taps
    elif ratio != '':
        ratio1 = eval(ratio.replace(' ','/'))
        stone_taps = round(taps/(ratio1+1))
        wood_taps = round(taps - stone_taps)

    taps_data = {       
                "taps":taps,
                "wood_taps":wood_taps,
                "stone_taps":stone_taps,
                "iron_taps":0,
                "dark_iron_taps":0,
                "jade_taps":0,
                "glaze_taps":0,
                "purple_gold_taps":0
    }
    print(wood_taps,stone_taps)

    taps_data.update(profile_data)
    post_tap = requests.post(tap_url, json=taps_data)
    try:
        if post_tap.json()['success'] == False:
            time.sleep(10)
    except:
        print(post_tap.text)
            
    time.sleep(200)
    t += 5
    if (t%40) == 0:
        print('ok')
        i = 0
    print(t)
            
