# Data Analysis of Janus Nanoparticles (JNPs)

In this project, we have studied and evaluated the effectiveness of Janus nanoparticles (JNPs) alongside other treatments. The data has been organized into structured formats to facilitate efficient analysis and interpretation.

## Experimental Analyses Covered:

- `Nanoparticle Stability Analysis`: Assessment of the stability of the synthesized nanoparticles over a four-week period.

- `Hemolytic Toxicity`: Assessing the potential toxicity of nanoparticles on blood cells.

- `In vitro Cytotoxicity Assays`: Evaluating the impact of nanoparticles on cell viability.

- `Cellular Internalization Studies`: Examining the uptake of nanoparticles by cells.

- `Serum Biochemical Assays`: Analyzing the effect of nanoparticles on serum enzyme levels.

- `In vivo Biodistribution`: Understanding the distribution of nanoparticles within living organisms.

- `MRI imaging`: Quantifying the MRI signal intensity to evaluate the effectiveness of magnetic targeting of nanoparticles.

- `Temperature Measurement Studies`: Monitoring temperature changes under various experimental conditions.

- `Tumor Volume Measurements`: Investigating the effect of nanoparticles on tumor growth.

- `Survival Proportions`: Assessing the survival outcomes of different treatment groups over time.

- `Western Blot Results`: Analyzing protein expression levels (Hsp70 and VEGF) normalized to beta-actin.

## Requirements

- Python 3.11.7
- Visual Studio Code with Jupyter Notebook extension
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

File names with their respective extensions have been provided for data reading. It is assumed that the data files are located in the same directory as the main script. Adjustments to the file paths may be necessary if the data files are stored elsewhere.

## Data Description
We've got our data neatly saved in CSV files, all set for analysis. Each file comes with clear instructions on how to use them for our studies.

#### **1. Nanoparticle Stability Data:**

This section includes two data files used to evaluate the long-term stability of Janus nanoparticles (JNPs) by tracking changes in their size and zeta potential over four weeks.

Nanoparticle Size Stability
File's name: `Stability_size.csv`

File's Columns:
-	Columns: week1, week2, week3, week4

Nanoparticle Zeta Stability
File's name: `Stability_zeta.csv`

File's Columns:
-	Columns: week1, week2, week3, week4

Description: Each week, three repeated measurements were taken and entered into the corresponding column.

#### **1. Hemolytic Toxicity Data:**
File's name: `Hemolytic toxicity.csv`

File's Columns:
-	Nanoparticle Concentration (mg/ml): Concentration of nanoparticles in milligrams per milliliter.
-	Hemolysis1 (%), Hemolysis2 (%), Hemolysis3 (%): Hemolysis percentages from three repetitions at each concentration.

The data in this file is used to examine the extent of red blood cell lysis upon exposure to different concentrations of nanoparticles.

#### 2. **In vitro Cytotoxicity Assay Data:**
File's name: `In vitro cytotoxicity assay.csv`

File's Columns:
-	Nanoparticle Concentration: Concentration of nanoparticles.
-	Viability_np1, Viability_np2, Viability_np3: Cell viability percentages for the nanoparticle-only group from three repetitions.
-	Viability_np_amf1, Viability_np_amf2, Viability_np_amf3: Cell viability percentages for the nanoparticle + AMF group from three repetitions.
-	Viability_np_nir1, Viability_np_nir2, Viability_np_nir3: Cell viability percentages for the nanoparticle + NIR group from three repetitions.
-	Viability_np_amf_nir1, Viability_np_amf_nir2, Viability_np_amf_nir3: Cell viability percentages for the nanoparticle + AMF + NIR group from three repetitions.

The data in this file is used to investigate the cellular toxicity of nanoparticles at various concentrations and under different treatment conditions.

#### **3. Cellular Internalization Data:**
File's name: `Cellular internalization.csv`

File's Columns:
-	Nanoparticle Concentration (µg/ml): Concentration of nanoparticles in micrograms per milliliter.
-	Fe Concentration per Cell1 (pg), Fe Concentration per Cell2 (pg), Fe Concentration per Cell3 (pg): Concentrations of iron (Fe) per cell from three repetitions.
-	Au Concentration per Cell1 (pg), Au Concentration per Cell2 (pg), Au Concentration per Cell3 (pg): Concentrations of gold (Au) per cell from three repetitions.

The data in this file is used to examine the extent of nanoparticle entry into cells at different concentrations.

#### **4. Serum Biochemical Assay Data:**
File's name: `Serum biochemical assay.csv`

File's Columns:
-	Enzyme: Type of enzyme (AST, ALT, ALP).
-	Control1, Control2, Control3: Enzyme levels in the control group from three repetitions.
-	JNPs1, JNPs2, JNPs3: Enzyme levels in JNPs group from three repetitions.

The data in this file is for evaluating and comparing the levels of liver enzymes between the control and treatment group

#### **5. In vivo Biodistribution Data:**
File's name: `In vivo biodistribution.csv`

File's Columns:
-	Organ: Name of the organ or tissue sample along with the time point.
-	Fe concentration/tissue1 (µg/g), Fe concentration/tissue2 (µg/g), Fe concentration/tissue3 (µg/g): Iron concentrations measured in three replicates for each sample.
-	Au concentration/tissue1 (µg/g), Au concentration/tissue2 (µg/g), Au concentration/tissue3 (µg/g): Gold concentrations measured in three replicates for each sample.

