# EP.01 — Blender shot list

Base scene: `blender/conan_mannequin_scene.py` (black mannequin, blue rim light,
Freestyle outline, black world). Each shot below reuses that look and only
changes the set, the camera and the blocking.

**Global**
- Resolution 1080×1920 (vertical) · 24 fps · EEVEE
- Camera lens 35 mm unless noted. All shots are third-person, camera above eye level.
- Never show the device in close-up, never show a body. Cut away or go to black.
- Render each shot to its own folder: `out/s01/frame_####.png`, then assemble.

| shot | len | set | camera | blocking |
|---|---|---|---|---|
| s01 | 8.5 s | bank exterior + parking lot | top-down, 12 m up, slow push in | one mannequin walks from lot to door |
| s02 | 8.0 s | pizza shop → road → tower site | high 3/4, slow pan across a map-like flat set | mannequin at counter, then a car shape sliding along the road |
| s03 | 8.5 s | forest clearing, TV tower in silhouette | wide, low, camera static and far away | two mannequins face each other; the taller one steps behind the first, then both freeze — cut |
| s04 | 7.5 s | bank interior, ceiling removed (dollhouse cut-away) | straight down, 8 m, slow rotate | mannequin walks a straight line to the counter, teller mannequin behind it |
| s05 | 7.0 s | parking lot | top-down, 15 m, static | mannequin sits on the asphalt; 4 car shapes close into a ring around it |
| s06 | 8.5 s | same as s05 | camera rises straight up, away from the mannequin | at 4.5 s the frame goes to full black (just before "the device went off"); audio only after that |
| s07 | 8.0 s | evidence board, flat on a table | straight down on the board | silhouette cards connected by lines; lines draw in one by one |
| s08 | 9.5 s | courtroom, cut-away | high 3/4 from behind the bench | one mannequin standing, two seated; hold, almost no motion (Barnes, then Diehl-Armstrong — no third figure) |
| s09 | 10.0 s | empty parking lot, no mannequins | the s01 top-down camera, pulling slowly back | empty frame; the set slowly fades to black |

Lengths above are the **targets** (audio target + 0.5 s), total 75.5 s.
Once the real narration is recorded, run `python ep01/build_srt.py` and render
each shot to the `frames` count in `ep01/timing.json` instead.

## Assembly
`ep01/assemble_vse.py` does steps 1–3 and 5 automatically — see `DUBBING.md`.
By hand:
Blender's Video Sequence Editor (VSE) works fine for this — no other editor needed:
1. New scene → Video Editing workspace.
2. Add the 9 image sequences in order on channel 1.
3. Add the 9 `.wav` narration files on channel 2, aligned to each shot's start.
4. Burn subtitles in afterwards with ffmpeg (styled command in `DUBBING.md`, step 5).
5. Output: H.264, MP4, 1080×1920, 24 fps.

The audio decides the timing: shot length = scene audio + 0.5 s.
