# functions
def return_number(number):
  return number

# list comprehensions
my_list = [1,2,3,4,5,6,7,8,9,10];

all_numbers = [x for x in my_list]
double_numbers = [2*x for x in my_list]
small_numbers = [x for x in my_list if x < 5]
special_numbers = [3 - x for x in my_list if x > 6]

special_numbers = []
for num in all_numbers:
  if num > 6:
    special_numbers.append(3 - num)


def dog_fact():
  return "Dogs have 4 legs!"

# classes
class Dog:
  def __init__(self, name):
    self.name = name

  # instance method (normal)
  def bark(self):
    print("my name is", self.name)

  @classmethod
  def president_dog(cls):
    return cls('Joe Biden')
  
  @staticmethod
  def dog_fact():
    return "Dogs have 4 legs!"
    
# decorators
def my_decorator(func):
  def wrapper(*args):
    print('starting function')
    result = func(*args);
    print ('ending function')
    return result

  return wrapper

@my_decorator
def add(a, b):
  return a + b

