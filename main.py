from Zero import Zero
import json

Zero_object = Zero()
Zero_output = Zero_object.warp_drive()
cards = Zero_output.get('cards')
input_string = Zero_output.get('input_string')
swaps = Zero_output.get('swaps')
errors = Zero_output.get('errors')

print('CARDS:\n')

for i, one_card in enumerate(cards):
    print(f"Card #{i+1}:\n{one_card}\n")

print('' + '-'*50 + '\n')

print(f"Input string:\n{input_string}\n")

print('' + '-'*50 + '\n')
print('SWAPS:\n')

for i, one_swap in enumerate(swaps):
    print(f"Swap #{i+1}:\n{one_swap}\n")

print('' + '-'*50 + '\n')

print('ERRORS:\n')

for i, one_error in enumerate(errors):
    print(f"Error #{i+1}:\n{one_error}\n")

print('' + '-'*50 + '\n')