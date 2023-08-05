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


class TextFormatter(object):
    flat = True

    def document(self, doc, output):
        self.layer(doc.flattened(), output)

    def layer(self, layer, output):
        if isinstance(layer, tree.Layer):
            output.write(layer.text)
        elif isinstance(layer, tree.FreeColorLayer):
            for y in six.moves.range(layer.height):
                for x in six.moves.range(layer.width):
                    char, color = layer.matrix.get((x, y), (" ", None))
                    output.write(char)
                output.write("\n")
        else:
            raise TypeError("Expected layer type")

    def color(self, color):
        return ""


factory.register(TextFormatter(), "txt")
