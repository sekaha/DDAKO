import matplotlib.pyplot as plt
from collections import defaultdict
from conversion import merge, rgb_to_hex, okhsl_to_srgb, oklab_to_linear_srgb, linear_srgb_to_oklab, srgb_to_okhsl
from math import log10

high_col = srgb_to_okhsl(252, 231, 44)
low_col = srgb_to_okhsl(67, 13, 85)

chars = "etaoinsrhldcumfgpywbvkxjzq"

# get bigram freqs
bigram_freqs = defaultdict(int)

with open('bigrams.txt') as f:
    for l in f:
        bigram, freq = l.split('\t')

        if bigram.isalpha():
            bigram_freqs[bigram] += int(freq)
            bigram_freqs[bigram[1]+bigram[0]] += int(freq)

# get skipgram freqs
skipgram_freqs = defaultdict(int)

with open('1-skip.txt') as f:
    for l in f:
        skipgram, freq = l.split('\t')

        if skipgram.isalpha():
            skipgram_freqs[skipgram] += int(freq)
            skipgram_freqs[skipgram[1]+skipgram[0]] += int(freq)

high_f = max(*skipgram_freqs.values(), *bigram_freqs.values())
high_scale = max(bigram_freqs[c1+c2]+skipgram_freqs[c1+c2] for c1 in chars for c2 in chars)*1

def get_col(freq, offset=0):
    t = (freq)/high_f

    h, s, l = merge(low_col, high_col, t)

    return rgb_to_hex(*okhsl_to_srgb(h, s, min(l+offset, 0.95)))

# Chart
for target in chars:
    labels = [target+c for c in chars]

    indices = sorted(range(len(labels)), key=lambda i: -(bigram_freqs[labels[i]])) # skipgram_freqs[labels[i]]+
    labels = [labels[i] for i in indices]

    bigram_colors = [get_col(bigram_freqs[l], 0.2) for l in labels]
    skipgram_colors = [get_col(skipgram_freqs[l], -0.05) for l in labels]

    fig, ax = plt.subplots(figsize=(18, 9))
    # ax.set_ylim(0, high_scale) # 10**int(log10(high_scale)+0.5)

    # Plot each bar type
    bigram_vals = [bigram_freqs[l] for l in labels]
    skipgram_vals = [skipgram_freqs[l] for l in labels]
    bigram_bar = ax.bar(labels, bigram_vals, label='bigram',  color=bigram_colors, edgecolor='white')
    skipgram_bar = ax.bar(labels, skipgram_vals, label='skipgram', bottom=bigram_vals, color=skipgram_colors, edgecolor='white')

    plt.ylabel('Occurence Count', fontsize=24)
    # plt.xlabel('Skipgram', fontsize=24)
    plt.title(f"{target.upper()} - Bigram (Bottom) vs. Skipgram (Top) Occurences", fontsize=32)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

    
    plt.savefig(f'Graph_Utils/out/{target.upper()}_Skipgram_Bars.png', format='png', dpi=300)
    # plt.show()
    print(f"Exported {target.upper()}_Skipgram_Bars.png")
    plt.close()
