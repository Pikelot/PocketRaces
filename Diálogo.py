import time
import sys

def delay(texto):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0 if char == ' ' else 0.1)
    print()