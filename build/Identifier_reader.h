#ifndef IDENTIFIER_READER_H
#define IDENTIFIER_READER_H

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


typedef const struct AllWatchSerialize_Identifier_table *AllWatchSerialize_Identifier_table_t;
typedef const flatbuffers_uoffset_t *AllWatchSerialize_Identifier_vec_t;
typedef flatbuffers_uoffset_t *AllWatchSerialize_Identifier_mutable_vec_t;
#ifndef AllWatchSerialize_Identifier_identifier
#define AllWatchSerialize_Identifier_identifier flatbuffers_identifier
#endif
#define AllWatchSerialize_Identifier_type_hash ((flatbuffers_thash_t)0xb03cc80c)
#define AllWatchSerialize_Identifier_type_identifier "\x0c\xc8\x3c\xb0"



struct AllWatchSerialize_Identifier_table { uint8_t unused__; };

static inline size_t AllWatchSerialize_Identifier_vec_len(AllWatchSerialize_Identifier_vec_t vec)
__flatbuffers_vec_len(vec)
static inline AllWatchSerialize_Identifier_table_t AllWatchSerialize_Identifier_vec_at(AllWatchSerialize_Identifier_vec_t vec, size_t i)
__flatbuffers_offset_vec_at(AllWatchSerialize_Identifier_table_t, vec, i, 0)
__flatbuffers_table_as_root(AllWatchSerialize_Identifier)

__flatbuffers_define_string_field(0, AllWatchSerialize_Identifier, packageName, 0)
__flatbuffers_define_find_by_string_field(AllWatchSerialize_Identifier, packageName)
__flatbuffers_define_sort_by_string_field(AllWatchSerialize_Identifier, packageName)
__flatbuffers_define_default_find_by_string_field(AllWatchSerialize_Identifier, packageName)
__flatbuffers_define_default_scan_by_string_field(AllWatchSerialize_Identifier, packageName)
#define AllWatchSerialize_Identifier_vec_sort AllWatchSerialize_Identifier_vec_sort_by_packageName
__flatbuffers_define_string_field(1, AllWatchSerialize_Identifier, friendlyName, 0)

#include "flatcc/flatcc_epilogue.h"
#endif /* IDENTIFIER_READER_H */
