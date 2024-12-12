from binaryninja import *

def register_rust_types(bv):
	rust_typedefs = {
		"u8": "typedef uint8_t u8;",
		"u16": "typedef uint16_t u16;",
		"u32": "typedef uint32_t u32;",
		"u64": "typedef uint64_t u64;",
		"i8": "typedef int8_t i8;",
		"i16": "typedef int16_t i16;",
		"i32": "typedef int32_t i32;",
		"i64": "typedef int64_t i64;",
		"f32": "typedef float f32;",
		"f64": "typedef double f64;",
		"usize": "typedef size_t usize;",
		"isize": "typedef ptrdiff_t isize;"
	}

	for rust_type, typedef in rust_typedefs.items():
		result = bv.parse_type_string(typedef)
		if result is not None:
			bv.define_user_type(rust_type, result[0])

def update_variable_types(bv, type_mapping):
	for func in bv.functions:
		for var in func.vars:
			if str(var.type) in type_mapping:
				new_type = Type.named_type_from_registered_type(bv, type_mapping[str(var.type)])
				if new_type:
					func.create_user_var(var, new_type, var.name)
					print(f"Updated {var.name} in function {func.name} from {var.type} to {type_mapping[str(var.type)]}")

	for var in bv.data_vars:
		var_type = bv.data_vars[var].type
		if str(var_type) in type_mapping:
			new_type = Type.named_type_from_registered_type(bv, type_mapping[str(var_type)])
			if new_type:
				bv.define_user_data_var(var, new_type)
				print(f"Updated global variable at {hex(var)} from {var_type} to {type_mapping[str(var_type)]}")

def update_function_return_types(bv, type_mapping):
	for func in bv.functions:
		func_return_type = func.type.return_value
		if str(func_return_type) in type_mapping:
			new_return_type = Type.named_type_from_registered_type(bv, type_mapping[str(func_return_type)])
			if new_return_type:
				new_func_type = Type.function(new_return_type, func.type.parameters, func.type.calling_convention, func.type.has_variable_arguments)
				func.set_user_type(new_func_type)
				print(f"Updated return type of function {func.name} from {func_return_type} to {type_mapping[str(func_return_type)]}")

def oxidize_types(bv):
	register_rust_types(bv)

	type_mapping = {
		"uint8_t": "u8",
		"uint16_t": "u16",
		"uint32_t": "u32",
		"uint64_t": "u64",
		"int8_t": "i8",
		"int16_t": "i16",
		"int32_t": "i32",
		"int64_t": "i64",
		"float": "f32",
		"double": "f64",
		"size_t": "usize",
		"ptrdiff_t": "isize"
    }

	update_variable_types(bv, type_mapping)
	update_function_return_types(bv, type_mapping)

# TODO: Register this as a plugin and not a snippet and enable toggle functionality via GUI.

# Run the snippet directly
oxidize_types(bv)