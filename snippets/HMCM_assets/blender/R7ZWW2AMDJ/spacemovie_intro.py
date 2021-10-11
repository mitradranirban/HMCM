# OpenShot Video Editor is a program that creates, modifies, and edits video files.
#   Copyright (C) 2009  Jonathan Thomas
#
# This file is part of OpenShot Video Editor (http://launchpad.net/openshot/).
#
# OpenShot Video Editor is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# OpenShot Video Editor is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with OpenShot Video Editor.  If not, see <http://www.gnu.org/licenses/>.


# Import Blender's python API.  This only works when the script is being
# run from the context of Blender.  Blender contains it's own version of Python
# with this library pre-installed.
import bpy
import json


def load_font(font_path):
    """ Load a new TTF font into Blender, and return the font object """
    # get the original list of fonts (before we add a new one)
    original_fonts = bpy.data.fonts.keys()

    # load new font
    bpy.ops.font.open(filepath=font_path)

    # get the new list of fonts (after we added a new one)
    for font_name in bpy.data.fonts.keys():
        if font_name not in original_fonts:
            return bpy.data.fonts[font_name]

    # no new font was added
    return None

# Debug Info:
# ./blender -b test.blend -P demo.py
# -b = background mode
# -P = run a Python script within the context of the project file


# Init all of the variables needed by this script.  Because Blender executes
# this script, OpenShot will inject a dictionary of the required parameters
# before this script is executed.
params = {
    'title': 'Oh Yeah! OpenShot!',
    'Alongtimeago': 'Some cycles ago, in The Grid\nfar, far inside....',
    'Episode': 'Episode I.V',
    'EpisodeTitle': 'A NEW OPENSHOT',
    'TitleSpaceMovie': 'Space\nMovie',
    'MainText': 'It is a period of software war. Free software developers have won some battles with free, and open-source applications. They leave the source code available for everybody in the Galaxy, allowing people to access software knowledge and truth.\n\nBut the EULA Galactic Empire is not dead and prepares its revenge with an ultimate weapon: the blue screen of DEATH. This armored system can anihilate an entire device by a simple segfault.\n\nBut the rebel hackers have a secret weapon too: an atomic penguin which protects them from almost all digital injuries...',

    'extrude': 0.1,
    'bevel_depth': 0.02,
    'spacemode': 'CENTER',
    'text_size': 1.5,
    'width': 1.0,
    'fontname': 'Bfont',

    'color': [0.8, 0.8, 0.8],
    'alpha': 1.0,

    'output_path': '/tmp/',
    'fps': 24,
    'quality': 90,
    'file_format': 'PNG',
    'color_mode': 'RGBA',
    'horizon_color': [0.0, 0.0, 0.0],
    'resolution_x': 1920,
    'resolution_y': 1080,
    'resolution_percentage': 100,
    'start_frame': 1,
    'end_frame': 2232,
    'animation': True,
}


