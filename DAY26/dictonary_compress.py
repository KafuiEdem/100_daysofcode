from unittest import result


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

result = {words:len(words) for words in sentence.split()}

print(result)

