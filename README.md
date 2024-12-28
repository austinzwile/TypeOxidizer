# Sample Plugin
Author: austinzwile / azw

_TypeOxidizer is a Binary Ninja plugin that seamlessly transforms the C-Style types in your HLIL / decompilation to their Rust equivalents._

## Description:
This is a longer description meant for a sample plugin that demonstrates the metadata format for Binary Ninja plugins. Note that the [community-plugins repo](https://github.com/Vector35/community-plugins) contains a useful [utility](https://github.com/Vector35/community-plugins/blob/master/generate_plugininfo.py) to validate the plugin.json. Additionally, the [release helper](https://github.com/Vector35/release_helper) plugin is helpful for more easily pushing new releases, incrementing versions, and creating the appropriate GitHub tags.

### Demo

Here's a nice before:

<img width="1281" alt="image" src="https://github.com/user-attachments/assets/25249368-7de6-4f25-99a9-de3e36a8a121" />

and after:

<img width="944" alt="image" src="https://github.com/user-attachments/assets/789aefae-94e6-4a74-9013-34976d4711f5" />

### Usage

First the plugin must be installed. This can be done by copying the `type_oxidizer.py` file into the plugins directory, which can be found by clicking on "Plugins" -> "Open Plugin Folder", and then restarting Binary Ninja. You will now have access to the registered commands via the plugins menu, as well as the command pallette with CMD+P.

The following types are currently handled:

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
| `char**`    | `str*`    |

### Todo

- [ ] Add proper conversion of types when typecasting. The decompilation currently doesn't allow for the retyping of anything on the right side of an equals sign so I will have to figure that out.
- [ ] Implement a drop-down/content menu to allow for selective conversion between C and Rust.
- [ ] Handle structs and typedefs. The types within already defined type definitions don't get handled right.

## License

This plugin is released under an [MIT license](./license).
