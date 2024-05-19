# decorator is a function name his type higher order function
def decorator(function_parameter):
    def decoration_function_1():
        print("Befo..")
        function_parameter()
        print("Afte..")
    return decoration_function_1()
@decorator # shuger syntax
def input_function():
    print("Say Hello")
# decorator(input_function)

################################################################
#by time module  Execution time of the code (decorator method)
# import time as t
#
# start_time = t.time()
#
# for i in range(4):
#     print(i)
# end_time = t.time()
#
# final_time = end_time - start_time
# print(final_time)
import inspect

signiture = inspect.signature
print(signiture)
################################################################
# import module and implement decorator method



















