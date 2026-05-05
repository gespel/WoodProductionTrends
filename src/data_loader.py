import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        try:
            self.data = pd.read_csv(file_path, sep=';', decimal=',')
        except Exception as e:
            print(f"Error loading data: {e}")
        return None
    
    def load_overall_production(self):
        if self.data is not None:
            filtered = self.data[self.data["2_variable_attribute_label"] == "Insgesamt"].copy()
            filtered["time"] = pd.to_numeric(filtered["time"], errors='coerce')
            filtered["value"] = pd.to_numeric(filtered["value"], errors='coerce')
            return filtered
        return None
