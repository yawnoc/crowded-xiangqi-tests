#!/usr/bin/env python3

"""
# tabulate.py

Tabulate the win statistics in `*/*/*.pgn`, updating `README.md`.
"""

import glob
import os
import sys


class Statistic:
    def __init__(self, os_engine, opening_timing, red_wins, black_wins, draws):
        self.os_engine = os_engine
        self.opening_timing = opening_timing
        self.red_wins = red_wins
        self.black_wins = black_wins
        self.draw = draws


def read_file_content(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()


def main():
    statistics = []

    for game_directory in sorted(glob.glob('*/*/')):
        os_engine, opening_timing = game_directory.split(os.sep)[0:2]

        game_file_names = sorted(glob.glob(f'{game_directory}/*.pgn'))
        game_file_contents = [read_file_content(gfn) for gfn in game_file_names]

        red_wins = sum(1 for gfc in game_file_contents if '[Result "1-0"]' in gfc)
        black_wins = sum(1 for gfc in game_file_contents if '[Result "0-1"]' in gfc)
        draws = sum(1 for gfc in game_file_contents if '[Result "1/2-1/2"]' in gfc)
        total_games = len(game_file_names)

        if red_wins + black_wins + draws != total_games:
            print(
                f'In game_directory `{game_directory}`, '
                f'red_wins ({red_wins}) + black_wins ({black_wins}) + draws ({draws}) '
                f'addeth not up unto total_games ({total_games}).',
                file=sys.stderr,
            )
            sys.exit(1)

        statistics.append(Statistic(os_engine, opening_timing, red_wins, black_wins, draws))


if __name__ == '__main__':
    main()
