def sound_decorator(func_as_param):
    def draw_pattern_nested():
        print("ππ±ππ±ππ±π")
        func_as_param() # <-- wywoΕanie
        print("ππ±ππ±ππ±π")
    return draw_pattern_nested


@sound_decorator
def get_dog_info():
    print("Pies to najlepszy przyjaciel czΕowieka")

@sound_decorator
def get_turtle_info():
    print("Ε»Γ³Εw to najnudniejsze zwierze domowe")

# dog_info = sound_decorator(get_dog_info) # dog_info = hau_nested
# dog_info() # ---> hau_nested()

get_dog_info()
print("*****************")
get_turtle_info()

