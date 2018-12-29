# automatically generated by the FlatBuffers compiler, do not modify

# namespace: AllWatchSerialize

import flatbuffers

class DataBinding(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsDataBinding(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = DataBinding()
        x.Init(buf, n + offset)
        return x

    # DataBinding
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # DataBinding
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

    # DataBinding
    def Bindings(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .PropertyBinding import PropertyBinding
            obj = PropertyBinding()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # DataBinding
    def BindingsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def DataBindingStart(builder): builder.StartObject(2)
def DataBindingAddId(builder, id): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(id), 0)
def DataBindingAddBindings(builder, bindings): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(bindings), 0)
def DataBindingStartBindingsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def DataBindingEnd(builder): return builder.EndObject()
