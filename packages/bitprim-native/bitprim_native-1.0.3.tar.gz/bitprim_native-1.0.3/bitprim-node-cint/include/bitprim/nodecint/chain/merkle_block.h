/**
 * Copyright (c) 2017 Bitprim developers (see AUTHORS)
 *
 * This file is part of Bitprim.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#ifndef BITPRIM_NODECINT_MERKLE_BLOCK_H_
#define BITPRIM_NODECINT_MERKLE_BLOCK_H_

#include <stdio.h>
#include <stdint.h>

#include <bitprim/nodecint/visibility.h>
#include <bitprim/nodecint/primitives.h>

#ifdef __cplusplus
extern "C" {
#endif

BITPRIM_EXPORT
hash_t merkle_block_hash_nth(merkle_block_t block, size_t n);

BITPRIM_EXPORT
header_t merkle_block_header(merkle_block_t block);

BITPRIM_EXPORT
int merkle_block_is_valid(merkle_block_t block);

BITPRIM_EXPORT
size_t merkle_block_hash_count(merkle_block_t block);

BITPRIM_EXPORT
size_t merkle_block_serialized_size(merkle_block_t block, uint32_t version);

BITPRIM_EXPORT
size_t merkle_block_total_transaction_count(merkle_block_t block);

BITPRIM_EXPORT
void merkle_block_destruct(merkle_block_t block);

BITPRIM_EXPORT
void merkle_block_reset(merkle_block_t block);

#ifdef __cplusplus
} // extern "C"
#endif

#endif /* BITPRIM_NODECINT_MERKLE_BLOCK_H_ */
