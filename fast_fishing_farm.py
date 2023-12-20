#Made By Shag420
#Discord: Shag420
#https://replit.com/@GH0STMAINE/fish

wait_time = False #True or False [Case Sensitive]

import aiohttp
import asyncio

async def make_request(session, url, params):
    async with session.post(url, params=params) as response:
        return await response.text()
async def main():
    FRPG_COOKIE = input("Please input your HighwindFRPG Cookie: ")
    Fish_Map_ID = input("\nFishing map ID in url heres an example : https://farmrpg.com/index.php#!/fishing.php?id=1 [ID is number 1 depending on the map in the url so just put just the number of which fishing location you are at] : ")
    if wait_time == True:
      wait_time1 = input("\nHow many seconds do you want to wait? [!Avoids account ban!] : ")
    print("\n!Auto-Fish Farm Working!")

    cookies = {
        'pac_ocean': '8106C6F2',
        '_ga': 'GA1.1.320387843.1700454041',
        'HighwindFRPG': '3AWwxFImQv1OiRQ5gJrBGg%3D%3D%3Cstrip%3E%24argon2id%24v%3D19%24m%3D7168%2Ct%3D4%2Cp%3D1%24S2pQcXk2SVBlLnF6RmhuZQ%24MH1GivzyTYKFnhHlS5k6IYUp6yShvH7hmg%2BovqbNaaQ',
        'farmrpg_auth': 've1tkerbsljm31795utkirdi23mf20j2ri6ij63a',
        '_ga_94M1PS2E9X': 'GS1.1.1702343895.4.1.1702349729.0.0.0',
    }

    headers = {
        'authority': 'farmrpg.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'origin': 'https://farmrpg.com',
        'pragma': 'no-cache',
        'referer': 'https://farmrpg.com/index.php',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    url = 'https://farmrpg.com/worker.php'

    async with aiohttp.ClientSession(headers=headers, cookies=cookies) as session:
        while True:
            tasks = [
                # Get Fish
                make_request(session, url, {'go': 'fishcaught', 'id': Fish_Map_ID, 'r': '', 'bamt': '1'}),
                # Sell All Items
                make_request(session, url, {'go': 'sellalluseritems'}),
                # Buy Worms
                make_request(session, url, {'go': 'buyitem', 'id': '18', 'qty': '2'}),
            ]

            responses = await asyncio.gather(*tasks)
            if wait_time == True:
              await asyncio.sleep(int(wait_time1)) #How many seconds avoids bans


if __name__ == '__main__':
    asyncio.run(main())
