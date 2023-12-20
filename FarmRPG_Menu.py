import tkinter as tk
from tkinter import ttk
import aiohttp
import asyncio
import threading

autofarm_running = False
explore_running = False
FRPG_COOKIE = None
temp_cookie = None
login_window = None
Explorelabel = None

temp_wait_time = None
temp_fish_map_id = None
fishing_autofarm = None
wait_time_var = None
fishing_label = None
fish_map_id_label = None
fish_map_id_entry = None
wait_time_label = None
wait_time_entry = None
start_button = None
wait_time_button = None
area_id_label = None
area_id_entry = None
start_button_explore = None
area_id = None


def on_login_button_click():
    global FRPG_COOKIE, temp_cookie, login_window
    FRPG_COOKIE = temp_cookie.get()
    login_window.destroy()
    create_main_window()


def on_toggle_wait_time():
    wait_time_label.config(state='normal' if wait_time_var.get() else 'disabled')
    wait_time_entry.config(state='normal' if wait_time_var.get() else 'disabled')


async def make_request(session, url, params):
    async with session.post(url, params=params) as response:
        return await response.text()


async def main():
    global autofarm_running, FRPG_COOKIE, temp_wait_time, temp_fish_map_id
    while autofarm_running:
        if wait_time_var.get():
            await asyncio.sleep(int(temp_wait_time.get()))

        cookies = {
            'farmrpg_token': 'qhmh2ah0kogpcus1hi40277fo4ed74634cpvggh6',
            'pac_ocean': '8106C6F2',
            '_ga': 'GA1.1.320387843.1700454041',
            'HighwindFRPG': FRPG_COOKIE,
            '_ga_94M1PS2E9X': 'GS1.1.1702343895.4.1.1702349729.0.0.0',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://farmrpg.com',
            'Connection': 'keep-alive',
            'Referer': 'https://farmrpg.com/index.php',
        }

        url = 'https://farmrpg.com/worker.php'

        async with aiohttp.ClientSession(headers=headers, cookies=cookies) as session:
            tasks = [
                make_request(session, url, {'go': 'fishcaught', 'id': temp_fish_map_id.get(), 'r': '', 'bamt': '1'}),
                make_request(session, url, {'go': 'sellalluseritems'}),
                make_request(session, url, {'go': 'buyitem', 'id': '18', 'qty': '2'}),
            ]

            responses = await asyncio.gather(*tasks)


async def explore_area(session, cookies, headers, params):
    url = 'https://farmrpg.com/worker.php'
    async with session.post(url, params=params, cookies=cookies, headers=headers) as response:
        return await response.text()


async def explore_main():
    global explore_running, FRPG_COOKIE, area_id_entry
    area_id = area_id_entry.get()

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
        'id': area_id,
    }

    async with aiohttp.ClientSession() as session:
        while explore_running:
            response = await explore_area(session, cookies, headers, params)


def toggle_autofarm(start_button):
    global autofarm_running, fishing_label, temp_wait_time, temp_fish_map_id
    autofarm_running = not autofarm_running
    start_button.config(text="Stop Autofarm" if autofarm_running else "Start Autofarm")
    fishing_label.config(text=f"Fishing Autofarm: {'On' if autofarm_running else 'Off'}")
    wait_time_label.config(state='normal' if autofarm_running and wait_time_var.get() else 'disabled')
    wait_time_entry.config(state='normal' if autofarm_running and wait_time_var.get() else 'disabled')
    if autofarm_running:
        asyncio_thread = threading.Thread(target=asyncio.run, args=(main(),))
        asyncio_thread.start()


def toggle_explore_autofarm(start_button_explore):
    global explore_running, Explorelabel, area_id_entry
    explore_running = not explore_running
    start_button_explore.config(text="Stop Autofarm" if explore_running else "Start Autofarm")
    Explorelabel.config(text=f"Explore Autofarm: {'On' if explore_running else 'Off'}")
    if explore_running:
        asyncio_thread = threading.Thread(target=asyncio.run, args=(explore_main(),))
        asyncio_thread.start()


def on_toggle_wait_time():
    global wait_time_label, wait_time_var
    wait_time_label.config(state='normal' if wait_time_var.get() else 'disabled')
    wait_time_entry.config(state='normal' if wait_time_var.get() else 'disabled')


def create_login_window():
    global temp_cookie, login_window
    login_window = tk.Tk()
    login_window.title("FarmRPG : HighwindFRPG Cookie Login")
    login_window.attributes('-topmost', True)

    temp_cookie = tk.StringVar()

    cookie_label = ttk.Label(login_window, text="HighwindFRPG Cookie:")
    cookie_entry = ttk.Entry(login_window, textvariable=temp_cookie)
    login_button = ttk.Button(login_window, text="Login", command=on_login_button_click)

    cookie_label.pack(pady=5)
    cookie_entry.pack(pady=5)
    login_button.pack(pady=10)

    login_window.mainloop()


def create_main_window():
    global temp_wait_time, temp_fish_map_id, fishing_autofarm, wait_time_var
    global fishing_label, fish_map_id_label, fish_map_id_entry, wait_time_label, wait_time_entry, start_button, wait_time_button
    global Explorelabel, area_id_label, area_id_entry, start_button_explore, area_id_var

    window = tk.Tk()
    window.title("FarmRPG Cheats")
    window.attributes('-topmost', True)

    notebook = ttk.Notebook(window)

    tab1 = ttk.Frame(notebook)
    tab2 = ttk.Frame(notebook)

    notebook.add(tab1, text="Fishing")
    notebook.add(tab2, text="Exploring")

    temp_wait_time = tk.StringVar()
    temp_fish_map_id = tk.StringVar()
    fishing_autofarm = False
    wait_time_var = tk.BooleanVar()

    fishing_label = ttk.Label(tab1, text="Fishing Autofarm: Off")
    fish_map_id_label = ttk.Label(tab1, text="Fishing Map ID (e.g. 1):")
    fish_map_id_entry = ttk.Entry(tab1, textvariable=temp_fish_map_id)
    wait_time_label = ttk.Label(tab1, text="Wait Time (seconds):")
    wait_time_entry = ttk.Entry(tab1, textvariable=temp_wait_time, state='disabled')
    start_button = ttk.Button(tab1, text="Start Autofarm", command=lambda: toggle_autofarm(start_button))
    wait_time_button = ttk.Checkbutton(tab1, text="Enable Wait Time", variable=wait_time_var, command=on_toggle_wait_time)

    fishing_label.pack(pady=5)
    fish_map_id_label.pack(pady=5)
    fish_map_id_entry.pack(pady=5)
    wait_time_button.pack(pady=5)
    wait_time_label.pack(pady=5)
    wait_time_entry.pack(pady=5)
    start_button.pack(pady=10)

    Explorelabel = ttk.Label(tab2, text="Explore Autofarm: Off")
    area_id_label = ttk.Label(tab2, text="Area ID (e.g. 1):")
    area_id_var = tk.StringVar()
    area_id_entry = ttk.Entry(tab2, textvariable=area_id_var)
    start_button_explore = ttk.Button(tab2, text="Start Autofarm", command=lambda: toggle_explore_autofarm(start_button_explore))

    Explorelabel.pack(pady=5)
    area_id_label.pack(pady=5)
    area_id_entry.pack(pady=5)
    start_button_explore.pack(pady=10)

    notebook.pack(expand=1, fill="both")

    window.mainloop()


create_login_window()
