# .9b9._tool.py
import os
import sys
import time
import threading
import asyncio
from pathlib import Path

import discord
from discord.ext import commands
from colorama import init as colorama_init, Fore, Style

# ---------- CONFIG ----------
APP_NAME = ".9b9. TOOL"
VERSION = "1.0.0"
RED = Fore.RED + Style.BRIGHT
PROGRESS_LEN = 60
PROGRESS_DELAY = 0.02
IS_WINDOWS = os.name == "nt"


MAX_CREATE = 10000
MAX_KADAPRA_MSGS = 10000
KADAPRA_DELAY = 0

colorama_init(autoreset=True)


def clear():
    os.system('cls' if IS_WINDOWS else 'clear')

def print_banner_and_about():
    clear()
    BANNER_ART = r"""
░░░░█████╗░██████╗░░█████╗░░░░  ████████╗░█████╗░░█████╗░██╗░░░░░
░░░██╔══██╗██╔══██╗██╔══██╗░░░  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
░░░╚██████║██████╦╝╚██████║░░░  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
░░░░╚═══██║██╔══██╗░╚═══██║░░░  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
██╗░█████╔╝██████╦╝░█████╔╝██╗  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗
╚═╝░╚════╝░╚═════╝░░╚════╝░╚═╝  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝
"""
    SKULL_ART = r"""
⠀⠀⠀…………………▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
……………▄▄█▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓█▄▄
…………▄▀▀▓▒░░░░░░░░░░░░░░░░▒▓▓▀▄
………▄▀▓▒▒░░░░░░░░░░░░░░░░░░░▒▒▓▀▄
……..█▓█▒░░░░░░░░░░░░░░░░░░░░░▒▓▒▓█
…..▌▓▀▒░░░░░░░░░░░░░░░░░░░░░░░░▒▀▓█
…..█▌▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█
…▐█▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█▌
…█▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█
..█▐▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒█▓█
…█▓█▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▒█▌▓█
..█▓▓█▒░░░░▒█▄▒▒░░░░░░░░░▒▒▄█▒░░░░▒█▓▓█
..█▓█▒░▒▒▒▒░░▀▀█▄▄░░░░░▄▄█▀▀░░▒▒▒▒░▒█▓█
.█▓▌▒▒▓▓▓▓▄▄▄▒▒▒▀█░░░░█▀▒▒▒▄▄▄▓▓▓▓▒▒▐▓█
.██▌▒▓███▓█████▓▒▐▌░░▐▌▒▓████▓████▓▒▐██
..██▒▒▓███▓▓▓████▓▄░░░▄▓████▓▓▓███▓▒▒██
..█▓▒▒▓██████████▓▒░░░▒▓██████████▓▒▒▓█
..█▓▒░▒▓███████▓▓▄▀░░▀▄▓▓███████▓▒░▒▓█
….█▓▒░▒▒▓▓▓▓▄▄▄▀▒░░░░░▒▀▄▄▄▓▓▓▓▒▒░▓█
……█▓▒░▒▒▒▒░░░░░░▒▒▒▒░░░░░░▒▒▒▒░▒▓█
………█▓▓▒▒▒░░██░░▒▓██▓▒░░██░░▒▒▒▓▓█
………▀██▓▓▓▒░░▀░▒▓████▓▒░▀░░▒▓▓▓██▀
………….░▀█▓▒▒░░░▓█▓▒▒▓█▓▒░░▒▒▓█▀░
…………█░░██▓▓▒░░▒▒▒░▒▒▒░░▒▓▓██░░█
………….█▄░░▀█▓▒░░░░░░░░░░▒▓█▀░░▄█
…………..█▓█░░█▓▒▒▒░░░░░▒▒▒▓█░░█▓█
…………….█▓█░░█▀█▓▓▓▓▓▓█▀░░█░█▓█▌
……………..█▓▓█░█░█░█▀▀▀█░█░▄▀░█▓█
……………..█▓▓█░░▀█▀█░█░█▄█▀░░█▓▓█
………………█▓▒▓█░░░░▀▀▀▀░░░░░█▓▓█
………………█▓▒▒▓█░░░░ ░░░░░░░█▓▓█
………………..█▓▒▓██▄█░░░▄░░▄██▓▒▓█
………………..█▓▒▒▓█▒█▀█▄█▀█▒█▓▒▓█
………………..█▓▓▒▒▓██▒▒██▒██▓▒▒▓█
………………….█▓▓▒▒▓▀▀███▀▀▒▒▓▓█
……………………▀█▓▓▓▓▒▒▒▒▓▓▓▓█▀
………………………..▀▀██▓▓▓▓██▀⠀⠀
"""

    ABOUT_ME = "Discord: .9b9. \n   GitHub: 5waf"

    print(RED + BANNER_ART + f"Version {VERSION}\n")
    print(RED + SKULL_ART)
    print(RED + ABOUT_ME)

