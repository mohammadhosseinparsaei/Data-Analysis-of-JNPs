# Data Analysis of Janus Nanoparticles (JNPs)

In this project, we have studied and evaluated the effectiveness of Janus nanoparticles (JNPs) alongside other treatments. The data has been organized into structured formats, including text files (.txt) and comma-separated values files (.csv), to facilitate efficient analysis and interpretation.

## Experimental Analyses Covered:

- `Dynamic Light Scattering (DLS) Data`: Investigating the size of nanoparticles.

- `Hemolytic Toxicity`: Assessing the potential toxicity of nanoparticles on blood cells.

- `In vitro Cytotoxicity Assays`: Evaluating the impact of nanoparticles on cell viability.

- `Cellular Internalization Studies`: Examining the uptake of nanoparticles by cells.

- `Serum Biochemical Assays`: Analyzing the effect of nanoparticles on serum enzyme levels.

- `In vivo Biodistribution`: Understanding the distribution of nanoparticles within living organisms.

- `Temperature Measurement Studies`: Monitoring temperature changes under various experimental conditions.

- `Tumor Volume Measurements`: Investigating the effect of nanoparticles on tumor growth.

- `Survival Proportions Analysis`: Assessing the survival outcomes of different treatment groups over time.

## Requirements

- Python 3.11.7
- Jupyter Notebook
- NumPy 1.24.3
- Pandas 2.1.4
- Matplotlib 3.8.4
- SciPy 1.12.0
- Statsmodels 0.14.0 
- Lifelines 0.28.0

**Additional Notes:**
-	Function Organization:

Two additional functions, namely `comparison` and `survival`, have been developed and stored in separate Python files named `comparison.py` and `survival.py`. These functions are intended to facilitate specific plotting of the figures and analyses. To ensure proper importation, these files should reside within the directory where the main script is located.

-	File Importation Method:

File names with their respective extensions (e.g., .csv, .txt) have been provided for data reading. It is assumed that the data files are located in the same directory as the main script. Adjustments to the file paths may be necessary if the data files are stored elsewhere.

## Data Description
We've got our data neatly saved in TXT and CSV files, all set for analysis. Each file comes with clear instructions on how to use them for our studies.
#### **1. DLS Data:**
File's name: `202302031519089.txt`
Explanations:
This file contains data from Dynamic Light Scattering (DLS) analysis. It was initially more comprehensive, but two specific types of data were extracted for separate analysis.
-	The remaining data includes:
Diameter (nm), and Frequency (%)

The data in this file is for investigating the size of nanoparticles.

#### **2. Hemolytic Toxicity Data:**
File's name: `Hemolytic toxicity.csv`
File's Columns:
-	Nanoparticle Concentration (mg/ml): Concentration of nanoparticles in milligrams per milliliter.
-	Hemolysis1 (%), Hemolysis2 (%), Hemolysis3 (%): Hemolysis percentages from three repetitions at each concentration.

The data in this file is for examining the extent of red blood cell lysis upon exposure to different concentrations of nanoparticles.

#### 3. **In vitro Cytotoxicity Assay Data:**
File's name: `In vitro cytotoxicity assay.csv`
File's Columns:
-	Nanoparticle Concentration (mg/ml): Concentration of nanoparticles in milligrams per milliliter.
-	Cell Viability1 (%), Cell Viability2 (%), Cell Viability3 (%): Cell viability percentages from three repetitions at each concentration.

The data in this file is for investigating the cellular toxicity of nanoparticles at various concentrations.

#### **4. Cellular Internalization Data:**
File's name: `Cellular internalization.csv`
File's Columns:
-	Nanoparticle Concentration (µg/ml): Concentration of nanoparticles in micrograms per milliliter.
-	Fe Concentration per Cell1 (pg), Fe Concentration per Cell2 (pg), Fe Concentration per Cell3 (pg): Concentrations of iron (Fe) per cell from three repetitions.
-	Au Concentration per Cell1 (pg), Au Concentration per Cell2 (pg), Au Concentration per Cell3 (pg): Concentrations of gold (Au) per cell from three repetitions.

The data in this file is for examining the extent of nanoparticle entry into cells at different concentrations.

#### **5. Serum Biochemical Assay Data:**
File's name: `Serum biochemical assay.csv`
File's Columns:
-	Enzyme: Type of enzyme (AST, ALT, ALP).
-	Control1, Control2, Control3: Enzyme levels in the control group from three repetitions.
-	JNPs1, JNPs2, JNPs3: Enzyme levels in JNPs group from three repetitions.

