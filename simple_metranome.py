# SPDX-FileCopyrightText: 2023 Dimitris Kardarakos <dimkard@posteo.net>
# SPDX-License-Identifier: AGPL-3.0-only

"""Simple metronome script"""

import subprocess
import argparse
import shutil
from pathlib import Path
import logging
import sys

BEAT_TIME = 0.005
TMP_FILE_DIR = "/tmp"
BEAT_TEXT_SIZE = 5
BEAT_TEXT_POSITION = 75
MIN_BPM = 20
MAX_BPM = 220
LOG_LEVEL = "WARNING"


def get_arg_parser() -> argparse.ArgumentParser:
    """Parse script arguments"""
    parser = argparse.ArgumentParser(
        prog="simple-metronome", description="A simple metronome script"
    )

    parser.add_argument("--bpm", help="set the beats per minute", type=int, default=60)
    parser.add_argument(
        "--beats", help="set the amount of beats", type=int, default="4"
    )
    parser.add_argument(
        "--strong", help="set the note of the strong beat", type=int, default="4000"
    )
    parser.add_argument(
        "--weak", help="set the note of the weak beat", type=int, default="2000"
    )

    return parser


def validate_args(arguments: argparse.Namespace):
    """Validate the console arguments"""
    if (arguments.bpm < MIN_BPM) or (arguments.bpm > MAX_BPM):
        logging.error("Please set a BPM value between %s and %s", MIN_BPM, MAX_BPM)
        sys.exit()


def main():
    """Run the metronome"""
    parser = get_arg_parser()
    args = parser.parse_args()
    validate_args(args)

    logging.basicConfig(level=LOG_LEVEL)

    deps = ["sox", "mpv"]
    for dep in deps:
        ensure_dep_exists(dep)

    back_pad_time = 60 / args.bpm - BEAT_TIME

    weak_note_file = note_file(args.weak, BEAT_TIME, back_pad_time)
    strong_note_file = note_file(args.strong, BEAT_TIME, back_pad_time)

    beats_list = beat_info_list(strong_note_file, weak_note_file, args.beats)
    beats_str = " ".join(x[0] for x in beats_list)

    create_subtitles(beats_list)

    cmd = (
        f"mpv {beats_str} --loop-playlist=inf --force-window --no-osc"
        f" --sub-pos={BEAT_TEXT_POSITION} --sub-scale={BEAT_TEXT_SIZE} --really-quiet"
    )

    subprocess.run(cmd, shell=True, check=True)


def ensure_dep_exists(program: str):
    """Check if program exists. If not exists, exit the application"""
    cmd = f"command -v {program}"
    try:
        subprocess.run(cmd, shell=True, capture_output=True, check=True)
    except subprocess.CalledProcessError:
        logging.error("Please install %s to use the metronome", program)
        sys.exit()


def create_subtitles(path_n_name_list: list):
    """Generate the beat text"""
    for path_n_name in path_n_name_list:
        srt_file_name = Path(path_n_name[0]).with_suffix(".srt")
        with open(srt_file_name, "w", encoding="utf-8") as file:
            file.write(f"1\n00:00:0,001 --> 00:00:1,0\n{path_n_name[1]}")


def beat_info_list(strong: str, weak: str, num_of_beats: int) -> list:
    """Generate the list of (file, name) tuples for each beat"""
    beats = []

    for i in range(num_of_beats):
        file_name = f"{TMP_FILE_DIR}/{i}.wav"

        if i == 0:
            beats.append((file_name, "*"))
            shutil.copy(strong, file_name)
        else:
            beats.append((file_name, "."))
            shutil.copy(weak, file_name)

    return beats


def note_file(note: int, synth_time: int, back_pad_time: int) -> str:
    """Generate the note file that should be played"""
    file_name = f"/{TMP_FILE_DIR}/{note}_{synth_time}.wav"
    cmd = f"sox -nq {file_name} synth {synth_time} sine {note} pad 0 {back_pad_time}"

    subprocess.run(cmd, shell=True, check=True)

    return file_name


if __name__ == "__main__":
    main()