def erase_last_lines(n=1):
    if n <= 0:
        return
    for _ in range(n):
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')
    sys.stdout.flush()

def startup_loader():
    sys.stdout.write("\n")
    for i in range(PROGRESS_LEN+1):
        bar = "█"*i + "-"*(PROGRESS_LEN-i)
        pct = int((i/PROGRESS_LEN)*100)
        sys.stdout.write(f"\r{RED}[{bar}] {pct}%")
        sys.stdout.flush()
        time.sleep(PROGRESS_DELAY)
    sys.stdout.write("\n\n")

def input_masked(prompt_text="Enter BOT token (hidden): "):
    """
    Windows: read char-by-char with msvcrt.getwch().
    If user pastes (Ctrl+V, '\x16'), try to read clipboard via tkinter.clipboard_get()
    and append full pasted text (but print '*' for each character).
    Non-Windows: fallback to getpass.getpass (handles paste normally).
    """
    if IS_WINDOWS:
        import msvcrt
        
        def get_clipboard_text():
            try:
               
                import tkinter
                root = tkinter.Tk()
                root.withdraw()
                try:
                    txt = root.clipboard_get()
                finally:
                    try:
                        root.destroy()
                    except:
                        pass
                return txt
            except Exception:
                return None

        sys.stdout.write(RED + prompt_text)
        sys.stdout.flush()
        chars = []
        while True:
            ch = msvcrt.getwch()
            
            if ch in ("\r", "\n"):
                print()
                break
            
            if ch == "\x03":
                raise KeyboardInterrupt
            
            if ch in ("\x08", "\x7f"):
                if chars:
                    chars.pop()
                    
                    sys.stdout.write('\b \b')
                    sys.stdout.flush()
                continue
            
            if ch == "\x16":
                pasted = get_clipboard_text()
                if pasted:
                    
                    chars.extend(list(pasted))
                    sys.stdout.write('*' * len(pasted))
                    sys.stdout.flush()
                
                continue
            
            
            if len(ch) > 1:
                
                chars.extend(list(ch))
                sys.stdout.write('*' * len(ch))
                sys.stdout.flush()
                continue
            
            chars.append(ch)
            sys.stdout.write('*')
            sys.stdout.flush()
        return ''.join(chars)
    else:
        import getpass
        
        return getpass.getpass(RED + prompt_text)
# ---------- Discord setup ----------
intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

bot_ready = threading.Event()
bot_loop = None
bot_thread = None
bot_exc = None

@bot.event
async def on_ready():
    bot_ready.set()

def start_bot_thread(token):
    def runner():
        global bot_exc, bot_loop
        try:
            bot_loop = asyncio.new_event_loop()
            asyncio.set_event_loop(bot_loop)
            bot_loop.run_until_complete(bot.start(token))
        except Exception as e:
            bot_exc = e
        finally:
            try:
                bot_loop.run_until_complete(bot.close())
            except:
                pass
            try:
                bot_loop.close()
            except:
                pass
    t = threading.Thread(target=runner, daemon=True)
    t.start()
    return t

def run_in_bot(coro):
    if not bot_loop:
        raise RuntimeError("Bot loop not running")
    fut = asyncio.run_coroutine_threadsafe(coro, bot_loop)
    return fut.result()


def get_guilds():
    if not bot_ready.wait(timeout=10):
        raise RuntimeError("Bot not ready")
    return list(bot.guilds)

def safe_change_guild(guild_id, new_name=None, icon_path=None):
    async def coro():
        g = bot.get_guild(guild_id)
        if not g: raise RuntimeError("Guild not found")
        kwargs = {}
        if new_name: kwargs['name'] = new_name
        if icon_path:
            p = Path(icon_path)
            if not p.exists(): raise RuntimeError("Icon not found")
            kwargs['icon'] = p.read_bytes()
        if kwargs:
            await g.edit(**kwargs)
            return True
        return False
    return run_in_bot(coro())

def safe_create_channel(guild_id, name):
    async def coro():
        g = bot.get_guild(guild_id)
        if not g: raise RuntimeError("Guild not found")
        return await g.create_text_channel(name)
    return run_in_bot(coro())

def safe_delete_channel(guild_id, channel_id):
    async def coro():
        g = bot.get_guild(guild_id)
        ch = g.get_channel(channel_id)
        if ch:
            await ch.delete()
            return True
        return False
    return run_in_bot(coro())

def safe_send_message(guild_id, channel_id, message):
    async def coro():
        g = bot.get_guild(guild_id)
        ch = g.get_channel(channel_id)
        if ch:
            await ch.send(message)
            return True
        return False
    return run_in_bot(coro())

