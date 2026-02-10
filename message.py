import subprocess
import sys
import time


def install_pyfiglet():
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "pyfiglet", "--quiet"]
        )
        return True
    except subprocess.CalledProcessError:
        return False


try:
    from pyfiglet import figlet_format

    use_figlet = True
except ImportError:
    use_figlet = install_pyfiglet()
    if use_figlet:
        from pyfiglet import figlet_format


def render(sentence, delay=0.1):
    for c in sentence:
        print(c, end="", flush=True)
        time.sleep(delay)
    print()
    print()


def render_figlet_char(sentence, delay=0.2):
    art = figlet_format(sentence, font="big")

    lines = art.splitlines()

    for line in lines:
        print(line)
        time.sleep(delay)


def spam():
    word = "big"

    for _ in range(40):
        render_figlet_char(word, delay=0.03)

    render_figlet_char("fatty jelly belly", delay=0.2)
    print()


# Codes for colors
RED = "\033[91m"
GREEN = "\033[92m"
ENDC = "\033[0m"  # Resets color


def main():
    time.sleep(3.5)
    
    render("hey")
    time.sleep(2)
    render("hey!")
    time.sleep(2)
    render("hey you!!")
    time.sleep(2)
    render("yeah you")
    time.sleep(3)

    render("let me ask you a question", 0.15)
    time.sleep(2)

    render("are you..", 0.25)
    time.sleep(2)
    render("are you a..", 0.25)
    time.sleep(3)
    render(f"{RED}fatty jelly belly??{ENDC}", 0.07)
    time.sleep(1)
    render(f"{RED}biiiig faattttt bigggg fattttt bigg fattttyyy jelly???{ENDC}", 0.07)

    render("hold on..", 0.2)
    time.sleep(1)
    render("wrong question", 0.2)
    time.sleep(1)
    render("i meant", 0.3)
    render("are you a ", 0.3)
    time.sleep(0.2)

    render_figlet_char("fatty jelly belly?")
    time.sleep(1)
    render_figlet_char("biggg biggggg bigggggg fatty jelly belly?")
    time.sleep(1)

    spam()

    render("yeah i know u are", 0.3)

    time.sleep(2)
    render("hold on..", 0.2)
    time.sleep(1)
    render("i have one more question", 0.2)
    time.sleep(1)
    render(f"{RED} will you be my valentine <3 ? {ENDC}", 0.4)
    time.sleep(1)
    render_figlet_char("yes [ ]    no [ ]")


if __name__ == "__main__":
    main()
