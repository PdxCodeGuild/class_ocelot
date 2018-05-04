# Set conversion multiples
conv_mult = {'meters': 0.3048}

# Enter feet to convert to meters
number_to_convert = rnd(float(input('what is the distance in feet? ')))


# Convert feet to meters
number_converted = number_to_convert * conv_mult_mt2ft


# Display result

print(number_converted)
