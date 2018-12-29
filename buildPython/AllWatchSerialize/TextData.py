# automatically generated by the FlatBuffers compiler, do not modify

# namespace: AllWatchSerialize

import flatbuffers

class TextData(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsTextData(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TextData()
        x.Init(buf, n + offset)
        return x

    # TextData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TextData
    def Major(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

    # TextData
    def Minor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

    # TextData
    def AdditionalComponents(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .Component import Component
            obj = Component()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # TextData
    def AdditionalComponentsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def TextDataStart(builder): builder.StartObject(3)
def TextDataAddMajor(builder, major): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(major), 0)
def TextDataAddMinor(builder, minor): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(minor), 0)
def TextDataAddAdditionalComponents(builder, additionalComponents): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(additionalComponents), 0)
def TextDataStartAdditionalComponentsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def TextDataEnd(builder): return builder.EndObject()
