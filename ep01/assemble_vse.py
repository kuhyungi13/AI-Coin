"""
Assemble EP.01 in Blender's Video Sequence Editor and render the final MP4.

    blender -b --python ep01/assemble_vse.py                 # build + render
    blender --python ep01/assemble_vse.py                    # build only, open GUI to check
    blender -b --python ep01/assemble_vse.py -- --no-render  # build + save .blend, no render

Reads ep01/timing.json (written by build_srt.py), then puts on the timeline:
  channel 1  shot image sequences   ep01/out/sNN/frame_0001.png ...
  channel 2  narration              ep01/audio/sNN.wav
Output: ep01/out/ep01_en_nosubs.mp4 (H.264 + AAC, 1080x1920, 24 fps).
Subtitles are burned in afterwards with ffmpeg (see DUBBING.md, step 5), which
handles SRT styling more reliably than VSE text strips.

A missing shot or wav is skipped with a warning, so a partial cut still renders.
Written for Blender 3.6 - 4.x; untested here (no Blender in the cloud box).
"""
import json
import sys
from pathlib import Path

import bpy

HERE = Path(__file__).resolve().parent
TIMING = HERE / "timing.json"
SHOTS_DIR = HERE / "out"
AUDIO_DIR = HERE / "audio"
OUT_FILE = HERE / "out" / "ep01_en_nosubs.mp4"
RES = (1080, 1920)


def main():
    args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    timing = json.loads(TIMING.read_text(encoding="utf-8"))
    fps = timing["fps"]

    sc = bpy.context.scene
    sc.render.fps = fps
    sc.render.resolution_x, sc.render.resolution_y = RES
    sc.render.resolution_percentage = 100
    sc.frame_start = 1
    sc.frame_end = timing["total_frames"]
    sc.sequence_editor_create()
    strips = sc.sequence_editor.sequences
    for s in list(strips):
        strips.remove(s)

    for shot in timing["shots"]:
        name, start, frames = shot["shot"], shot["start_frame"], shot["frames"]
        pngs = sorted((SHOTS_DIR / name).glob("frame_*.png"))
        if pngs:
            img = strips.new_image(name=f"{name}_v", filepath=str(pngs[0]),
                                   channel=1, frame_start=start)
            for p in pngs[1:]:
                img.elements.append(p.name)
            # hold the last frame / trim so the shot is exactly `frames` long
            img.frame_final_duration = frames
            if len(pngs) != frames:
                print(f"[warn] {name}: {len(pngs)} frames rendered, timeline wants {frames}")
        else:
            print(f"[warn] {name}: no frames in {SHOTS_DIR / name}")

        wav = AUDIO_DIR / f"{name}.wav"
        if wav.exists():
            strips.new_sound(name=f"{name}_a", filepath=str(wav),
                             channel=2, frame_start=start)
        else:
            print(f"[warn] {name}: missing {wav}")

    r = sc.render
    r.image_settings.file_format = "FFMPEG"
    r.ffmpeg.format = "MPEG4"
    r.ffmpeg.codec = "H264"
    r.ffmpeg.constant_rate_factor = "HIGH"
    r.ffmpeg.audio_codec = "AAC"
    r.ffmpeg.audio_bitrate = 192
    r.ffmpeg.audio_mixrate = 48000
    r.filepath = str(OUT_FILE)
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    bpy.ops.wm.save_as_mainfile(filepath=str(HERE / "out" / "ep01_edit.blend"))
    if bpy.app.background and "--no-render" not in args:
        bpy.ops.render.render(animation=True)
        print(f"rendered {OUT_FILE}")


main()
