import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        try:
            self.data = pd.read_csv(file_path, sep=';')
        except Exception as e:
            print(f"Error loading data: {e}")
        return None
    
    def load_overall_production(self):
        if self.data is not None:
            return self.data[self.data["2_variable_attribute_label"] == "Insgesamt"]
        return None