This dataset is used to analyze the biodistribution and magnetic targeting efficiency of the injected nanoparticles over different time intervals.

#### **6. MRI imaging:**
File's name: `MRI.csv`

File's Columns:
-	Status indicator (Pre injection or Post injection).
-	Right tumor1, Right tumor2, Right tumor3: Right tumor volume measurements from three repetitions.
-	Left tumor1, Left tumor2, Left tumor3: Left tumor volume measurements from three repetitions.

This data is used to measure and compare signal intensity before and after nanoparticle injection.

#### **7. Specific Absorption Rate (SAR) Calculation:**
File's name: `SAR.csv`

File's Columns:
-	Time(min): The time at which the temperature was recorded.
-	Control1, Control2, Control3: Temperature measurements for the control group from three repetitions.
-	C0.25_1, C0.25_2, C0.25_3: Temperature measurements with 0.25 mg/ml nanoparticle concentration from three repetitions.
-	C0.5_1, C0.5_2, C0.5_3: Temperature measurements with 0.5 mg/ml nanoparticle concentration from three repetitions.
-	C1_1, C1_2, C1_3: Temperature measurements with 1 mg/ml nanoparticle concentration from three repetitions.

This data is used to analyze temperature changes and calculate the Specific Absorption Rate (SAR) of the nanoparticles at different concentrations under an alternating magnetic field (AMF).

#### **8. In Vitro NIR Heating Data:**
File's name: `NIR_in_vitro.csv`

File's Columns:
-	Time(min): The time at which the temperature was recorded.
-	Control1, Control2, Control3: Temperature measurements for the control group from three repetitions.
-	C50_1, C50_2, C50_3: Temperature measurements at 50 µg/ml nanoparticle concentration from three repetitions.
-	C100_1, C100_2, C100_3: Temperature measurements at 100 µg/ml nanoparticle concentration from three repetitions.
-	C200_1, C200_2, C200_3: Temperature measurements at 200 µg/ml nanoparticle concentration from three repetitions.
-	C400_1, C400_2, C400_3: Temperature measurements at 400 µg/ml nanoparticle concentration from three repetitions.

This data is used to investigate the temperature changes of nanoparticle solutions at various concentrations under NIR irradiation.

#### **9. UV-Vis Spectroscopy Data:**
File's name: `uv.csv`

File's Columns:
-	NANOMETERS: Wavelength in nanometers.
-	ABSORBANCE: Absorbance value at each wavelength.

This data is used to analyze the absorption spectrum of the nanoparticles in the UV-Vis range.

#### **10. Photothermal Conversion Efficiency (PCE) Calculation:**
File's name: `PCE.csv`

File's Columns:
-	Time(s): The time at which the temperature was recorded.
-	C400_1, C400_2, C400_3: Temperature measurements at 400 µg/ml nanoparticle concentration from three repetitions.

This data is used to calculate the Photothermal Conversion Efficiency (PCE) of the nanoparticles.

#### **11. Temperature Measurement Study Data (in vivo):**
File's name: `Temperature measurement study.csv`

File's Columns:
-	Time (min): Different times at which the temperature was recorded
-	AMF1 (°C), AMF2 (°C), AMF3 (°C): Temperature measurements under AMF conditions from three repetitions.
-	NIR1 (°C), NIR2 (°C), NIR3 (°C): Temperature measurements under NIR conditions from three repetitions.
-	JNPs+MF+AMF1 (°C), JNPs+MF+AMF2 (°C), JNPs+MF+AMF3 (°C): Temperature measurements under JNPs+MF+AMF treatment from three repetitions.
-	JNPs+MF+NIR1 (°C), JNPs+MF+NIR2 (°C), JNPs+MF+NIR3 (°C): Temperature measurements under JNPs+MF+NIR treatment from three repetitions.
-	PMT1 (°C), PMT2 (°C), PMT3 (°C): Temperature measurements under PMT treatment from three repetitions.
-	JNPs+MF+PMT1 (°C), JNPs+MF+PMT2 (°C), JNPs+MF+PMT3 (°C): Temperature measurements under JNPs+MF+PMT treatment from three repetitions.

The data in this file is used to investigate temperature changes following various treatment methods.

#### **12. Tumor Volume Data:**
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

#### **13. Survival Proportions Data:**
File's name: `Survival proportions.csv`

File's Columns:
-	Groups: Treatment groups (Control, JNPs+MF, etc.).
-	Time (day): Time of sample death after each treatment in days.
-	Dead(1)/Alive(0): Status indicator (0 for alive, 1 for dead).

The data in this file is for plotting Kaplan-Meier survival curves, illustrating the survival proportions over time for different treatment groups.

#### **14. Western Blot Quantification Data:**
File names: `Hsp70_actin.csv`, `VEGF_actin.csv`

File's Columns: Control, JNPs+MF, AMF, NIR, RT, PMT, JNPs+MF+AMF, JNPs+MF+NIR, JNPs+MF+RT, JNPs+MF+PMT, JNPs+MF+RT+PMT: Each column represents the quantification of protein expression (Hsp70 or VEGF) normalized to beta-actin for a specific treatment group. Each group has three repeated measurements.

The data in these files is intended for analyzing the expression levels of Hsp70 and VEGF under various treatments to understand their role in therapeutic outcomes.

