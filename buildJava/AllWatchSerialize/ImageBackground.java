// automatically generated by the FlatBuffers compiler, do not modify

package AllWatchSerialize;

import java.nio.*;
import java.lang.*;
import java.util.*;
import com.google.flatbuffers.*;

@SuppressWarnings("unused")
public final class ImageBackground extends Table {
  public static ImageBackground getRootAsImageBackground(ByteBuffer _bb) { return getRootAsImageBackground(_bb, new ImageBackground()); }
  public static ImageBackground getRootAsImageBackground(ByteBuffer _bb, ImageBackground obj) { _bb.order(ByteOrder.LITTLE_ENDIAN); return (obj.__assign(_bb.getInt(_bb.position()) + _bb.position(), _bb)); }
  public void __init(int _i, ByteBuffer _bb) { bb_pos = _i; bb = _bb; }
  public ImageBackground __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }

  public byte image(int j) { int o = __offset(4); return o != 0 ? bb.get(__vector(o) + j * 1) : 0; }
  public int imageLength() { int o = __offset(4); return o != 0 ? __vector_len(o) : 0; }
  public ByteBuffer imageAsByteBuffer() { return __vector_as_bytebuffer(4, 1); }
  public ByteBuffer imageInByteBuffer(ByteBuffer _bb) { return __vector_in_bytebuffer(_bb, 4, 1); }

  public static int createImageBackground(FlatBufferBuilder builder,
      int imageOffset) {
    builder.startObject(1);
    ImageBackground.addImage(builder, imageOffset);
    return ImageBackground.endImageBackground(builder);
  }

  public static void startImageBackground(FlatBufferBuilder builder) { builder.startObject(1); }
  public static void addImage(FlatBufferBuilder builder, int imageOffset) { builder.addOffset(0, imageOffset, 0); }
  public static int createImageVector(FlatBufferBuilder builder, byte[] data) { builder.startVector(1, data.length, 1); for (int i = data.length - 1; i >= 0; i--) builder.addByte(data[i]); return builder.endVector(); }
  public static void startImageVector(FlatBufferBuilder builder, int numElems) { builder.startVector(1, numElems, 1); }
  public static int endImageBackground(FlatBufferBuilder builder) {
    int o = builder.endObject();
    return o;
  }
}

