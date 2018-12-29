# automatically generated by the FlatBuffers compiler, do not modify

# namespace: AllWatchSerialize

import flatbuffers

class Widget(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsWidget(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Widget()
        x.Init(buf, n + offset)
        return x

    # Widget
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Widget
    def Refresh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # Widget
    def Template(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .TemplateRoot import TemplateRoot
            obj = TemplateRoot()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Widget
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .Id import Id
            obj = Id()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def WidgetStart(builder): builder.StartObject(3)
def WidgetAddRefresh(builder, refresh): builder.PrependInt64Slot(0, refresh, 0)
def WidgetAddTemplate(builder, template): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(template), 0)
def WidgetAddId(builder, id): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(id), 0)
def WidgetEnd(builder): return builder.EndObject()