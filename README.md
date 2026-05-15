# Logging the logging over the last decades
This project examines the trends of logging over the last decades, analyzing data from the Statistisches Bundesamt (Destatis). The data includes various metrics related to logging activities, such as the volume of timber harvested, the types of trees logged, and the usage types of the harvested timber.
## Data Source
The primary data source for this project is the Statistisches Bundesamt (Destatis), which provides comprehensive statistics on logging activities in Germany. The data is available in CSV format and can be found in the `data` directory.
## Data Analysis
The analysis focuses on identifying trends and patterns in logging activities over the years. This includes:
- The total volume of timber harvested annually.
- The distribution of different tree species logged.
- The usage types of the harvested timber (e.g., construction, paper production, energy).
- The impact of logging on forest sustainability and biodiversity.
## Usage
To run the analysis, you can use the provided Jupyter Notebook in the `src` directory named `main.ipynb`. This notebook is used for the computational narrative. The data preprocessing and loading is handled in the `src/data_loader.py` script, which can be imported into the notebook for data manipulation and analysis. It can also be used for further analysis or for creating visualizations to better understand the trends in logging activities. In order to run the notebook, ensure to install the required dependencies listed in the `requirements.txt` file. You can do this using pip in the `src` directory:
```bash
pip install -r requirements.txt
```
## License
This project is licensed under the MIT License. See `LICENSE`.
## Contact
For any questions or suggestions regarding this project, please feel free to contact the author at heimbrodt@uni-potsdam.de. This project is part of the course "Research Software Engineering" at the University of Potsdam, supervised by Prof. Dr. Anna Lena Lamprecht.

## Contributing
Contributions to this project are welcome! If you have any ideas for improvements or would like to contribute, please fork the repository and submit a pull request. Please ensure that your contributions adhere to the coding standards and include appropriate tests if necessary.