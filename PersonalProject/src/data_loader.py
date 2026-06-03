import pandas as pd

class DataLoader:
    def __init__(self) -> DataLoader:
        pass
    
    # The following methods load the data from the specified file path and return filtered DataFrames based on the criteria defined in the original code.
    # Each method handles potential exceptions during the loading process and ensures that the data is properly filtered and sorted before being returned.

    def load_overall_production(self, file_path: str) -> pd.DataFrame | None:
        try:
            self.data = pd.read_csv(file_path, sep=';', decimal=',')
        except Exception as e:
            print(f"Error loading data: {e}")

        if self.data is not None:
            filtered = self.data[self.data["2_variable_attribute_label"] == "Insgesamt"].copy()
            filtered["time"] = pd.to_numeric(filtered["time"], errors='coerce')
            filtered["value"] = pd.to_numeric(filtered["value"], errors='coerce')
            return filtered
        return None
    
    def load_wood_production_by_type(self, file_path: str) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame] | None:
        try:
            self.data = pd.read_csv(file_path, sep=';', decimal=',')
        except Exception as e:
            print(f"Error loading data: {e}")

        if self.data is not None:
            filtered = self.data[self.data["2_variable_attribute_label"] != "Insgesamt"].copy()
            filtered["time"] = pd.to_numeric(filtered["time"], errors='coerce')
            filtered["value"] = pd.to_numeric(filtered["value"], errors='coerce')

            beech_and_other_hardood = filtered[filtered["2_variable_attribute_label"] == "Buche und sonstiges Laubholz"].sort_values("time")
            jaw_and_larch = filtered[filtered["2_variable_attribute_label"] == "Kiefer und Lärche"].sort_values("time")
            oak_and_red_oak = filtered[filtered["2_variable_attribute_label"] == "Eiche und Roteiche"].sort_values("time")
            spruce_fir_douglas_fir_and_other_softwood = filtered[filtered["2_variable_attribute_label"] == "Fichte, Tanne, Douglasie und sonstiges Nadelholz"].sort_values("time")

            return beech_and_other_hardood, jaw_and_larch, oak_and_red_oak, spruce_fir_douglas_fir_and_other_softwood
        return None
    
    def load_spruce_usage(self, file_path: str) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame] | None:
        try:
            self.data = pd.read_csv(file_path, sep=';', decimal=',')
        except Exception as e:
            print(f"Error loading data: {e}")

        if self.data is not None:
            filtered = self.data.copy()
            filtered["time"] = pd.to_numeric(filtered["time"], errors='coerce')
            filtered["value"] = pd.to_numeric(filtered["value"], errors='coerce')

            stammholz = filtered[filtered["usage_type"] == "Stammholz"].sort_values("time")
            industrieholz = filtered[filtered["usage_type"] == "Industrieholz"].sort_values("time")
            energieholz = filtered[filtered["usage_type"] == "Energieholz"].sort_values("time")
            unbenutzt = filtered[filtered["usage_type"] == "nicht verwertet"].sort_values("time")
            
            return stammholz, industrieholz, energieholz, unbenutzt
        return None
    