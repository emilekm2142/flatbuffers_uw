#ifndef BACKGROUND_READER_H
#define BACKGROUND_READER_H

/* Generated by flatcc 0.5.2 FlatBuffers schema compiler for C by dvide.com */

#ifndef FLATBUFFERS_COMMON_READER_H
#include "flatbuffers_common_reader.h"
#endif
#include "flatcc/flatcc_flatbuffers.h"
#ifndef __alignas_is_defined
#include <stdalign.h>
#endif
#include "flatcc/flatcc_prologue.h"
#ifndef flatbuffers_identifier
#define flatbuffers_identifier 0
#endif
#ifndef flatbuffers_extension
#define flatbuffers_extension ".bin"
#endif


typedef const struct AllWatchSerialize_Background_table *AllWatchSerialize_Background_table_t;
typedef const flatbuffers_uoffset_t *AllWatchSerialize_Background_vec_t;
typedef flatbuffers_uoffset_t *AllWatchSerialize_Background_mutable_vec_t;
#ifndef AllWatchSerialize_Background_identifier
#define AllWatchSerialize_Background_identifier flatbuffers_identifier
#endif
#define AllWatchSerialize_Background_type_hash ((flatbuffers_thash_t)0xe07f766b)
#define AllWatchSerialize_Background_type_identifier "\x6b\x76\x7f\xe0"



struct AllWatchSerialize_Background_table { uint8_t unused__; };

static inline size_t AllWatchSerialize_Background_vec_len(AllWatchSerialize_Background_vec_t vec)
__flatbuffers_vec_len(vec)
static inline AllWatchSerialize_Background_table_t AllWatchSerialize_Background_vec_at(AllWatchSerialize_Background_vec_t vec, size_t i)
__flatbuffers_offset_vec_at(AllWatchSerialize_Background_table_t, vec, i, 0)
__flatbuffers_table_as_root(AllWatchSerialize_Background)

__flatbuffers_define_scalar_field(0, AllWatchSerialize_Background, backgroundColor, flatbuffers_int32, int32_t, INT32_C(0))
__flatbuffers_define_vector_field(1, AllWatchSerialize_Background, backgroundImage, flatbuffers_uint8_vec_t, 0)

#include "flatcc/flatcc_epilogue.h"
#endif /* BACKGROUND_READER_H */
