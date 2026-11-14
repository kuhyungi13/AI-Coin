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
| s01 | 8.0 s | bank exterior + parking lot | top-down, 12 m up, slow push in | one mannequin walks from lot to door |
| s02 | 8.5 s | pizza shop → road → tower site | high 3/4, slow pan across a map-like flat set | mannequin at counter, then a car shape sliding along the road |
| s03 | 11.5 s | forest clearing, TV tower in silhouette | wide, low, camera static and far away | two mannequins face each other; the taller one steps behind the first, then both freeze — cut |
| s04 | 11.0 s | bank interior, ceiling removed (dollhouse cut-away) | straight down, 8 m, slow rotate | mannequin walks a straight line to the counter, teller mannequin behind it |
| s05 | 7.5 s | parking lot | top-down, 15 m, static | mannequin sits on the asphalt; 4 car shapes close into a ring around it |
| s06 | 7.5 s | same as s05 | camera rises straight up, away from the mannequin | at 5.0 s the frame goes to full black; audio only for the last 2.5 s |
| s07 | 11.5 s | evidence board, flat on a table | straight down on the board | silhouette cards connected by lines; lines draw in one by one |
| s08 | 17.5 s | courtroom, cut-away | high 3/4 from behind the bench | one mannequin standing, two seated; hold, almost no motion |
| s09 | 9.0 s | empty parking lot, no mannequins | the s01 top-down camera, pulling slowly back | empty frame; the set slowly fades to black |

## Assembly
Blender's Video Sequence Editor (VSE) works fine for this — no other editor needed:
1. New scene → Video Editing workspace.
2. Add the 9 image sequences in order on channel 1.
3. Add the 9 `.wav` narration files on channel 2, aligned to each shot's start.
4. Add `ep01/ep01_en.srt` as a Text strip set — or burn subtitles in afterwards
   with `ffmpeg -i video.mp4 -vf subtitles=ep01_en.srt out.mp4`.
5. Output: H.264, MP4, 1080×1920, 24 fps.

The shot lengths above match the per-scene audio targets in `narration_en.md`,
so the audio and the picture line up if each shot is rendered at its stated length.
