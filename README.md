# Analysis of Biological Networks Final Project

This repository contains the code and files for the "Analysis of Biological Networks" final project. The project focuses on analyzing biological networks using statistical null hypothesis testing to investigate the differences in protein distributions based on their functional relationships.

## Project Structure

- **Code.ipynb**: Jupyter Notebook containing the main code for data analysis and statistical testing.
- **generate ppi csv.ipynb**: Jupyter Notebook for generating protein-protein interaction (PPI) data in CSV format.
- **generate train dataset.py**: Python script to generate the training dataset for statistical testing.
- **generate work scores csv.ipynb**: Jupyter Notebook to generate work scores CSV file.
- **read ppi.ipynb**: Jupyter Notebook for reading and processing PPI data.

## Data Folder

The **data** folder contains the necessary files for the project, including input data and generated output files.

## Statistical Null Hypothesis Testing

Statistical null hypothesis testing is a method used to compare observed data against an expected distribution or pattern. In this project, we apply statistical tests to examine whether the distribution of proteins that work together differs significantly from those that don't work together within specific Gene Ontology namespaces.

## Evaluation

The project evaluates the results of the statistical tests to determine the statistical significance of the observed differences in protein distributions. This helps gain insights into the functional relationships among proteins in the biological networks under investigation.

## Getting Started

To reproduce the results of this project, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies listed in the `requirements.txt` file.
3. Run the notebooks or scripts in the specified order to generate the necessary files and perform the analysis.

Please refer to the individual notebooks and scripts for detailed instructions and explanations.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

