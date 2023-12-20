#Made By Shag420
#Discord: Shag420
#Try here: https://replit.com/@GH0STMAINE/explore

import aiohttp
import asyncio

async def explore_area(session, cookies, headers, params):
    url = 'https://farmrpg.com/worker.php'
    async with session.post(url, params=params, cookies=cookies, headers=headers) as response:
        return await response.text()

async def main():
    FRPG_COOKIE = input("Please input your HighwindFRPG Cookie: ")
    Area_ID = input("\nArea ID in url heres an example : https://farmrpg.com/index.php#!/area.php?id=1 [ID is number 1 depending on the map in the url so just put just the number of which explore area location you are at] : ")

    print("\n!Auto-Explore Farm Working!")

    cookies = {
        'pac_ocean': 'C10F9330',
        '_ga': 'GA1.1.1967035359.1687993870',
        'HighwindFRPG': FRPG_COOKIE,
        '_ga_94M1PS2E9X': 'GS1.1.1702759442.3.1.1702760539.0.0.0',
    }

    headers = {
        'authority': 'farmrpg.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://farmrpg.com',
        'referer': 'https://farmrpg.com/index.php',
        'sec-ch-ua': '"Chromium";v="118", "Opera GX";v="104", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'go': 'explore',
        'id': Area_ID,
    }

    async with aiohttp.ClientSession() as session:
        while True:
            response = await explore_area(session, cookies, headers, params)
            #print(response)
            #await asyncio.sleep(1)  # Adjust the delay as needed

if __name__ == "__main__":
    asyncio.run(main())
