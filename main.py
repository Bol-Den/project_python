import addition_function
import addition_function_error_handling

result = addition_function.addition(5,6) # should return 11
result1 = addition_function.addition(3,6,11) # should return 20
result2 = addition_function.addition("a","b","bv") # parameters cant be type of String

print(result)
print(result1)
print(result2)

result_with_error_handling = addition_function_error_handling.addition(10, 15, 5)
print(result_with_error_handling)

result_with_error_handling1 = addition_function_error_handling.addition(10,15, "a")
print(result_with_error_handling1)


