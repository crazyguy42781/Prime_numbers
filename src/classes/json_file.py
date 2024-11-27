import json

class PrimeGapJSON:
    def __init__(self, filepath=None):
        self.filepath = filepath
        self.data = {
            "file_version": "1.0",
            "base": 174,
            "conversion_type": "prime gaps",
            "chain": {
                "previous_file": None,
                "current_file": None,
                "next_file": None
            },
            "metadata": {
                "start_prime": None,
                "end_prime": None,
                "last_prime": None,
                "trailing_zeros": None,
                "total_primes": None,
                "total_gaps": None,
                "max_gap": None,
                "min_gap": None,
                "average_gap": None,
                "encoded_data_size": None,
                "compression": None,
                "sha256_hash": None,
                "bit_array_size": None
            },
            "system_info": {
                "generator": "PrimeEncoder v2.0",
                "creation_date": None,
                "author": "Your Name or Organization",
                "notes": None
            },
            "data": {
                "structure": {
                    "chunk_size": None,
                    "chunk_count": None
                },
                "encoded_data": None
            }
        }

    def load(self, filepath=None):
        """Loads a JSON file into the class."""
        self.filepath = filepath or self.filepath
        if not self.filepath:
            raise ValueError("Filepath not provided.")
        try:
            with open(self.filepath, 'r') as file:
                self.data = json.load(file)
            print(f"File loaded successfully: {self.filepath}")
        except Exception as e:
            print(f"Error loading file: {e}")
            raise

    def save(self, filepath=None):
        """Saves the current data to a JSON file."""
        self.filepath = filepath or self.filepath
        if not self.filepath:
            raise ValueError("Filepath not provided.")
        try:
            with open(self.filepath, 'w') as file:
                json.dump(self.data, file, indent=4)
            print(f"File saved successfully: {self.filepath}")
        except Exception as e:
            print(f"Error saving file: {e}")
            raise

    def rebuild(self, rebuild_data):
        """
        Rebuilds metadata or other parts of the file using provided data.
        `rebuild_data` is expected to be a dictionary with keys matching the structure of `self.data`.
        """
        for section, values in rebuild_data.items():
            if section in self.data:
                self.data[section].update(values)
            else:
                print(f"Warning: Section {section} does not exist in data structure.")
        print("Rebuild complete.")

    def validate(self):
        """Validates that all required fields in the JSON structure are filled."""
        missing_fields = []
        for section, values in self.data.items():
            if isinstance(values, dict):
                for key, value in values.items():
                    if value is None:
                        missing_fields.append(f"{section}.{key}")
        if missing_fields:
            print("Missing fields:", missing_fields)
            return False
        print("Validation passed. All fields are populated.")
        return True

    def print_summary(self):
        """Prints a summary of the JSON file data."""
        print(json.dumps(self.data, indent=4))
