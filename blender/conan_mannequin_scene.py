"""
CASE FILE - Blender base scene (Detective Conan "culprit silhouette" look)

Run on your own machine:
  blender --python conan_mannequin_scene.py            # opens GUI with the scene
  blender -b --python conan_mannequin_scene.py -- --render out/frame_  # headless still

Look: pitch-black room, black mannequins with a thin blue-grey rim light,
optional white eye slits + grin, high third-person camera.
Written for Blender 3.6 - 4.x. Untested here (no Blender in the cloud box), tweak freely.
"""
import sys
import bpy
import math
from mathutils import Vector

# ------------------------------------------------------------------ settings
RIM_COLOR = (0.30, 0.45, 0.65, 1.0)   # blue-grey edge glow, like the reference
RIM_STRENGTH = 3.0
FPS = 24
RES = (1080, 1920)                    # vertical shorts; use (1920, 1080) for long-form
SAMPLES = 64


def reset_scene():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    sc.render.fps = FPS
    sc.render.resolution_x, sc.render.resolution_y = RES
    for name in ("BLENDER_EEVEE_NEXT", "BLENDER_EEVEE"):
        try:
            sc.render.engine = name
            break
        except TypeError:
            continue
    try:
        sc.eevee.taa_render_samples = SAMPLES
    except AttributeError:
        pass
    # black world
    w = bpy.data.worlds.new("World")
    w.use_nodes = True
    w.node_tree.nodes["Background"].inputs[0].default_value = (0, 0, 0, 1)
    sc.world = w
    # thin dark outline (Freestyle) for the anime feel
    sc.render.use_freestyle = True
    sc.render.line_thickness = 1.2
    return sc


def mannequin_material(name="MannequinBlack"):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    base = nt.nodes.new("ShaderNodeBsdfDiffuse")
    base.inputs["Color"].default_value = (0.005, 0.008, 0.012, 1)
    rim = nt.nodes.new("ShaderNodeEmission")
    rim.inputs["Color"].default_value = RIM_COLOR
    rim.inputs["Strength"].default_value = RIM_STRENGTH
    lw = nt.nodes.new("ShaderNodeLayerWeight")
    lw.inputs["Blend"].default_value = 0.7          # smaller = thinner rim
    ramp = nt.nodes.new("ShaderNodeMath")
    ramp.operation = "POWER"
    ramp.inputs[1].default_value = 3.0
    mix = nt.nodes.new("ShaderNodeMixShader")
    nt.links.new(lw.outputs["Facing"], ramp.inputs[0])
    nt.links.new(ramp.outputs[0], mix.inputs[0])
    # Facing = 1 at silhouette edge -> emission there
    nt.links.new(base.outputs[0], mix.inputs[1])
    nt.links.new(rim.outputs[0], mix.inputs[2])
    nt.links.new(mix.outputs[0], out.inputs[0])
    return m


def white_material():
    m = bpy.data.materials.new("EyeWhite")
    m.use_nodes = True
    nt = m.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    em = nt.nodes.new("ShaderNodeEmission")
    em.inputs["Strength"].default_value = 6
    nt.links.new(em.outputs[0], out.inputs[0])
    return m


def _add(kind, name, loc, scale, mat, parent=None, rot=(0, 0, 0)):
    if kind == "sphere":
        bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16)
    else:
        bpy.ops.mesh.primitive_cylinder_add(vertices=24)
    o = bpy.context.object
    o.name = name
    o.location = loc
    o.scale = scale
    o.rotation_euler = rot
    o.data.materials.append(mat)
    bpy.ops.object.shade_smooth()
    if parent:
        o.parent = parent
    return o


def make_mannequin(name="Mannequin", pos=(0, 0, 0), face=True, yaw=0.0):
    """Faceless black mannequin built from primitives, ~1.75 m tall."""
    mat = mannequin_material()
    root = bpy.data.objects.new(name, None)
    bpy.context.collection.objects.link(root)
    root.location = pos
    root.rotation_euler = (0, 0, yaw)

    _add("sphere", f"{name}_head", (0, 0, 1.62), (0.11, 0.12, 0.14), mat, root)
    _add("cyl", f"{name}_neck", (0, 0, 1.46), (0.04, 0.04, 0.06), mat, root)
    _add("sphere", f"{name}_torso", (0, 0, 1.20), (0.19, 0.11, 0.30), mat, root)
    _add("sphere", f"{name}_hips", (0, 0, 0.90), (0.16, 0.10, 0.14), mat, root)
    for s, x in (("L", 0.25), ("R", -0.25)):
        _add("cyl", f"{name}_arm{s}", (x, 0, 1.18), (0.04, 0.04, 0.28), mat, root,
             rot=(0, math.radians(-8 if s == "L" else 8), 0))
        _add("cyl", f"{name}_leg{s}", (x * 0.45, 0, 0.45), (0.07, 0.07, 0.45), mat, root)

    if face:  # white eye slits + grin, the Conan "culprit" look
        wm = white_material()
        for x in (-0.05, 0.05):
            _add("sphere", f"{name}_eye", (x, -0.10, 1.64), (0.030, 0.012, 0.018), wm, root,
                 rot=(0, math.radians(12 if x > 0 else -12), 0))
        _add("sphere", f"{name}_grin", (0, -0.105, 1.57), (0.05, 0.010, 0.012), wm, root)
    return root


def add_set(sc):
    """Dark floor + a simple counter so the rim light has something to catch."""
    mat = mannequin_material("SetBlack")
    bpy.ops.mesh.primitive_plane_add(size=30)
    bpy.context.object.data.materials.append(mat)
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 3, 0.55))
    c = bpy.context.object
    c.scale = (3, 0.4, 0.55)
    c.data.materials.append(mat)


def add_lights():
    # cold back/rim lights give the blue-grey edge; keep fill ~0
    for loc in ((-4, 4, 4), (4, 4, 4)):
        bpy.ops.object.light_add(type="AREA", location=loc)
        L = bpy.context.object
        L.data.energy = 300
        L.data.color = RIM_COLOR[:3]
        L.rotation_euler = (math.radians(60), 0, math.radians(180 if loc[0] > 0 else 0))


def add_camera(sc, loc=(0, -7, 8), target=(0, 1, 1)):
    bpy.ops.object.camera_add(location=loc)
    cam = bpy.context.object
    d = Vector(target) - Vector(loc)
    cam.rotation_euler = d.to_track_quat("-Z", "Y").to_euler()
    cam.data.lens = 35
    sc.camera = cam
    return cam


def walk_to(obj, start, end, f0=1, f1=96):
    """Simple slide + bob; replace with a proper walk cycle later."""
    for f, p in ((f0, start), (f1, end)):
        obj.location = p
        obj.keyframe_insert("location", frame=f)
    sc = bpy.context.scene
    sc.frame_start, sc.frame_end = f0, f1


def main():
    sc = reset_scene()
    add_set(sc)
    add_lights()
    add_camera(sc)
    m = make_mannequin("Delivery", pos=(0, -2, 0), face=True)
    walk_to(m, (0, -2, 0), (0, 1.5, 0))
    # headless still: blender -b --python this.py -- --render out/frame_
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    if "--render" in argv:
        sc.render.filepath = argv[argv.index("--render") + 1]
        bpy.ops.render.render(animation=True)


main()
