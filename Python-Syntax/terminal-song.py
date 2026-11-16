import time
import sys

def type_line(text, char_delay=0.08):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(char_delay)
    print()


start = time.time()


lyrics = [
    (2.2,   "I found a love,",0.08),
    (5,   "for me",0.5),
    (10,  "Oh Darling, just dive right in",0.08),
    (14,  "and follow my lead",0.08),
    (18,  "Well, I found a girl",0.08),
    (21,  "beautiful and sweet",0.08),
    (25.0, "Oh, I never knew you were the someone waiting for", 0.06, 0.1, False, True), 
    (29.6, "me", 0.5, 0.0, True, False),
    (32,  "Cause we were just kids when we fell in love",0.08),
    (37,  "Not knowing what it was",0.08),
    (41,  "I will not give you up",0.08),
    (45,  "this time",0.08),
    (48,  "But darling, just kiss me slow,",0.08),
    (52,  "your heart is all I own",0.08),
    (55.5,  "And in your eyes, you're holding mine",0.08),
]



for item in lyrics:
    at_second = item[0]
    line = item[1]
    char_delay = item[2] if len(item) > 2 else 0.08
    elapsed = time.time() - start
    wait_time = at_second - elapsed
    if wait_time > 0:
        time.sleep(wait_time)
    type_line(line, char_delay=char_delay)