import sys

from weather import get_weather


def search_weather()-> None:
    city = input("Introduzca la ciudad: ").strip()

    weather = get_weather(city)

    if weather is None:
        print("\nCiudad no encotrada.\n")
        return

    print("=" * 20, " Weather ", "=" * 20)
    print(f"City        : {weather['city']}")
    print(f"Temperature : {weather['temperature']} °C")
    print(f"Feels Like  : {weather['feels_like']} °C")
    print(f"Humidity    : {weather['humidity']} %")
    print(f"Wind Speed  : {weather['wind_speed']} m/s")
    print(f"Description : {weather['description']}")
    print("=" * 49)

def show_menu() -> None:
    print("\n" * 2 + "=" * 35)
    print("       WEATHER DASHBOARD")
    print("=" * 35)
    print("1. Search weather")
    print("2. Show history")
    print("\nesc. Exit")
    print("=" * 35, "\n")


commands =  {"1" : search_weather, "2" : show_menu}

