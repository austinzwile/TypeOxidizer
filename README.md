# TypeOxidizer
---
TypeOxidizer is a Binary Ninja plugin that seamlessly transforms the C-Style types in your HLIL / decompilation to their Rust equivalents, making for a cleaner and more precise decompilation. With built-in support for standard integer and floating-point types, TypeOxidizer redefines your analysis by "oxidizing" legacy type definitions into Rust's clean and precise syntax. Reverse engineers rejoice - your types just got an upgrade! 🚀

The following types are currently handled automatically:

| C Type     | Rust Type |
|------------|-----------|
| uint8_t    | u8        |
| uint16_t   | u16       |
| uint32_t   | u32       |
| uint64_t   | u64       |
| int8_t     | i8        |
| int16_t    | i16       |
| int32_t    | i32       |
| int64_t    | i64       |
| float      | f32       |
| double     | f64       |
| size_t     | usize     |
| ptrdiff_t  | isize     |

Interestingly, `size_t` and `ptrdiff_t` both get automatically retyped upon reanalysis to `uint64_t` or `int64_t`, so this is something I will have to address at some point to make the typing more precise when using this plugin. I will still leave the conversion in the plugin for now in the event there are some cases which I have yet to see where this doesn't happen.
