import glob

# The glob module, which is short for global, is a function that's used to search for files that match a specific file pattern or name.
list = glob.glob('*.py')
print(list)

"""
Results:
 >>> ['classes_and_objects.py', 'conditionStatements.py', 'counting_in_loops.py', 'dataclass.py', 'dictionary.py', 'evenNumbers.py', 'fibonacci.py', 'file_wildcards.py', 'filtering_in_loop.py', 'forloop.py', 'functions.py', 'generators.py', 'generator_expressions.py', 
'in_logical_operator.py', 'iterators.py', 'list.py', 'newline_character.py', 'open_and_read.py', 'os_module.py', 'read_file.py', 'scope_test.py', 'search_file.py', 'search_with_boolean_variable.py', 'shutil_module.py', 'slicing_strings.py', 'strings.py', 'string_concatenation.py', 'string_find_operator.py', 'string_format.py', 'string_library.py', 'string_search_and_replace.py', 'string_startswith.py', 'string_strip_whitespace.py', 'try_and_except.py', 'type.py', 'typeConversions.py', 'whileloop.py']
"""