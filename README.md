# DS-4002-Project3
DS 4002 Project 3: Classifying Skin Lesions for Melanoma Detection

## Section 1: Software and platform section
In this project, we used Python and Jupyter Notebooks in VS Code as our coding language. To complete exploratory data analysis pandas, numpy, seaborn, and matplotlib were utilized. To conduct an image analysis a Python library called PyTorch was explored to provide modeling needs. Additionally, we used the Python package scipy,stats to run both Friedman and pairwise Wilcoxon statistical testing. Both Mac and Windows were used. 

## Section 2: Map of Documentation
- Data
  - cleaned_data.csv
  - raw_data.csv
  - slim_2000.csv
- Output
  - figures
    - age_by_target.png
    - age_histogram.png
    - anatomical_site_by_target.png
    - anatomical_site_count.png
    - diagnosis_count.png
    - sex_by_target.png
    - target_count.png
  - Gradcam_Outputs_DenseNet121
  - Gradcam_Outputs_EfficietNetB0
  - Gradcam_Outputs_ResNet18
- Scripts
  - EfficientNet_PyTorch_Model.ipynb
  - ResNet_PyTorch_Model.ipynb
  - DenseNet_PyTorch_Model.ipynb
  - Data_Cleaning.ipynb
  - Statistical_Testing.ipynb
  - eda.py
- .gitignore
- LICENSE.md
- README.md

## Section 3: Instructions for Reproducibility
1. Download both ISIC image data and the cleaned_data.csv
2. Run the eda.py to produce all the figures
3. In each PyTorch Model, fill in the necessary file paths for the image directory, csv_path, and gradcam directories
4. Run each model and record results in a csv file
5. Run this csv file within Statistical_Testing.ipynb to produce the statistical conclusions
