
# metranome-cli

A Python script that offers a simple metronome for music practice. It makes use of [sox](https://sox.sourceforge.net) and [mpv](https://mpv.io/).

## Usage

Possible options:
* `--bpm`

The beats per minute, e.g., 120. The default is 80.
* `--beats`

The number of beats in a bar, e.g., 6. The default is 4.
* `--strong`
The note of the strong beat, in Hertz. The default is 4000.

* `--weak`
The note of the weak beats, in Hertz. The default is 2000.

## Examples 

```bash
# 120bpm with 6 beats per measure
python simple_metronome.py --bpm 120 --beats 6

# Sample Alias to set BPM, play uniform sounds, and hide video.
alias m="python3 ./metranome/simple_metranome.py --no-video --strong 1200 --weak 1200 --bpm"
m 80 # trigger alias
```

