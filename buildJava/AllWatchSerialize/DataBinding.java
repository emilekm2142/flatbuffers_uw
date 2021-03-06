// automatically generated by the FlatBuffers compiler, do not modify

package AllWatchSerialize;

import java.nio.*;
import java.lang.*;
import java.util.*;
import com.google.flatbuffers.*;

@SuppressWarnings("unused")
public final class DataBinding extends Table {
  public static DataBinding getRootAsDataBinding(ByteBuffer _bb) { return getRootAsDataBinding(_bb, new DataBinding()); }
  public static DataBinding getRootAsDataBinding(ByteBuffer _bb, DataBinding obj) { _bb.order(ByteOrder.LITTLE_ENDIAN); return (obj.__assign(_bb.getInt(_bb.position()) + _bb.position(), _bb)); }
  public void __init(int _i, ByteBuffer _bb) { bb_pos = _i; bb = _bb; }
  public DataBinding __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }

  public String id() { int o = __offset(4); return o != 0 ? __string(o + bb_pos) : null; }
  public ByteBuffer idAsByteBuffer() { return __vector_as_bytebuffer(4, 1); }
  public ByteBuffer idInByteBuffer(ByteBuffer _bb) { return __vector_in_bytebuffer(_bb, 4, 1); }
  public PropertyBinding bindings(int j) { return bindings(new PropertyBinding(), j); }
  public PropertyBinding bindings(PropertyBinding obj, int j) { int o = __offset(6); return o != 0 ? obj.__assign(__indirect(__vector(o) + j * 4), bb) : null; }
  public int bindingsLength() { int o = __offset(6); return o != 0 ? __vector_len(o) : 0; }

  public static int createDataBinding(FlatBufferBuilder builder,
      int idOffset,
      int bindingsOffset) {
    builder.startObject(2);
    DataBinding.addBindings(builder, bindingsOffset);
    DataBinding.addId(builder, idOffset);
    return DataBinding.endDataBinding(builder);
  }

  public static void startDataBinding(FlatBufferBuilder builder) { builder.startObject(2); }
  public static void addId(FlatBufferBuilder builder, int idOffset) { builder.addOffset(0, idOffset, 0); }
  public static void addBindings(FlatBufferBuilder builder, int bindingsOffset) { builder.addOffset(1, bindingsOffset, 0); }
  public static int createBindingsVector(FlatBufferBuilder builder, int[] data) { builder.startVector(4, data.length, 4); for (int i = data.length - 1; i >= 0; i--) builder.addOffset(data[i]); return builder.endVector(); }
  public static void startBindingsVector(FlatBufferBuilder builder, int numElems) { builder.startVector(4, numElems, 4); }
  public static int endDataBinding(FlatBufferBuilder builder) {
    int o = builder.endObject();
    return o;
  }
}

