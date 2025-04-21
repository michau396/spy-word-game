import random
import os
import sys
import time

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_sound():
        if sys.platform == "darwin":  # Mac
            os.system("afplay /System/Library/Sounds/Glass.aiff")
        elif sys.platform == "win32":  # Windows
            import winsound
            winsound.MessageBeep()
        else:
            print("\a")  # Unix 

def loading_bar(duration):
    bar_length = 50
    for i in range(bar_length + 1):
        time.sleep(duration / bar_length) 
        filled_length = int(bar_length * i // bar_length)
        bar = '#' * filled_length + '-' * (bar_length - filled_length) 
        sys.stdout.write(f'\r[{bar}] {i * 100 // bar_length}%')
        sys.stdout.flush()
    print()

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("⚠️ Podaj poprawną liczbę!")

def show_intro():
    clear_terminal()
    print("=" * 50)
    print("🔍  WITAJ W GRZE: SZPIEG  🔍".center(50))
    print("=" * 50)
    print("\nWitaj w towarzyskiej grze dedukcji i blefu!")
    print("Twoim zadaniem jest odnaleźć szpiega lub ukryć się wśród graczy.\n")
    print("💡 ZASADY:")
    print("1. Obywatele znają hasło.")
    print("2. Szpieg zna jedynie podpowiedź.")
    print("3. Zadawajcie po kolei pytania i analizujcie odpowiedzi!")
    print("4. Na końcu wszyscy głosują kto jest szpiegiem.\n")
    print("=" * 50)
    input("Naciśnij Enter, aby rozpocząć grę!")
    clear_terminal()

def start_game():
    print("🔍 Uruchamianie gry szpieg...")
    loading_bar(1)
    clear_terminal()
    show_intro()
    players = get_int_input("👥 Podaj liczbę graczy: ")
    
    spies = get_int_input("🕵️‍♂️ Podaj liczbę szpiegów: ")
    if spies >= players:
        print("Liczba szpiegów musi być mniejsza niż liczba graczy!")
        return
    
    game_time = get_int_input("⏳ Podaj czas gry (w sekundach): ")
    with open('words.txt', 'r', encoding='utf-8') as file:
        words = [line.strip() for line in file]
    with open('hints.txt', 'r', encoding='utf-8') as file:
        hints = [line.strip() for line in file]

    if not words or not hints:
        print("Błąd: Pliki 'words.txt' lub 'hints.txt' są puste!")
        return

    print("Gra rozpoczęta!")
    
    chosen_word = random.choice(words)
    hint_for_word = hints[words.index(chosen_word)]
    roles = ["szpieg"] * spies + ["obywatel"] * (players - spies)
    random.shuffle(roles)

    print("Każdy gracz podchodzi po kolei i naciska Enter, aby zobaczyć swoją rolę.\n")

    for i in range(players):
        input(f"👤 Gracz {i+1} naciśnij Enter, aby zobaczyć swoją rolę.")

        if roles[i] == "szpieg":
            print(f"Twoja rola: \033[31mSZPIEG\033[0m 🕵️‍♂️ — Podpowiedź to: '\033[1m{hint_for_word}\033[0m'\n")
        else:
            print(f"Twoja rola: \033[34mOBYWATEL\033[0m 🧑‍🤝‍🧑 — Hasło to: '\033[1m{chosen_word}\033[0m'— Kategoria: '\033[1m{hint_for_word}\033[0m'\n")
        
        input("Naciśnij Enter i przekaż kolejnej osobie.\n")
        clear_terminal()

    print("Wszyscy gracze znają swoje role! Gra rozpoczęta!")
    print(f"Macie {game_time} sekund na zadawanie pytań! ⏳ Czas start!\n")
    loading_bar(game_time)
    play_sound()
    print("Koniec czasu, zacznijcie głosowanie!\n")

def main():
    while True:
        start_game()
        play_again = input("Czy chcesz zagrać ponownie? (t/n): ").lower()
        if play_again != "t":
            print("Dziękuję za grę do widzenia!")
            break

if __name__ == "__main__":
    main() 
