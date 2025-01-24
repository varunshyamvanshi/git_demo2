def decorator_func(original_func):
  def wrapper():
    print("hey it's decorated now")
    original_func()
  return wrapper

@decorator_func
def cities():
  print("panipat,karnal,kurukshetra")


cities()