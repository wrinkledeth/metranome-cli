
# metranome-cli

A Python script that offers a simple metronome for music practice. It makes use of [sox](https://sox.sourceforge.net) and [mpv](https://mpv.io/).

## CLI Arguments

```bash
--bpm # set the beats per minute, default is 80
--beats # number of beats per bar, default is 4
--strong # Note of the strong beat in hertz, default is 4000
--weak # note of the weak beats in hertz, detault is 2000
```

## Examples 

```bash
# 120bpm with 6 beats per measure
python simple_metronome.py --bpm 120 --beats 6

# Sample Alias to set BPM, play uniform sounds, and hide video.
alias m="python3 ./metranome/simple_metranome.py --no-video --strong 1200 --weak 1200 --bpm"
m 80 # trigger alias
```

## Credits

Forked from [dimkard](https://codeberg.org/dimkard/simple-metronome/src/branch/main/README.md)