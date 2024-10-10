import pandas as pd

class DataCleaning:
    def __init__(self, df):
        """Initialize the class with the DataFrame."""
        self.df = df

    def remove_duplicates(self):
        """Remove duplicate rows based on the 'id' column."""
        self.df = self.df.drop_duplicates(subset='id')
        return self.df

    def handle_missing_values(self):
        """Handle missing values in 'text' and 'image' columns.
        For 'text': Fill NaNs with 'No Text'.
        For 'image': Fill NaNs with 'No Image'."""
        self.df['text'].fillna('No Text', inplace=True)
        self.df['image'].fillna('No Image', inplace=True)
        return self.df

    def standardize_timestamp(self):
        """Convert the 'timestamp' column to a standardized datetime format."""
        self.df['timestamp'] = pd.to_datetime(self.df['timestamp'], errors='coerce')  # Coerce invalid formats to NaT
        return self.df

    def validate_data(self):
        """Perform basic validation checks.
        - Ensure 'timestamp' is not NaT (not a time).
        - Remove rows where both 'text' and 'image' are missing."""
        self.df = self.df.dropna(subset=['timestamp'])  # Remove rows with invalid timestamp
        self.df = self.df[~((self.df['text'] == 'No Text') & (self.df['image'] == 'No Image'))]
        return self.df

    def save_clean_data(self, file_path):
        """Save the cleaned DataFrame to a CSV file."""
        self.df.to_csv(file_path, index=False)
        return file_path

