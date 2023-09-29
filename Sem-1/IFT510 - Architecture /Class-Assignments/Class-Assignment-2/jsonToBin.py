import struct

# Sample data to be serialized
data = [
    {
        "Name": "John Doe",
        "Address": "123 Main St",
        "Telephone": "555-555-1234",
        "DOB": "1990-01-01",
        "Age": 33
    },
    {
        "Name": "Alice Smith",
        "Address": "456 Elm St",
        "Telephone": "555-555-5678",
        "DOB": "1985-05-15",
        "Age": 38
    },
    {
        "Name": "Bob Johnson",
        "Address": "789 Oak St",
        "Telephone": "555-555-9012",
        "DOB": "1978-12-30",
        "Age": 44
    },
    {
        "Name": "Emily Davis",
        "Address": "101 Pine St",
        "Telephone": "555-555-3456",
        "DOB": "1995-07-20",
        "Age": 27
    },
    {
        "Name": "Michael Wilson",
        "Address": "202 Cedar St",
        "Telephone": "555-555-6789",
        "DOB": "1980-03-10",
        "Age": 42
    }
]

# Define the format for serializing each data row
# In this example, we use string format '!50s 50s 15s 10s I' to represent name, address, telephone, DOB, and Age.
format_string = '!50s 50s 15s 10s I'

# Serialize and write the data to the binary file
output_file_path = "data.bin"

with open(output_file_path, 'wb') as binary_file:
    for row in data:
        serialized_row = struct.pack(
            format_string,
            row["Name"].encode('utf-8'),
            row["Address"].encode('utf-8'),
            row["Telephone"].encode('utf-8'),
            row["DOB"].encode('utf-8'),
            row["Age"]
        )
        binary_file.write(serialized_row)

print(f"Data has been serialized and saved to {output_file_path}")
