from conversion import *
# Used for my poster
bg_col = srgb_to_okhsl(18, 21, 31)
fg_col = srgb_to_okhsl(29, 200, 255)

freqs = {
    "m" : 2.22,
    "r" : 5.85,
    "t" : 8.44,
    "c" : 2.83,
    "w" : 1.63,
    "," : 0.99,
    "k" : 0.75,
    "a" : 7.57,
    "e" : 11.47,
    "'" : 0.26,
    "l" : 3.97,
    "n" : 6.59,
    "d" : 3.45,
    "s" : 6.05,
    "v" : 1.01,
    "y" : 1.84,
    "u" : 2.79,
    "o" : 7.41,
    "i" : 6.63,
    "g" : 1.93,
    "h" : 4.38,
    "x" : 0.2,
    "z" : 0.09,
    "b" : 1.32,
    "f" : 1.99,
    "." : 1.08,
    "-" : 0.26,
    "q" : 0.09,
    "j" : 0.11,
    "p" : 1.92,
}

low_f = min(freqs.values())
high_f = max(freqs.values())

def get_col(freq):
    lerp = lambda a, b, t : a + (b-a) * t
    t = (freq-low_f)/(high_f-low_f)

    return okhsl_to_srgb(*(lerp(a, b, t) for a, b in zip(bg_col, fg_col)))

for char, freq in freqs.items():
    print(char, rgb_to_hex(*(int(v) for v in get_col(freq)))[1:])
