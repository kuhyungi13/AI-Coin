# EP.01 — English dub, subtitles and final cut

One clock for everything: **the dubbed audio decides the timing**. Shots are
rendered to the audio's length, and the subtitles are generated from the same
numbers, so nothing has to be lined up by eye.

```
narration_en.md ──► Voicestudio ──► audio/s01..s09.wav ──► OpenWhispr check
                                           │
                                           ▼
                               build_srt.py ──► ep01_en.srt + timing.json
                                                         │
                     Blender shots (shotlist.md, frame counts from timing.json)
                                                         │
                                                         ▼
                        assemble_vse.py ──► out/ep01_en_nosubs.mp4 ──► ffmpeg burn-in ──► out/ep01_en.mp4
```

## 1. Dub in Voicestudio
1. Pick the channel voice (low, calm narrator) and keep it for every episode.
   Note the voice name and settings at the bottom of this file once chosen.
2. For each `## sNN` section of `narration_en.md`, paste the scene as **one
   paragraph** (join its lines with spaces) and generate.
3. Export as **WAV, 48 kHz, 16-bit, mono** and save as `ep01/audio/s01.wav` …
   `s09.wav`. Trim leading silence to ~0.1 s; leave trailing silence off
   (the script adds 0.5 s after every scene).
4. Listen for: "Diehl-Armstrong" (DEEL-Armstrong; retype as `Deel Armstrong`
   if wrong), "eighty-seven hundred dollars", "forty-six". Redo only the scene
   that's off.

Target lengths are in the table at the top of `narration_en.md`. ±1 s is fine;
the timing follows whatever the real files are.

## 2. Check the dub with OpenWhispr
OpenWhispr is used as a **proofreader**, not as the timing source: it tells you
whether the TTS said the right words.
1. In OpenWhispr, use the offline Whisper model (English) and transcribe each
   `sNN.wav` (play it into OpenWhispr, or use its file/meeting transcription).
2. Compare the text with the scene in `narration_en.md`. Any word Whisper hears
   differently is a word viewers may hear differently too — regenerate that scene.
3. Names are the usual suspects. A small spelling difference in a name
   (e.g. "Diel Armstrong") is fine if it *sounds* right.

Why not take subtitle timestamps from OpenWhispr? It's built for dictation and
meeting notes, and doesn't export SRT with word timings. The per-scene WAV
lengths already give exact scene boundaries, and within a scene a steady TTS
voice is close enough to proportional that cues land within a few tenths of a
second.

## 3. Generate the subtitles and the timing
```
python ep01/build_srt.py
```
- Reads every `audio/sNN.wav` length (falls back to the target length when a
  file is missing, and says so in the `audio` column).
- Writes `ep01_en.srt` (one cue per line in `narration_en.md`, numbers shown as
  digits, ≤ 42 characters per line, max two lines) and `timing.json`
  (each shot's start frame and frame count at 24 fps).
- Re-run it every time a wav changes. Never hand-edit the `.srt`; edit
  `narration_en.md` and re-run.

## 4. Render the shots in Blender
Use `shotlist.md` for what each shot shows, but take **each shot's length from
`timing.json` (`frames`)**, not from the table, once the real audio exists.
Render to `ep01/out/sNN/frame_####.png` (1080×1920, 24 fps).

## 5. Assemble and burn in subtitles
```
blender -b --python ep01/assemble_vse.py
ffmpeg -i ep01/out/ep01_en_nosubs.mp4 \
  -vf "subtitles=ep01/ep01_en.srt:force_style='FontName=Arial,FontSize=8,Bold=1,Outline=1.5,Shadow=0,MarginV=60,Alignment=2'" \
  -c:a copy ep01/out/ep01_en.mp4
```
- `assemble_vse.py` puts the shots on channel 1 and the wavs on channel 2 at the
  frames in `timing.json`, then renders H.264/AAC.
- The ffmpeg style puts white bold text with a dark outline in the lower third,
  above the Shorts UI buttons. If it sits under the caption bar on your phone,
  raise `MarginV`. FontSize 8 is the largest that keeps a 42-character line on one line in a 1080-wide frame (tested).
- Also upload `ep01_en.srt` as a caption track on YouTube, so viewers can turn
  on translated captions.

## Before upload
- Watch once on a phone with sound off: every subtitle readable before it disappears?
- Re-check the fact list in `../ep01_collar_bomb_script.md`.

## Channel voice (fill in once chosen)
- Voicestudio voice:
- Settings (speed / pitch / stability):
