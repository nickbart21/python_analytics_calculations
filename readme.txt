
This repository is made up of basic calculations and analysis. Each file is a standalone script.
Below are descriptions of the datasets used.
--------------------------------------------------------------------------------------
mtcars.csv

fields:
mpg - Miles per Gallon
cyl - # of cylinders
disp - displacement, in cubic inches
hp - horsepower
drat - driveshaft ratio
wt - weight
qsec - 1/4 mile time; a measure of acceleration
vs - 'V' or straight - engine shape
am - transmission; auto or manual
gear - # of gears
carb - # of carburetors.
---------------------------------------------------------------------------------------
breast_cancer_ds.csv

There are 10 predictors, all quantitative, and a binary dependent variable, indicating the presence or absence of breast cancer.
The predictors are anthropometric data and parameters which can be gathered in routine blood analysis.
Prediction models based on these predictors, if accurate, can potentially be used as a biomarker of breast cancer.

Age	            Feature	    Integer	      Age		                                year
BMI	            Feature	    Continuous		BodyMassIndex	                        kg/m2
Glucose	        Feature	    Integer			  Sugar in blood                        mg/dL
Insulin	        Feature	    Continuous		Insulin         	                    µU/mL
HOMA	          Feature	    Continuous		Homeostatic Model Assessment
Leptin	        Feature	    Continuous		Hormone                        	      ng/mL
Adiponectin	    Feature	    Continuous		Hormone                     	        µU/mL
Resistin	      Feature	    Continuous		Hormone                     	        ng/mL
MCP.1	          Feature	    Continuous		Protein                     	        pg/dL
Classification	Target	    Integer		    1=Healthy controls, 2=Cancer Patients

