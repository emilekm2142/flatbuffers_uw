// automatically generated by the FlatBuffers compiler, do not modify

package AllWatchSerialize;

import java.nio.*;
import java.lang.*;
import java.util.*;
import com.google.flatbuffers.*;

@SuppressWarnings("unused")
public final class Open extends Table {
  public static Open getRootAsOpen(ByteBuffer _bb) { return getRootAsOpen(_bb, new Open()); }
  public static Open getRootAsOpen(ByteBuffer _bb, Open obj) { _bb.order(ByteOrder.LITTLE_ENDIAN); return (obj.__assign(_bb.getInt(_bb.position()) + _bb.position(), _bb)); }
  public void __init(int _i, ByteBuffer _bb) { bb_pos = _i; bb = _bb; }
  public Open __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }

  public Id id() { return id(new Id()); }
  public Id id(Id obj) { int o = __offset(4); return o != 0 ? obj.__assign(__indirect(o + bb_pos), bb) : null; }

  public static int createOpen(FlatBufferBuilder builder,
      int idOffset) {
    builder.startObject(1);
    Open.addId(builder, idOffset);
    return Open.endOpen(builder);
  }

  public static void startOpen(FlatBufferBuilder builder) { builder.startObject(1); }
  public static void addId(FlatBufferBuilder builder, int idOffset) { builder.addOffset(0, idOffset, 0); }
  public static int endOpen(FlatBufferBuilder builder) {
    int o = builder.endObject();
    return o;
  }
}

