def sound_decorator(func_as_param):
    def draw_pattern_nested():
        print("🐕🐱🐕🐱🐕🐱🐕")
        func_as_param() # <-- wywołanie
        print("🐕🐱🐕🐱🐕🐱🐕")
    return draw_pattern_nested


@sound_decorator
def get_dog_info():
    print("Pies to najlepszy przyjaciel człowieka")

@sound_decorator
def get_turtle_info():
    print("Żółw to najnudniejsze zwierze domowe")

# dog_info = sound_decorator(get_dog_info) # dog_info = hau_nested
# dog_info() # ---> hau_nested()

get_dog_info()
print("*****************")
get_turtle_info()

