# Simple Metronome
A Python script that offers a simple metronome for music practice. It makes use of [sox](https://sox.sourceforge.net) and [mpv](https://mpv.io/).

## Usage
These options can be specified:

* `--bpm`

The beats per minute, e.g., 120. The default is 80.

* `--beats`

The number of beats in a bar, e.g., 6. The default is 4.

* `--strong`

The note of the strong beat, in Hertz. The default is 4000.

* `--weak`

The note of the weak beats, in Hertz. The default is 2000.

*Example*

```python simple_metronome.py --bpm 120 --beats 6```

## Sxmo
The metronome comes with a shell script that facilitates its execution on a Linux phone that runs [Sxmo](https://sxmo.org/). Copy: 

* `simple_metronome.py` to `~/.local/share/scripts/`
* `simple-metronome.sh` to `~/.config/sxmo/userscripts/`


# metranome-cli
