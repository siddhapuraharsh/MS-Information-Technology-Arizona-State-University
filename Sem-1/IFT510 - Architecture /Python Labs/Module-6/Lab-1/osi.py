## Student Name: Harsh Siddhapura
## Student ID: 1230169813
## Date: 10/23/2023


# Lab Assignment: Simulating OSI Layers
# Programming Language: Python

# Layer 1: Physical Layer
# Simulate physical transmission of data

def physical_layer(data):
    # Code to transmit data physically
    encoded_data = encode(data)  # Encode the data for physical transmission
    transmitted_data = transmit(encoded_data)  # Simulate the transmission of data
    return transmitted_data

def encode(data):
    # Code to encode the data
    encoded_data = data.encode('utf-8')  # Convert data to bytes
    return encoded_data

def transmit(data):
    # Code to simulate transmission of data
    data_str = data.decode('utf-8') if isinstance(data, bytes) else data  # Convert data to string if it's bytes
    transmitted_data = data_str + " (Transmitted)"  # Add a label to indicate transmission
    return transmitted_data


# Layer 2: Data Link Layer
# Simulate framing and error detection

def data_link_layer(data):
    # Code for framing and error detection
    framed_data = frame(data)  # Frame the data for transmission
    error_detected = detect_error(framed_data)  # Simulate error detection
    return framed_data, error_detected

def frame(data):
    # Code to frame the data
    framed_data = "[START]" + data + "[END]"  # Add framing delimiters to the data
    return framed_data

def detect_error(data):
    # Code to simulate error detection
    error_detected = False
    if "ERROR" in data:  # Check if "ERROR" is present in the data
        error_detected = True
    return error_detected


# Layer 3: Network Layer
# Simulate routing and addressing

def network_layer(data):
    # Code for routing and addressing
    routed_data = route(data)  # Simulate routing the data
    addressed_data = address(routed_data)  # Add network address to the data
    return addressed_data

def route(data):
    # Code to simulate routing the data
    routed_data = data + " [Routed]"  # Add a label to indicate routing
    return routed_data

def address(data):
    # Code to add network address to the data
    addressed_data = "192.168.0.1:" + data  # Add a network address to the data
    return addressed_data


# Layer 4: Transport Layer
# Simulate reliable data transfer

def transport_layer(data):
    # Code for reliable data transfer
    reliable_data = ensure_reliability(data)  # Simulate ensuring reliable data transfer
    return reliable_data

def ensure_reliability(data):
    # Code to simulate ensuring reliable data transfer
    reliable_data = data + " (Reliable)"  # Add a label to indicate reliability
    return reliable_data


# Layer 5: Session Layer
# Simulate session management

def session_layer(data):
    # Code for session management
    managed_data = manage_session(data)  # Simulate session management
    return managed_data

def manage_session(data):
    # Code to simulate session management
    managed_data = "[SESSION_START]" + data + "[SESSION_END]"  # Add session delimiters to the data
    return managed_data


# Layer 6: Presentation Layer
# Simulate data formatting and encryption

def presentation_layer(data):
    # Code for data formatting and encryption
    formatted_data = format_data(data)  # Format the data for presentation
    encrypted_data = encrypt_data(formatted_data)  # Encrypt the data
    return encrypted_data

def format_data(data):
    # Code to format the data
    formatted_data = data.upper()  # Convert the data to uppercase
    return formatted_data

def encrypt_data(data):
    # Code to encrypt the data
    encrypted_data = data + " (Encrypted)"  # Add a label to indicate encryption
    return encrypted_data


# Layer 7: Application Layer
# Simulate application-specific functionality

def application_layer(data):
    # Code for application-specific functionality
    processed_data = process_data(data)  # Perform application-specific processing
    return processed_data

def process_data(data):
    # Code to simulate application-specific processing
    processed_data = data + " (Processed)"  # Add a label to indicate processing
    return processed_data


# Main function to demonstrate the simulation of OSI layers

def main():
    # Data to be transmitted
    data = "Hello, World!"

    # Layer 1: Physical Layer
    transmitted_data = physical_layer(data)
    print("Transmitted Data (Physical Layer):", transmitted_data)

    # Layer 2: Data Link Layer
    framed_data, error_detected = data_link_layer(transmitted_data)
    print("Framed Data (Data Link Layer):", framed_data)
    print("Error Detected (Data Link Layer):", error_detected)

    # Layer 3: Network Layer
    addressed_data = network_layer(framed_data)
    print("Addressed Data (Network Layer):", addressed_data)

    # Layer 4: Transport Layer
    reliable_data = transport_layer(addressed_data)
    print("Reliable Data (Transport Layer):", reliable_data)

    # Layer 5: Session Layer
    managed_data = session_layer(reliable_data)
    print("Managed Data (Session Layer):", managed_data)

    # Layer 6: Presentation Layer
    encrypted_data = presentation_layer(managed_data)
    print("Encrypted Data (Presentation Layer):", encrypted_data)

    # Layer 7: Application Layer
    processed_data = application_layer(encrypted_data)
    print("Processed Data (Application Layer):", processed_data)


# Execute the simulation when the script is run
if __name__ == "__main__":
    main()