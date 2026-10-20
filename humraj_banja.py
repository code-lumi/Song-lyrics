import time
import sys
import os
import random
SOFT_INDIGO = '\033[38;5;104m'
WARM_CREAM = '\033[38;5;223m'
DEEP_ROSE = '\033[38;5;168m'
SOFT_GOLD = '\033[38;5;180m'
FAINT = '\033[38;5;253m'
BOLD = '\033[1m'
RESET = '\033[0m'

def soft_typing(text, color):
    for char in text:
        sys.stdout.write(f"{BOLD}{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(0.071)

def run_humraz_code():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"\n{FAINT}        ·  humraz ban ja  ·{RESET}")
    time.sleep(1.3)
    print(f"{SOFT_GOLD}        ──────────────────{RESET}\n")
    time.sleep(0.85)

    lyrics = [
        ("Main raaz tujhse kahun humraz ban ja zara...", SOFT_INDIGO),
        ("karni hai kuch guftgu alfaaz ban ja zara...", SOFT_INDIGO),
        ("Juda jab se hua...", DEEP_ROSE),
        ("tere bina khamosh rehta hoon me...", DEEP_ROSE),
        ("Labon ke paas aa...", WARM_CREAM),
        ("ab tu meri aawaaz bann ja zara...", WARM_CREAM)
    ]

    for line, color in lyrics:
        indent = " " * random.randint(4, 13)
        sys.stdout.write(indent)
        
        soft_typing(line, color)
        
        if "raaz" in line.lower() or "humraz" in line.lower():
            sys.stdout.write("  🤫")
        elif "guftgu" in line.lower() or "alfaaz" in line.lower():
            sys.stdout.write("  💬")
        elif "juda" in line.lower() or "khamosh" in line.lower():
            sys.stdout.write("  😔")
        elif "aawaaz" in line.lower() or "labon" in line.lower():
            sys.stdout.write("  ❤️")
        else:
            sys.stdout.write("  ✨")
            
        print("\n")
        time.sleep(1.55)

    print(f"\n{SOFT_GOLD}        ──────────────────{RESET}")
    print(f"{FAINT}        labon ke paas aa...{RESET}")
    print(f"{DEEP_ROSE}        meri aawaaz bann ja zara ❤️{RESET}\n")

if __name__ == "__main__":
    run_humraz_code()