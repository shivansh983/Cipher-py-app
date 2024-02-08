class TranspositionCipher:
    def __init__(self, key):
        if not isinstance(key, int) or key <= 0:
            raise ValueError("Key must be a positive integer.")
        self.key = key

    def encrypt_message(self, message):
        if not isinstance(message, str):
            raise TypeError("Message must be a string.")

        # Calculate the number of columns and rows
        num_columns = (len(message) // self.key) + (len(message) % self.key > 0)
        num_rows = self.key
        num_empty_cells = (num_columns * num_rows) - len(message)

        # Create a 2D array of cells
        cells = [['' for _ in range(num_columns)] for _ in range(num_rows)]

        # Fill the cells
        col, row = 0, 0
        for symbol in message:
            cells[row][col] = symbol
            col += 1
            if col == num_columns:
                col = 0
                row += 1

        # Convert the cells to a string
        encrypted_message = ''.join(''.join(row) for row in cells)

        return encrypted_message

    def decrypt_message(self, encrypted_message):
        if not isinstance(encrypted_message, str):
            raise TypeError("Encrypted message must be a string.")

        # Calculate the number of columns and rows
        num_columns = len(encrypted_message) // self.key
        num_rows = self.key

        # Create a 2D array of cells
        cells = [['' for _ in range(num_columns)] for _ in range(num_rows)]

        # Fill the cells
        idx = 0
        for col in range(num_columns):
            for row in range(num_rows):
                if idx < len(encrypted_message):
                    cells[row][col] = encrypted_message[idx]
                    idx += 1

        # Convert the cells to a string
        decrypted_message = ''.join(''.join(row) for row in cells)

        return decrypted_message.rstrip()


# Example usage:
cipher = TranspositionCipher(3)
plaintext = "Hello, world!"
encrypted = cipher.encrypt_message(plaintext)
print("Encrypted:", encrypted)
decrypted = cipher.decrypt_message(encrypted)
print("Decrypted:", decrypted)
