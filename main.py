name = input("What is your name : ");

# name = name.strip(); #no more white space
# name = name.title(); #capitalize the name
# print("hello, "+ name);
# print("Hello, ", name);

name = name.strip().title(); #titlize the whole string after stripping

print(f"Hello, {name}");

