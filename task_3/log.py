from colorama import Fore

def log_folger(folder):
    return f"{Fore.BLUE}{folder}{Fore.RESET}"

def log_file(file):
    return f"{Fore.YELLOW}{file}{Fore.RESET}"
