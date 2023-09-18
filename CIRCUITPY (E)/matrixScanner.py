# At its core, a Switch Matrix is a collection of inputs and outputs
# When the inputs are in a specific electrical configuration
# The outputs can be read to gain information about which switches are pressed. 

# Each Matrix input and output can also have variety of implementations:
# An input/output can be directly connected to a GPIO Pin
# An input/output can be directly connected to a Multiplexer/De-multiplexer

import board


# TODO Implement Mux Read
def mux_read(name, address):
    # print("Read Mux at address " + address)
    return True


# TODO Implement DeMux Write
def demux_write(name, address, value):
    # print("Demux write value " + value + " at address " + address)
    return False


# Matrix Scanner function that iterates through the in/out arrays given a button
# matrix dictionary
def scan_button_matrix(matrix):
    scan_result = []
    for sub_out in matrix['outputs']:
        # Output Direct GPIO Implementation
        if sub_out['implementation'] == "DIRECT":
            for output_pin in sub_out['locations']:
                # Bring Output Line High
                output_pin = True
                # Scan Inputs and append results to result
                scan_result.append(scan_inputs(matrix))
                # Bring Output Line Low to not interfere with next read
                output_pin = False

        # Output De-Multiplexer Implementation
        elif sub_out['implementation'] == "DEMUX":
            for output_address in sub_out['locations']['address']:
                demux_name = output_address['name']
                # Bring Output Line High
                demux_write(demux_name, output_address, True)
                # Scan Inputs and append results to result
                scan_result.append(scan_inputs(matrix))
                # Bring Output Line Low to not interfere with next read
                demux_write(demux_name, output_address, False)
        # Add Other Output Implementation Types Here
    return scan_result


# End scan_button_matrix

def scan_inputs(matrix):
    input_scan = []
    for sub_in in matrix['inputs']:
        # Input Direct GPIO Implementation
        if sub_in['implementation'] == "DIRECT":
            for input_pin in sub_in['locations']:
                current_read = input_pin.value
                input_scan.append(current_read)

        # Input Multiplexer Implementation
        elif sub_in['implementation'] == "MUX":
            for input_address in sub_in['locations']['address']:
                mux_name = sub_in['locations']['name']
                current_read = mux_read(mux_name, input_address)
                input_scan.append(current_read)
        # Add Other Input Implementation Types Here
    return input_scan


# End scan_inputs

# Usage
# TODO Create this button matrix from the init 
example_matrix = {
    "name": "matrix0",
    "inputs": [{
        "layout_role": "rows",
        "implementation": "MUX",
        "locations": {
            "name": "mux0",
            "address": [0, 1, 2, 3, 4, 5, 6, 7, 8]
        }
    }],
    "outputs": [{
        "layout_role": "columns",
        "implementation": "DIRECT",
        "locations": [board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6]
    }]
}

# Pass the Dictionary into the scanButton Matrix
# That way, you can have different button matrices in different
# Combinations across the same design
print(scan_button_matrix(example_matrix))
