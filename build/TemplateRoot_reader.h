#ifndef TEMPLATEROOT_READER_H
#define TEMPLATEROOT_READER_H

/* Generated by flatcc 0.5.2 FlatBuffers schema compiler for C by dvide.com */

#ifndef FLATBUFFERS_COMMON_READER_H
#include "flatbuffers_common_reader.h"
#endif
#ifndef DATABINDING_READER_H
#include "DataBinding_reader.h"
#endif
#ifndef EXTRAS_READER_H
#include "Extras_reader.h"
#endif
#ifndef TEMPLATE_READER_H
#include "Template_reader.h"
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


typedef const struct AllWatchSerialize_TemplateRoot_table *AllWatchSerialize_TemplateRoot_table_t;
typedef const flatbuffers_uoffset_t *AllWatchSerialize_TemplateRoot_vec_t;
typedef flatbuffers_uoffset_t *AllWatchSerialize_TemplateRoot_mutable_vec_t;
#ifndef AllWatchSerialize_TemplateRoot_identifier
#define AllWatchSerialize_TemplateRoot_identifier flatbuffers_identifier
#endif
#define AllWatchSerialize_TemplateRoot_type_hash ((flatbuffers_thash_t)0x6ab2b525)
#define AllWatchSerialize_TemplateRoot_type_identifier "\x25\xb5\xb2\x6a"



struct AllWatchSerialize_TemplateRoot_table { uint8_t unused__; };

static inline size_t AllWatchSerialize_TemplateRoot_vec_len(AllWatchSerialize_TemplateRoot_vec_t vec)
__flatbuffers_vec_len(vec)
static inline AllWatchSerialize_TemplateRoot_table_t AllWatchSerialize_TemplateRoot_vec_at(AllWatchSerialize_TemplateRoot_vec_t vec, size_t i)
__flatbuffers_offset_vec_at(AllWatchSerialize_TemplateRoot_table_t, vec, i, 0)
__flatbuffers_table_as_root(AllWatchSerialize_TemplateRoot)

__flatbuffers_define_string_field(0, AllWatchSerialize_TemplateRoot, name, 0)
__flatbuffers_define_table_field(1, AllWatchSerialize_TemplateRoot, layout, AllWatchSerialize_Template_table_t, 0)
__flatbuffers_define_vector_field(2, AllWatchSerialize_TemplateRoot, dataBindings, AllWatchSerialize_DataBinding_vec_t, 0)

#include "flatcc/flatcc_epilogue.h"
#endif /* TEMPLATEROOT_READER_H */
