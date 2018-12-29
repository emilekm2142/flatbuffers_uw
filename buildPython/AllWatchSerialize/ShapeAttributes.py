# automatically generated by the FlatBuffers compiler, do not modify

# namespace: AllWatchSerialize

import flatbuffers

class ShapeAttributes(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsShapeAttributes(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ShapeAttributes()
        x.Init(buf, n + offset)
        return x

    # ShapeAttributes
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ShapeAttributes
    def Type(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 0

    # ShapeAttributes
    def Fill(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0

def ShapeAttributesStart(builder): builder.StartObject(2)
def ShapeAttributesAddType(builder, type): builder.PrependInt16Slot(0, type, 0)
def ShapeAttributesAddFill(builder, fill): builder.PrependBoolSlot(1, fill, 0)
def ShapeAttributesEnd(builder): return builder.EndObject()