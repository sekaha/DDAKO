# DDAKO: A Data-Driven Approach to Keyboard Optimization ⌨️✨

[![License: AGPL-v3](https://img.shields.io/badge/license-AGPL--v3-blue)](https://github.com/sekaha/DDAKO/blob/main/LICENSE)

DDAKO is a research project that explores the optimization of keyboard layouts using data-driven techniques. By leveraging large-scale empirical typing data, a high-quality web-based English corpus, and a custom simulated annealing algorithm, the project aims to design keyboard layouts that improve predicted typing speed. This is the first step in a more objective creation of keyboard layouts, starting with the speed aspect, future work will delve into ergonomics as they relate to fatigue and hand muscle usage.

**Full Research Paper:** [A Data-Driven Approach to Keyboard Optimization (PDF)](https://github.com/sekaha/DDAKO/blob/main/Data-Driven%20Approach%20to%20Keyboard%20Optimization.pdf)
**Poster:** [Poster.pdf](https://github.com/sekaha/DDAKO/blob/main/Poster.pdf)

## Table of Contents

- [Abstract](#abstract)
- [Overview](#overview)
- [Key Features](#key-features)
- [Key Results](#key-results)
- [Installation](#installation)
- [Usage](#usage)

## Abstract

The QWERTY layout, first developed in the 1870s for typewriters, is the most widely used keyboard layout today despite its inefficiencies. The development of an alternative layout faces two major challenges: quantifying the impact of ergonomic features and effectively navigating the vast search space of possible keyboard layouts. To address these challenges, this paper proposes a data-driven approach using simulated annealing with an objective function derived from empirical typing data. The two data sets used are the 136M Keystrokes data set from Aalto University, containing 8,228 hours of typing data from 168,000 participants, for a controlled analysis of four layouts (AZERTY, Dvorak, QWERTY, and QWERTZ), and the iWeb corpus, one of the largest collections of English text, for frequency analysis. A custom implementation of simulated annealing is employed, featuring a dynamic initial temperature and termination criterion that enables compatibility with different subsets of keys, corpora, and optimization criteria. An analysis reveals a number of factors that impact typing speed. Based on this analysis, a cost function is devised and fine-tuned using the Levenberg-Marquardt algorithm (MAE:12ms, R²:0.78 at 80 WPM). To estimate the typing efficiency of a candidate layout, the cost function evaluates the predicted typing time for each sequence in the corpus based on the given layout. The sum of these predicted times serves as the objective function for optimization via simulated annealing. The result is a layout estimated to be 6% faster for typing English compared to QWERTY.

## Overview

Traditional keyboard layouts like QWERTY were not designed with modern typing efficiency or robust ergonomic principles in mind. DDAKO addresses this by:

-   Analyzing large-scale empirical typing data (136M Keystrokes dataset) and extensive text corpora (iWeb corpus).
-   Developing a quantitative objective function to predict typing time based on key placement, finger dexterity, and character/n-gram frequency.
-   Employing a custom simulated annealing algorithm with dynamic parameter tuning to optimize key placements.
-   Evaluating layouts based on predicted typing speed and ergonomic considerations derived from data.

The project includes Python scripts for the entire pipeline, from data processing to layout optimization and evaluation, as well as LaTeX documents presenting the research findings.

## Key Features

-   **Empirical Data Analysis**: Processes and analyzes the 136M Keystrokes dataset and iWeb corpus for insights into typing patterns and language statistics.
-   **Sophisticated Cost Function**: A nuanced cost function for bistrokes and tristrokes, fine-tuned with the Levenberg-Marquardt algorithm, considering:
    -   Positional penalties (columnar and row).
    -   Frequency penalties (logarithmic).
    -   Categorical penalties for Alternating Hand (ALT), Single-Hand (SHB), and Single-Finger (SFB) bistrokes.
    -   Penalties for single-finger skipstrokes in trigrams.
-   **Customizable Simulated Annealing**: Implements simulated annealing with:
    -   Dynamic initial temperature calculation.
    -   Probabilistic termination criterion.
    -   Geometric cooling schedule.
    -   Ability to optimize for different WPM ranges, languages, or key subsets.
-   **Layout Evaluation**: Assesses generated layouts against existing ones like QWERTY and Dvorak using the derived objective function.
-   **Research Documentation**: Includes LaTeX source for the research paper and poster.

## Key Results

![image](https://github.com/user-attachments/assets/cc4ef547-6cb2-45b2-8a62-887950de3462)

-   The generated layout is predicted to be **6% faster** for typing English text (iWeb corpus) compared to QWERTY, and 2% faster than Dvorak, when optimized for typists at ≥ 80 WPM.
    -   QWERTY: 54,934,582 seconds ~15,259 hours (predicted time on iWeb corpus)
    -   Dvorak: 52,565,249 seconds ~14,601 hours (4% speedup vs. QWERTY)
    -   DDAKO Layout: 51,429,827 seconds ~14,286 hours (6% speedup vs. QWERTY)
-   **Ergonomic Improvements (Bistroke Categories):**
    | Layout      | Alternating Hand (ALT) | Single Finger (SFB) |
    | :---------- | :--------------------: | :-----------------: |
    | QWERTY      |         18.3%          |        5.7%         |
    | Dvorak      |         33.6%          |        2.8%         |
    | DDAKO Layout|         33.6%          |        **1.4%**     |
    *(Lower SFB % and higher ALT % are generally better)*


It should be noted that the layout presented in the research paper is **foremost a proof of concept, designed to validate the optimization methodology based on a singular, quantifiable metric: typing speed.** Speed offers an objective target, allowing for clearer analysis and a more straightforward foundation for exploring complex optimization problems. This approach makes it easier to reason about and potentially extend the methodology to include other factors in the future. Aspects such as long-term comfort, transition effort from existing layouts (like QWERTY), specific ergonomic needs (e.g., minimizing certain finger strains beyond general speed), and overall subjective user preference were not primary objectives for *this specific generated layout*. Therefore, while the generated layout serves as an interesting outcome of the speed optimization, it is **not presented as a universally recommended alternative for everyday typing** without individual consideration and further research into these broader usability aspects.


## Installation

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/sekaha/DDAKO.git
    cd DDAKO
    ```

2.  **Set Up a Virtual Environment (Recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    I'm too lazy to make one rn remind me in the future... We'll see how many people actually read this. This is my test!
    
## Usage

The core optimization (`simulated_annealing.py`) script uses pre-calculated model weights (derived from the analysis in `trigram_model.ipynb`) that are hardcoded. This means **you do not need to download the large dataset or run the `trigram_model.ipynb` notebook to generate and evaluate optimized keyboard layouts.**

1.  **Running the Layout Optimization and Evaluation (No Data Download Needed):**
    *   **To run the keyboard layout optimization using simulated annealing:**
        ```bash
        python simulated_annealing.py
        ```
        This script uses hardcoded cost function parameters (derived from `trigram_model.ipynb`) to predict sequence typing times and optimize a layout based on the n-gram frequencies found in `bigrams.txt` and `trigrams.txt` (which should be present in the repository as standard inputs for this script).

2.  **Optional: Re-deriving Model Weights or Custom Analysis (Requires Data Download):**
    *   If you wish to:
        *   Understand how the cost function weights were derived.
        *   Re-run the model fitting process (e.g., with different data or parameters).
        *   Perform custom data analysis or visualizations.
        
        ...then you will need to use the `trigram_model.ipynb` notebook and the associated full dataset.

    *   **Data Preparation for `trigram_model.ipynb`:**
        *   The dataset containing processed keystroke timing data for the `trigram_model.ipynb` notebook can be downloaded from:
            *   [**Download Core Dataset (ngram_dataset.zip from Google Drive)**](https://drive.google.com/file/d/1NCXE8hl6SkDjoG_lPoUzMD4tlV6mCgTB/view?usp=sharing)
        *   Download and unzip `ngram_dataset.zip`. This archive should contain:
            *   `bistrokes.tsv`
            *   `tristrokes.tsv`
        *   Place these extracted files into the root project directory (e.g., alongside `trigram_model.ipynb`).

---

*For more detailed information on the research methodology, analysis, and results, please refer to the [Paper.pdf](https://github.com/sekaha/DDAKO/blob/main/Data-Driven%20Approach%20to%20Keyboard%20Optimization.pdf) and [Poster.pdf](https://github.com/sekaha/DDAKO/blob/main/Poster.pdf) files included in the repository.*
