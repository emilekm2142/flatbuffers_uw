# automatically generated by the FlatBuffers compiler, do not modify

# namespace: AllWatchSerialize

import flatbuffers

class ListData(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsListData(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ListData()
        x.Init(buf, n + offset)
        return x

    # ListData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ListData
    def UseCustomTemplate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0

    # ListData
    def CustomContent(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .Template import Template
            obj = Template()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ListData
    def CustomContentLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ListData
    def SimpleEntries(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .SimpleListEntry import SimpleListEntry
            obj = SimpleListEntry()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ListData
    def SimpleEntriesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def ListDataStart(builder): builder.StartObject(3)
def ListDataAddUseCustomTemplate(builder, useCustomTemplate): builder.PrependBoolSlot(0, useCustomTemplate, 0)
def ListDataAddCustomContent(builder, customContent): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(customContent), 0)
def ListDataStartCustomContentVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ListDataAddSimpleEntries(builder, simpleEntries): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(simpleEntries), 0)
def ListDataStartSimpleEntriesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ListDataEnd(builder): return builder.EndObject()