#BEGIN INJECTING PARAMS
params_json = r"""{"file_name": "TitleFileName", "Alongtimeago": "\u0985\u09cd\u09af\u09be\u09a4\u09bf\u09aa\u09cd\u09b0\u09be \u0985\u09cd\u09af\u09be\u09a8\u09bf\u09ae\u09c7\u09b6\u09a8\u09c7\u09b0", "TitleSpaceMovie": "\u09aa\u09cd\u09b0\u09a5\u09ae \u09a8\u09bf\u09ac\u09c7\u09a6\u09a8", "Episode": "\u0995\u09cc\u09a4\u09c1\u09b0 \u0985\u09a8\u09c1\u09a8\u09be\u099f\u09cd\u09af", "EpisodeTitle": "\u09b9\u09c7\u0981\u099a\u09c7 \u09ae\u09b0\u09bf \u0993 \u0995\u09c7\u09b6\u09c7 \u09ae\u09b0\u09bf", "MainText": "\u0995\u09be\u09b9\u09bf\u09a8\u09c0\n\u099a\u09bf\u09a4\u09cd\u09b0\u09a8\u09be\u099f\u09cd\u09af,\n\u0985\u09cd\u09af\u09be\u09a8\u09bf\u09ae\u09c7\u09b6\u09a8,\n\u0995\u09a3\u09cd\u09a0\n\u0985\u09a8\u09bf\u09b0\u09cd\u09ac\u09be\u09a3\n\u09a8\u09bf\u09b0\u09cd\u09ae\u09be\u09a8\u09c7 \u09ac\u09cd\u09af\u09ac\u09b9\u09c3\u09a4 \u09b9\u09df\u09c7\u099b\u09c7 -\n\u098f\u09ae \u0986\u0987 \u099f\u09bf \u09b8\u09cd\u0995\u09cd\u09b0\u09cd\u09af\u09be\u099a\u09cd \n\u0993\u09aa\u09c7\u09a8 \u09b6\u099f\u09cd \u09ad\u09bf\u09a1\u09bf\u0993 \u098f\u09a1\u09bf\u099f\u09b0\n\u09b8\u09bf\u09ae\u09cd\u09aa\u09b2 \u09b8\u09cd\u0995\u09cd\u09b0\u09bf\u09a8 \u09b0\u09c7\u0995\u09b0\u09cd\u09a1\u09be\u09b0\n\u0997\u09bf\u09ae\u09cd\u09aa\n\u0993\u09aa\u09c7\u09a8 \u09ad\u09df\u09c7\u09b8 \u09b0\u09c7\u0995\u09b0\u09cd\u09a1\u09be\u09b0\n\n\u09e8\u09e6\u09e8\u09e7 \u0995\u09cd\u09b0\u09bf\u09df\u09c7\u099f\u09bf\u09ad \u0995\u09ae\u09a8 \u09ac\u09be\u0987 \u098f\u099f\u09cd\u09b0\u09bf\u09ac\u09bf\u0989\u09b6\u09a8 \u09b6\u09c7\u09af\u09be\u09b0 \u098f\u09b2\u09be\u0987\u0995 \u0986\u09a8\u09cd\u09a4\u09b0\u09cd\u099c\u09be\u09a4\u09bf\u0995 \u09b2\u09be\u0987\u09b8\u09c7\u09a8\u09cd\u09b8 \u0985\u09a8\u09c1\u09b8\u09be\u09b0\u09c7 \u09aa\u09cd\u09b0\u09b8\u09be\u09b0\u09bf\u09a4", "start_frame": 1, "end_frame": 2232, "length_multiplier": "1", "fps": 24, "resolution_x": 1280, "resolution_y": 720, "resolution_percentage": 100, "quality": 100, "file_format": "PNG", "color_mode": "RGBA", "alpha_mode": 1, "horizon_color": [0.57, 0.57, 0.57], "animation": true, "output_path": "/home/artim/Videos/HMCM/snippets/HMCM_assets/blender/R7ZWW2AMDJ/TitleFileName"}"""
#END INJECTING PARAMS


# The remainder of this script will modify the current Blender .blend project
# file, and adjust the settings.  The .blend file is specified in the XML file
# that defines this template in OpenShot.
# ----------------------------------------------------------------------------

# Process parameters supplied as JSON serialization
try:
    injected_params = json.loads(params_json)
    params.update(injected_params)
except NameError:
    pass

# Modify Text / Curve settings
#print (bpy.data.curves.keys())
bpy.data.objects['Alongtimeago'].data.body = params['Alongtimeago']
bpy.data.objects['Episode'].data.body = params['Episode']
bpy.data.objects['EpisodeTitle'].data.body = params['EpisodeTitle']
bpy.data.objects['TitleSpaceMovie'].data.body = params['TitleSpaceMovie']
bpy.data.objects['MainText'].data.body = params['MainText']

# Set the render options.  It is important that these are set
# to the same values as the current OpenShot project.  These
# params are automatically set by OpenShot
bpy.context.scene.render.filepath = params["output_path"]
bpy.context.scene.render.fps = params["fps"]
if "fps_base" in params:
    bpy.context.scene.render.fps_base = params["fps_base"]
bpy.context.scene.render.image_settings.file_format = params["file_format"]
bpy.context.scene.render.image_settings.color_mode = params["color_mode"]
bpy.context.scene.render.film_transparent = params["alpha_mode"]
bpy.data.worlds[0].color = params["horizon_color"]
bpy.context.scene.render.resolution_x = params["resolution_x"]
bpy.context.scene.render.resolution_y = params["resolution_y"]
bpy.context.scene.render.resolution_percentage = params["resolution_percentage"]

# Animation Speed (use Blender's time remapping to slow or speed up animation)
length_multiplier = int(params["length_multiplier"])  # time remapping multiplier
new_length = int(params["end_frame"]) * length_multiplier  # new length (in frames)
bpy.context.scene.render.frame_map_old = 1
bpy.context.scene.render.frame_map_new = length_multiplier

# Set render length/position
bpy.context.scene.frame_start = params["start_frame"]
bpy.context.scene.frame_end = new_length
