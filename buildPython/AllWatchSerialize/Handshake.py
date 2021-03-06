# automatically generated by the FlatBuffers compiler, do not modify

# namespace: AllWatchSerialize

import flatbuffers

class Handshake(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsHandshake(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Handshake()
        x.Init(buf, n + offset)
        return x

    # Handshake
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Handshake
    def Manufacturer(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

    # Handshake
    def ModelName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

    # Handshake
    def ExtraModelInfo(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

    # Handshake
    def FirmwareVersion(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

    # Handshake
    def BufferKbSize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 0

    # Handshake
    def UsesEncryption(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0

    # Handshake
    def Requirements(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int16Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 2))
        return 0

    # Handshake
    def RequirementsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int16Flags, o)
        return 0

    # Handshake
    def RequirementsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def HandshakeStart(builder): builder.StartObject(7)
def HandshakeAddManufacturer(builder, manufacturer): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(manufacturer), 0)
def HandshakeAddModelName(builder, modelName): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(modelName), 0)
def HandshakeAddExtraModelInfo(builder, extraModelInfo): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(extraModelInfo), 0)
def HandshakeAddFirmwareVersion(builder, firmwareVersion): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(firmwareVersion), 0)
def HandshakeAddBufferKbSize(builder, bufferKbSize): builder.PrependUint16Slot(4, bufferKbSize, 0)
def HandshakeAddUsesEncryption(builder, usesEncryption): builder.PrependBoolSlot(5, usesEncryption, 0)
def HandshakeAddRequirements(builder, requirements): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(requirements), 0)
def HandshakeStartRequirementsVector(builder, numElems): return builder.StartVector(2, numElems, 2)
def HandshakeEnd(builder): return builder.EndObject()
