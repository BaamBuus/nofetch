import platform
import psutil
import time

import ctypes

# Set the window title
ctypes.windll.kernel32.SetConsoleTitleW("NOfetch")


# Define the logo ASCII art for different operating systems
LOGOS = {
    'Windows': r"""
_____________________________________
|                 |                  |
|                 |                  | 
|                 |                  | 
|                 |                  | 
|                 |                  | 
|                 |                  | 
|                 |                  | 
|                 |                  | 
|------------------------------------| 
|                 |                  | 
|                 |                  | 
|                 |                  | 
|                 |                  | 
|                 |                  | 
|                 |                  | 
|____________________________________| I couldn't find good ASCII art of the Windows logo.
""",
    'Linux': r"""
                    .88888888:.
                88888888.88888.
              .8888888888888888.
              888888888888888888
              88' _`88'_  `88888
              88 88 88 88  88888
              88_88_::_88_:88888
              88:::,::,:::::8888
              88`:::::::::'`8888
             .88  `::::'    8:88.
            8888            `8:888.
          .8888'             `888888.
         .8888:..  .::.  ...:'8888888:.
        .8888.'     :'     `'::`88:88888
       .8888        '         `.888:8888.
      888:8         .           888:88888
    .888:88        .:           888:88888:
    8888888.       ::           88:888888
    `.::.888.      ::          .88888888
   .::::::.888.    ::         :::`8888'.:.
  ::::::::::.888   '         .::::::::::::
  ::::::::::::.8    '      .:8::::::::::::.
 .::::::::::::::.        .:888:::::::::::::
 :::::::::::::::88:.__..:88888:::::::::::'
  `'.:::::::::::88888888888.88:::::::::'
        `':::_:' -- '' -'-' `':_::::'`           tux yes
    """
}

# Get system information using platform and psutil
system = platform.system()
release = platform.release()
architecture = platform.architecture()[0]
cpu = platform.processor()
cores = psutil.cpu_count(logical=False)
ram = psutil.virtual_memory().total // (1024 ** 3)

print('welcome to NOfetch, a neofetch clone made in python.')
print('-bambus was here https://bambus.lol')
time.sleep(1)

# Print the ASCII art logo and system information
print(LOGOS.get(system, "Unknown OS"))
time.sleep(1)
print(f"OS: {system} {release} {architecture}")
time.sleep(1)
print(f"CPU: {cpu}")
time.sleep(0.5)
print(f"Cores: {cores}")
time.sleep(0.2)
print(f"RAM: {ram}GB")
print('Note: The CPU might say something like \n"Intel64 Family 6 Model 158 Stepping 9, GenuineIntel". \nI dont know a good way to get rid of that, have mercy pls.')
input('Press enter to close.\n')