def safe_close_bot():
    async def coro():
        await bot.close()
    try:
        return run_in_bot(coro())
    except:
        return None

# ---------- Main ----------
def main():
    try:
        print_banner_and_about()
        startup_loader()
        print_banner_and_about()
        token = input_masked()
        if not token:
            print(RED + "No token entered. Exiting.")
            return
        global bot_thread
        bot_thread = start_bot_thread(token)
        print(RED + "\nLogging in... waiting up to 10s")
        if not bot_ready.wait(timeout=10):
            time.sleep(0.3)
            if bot_exc:
                print(RED + f"Login error: {bot_exc}")
                return
            print(RED + "Bot not ready. Check token/network.")
            return

        guilds = get_guilds()
        if not guilds:
            print(RED + "Bot not in any guilds. Exiting.")
            safe_close_bot()
            return

        guild_idx = 0
        if len(guilds) > 1:
            for i, g in enumerate(guilds):
                print(f"{i}: {g.name}")
            guild_idx = int(input("Select guild index (0-based): "))
        guild = guilds[guild_idx]

        while True:
            # =================== Main Menu ===================
            print_banner_and_about()
            connected_text = f"Connected as: {bot.user}    Selected: {guild.name}"
            print(RED + connected_text + "\n")

            # Main Menu rectangle
            print(RED + "╔" + "═"*68 + "╗")
            print(RED + "║" + " "*((68-len(" MAIN MENU "))//2) + "MAIN MENU" + " "*((68-len(" MAIN MENU "))//2) + "║")
            print(RED + "╠" + "═"*68 + "╣")
            print(RED + "║ 1 - Create Channels".ljust(68) + "║")
            print(RED + "║ 2 - Delete Channels".ljust(68) + "║")
            print(RED + "║ 3 - Send Messages".ljust(68) + "║")
            print(RED + "║ 4 - Rename Server".ljust(68) + "║")
            print(RED + "║ 5 - Change Server Icon".ljust(68) + "║")
            print(RED + "║ 0 - Logout & Exit".ljust(68) + "║")
            print(RED + "╚" + "═"*68 + "╝\n")

            choice = input(RED + "Choose option number: ").strip()
            erase_last_lines(1)

            if choice == "0":
                print(RED + "Logging out...")
                safe_close_bot()
                break

            if choice == "1":
                base_name = input(RED + "Base name for channels: ").strip()
                count = int(input(RED + "How many channels to create: ").strip())
                count = min(count, MAX_CREATE)
                for i in range(1, count+1):
                    safe_create_channel(guild.id, f"{base_name}-{i}")
                    print(RED + f"Created {base_name}-{i}")
                input(RED + "Press Enter to continue...")
                erase_last_lines(1)
                continue

            if choice == "2":
                for idx, ch in enumerate(guild.text_channels):
                    print(f"{idx}: {ch.name} (ID: {ch.id})")
                ch_idx = int(input(RED + "Select channel index to delete: ").strip())
                channel = guild.text_channels[ch_idx]
                confirm = input(RED + f"Type YES to delete {channel.name}: ").strip()
                if confirm == "YES":
                    safe_delete_channel(guild.id, channel.id)
                    print(RED + f"{channel.name} deleted")
                input(RED + "Press Enter to continue...")
                erase_last_lines(1)
                continue

            if choice == "3":
                for idx, ch in enumerate(guild.text_channels):
                    print(f"{idx}: {ch.name} (ID: {ch.id})")
                ch_idx = int(input(RED + "Select channel index to send message: ").strip())
                message = input(RED + "Message content: ").strip()
                channel = guild.text_channels[ch_idx]
                safe_send_message(guild.id, channel.id, message)
                print(RED + "Message sent")
                input(RED + "Press Enter to continue...")
                erase_last_lines(1)
                continue

            if choice == "4":
                new_name = input(RED + "Enter new server name: ").strip()
                confirm = input(RED + "Type YES to rename server: ").strip()
                if confirm == "YES":
                    safe_change_guild(guild.id, new_name=new_name)
                    print(RED + f"Server renamed to {new_name}")
                input(RED + "Press Enter to continue...")
                erase_last_lines(1)
                continue

            if choice == "5":
                icon_path = input(RED + "Path to new icon image: ").strip()
                confirm = input(RED + "Type YES to change server icon: ").strip()
                if confirm == "YES":
                    safe_change_guild(guild.id, icon_path=icon_path)
                    print(RED + "Server icon changed")
                input(RED + "Press Enter to continue...")
                erase_last_lines(1)
                continue

            print(RED + "Unknown option")
            time.sleep(0.4)

    except KeyboardInterrupt:
        print(RED + "\nExiting...")
        safe_close_bot()
    except Exception as e:
        print(RED + f"Error: {e}")
        safe_close_bot()


if __name__ == "__main__":
    main()
# .9b9._tool.py