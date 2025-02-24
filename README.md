# TypeOxidizer (v1.2)
Author: **azw / austinzwile**

_TypeOxidizer converts the C-Style types in your HLIL / decompilation to their Rust equivalents for easier reading / interpretation and shorter decompilation._

## Description:

TypeOxidizer is a Binary Ninja plugin that seamlessly transforms the C-Style types in your HLIL / decompilation to their Rust equivalents through automatic typedef declaration and retyping, making for a cleaner and more precise decompilation. With built-in support for standard integer and floating-point types as well as strings, TypeOxidizer enhances your analysis by "oxidizing" legacy type definitions into Rust's clean and precise syntax.

## Demo

Here's a nice before:

<img width="1281" alt="image" src="https://github.com/user-attachments/assets/25249368-7de6-4f25-99a9-de3e36a8a121" />

and after:

<img width="944" alt="image" src="https://github.com/user-attachments/assets/789aefae-94e6-4a74-9013-34976d4711f5" />

## Usage

The following registered commands are available via the Plugins dropdown menu as well as the command pallette with `CMD+P`:

 - Convert from C to Rust Types
 - Revert to C Types from Rust

## Features

The conversion from and to following types are currently handled:

| C Type      | Rust Type |
|-------------|-----------|
| `uint8_t`   | `u8`      |
| `uint16_t`  | `u16`     |
| `uint32_t`  | `u32`     |
| `uint64_t`  | `u64`     |
| `uint128_t` | `u128`    |
| `int8_t`    | `i8`      |
| `int16_t`   | `i16`     |
| `int32_t`   | `i32`     |
| `int64_t`   | `i64`     |
| `int128_t`  | `i128`    |
| `float`     | `f32`     |
| `double`    | `f64`     |
| `size_t`    | `usize`   |
| `ssize_t`   | `isize`   |
| `char*`     | `str`     |

## Installation Instructions

### Darwin

Install via the Plugin Manager or by cloning the repo at https://github.com/austinzwile/TypeOxidizer and dropping the folder into your plugins directory.

### Linux

Install via the Plugin Manager or by cloning the repo at https://github.com/austinzwile/TypeOxidizer and dropping the folder into your plugins directory.

### Windows

Install via the Plugin Manager or by cloning the repo at https://github.com/austinzwile/TypeOxidizer and dropping the folder into your plugins directory.

## Minimum Version

This plugin requires the following minimum version of Binary Ninja:

* 3164

## Required Dependencies

The following dependencies are required for this plugin:

## Todo

- [ ] Add proper conversion of types when typecasting. The decompilation currently doesn't allow for the retyping of anything on the right side of an equals sign so I will have to figure that out.
- [ ] Implement a drop-down/content menu to allow for selective conversion between C and Rust.
- [ ] Handle structs and typedefs. The types within already defined type definitions don't get handled right.

## Required Dependencies

The following dependencies are required for this plugin:

## License

This plugin is released under a MIT license.

## Metadata Version

2
