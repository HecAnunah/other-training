import re

def from_camel_case(name: str) -> str:
    split_name = re.findall(r'[A-ZА-Я][^A-ZА-Я]*', name)
    words_lower = [word.lower() for word in split_name]
    return '_'.join(words_lower)


print("Example:")
print(from_camel_case("MyFunctionName"))

# These "asserts" are used for self-checking
assert from_camel_case("MyFunctionName") == "my_function_name"
assert from_camel_case("IPhone") == "i_phone"

print("The mission is done! Click 'Check Solution' to earn rewards!")