The data in this file is for evaluating and comparing the levels of liver enzymes between the control and treatment group

#### **6. In vivo Biodistribution Data:**
File's name: `In vivo biodistribution.csv`
File's Columns:
-	Organ: Organ name (Heart, Right Lung, Left Lung, Spleen, Liver, Right Kidney, Left Kidney, Tumor).
-	Fe Concentration per Tissue1 (µg/g), Fe Concentration per Tissue2 (µg/g), Fe Concentration per Tissue3 (µg/g): Concentrations of iron (Fe) per tissue from three repetitions.
-	Au Concentration per Tissue1 (µg/g), Au Concentration per Tissue2 (µg/g), Au Concentration per Tissue3 (µg/g): Concentrations of gold (Au) per tissue from three repetitions.

The data in this file is for evaluating the dispersion of nanoparticles in different organs following their injection.

#### **7. Temperature Measurement Study Data:**
File's name: `Temperature measurement study.csv`
File's Columns:
-	Time (min): Different times at which the temperature was recorded
-	AMF1 (°C), AMF2 (°C), AMF3 (°C): Temperature measurements under AMF conditions from three repetitions.
-	NIR1 (°C), NIR2 (°C), NIR3 (°C): Temperature measurements under NIR conditions from three repetitions.
-	JNPs+MF+AMF1 (°C), JNPs+MF+AMF2 (°C), JNPs+MF+AMF3 (°C): Temperature measurements under JNPs+MF+AMF treatment from three repetitions.
-	JNPs+MF+NIR1 (°C), JNPs+MF+NIR2 (°C), JNPs+MF+NIR3 (°C): Temperature measurements under JNPs+MF+NIR treatment from three repetitions.
-	PMT1 (°C), PMT2 (°C), PMT3 (°C): Temperature measurements under PMT treatment from three repetitions.
-	JNPs+MF+PMT1 (°C), JNPs+MF+PMT2 (°C), JNPs+MF+PMT3 (°C): Temperature measurements under JNPs+MF+PMT treatment from three repetitions.

The data in this file is for investigating temperature changes following various treatment methods.

#### **8. Tumor Volume Data:**
File's name: `Tumor volume.csv`
File's Columns:
-	Time(day): Recorded time of death of mice
-	Control1, Control2, Control3: Tumor volumes in the control group from three repetitions.
-	JNPs+MF1, JNPs+MF2, JNPs+MF3: Tumor volumes in the JNPs+MF group from three repetitions.
-	RT1, RT2, RT3: Tumor volumes in the RT (Radiotherapy) group from three repetitions.
-	AMF1, AMF2, AMF3: Tumor volumes in the AMF (Alternating Magnetic Field) group from three repetitions.
-	NIR1, NIR2, NIR3: Tumor volumes in the NIR (Near-Infrared Radiation) group from three repetitions.
-	JNPs+MF+RT1, JNPs+MF+RT2, JNPs+MF+RT3: Tumor volumes in the combined JNPs+MF+RT group from three repetitions.
-	JNPs+MF+AMF1, JNPs+MF+AMF2, JNPs+MF+AMF3: Tumor volumes in the combined JNPs+MF+AMF group from three repetitions.
-	JNPs+MF+NIR1, JNPs+MF+NIR2, JNPs+MF+NIR3: Tumor volumes in the combined JNPs+MF+NIR group from three repetitions.
-	PMT1, PMT2, PMT3: Tumor volumes in the PMT (Photothermal Therapy) group from three repetitions.
-	JNPs+MF+PMT1, JNPs+MF+PMT2, JNPs+MF+PMT3: Tumor volumes in the combined JNPs+MF+PMT group from three repetitions.
-	JNPs+MF+RT+PMT1, JNPs+MF+RT+PMT2, JNPs+MF+RT+PMT3: Tumor volumes in the combined JNPs+MF+RT+PMT group from three repetitions.

The data in this file is intended for comparing tumor volume curves across different treatment groups to evaluate the effectiveness of treatments.

#### **9. Survival Proportions Data:**
File's name: `Survival proportions.csv`
File's Columns:
-	Groups: Treatment groups (Control, JNPs+MF, etc.).
-	Time (day): Time of sample death after each treatment in days.
-	Dead(1)/Alive(0): Status indicator (0 for alive, 1 for dead).

The data in this file is for plotting Kaplan-Meier survival curves, illustrating the survival proportions over time for different treatment groups.
