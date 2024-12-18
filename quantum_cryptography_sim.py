from quantum_cryptography_experiment import simulation_without_eve
from quantum_cryptography_experiment import create_key
from quantum_cryptography_experiment import compare_keys
from quantum_cryptography_experiment import string_to_binary
from quantum_cryptography_experiment import binary_to_string
from quantum_cryptography_experiment import binary_converter
from quantum_cryptography_experiment import encryption
from quantum_cryptography_experiment import decryption
from quantum_cryptography_experiment import string_converter
from quantum_cryptography_experiment import random_with_eve
from quantum_cryptography_experiment import simulation_with_eve
from quantum_cryptography_experiment import check_eve

# Alice & Bob 18 bit example

# Simulation
alice_base_theory = ['x','x','+','x','+','+','+','x','x','+','x','x','x','+','+','x','+','x']
alice_bit_theory = [1,0,0,1,1,0,0,1,1,1,0,1,0,0,0,1,0,1]
bob_base_theory = ['+','x','x','x','+','+','+','x','+','x','x','+','+','x','+','+','+','x']

print('\n','Alice Base:',alice_base_theory)
print('\n','Alice Bit:',alice_bit_theory)
print('\n','Bob Base:',bob_base_theory)

bob_bit_theory = simulation_without_eve(alice_base_theory,alice_bit_theory,bob_base_theory)
print('\n','Bob bit theory:',bob_bit_theory)

# Experiment
alice_base_exp = ['x','x','+','x','+','+','+','x','x','+','x','x','x','+','+','x','+','x']
alice_bit_exp = [1,0,0,1,1,0,0,1,1,1,0,1,0,0,0,1,0,1]
bob_base_exp = ['+','x','x','x','+','+','+','x','+','x','x','+','+','x','+','+','+','x']

# data from the experiment
bob_bit_exp = [1,0,1,1,1,0,0,1,1,0,0,1,0,1,0,1,0,1]
print('\n','Bob bit experiment:',bob_bit_exp)


# create keys
key_theory = create_key(alice_base_theory,alice_bit_theory,bob_base_theory,bob_bit_theory)
key_exp = create_key(alice_base_exp,alice_bit_exp,bob_base_exp,bob_bit_exp)

print('\n','Theory','\n','Key Theory:',key_theory[0],'\n','Number of matching base:',key_theory[2],'\n','Number of matching bits:',key_theory[3],'\n','Accuracy:',key_theory[5])
print('\n','Experiment','\n','Key Experiment:',key_exp[0],'\n','Number of matching base:',key_exp[2],'\n','Number of matching bits:',key_exp[3],'\n','Accuracy:',key_exp[5])

# print True if keys are similar, False if different
print('\n','Keys are the Same?:',compare_keys(key_theory[0],key_exp[0]),'\n')


# Send an encrypted message with key from experiment

_message = input("Enter the message: ")

# Convert the string message to binary
binary_message = string_to_binary(_message)
print('Binary message:', binary_message)

# Ensure the key length matches the length of the binary message
key_exp_for_message = key_exp[0][:len(binary_message)]  # Adjust the key length to match the message length
print('Adjusted key for message length:', key_exp_for_message)

# write message given the binary representation - without leading integers as explained above
message = binary_converter(binary_message)
print('Alice message:',message)

# Alice creates the encrypted message
encrypted_message = encryption(message, key_exp_for_message)
print('\n','Alice sends encrypted message:',encrypted_message)

# Bob's received bits (should be the same as Alice's encrypted message with base +) - from the experiment
# This is where Bob receives the encrypted message, so it should reflect the encrypted form, not the initial binary
bob_received_bits = encrypted_message  # Bob gets the encrypted message directly from Alice
print('\n','Bob received (encrypted message):', bob_received_bits)

# Bob recreates the message from the received bits
decrypted_message = decryption(bob_received_bits, key_exp_for_message)
print('\n','Bob recreates the message:', decrypted_message)

# Convert the decrypted message back to a string
message_bob = string_converter(decrypted_message)
print('\n',"Bob's recreated string message:", message_bob)

#########################################################################################################################
# Eve 18 bit example

# generate random numbers using the function
random_gen = random_with_eve(18)

alice_bit_theory = random_gen[0]
alice_base_theory = random_gen[1]
bob_base_theory = random_gen[2]
eve_base_inc_theory = random_gen[3]
eve_base_tran_theory = random_gen[4]

print('\n','Alice Base:',alice_base_theory)
print('\n','Alice Bit:',alice_bit_theory)
print('\n','Bob Base:',bob_base_theory)
print('\n','Eve Base Incident:',eve_base_inc_theory)
print('\n','Eve Base Transmitted:',eve_base_tran_theory)

# Simulation
sim_bit = simulation_with_eve(alice_base_theory,alice_bit_theory,bob_base_theory,eve_base_inc_theory,eve_base_tran_theory)
bob_bit_theory = sim_bit[0]
eve_bit_theory = sim_bit[1]

print('\n','Bob bit theory:',bob_bit_theory)
print('\n','Eve bit theory:',eve_bit_theory)

#######################################################################################################################
# 18 bit example - Continue

# Experiment - Same random base and bit as simulation (For comparison)
alice_bit_exp = alice_bit_theory
alice_base_exp = alice_base_theory
bob_base_exp = bob_base_theory
eve_base_inc_exp = eve_base_inc_theory
eve_base_tran_exp = eve_base_tran_theory

# From experiment results
bob_bit_exp = [1,0,1,1,1,1,0,1,0,1,1,1,1,0,1,0,1,1]
eve_bit_exp = [1,1,1,1,1,1,1,1,0,1,0,1,1,0,1,0,1,1]
print('\n','Eve bit experiment:',eve_bit_exp) # Unnecessary for the experiment, only for explanatory reasons
print('\n','Bob bit experiment:',bob_bit_exp)


# Check for Eve
print('\n','Check For Eve from Simulation:','\n')
check_for_eve_theory = check_eve(alice_base_theory,bob_base_theory,alice_bit_theory,bob_bit_theory)
print('\n','Check For Eve from Experiment:','\n')
check_for_eve_exp = check_eve(alice_base_exp,bob_base_exp,alice_bit_exp,bob_bit_exp)
