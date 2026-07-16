from menu import show_menu, commands


def main() -> None:
    while True:
        show_menu()

        option = input("Choose an option: ").strip()
        if option == "esc": break
        command = commands.get(option)

        if command:
            command()
        else:
            print("\nOpcion invalida.\n")

        input("\nPresiona Enter para volver al menu...")


if __name__ == "__main__":
    main()