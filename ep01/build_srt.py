"""
Build ep01_en.srt and timing.json from narration_en.md + the dubbed audio.

    python ep01/build_srt.py            # uses ep01/audio/sNN.wav when present,
                                        # otherwise the target lengths in the table
    python ep01/build_srt.py --check    # only print the timing table

How timing works
- Each shot lasts (its wav length + PAD seconds). Shots play back to back, so
  shot N starts where shot N-1 ends. Blender renders each shot at that length
  (timing.json gives the frame counts), so picture, audio and subtitles share
  one clock.
- Inside a shot, the narration starts at 0 and the cues split the wav length in
  proportion to their character count. Calm TTS reads at a steady pace, so this
  lands within a few tenths of a second. Nudge by hand only if a cue is visibly off.

Only the standard library is used (wave, json, re), so it runs anywhere.
"""
import json
import re
import sys
import wave
from pathlib import Path

HERE = Path(__file__).resolve().parent
NARRATION = HERE / "narration_en.md"
AUDIO_DIR = HERE / "audio"
SRT_OUT = HERE / "ep01_en.srt"
TIMING_OUT = HERE / "timing.json"

FPS = 24
PAD = 0.5            # silence after each scene's audio, seconds
MAX_LINE = 42        # characters per subtitle line (common subtitle standard)
MIN_CUE = 1.2        # never flash a cue for less than this

# Spoken form (what the TTS reads) -> display form (what the subtitle shows)
DISPLAY = [
    ("about eighty-seven hundred dollars", "about $8,700"),
    ("forty-six", "46"),
    ("forty-five", "45"),
    ("thirty years", "30 years"),
]


def parse_narration(path=NARRATION):
    """Return [(shot, [cue lines]), ...] and {shot: target seconds}."""
    text = path.read_text(encoding="utf-8")
    targets = {m.group(1): float(m.group(2))
               for m in re.finditer(r"`(s\d\d)\.wav`\s*\|\s*([\d.]+)\s*s", text)}
    scenes, cur = [], None
    for line in text.splitlines():
        m = re.match(r"^##\s+(s\d\d)\b", line)
        if m:
            cur = (m.group(1), [])
            scenes.append(cur)
            continue
        if line.startswith("---") or line.startswith("## "):
            cur = None
            continue
        if cur is not None and line.strip():
            cur[1].append(line.strip())
    return scenes, targets


def wav_seconds(path):
    with wave.open(str(path), "rb") as w:
        return w.getnframes() / float(w.getframerate())


def display(s):
    for spoken, shown in DISPLAY:
        s = s.replace(spoken, shown)
    return s


def wrap(s, width=MAX_LINE):
    """Break a cue into at most two balanced lines."""
    if len(s) <= width:
        return s
    words = s.split()
    best, best_cost = s, None
    for i in range(1, len(words)):
        a, b = " ".join(words[:i]), " ".join(words[i:])
        cost = max(len(a), len(b))
        if a[-1] in ",.;:":
            cost -= 6                 # prefer breaking after punctuation
        if words[i - 1][0].isupper() and words[i][0].isupper():
            cost += 12                # don't split a name ("Kenneth / Barnes")
        if best_cost is None or cost < best_cost:
            best, best_cost = a + "\n" + b, cost
    return best


def ts(t):
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def build(audio_dir=AUDIO_DIR):
    scenes, targets = parse_narration()
    shots, cues, t = [], [], 0.0
    for shot, lines in scenes:
        wav = audio_dir / f"{shot}.wav"
        if wav.exists():
            speech, source = wav_seconds(wav), "wav"
        else:
            speech, source = targets[shot], "target"
        length = speech + PAD
        frames = round(length * FPS)
        length = frames / FPS                 # snap to whole frames
        shots.append({"shot": shot, "start": round(t, 3), "length": round(length, 3),
                      "start_frame": round(t * FPS) + 1, "frames": frames,
                      "audio_seconds": round(speech, 3), "audio_source": source})
        total_chars = sum(len(l) for l in lines)
        c = t
        for i, line in enumerate(lines):
            share = speech * len(line) / total_chars
            end = t + speech if i == len(lines) - 1 else c + share
            end = max(end, c + MIN_CUE)
            cues.append((c, end, wrap(display(line))))
            c = end
        t += length
    return shots, cues, t


def main():
    shots, cues, total = build()
    print(f"{'shot':5} {'start':>7} {'length':>7} {'frames':>6}  audio")
    for s in shots:
        print(f"{s['shot']:5} {s['start']:7.2f} {s['length']:7.2f} {s['frames']:6d}  "
              f"{s['audio_seconds']:.2f}s ({s['audio_source']})")
    print(f"total {total:.2f}s = {round(total * FPS)} frames @ {FPS} fps")
    if "--check" in sys.argv:
        return
    srt = "\n".join(f"{i}\n{ts(a)} --> {ts(b)}\n{txt}\n"
                    for i, (a, b, txt) in enumerate(cues, 1))
    SRT_OUT.write_text(srt, encoding="utf-8")
    TIMING_OUT.write_text(json.dumps({"fps": FPS, "pad": PAD, "total_seconds": round(total, 3),
                                      "total_frames": round(total * FPS), "shots": shots},
                                     indent=2) + "\n", encoding="utf-8")
    print(f"wrote {SRT_OUT.name} ({len(cues)} cues) and {TIMING_OUT.name}")


if __name__ == "__main__":
    main()
