# TypeOxidizer

TypeOxidizer is a Binary Ninja plugin that seamlessly transforms the C-Style types in your HLIL / decompilation to their Rust equivalents, making for a cleaner and more precise decompilation. With built-in support for standard integer and floating-point types, TypeOxidizer redefines your analysis by "oxidizing" legacy type definitions into Rust's clean and precise syntax.

The following types are currently handled automatically:

| C Type     | Rust Type |
|------------|-----------|
| `uint8_t`  | `u8`      |
| `uint16_t` | `u16`     |
| `uint32_t` | `u32`     |
| `uint64_t` | `u64`     |
| `int8_t`   | `i8`      |
| `int16_t`  | `i16`     |
| `int32_t`  | `i32`     |
| `int64_t`  | `i64`     |
| `float`    | `f32`     |
| `double`   | `f64`     |
| `size_t`   | `usize`   |
| `ssize_t`  | `isize`   |

## Usage

First the plugin must be installed. This can be done by copying the `type_oxidizer.py` file into the plugins directory, which can be found by clicking on "Plugins" -> "Open Plugin Folder", and then restarting Binary Ninja. You will now have access to the registered commands via the plugins menu, as well as the command pallette with CMD+P.
