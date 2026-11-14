# EP.01 — English narration script (TTS input)

**Voice direction:** low, calm, unhurried documentary narrator.
No dramatic rise at the end of sentences. Target pace ≈ 2.5 words/sec.
Audio total ≈ 71 s, finished video ≈ 75 s (each shot = its audio + 0.5 s).

Render each scene as its own audio file so one line can be redone without
re-rendering the whole track. File names match the Blender shot names, and go
in `ep01/audio/` (see `DUBBING.md`).

This file is also the **single source for the subtitles**: every line under a
`## sNN` heading is one subtitle cue, and `build_srt.py` turns them into
`ep01_en.srt`. Edit the words here, never in the `.srt`.

| file | target audio |
|---|---|
| `s01.wav` | 8.0 s |
| `s02.wav` | 7.5 s |
| `s03.wav` | 8.0 s |
| `s04.wav` | 7.0 s |
| `s05.wav` | 6.5 s |
| `s06.wav` | 8.0 s |
| `s07.wav` | 7.5 s |
| `s08.wav` | 9.0 s |
| `s09.wav` | 9.5 s |

---

## s01 — Hook
August 2003. A pizza delivery man walks into a bank in Erie, Pennsylvania,
with a bomb locked around his neck.

## s02 — The order
His name was Brian Wells.
That afternoon, he took an order to an empty TV tower site outside town.

## s03 — The collar
There, a metal collar was locked onto his neck.
He was told to rob a bank and follow a set of written instructions.

## s04 — The robbery
He walked out with about eighty-seven hundred dollars,
and a trail of notes, like a scavenger hunt.

## s05 — Surrounded
Minutes later, police stopped him.
He told them he had been forced. They called the bomb squad.

## s06 — The end (no on-screen violence)
It was still on its way when the device went off, in front of news cameras.
Brian Wells was forty-six.

## s07 — The investigation
The investigation took years.
At its center was Marjorie Diehl-Armstrong,
already tied to the death of a former boyfriend.

## s08 — Sentencing
Accomplice Kenneth Barnes pleaded guilty.
In 2011, Diehl-Armstrong was sentenced to life plus thirty years.
She died in prison in 2017.

## s09 — Closing
Whether Wells was part of the plot or only its victim is still debated.
What we know is that he died waiting for help.

---

## TTS notes
- Numbers are spelled out where TTS engines usually stumble. `build_srt.py`
  turns them back into digits for the subtitles (`eighty-seven hundred dollars`
  → `$8,700`, `forty-six` → `46`, `thirty years` → `30 years`).
- A line break inside a scene is only a subtitle break. Paste each scene into the
  TTS as one paragraph (line breaks joined with a space).
- "Diehl-Armstrong" is commonly read as **DEEL-Armstrong**. If the engine mangles
  it, feed it `Deel Armstrong` — the subtitle still comes from this file.
- Keep one consistent voice across all episodes — it becomes the channel's signature.

## What changed from the first draft (and why)
- **Shorter: 96 s → ~75 s.** The series format targets 60–90 s for shorts;
  this leaves margin for the 0.5 s gaps and a title card. Cut William
  Rothstein (a third name the viewer can't hold onto in a short) and the
  duplicate "waiting for someone to save him" line.
- **Facts corrected** (checked against Wikipedia "Pizza bomber" and CBS News, Feb 2011):
  - Diehl-Armstrong was sentenced in **2011 to life plus 30 years**, not 45 years in 2010.
    The 45 years was **Barnes's** sentence (pleaded guilty 2008, later reduced
    after he testified), so the script now just says he pleaded guilty.
  - Wells told police he was forced **while handcuffed at the scene**, not "later".
  - The bomb went off **before the bomb squad arrived**, in front of news cameras.
  - Added the city (Erie) and the amount stays "about $8,700" (actual $8,702).
