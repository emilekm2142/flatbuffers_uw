#ifndef PROFILE_READER_H
#define PROFILE_READER_H

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


typedef const struct AllWatchSerialize_Profile_table *AllWatchSerialize_Profile_table_t;
typedef const flatbuffers_uoffset_t *AllWatchSerialize_Profile_vec_t;
typedef flatbuffers_uoffset_t *AllWatchSerialize_Profile_mutable_vec_t;
#ifndef AllWatchSerialize_Profile_identifier
#define AllWatchSerialize_Profile_identifier flatbuffers_identifier
#endif
#define AllWatchSerialize_Profile_type_hash ((flatbuffers_thash_t)0x18ea5a38)
#define AllWatchSerialize_Profile_type_identifier "\x38\x5a\xea\x18"



struct AllWatchSerialize_Profile_table { uint8_t unused__; };

static inline size_t AllWatchSerialize_Profile_vec_len(AllWatchSerialize_Profile_vec_t vec)
__flatbuffers_vec_len(vec)
static inline AllWatchSerialize_Profile_table_t AllWatchSerialize_Profile_vec_at(AllWatchSerialize_Profile_vec_t vec, size_t i)
__flatbuffers_offset_vec_at(AllWatchSerialize_Profile_table_t, vec, i, 0)
__flatbuffers_table_as_root(AllWatchSerialize_Profile)

__flatbuffers_define_string_field(0, AllWatchSerialize_Profile, name, 0)
__flatbuffers_define_vector_field(1, AllWatchSerialize_Profile, image, flatbuffers_uint8_vec_t, 0)

#include "flatcc/flatcc_epilogue.h"
#endif /* PROFILE_READER_H */