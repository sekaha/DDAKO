order = "mrtcw,kae'lndsvyuoighxzbf.-qjp"

freqs = {
    "a" : 7.57,
    "b" : 1.32,
    "c" : 2.83,
    "d" : 3.45,
    "e" : 11.47,
    "f" : 1.99,
    "g" : 1.93,
    "h" : 4.38,
    "i" : 6.63,
    "j" : 0.11,
    "k" : 0.75,
    "l" : 3.97,
    "m" : 2.22,
    "n" : 6.59,
    "o" : 7.41,
    "p" : 1.92,
    "q" : 0.09,
    "r" : 5.85,
    "s" : 6.05,
    "t" : 8.44,
    "u" : 2.79,
    "v" : 1.01,
    "w" : 1.63,
    "x" : 0.2,
    "y" : 1.84,
    "z" : 0.09,
    "-" : 0.26,
    "'" : 0.26,
    "," : 0.99,
    "." : 1.08,
}

for c in order:
    print(f"\"{c}\" : {freqs[c]},")