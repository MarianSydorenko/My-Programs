import pyowm
from colorama import init

init()
from colorama import Fore, Back, Style

owm = pyowm.OWM('76e18efcbfa195166b63df2f3eb6b2c9', language="ua")
print(Fore.BLACK)
print(Back.YELLOW)
place = input("В якому місті/країні?: ")

observation = owm.weather_at_place(place)
w = observation.get_weather()
temp = w.get_temperature('celsius')["temp"]

print(Fore.BLACK)
print(Back.CYAN)

print("В місті/країні: " + place + " зараз " + w.get_detailed_status())
print("Температура  в районі " + str(temp))

print(Fore.BLACK)
print(Back.GREEN)

if temp < 5:
    print("Зараз дуже холодно ! Варто вдітися тепліше.")
elif temp < 20:
    print(" Досить прохолодно але не смертельно.")
else:
    print("Температура супер , вдівай все що завгодно.")
input()
