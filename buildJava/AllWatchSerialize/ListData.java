// automatically generated by the FlatBuffers compiler, do not modify

package AllWatchSerialize;

import java.nio.*;
import java.lang.*;
import java.util.*;
import com.google.flatbuffers.*;

@SuppressWarnings("unused")
public final class ListData extends Table {
  public static ListData getRootAsListData(ByteBuffer _bb) { return getRootAsListData(_bb, new ListData()); }
  public static ListData getRootAsListData(ByteBuffer _bb, ListData obj) { _bb.order(ByteOrder.LITTLE_ENDIAN); return (obj.__assign(_bb.getInt(_bb.position()) + _bb.position(), _bb)); }
  public void __init(int _i, ByteBuffer _bb) { bb_pos = _i; bb = _bb; }
  public ListData __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }

  public boolean useCustomTemplate() { int o = __offset(4); return o != 0 ? 0!=bb.get(o + bb_pos) : false; }
  public Template customContent(int j) { return customContent(new Template(), j); }
  public Template customContent(Template obj, int j) { int o = __offset(6); return o != 0 ? obj.__assign(__indirect(__vector(o) + j * 4), bb) : null; }
  public int customContentLength() { int o = __offset(6); return o != 0 ? __vector_len(o) : 0; }
  public SimpleListEntry simpleEntries(int j) { return simpleEntries(new SimpleListEntry(), j); }
  public SimpleListEntry simpleEntries(SimpleListEntry obj, int j) { int o = __offset(8); return o != 0 ? obj.__assign(__indirect(__vector(o) + j * 4), bb) : null; }
  public int simpleEntriesLength() { int o = __offset(8); return o != 0 ? __vector_len(o) : 0; }

  public static int createListData(FlatBufferBuilder builder,
      boolean useCustomTemplate,
      int customContentOffset,
      int simpleEntriesOffset) {
    builder.startObject(3);
    ListData.addSimpleEntries(builder, simpleEntriesOffset);
    ListData.addCustomContent(builder, customContentOffset);
    ListData.addUseCustomTemplate(builder, useCustomTemplate);
    return ListData.endListData(builder);
  }

  public static void startListData(FlatBufferBuilder builder) { builder.startObject(3); }
  public static void addUseCustomTemplate(FlatBufferBuilder builder, boolean useCustomTemplate) { builder.addBoolean(0, useCustomTemplate, false); }
  public static void addCustomContent(FlatBufferBuilder builder, int customContentOffset) { builder.addOffset(1, customContentOffset, 0); }
  public static int createCustomContentVector(FlatBufferBuilder builder, int[] data) { builder.startVector(4, data.length, 4); for (int i = data.length - 1; i >= 0; i--) builder.addOffset(data[i]); return builder.endVector(); }
  public static void startCustomContentVector(FlatBufferBuilder builder, int numElems) { builder.startVector(4, numElems, 4); }
  public static void addSimpleEntries(FlatBufferBuilder builder, int simpleEntriesOffset) { builder.addOffset(2, simpleEntriesOffset, 0); }
  public static int createSimpleEntriesVector(FlatBufferBuilder builder, int[] data) { builder.startVector(4, data.length, 4); for (int i = data.length - 1; i >= 0; i--) builder.addOffset(data[i]); return builder.endVector(); }
  public static void startSimpleEntriesVector(FlatBufferBuilder builder, int numElems) { builder.startVector(4, numElems, 4); }
  public static int endListData(FlatBufferBuilder builder) {
    int o = builder.endObject();
    return o;
  }
}
