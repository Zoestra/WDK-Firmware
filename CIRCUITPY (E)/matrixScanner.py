# At its core, a Switch Matrix is a collection of inputs and outputs
# When the inputs are in a specific electrical configuration
# The outputs can be read to gain information about which switches are pressed. 

# Each Matrix input and output can also have variety of implementations:
# An input/output can be directly connected to a GPIO Pin
# An input/output can be directly connected to a Multiplexer/De-multiplexer

import board 

# TODO Implement Mux Read
def muxRead(name, address):
    #print("Read Mux at address " + address)
    return True

# TODO Implement DeMux Write
def demuxWrite(name, address, value):
    #print("Demux write value " + value + " at address " + address)
    return False

# Matrix Scanner function that iterates through the in/out arrays given a button
# matrix dictionary
def scanButtonMatrix(matrix):
    scanResult = []
    for subOut in matrix['outputs']:
        #Output Direct GPIO Implementation
        if subOut['implementation'] == "DIRECT":
            for output in subOut['locations']:
                #Bring Output Line High
                output = True
                #Scan Inputs and append results to result
                scanResult.append(scanInputs(matrix))
                #Bring Output Line Low to not interfere with next read
                output = False

        #Output De-Multiplexer Implementation
        elif subOut['implementation'] == "DEMUX":
            for output in subOut['locations']['address']:
                demuxName = output['name']
                #Bring Output Line High
                demuxWrite(demuxName, output, True)  
                #Scan Inputs and append results to result
                scanResult.append(scanInputs(matrix))
                #Bring Output Line Low to not interfere with next read
                demuxWrite(demuxName, output, False)
        #Add Other Output Implementation Types Here
    return scanResult
#End scanButtonMatrix

def scanInputs(matrix):
    inputScan = []
    for subIn in matrix['inputs']:
        #Input Direct GPIO Implementation
        if subIn['implementation'] == "DIRECT":
            for input in subIn['locations']: 
                currentRead = input.value
                inputScan.append(currentRead)

        #Input Multiplexer Implementation
        elif subIn['implementation'] == "MUX":
            for inputAddress in subIn['locations']['address']: 
                muxName = subIn['locations']['name']
                currentRead = muxRead(muxName, inputAddress)
                inputScan.append(currentRead)
        #Add Other Input Implementation Types Here
    return inputScan
#End scanInputs

# Usage
# TODO Create this button matrix from the init 
exampleMatrix = {
    "name":"matrix0",
    "inputs":[{
        "layout_role": "rows",
        "implementation":"MUX",
        "locations": {
            "name": "mux0", 
            "address" : [0,1,2,3,4,5,6,7,8]
        }
    }],
    "outputs":[{
        "layout_role":"columns",
        "implementation":"DIRECT",
        "locations": [board.GP0,board.GP1,board.GP2,board.GP3,board.GP4,board.GP5,board.GP6]
    }]
}

#Pass the Dictionary into the scanButton Matrix
#That way, you can have different button matrices in different
#Combinations across the same design
print(scanButtonMatrix(exampleMatrix))
