def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")



print_kwargs(name="Shaktiman",power="Laser")
print_kwargs(name="Shaktiman",power="Laser",enemy="Dr.Jackaal")
