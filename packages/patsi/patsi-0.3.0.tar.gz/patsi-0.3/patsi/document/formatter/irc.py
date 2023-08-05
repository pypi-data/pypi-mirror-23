#
# Copyright (C) 2016-2017 Mattia Basaglia
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
import six

from . import factory
from .. import tree
from .. import color
from .. import palette


class IrcFormatter(object):
    flat = True
    colors = [
        "01", "05", "03", "07", "02", "06", "10", "15",
        "14", "04", "09", "08", "12", "13", "11", "00"
    ]

    def document(self, doc, output):
        self.layer(doc.flattened(), output)

    def layer(self, layer, output):
        if isinstance(layer, tree.Layer):
            for line in layer.text.splitlines(True):
                output.write(self.color(layer.color) + line)
        elif isinstance(layer, tree.FreeColorLayer):
            for y in six.moves.range(layer.height):
                prev_color = None
                for x in six.moves.range(layer.width):
                    char, col = layer.matrix.get((x, y), (" ", color.UnchangedColor))
                    if col is not color.UnchangedColor and col != prev_color:
                        prev_color = col
                        output.write(self.color(col))
                    output.write(char)
                output.write("\n")
        else:
            raise TypeError("Expected layer type")

    def color(self, col):
        if col is None:
            return "\x0f"
        elif isinstance(col, color.IndexedColor):
            if len(col.palette) == 8:
                bright = 8 if getattr(col.palette, "bright", False) else 0
                code = self.colors[col.index + bright]
            elif len(col.palette) == 16:
                code = self.colors[col.index]
            else:
                code = self.colors[col.rgb.to_indexed(palette.colors16).index]
        elif isinstance(col, color.RgbColor):
            code = self.colors[col.to_indexed(palette.colors16).index]
        else:
            raise TypeError("Expected document color")

        return "\x03%s,01" % code


factory.register(IrcFormatter(), "irc")
