def get_name(first, last, format):
    return format(first, last)

name = get_name(
    'Jane',
    'Doe',
    lambda first, last: f"{first} {last}"
)

print(name)
#llama guns