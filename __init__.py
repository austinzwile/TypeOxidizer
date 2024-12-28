from binaryninja import *

def register_rust_types(bv):
	rust_typedefs = {
		"u8":    "typedef uint8_t   u8;",
		"u16":   "typedef uint16_t  u16;",
		"u32":   "typedef uint32_t  u32;",
		"u64":   "typedef uint64_t  u64;",
		"u128":  "typedef uint128_t u128;",
		"i8":    "typedef int8_t    i8;",
		"i16":   "typedef int16_t   i16;",
		"i32":   "typedef int32_t   i32;",
		"i64":   "typedef int64_t   i64;",
		"i128":  "typedef int128_t  i128;",
		"f32":   "typedef float     f32;",
		"f64":   "typedef double    f64;",
		"usize": "typedef size_t    usize;",
		"isize": "typedef ssize_t   isize;",
		"str":   "typedef char*     str;",
	}

	for rust_type, typedef in rust_typedefs.items():
		result = bv.parse_type_string(typedef)
		if result is not None:
			bv.define_user_type(rust_type, result[0])

def update_function_return_types(bv, type_mapping, use_rust_types):
	for func in bv.functions:
		func_return_type = func.type.return_value
		if str(func_return_type) in type_mapping:
			mapped_type = type_mapping[str(func_return_type)]

			new_return_type = None
			if use_rust_types:
				new_return_type = Type.named_type_from_registered_type(bv, mapped_type)
			else:
				result = bv.parse_type_string(mapped_type)
				if result:
					new_return_type = result[0]

			if new_return_type:
				new_func_type = Type.function(new_return_type, func.type.parameters, func.type.calling_convention, func.type.has_variable_arguments)
				func.set_user_type(new_func_type)
				print(f"Updated return type of {func.name} to {str(new_return_type)}")

def update_local_variable_types(bv, type_mapping, use_rust_types):
	for func in bv.functions:
		for var in func.vars:
			if str(var.type) in type_mapping:
				mapped_type = type_mapping[str(var.type)]

				new_type = None
				if use_rust_types:
					new_type = Type.named_type_from_registered_type(bv, mapped_type)
				else:
					result = bv.parse_type_string(mapped_type)
					if result:
						new_type = result[0]

				if new_type:
					func.create_user_var(var, new_type, var.name)
					print(f"Updated local variable {var.name} in {func.name} from {var.type} to {type_mapping[str(var.type)]}")

def update_global_variable_types(bv, type_mapping, use_rust_types):
	for var in bv.data_vars:
		var_type = bv.data_vars[var].type
		if str(var_type) in type_mapping:
			mapped_type = type_mapping[str(var_type)]

			new_type = None
			if use_rust_types:
				new_type = Type.named_type_from_registered_type(bv, mapped_type)
			else:
				result = bv.parse_type_string(mapped_type)
				if result:
					new_type = result[0]

			if new_type:
				bv.define_user_data_var(var, new_type)
				print(f"Updated global variable at {hex(var)} from {var_type} to {type_mapping[str(var_type)]}")

def oxidize_types(bv, type_mapping, use_rust_types):
	if use_rust_types:
		register_rust_types(bv)

	update_function_return_types(bv, type_mapping, use_rust_types)
	update_local_variable_types(bv, type_mapping, use_rust_types)
	update_global_variable_types(bv, type_mapping, use_rust_types)

	bv.update_analysis()

def convert_to_rust_types(bv):
	rust_type_mapping = {
		"uint8_t":   "u8",
		"uint16_t":  "u16",
		"uint32_t":  "u32",
		"uint64_t":  "u64",
		"int128_t":  "u128",
		"int8_t":    "i8",
		"int16_t":   "i16",
		"int32_t":   "i32",
		"int64_t":   "i64",
		"uint128_t": "i128",
		"float":     "f32",
		"double":    "f64",
		"size_t":    "usize",
		"ssize_t":   "isize",
		"char*":     "str",
	}

	oxidize_types(bv, rust_type_mapping, use_rust_types=True)
	print("Converted to Rust types.")

def revert_to_c_types(bv):
	c_type_mapping = {
		"u8":    "unsigned char",
		"u16":   "unsigned short",
		"u32":   "unsigned int",
		"u64":   "unsigned long long",
		"u128":  "unsigned __int128",
		"i8":    "signed char",
		"i16":   "short",
		"i32":   "int",
		"i64":   "long long",
		"i128":  "__int128",
		"f32":   "float",
		"f64":   "double",
		"usize": "unsigned long",
		"isize": "long",
		"str":   "char*",
	}

	oxidize_types(bv, c_type_mapping, use_rust_types=False)
	print("Reverted to C types.")

PluginCommand.register(
	"Convert from C to Rust Types",
	"Convert all C types to their Rust equivalents in the binary.",
	convert_to_rust_types
)

PluginCommand.register(
	"Revert to C Types from Rust",
	"Revert all Rust types back to their original C equivalents in the binary.",
	revert_to_c_types
)
