# Market_cap_prediction

## Introduction  

This is a information program designed for investors and stock traders. It has 5 functions:  
1. show company profile information  
2. show key financial numbers  
3. get financial reports of selected company
4. do visualization of income and cost of companies  
5. predict the market cap of companies and give recommended valuation based on AI models  
6. show rankings of the selected company among its sector and industry

## Dependence
pandas, numpy, joblib, yfinance, matplotlib, os, seaborn  
if no, please download this modules using pip


## Model Explanation
The prediction model is based on SGboosting with accuracy around 78%.
As for the train set, considering that companies with extremely high market cap are not usually having accordingly amazing financial data. For this model which aim is to make reasonable prediction using financial data, these over-valued companies are not conductive for model performance. Therefore, these companies are deleted from the train set as outliers. And the range of market in trainset is 10 billion. 
We categorized y(2023 market cap of 1795 NASDAQ companies) into 5 bins, binned ranges are from 0 to 0.1 billion, 0.1 billion to 1 billion, 1 billion to 3 billion, 3 billion to 5 billion, 5 billion to 10 billion.Our results show that misclassification error exists most in the 4th bin.And misclassified samples are mostly assigned to neighboring bins,which can prove our model's reasonableness in a sense.
<img width="400" alt="image" src="https://github.com/user-attachments/assets/d6fd048f-67bf-4b3a-84a2-e4c53e5b8b04">
<img width="400" alt="image" src="https://github.com/user-attachments/assets/3a8683e0-0530-4a01-8c3f-2002be6d4dc5">
More often, it is hard to predict the marketcap of company, because the factors are extremely complicated. But this model could give investors a relatively helpful reference.


## Demo
Firstly, change the dir
```bash
cd ./project_folder  
```

Call python3 to run program
```bash
python3 app.py
```
## Initialize the environment

Clone the source code from remote through your preferred protocol.

```bash
# through HTTP
git clone https://github.com/Ivanhandsome777/Market_cap_prediction.git
```



Initialize the Conda env.

```bash
# first time setup
conda env create -f environment.yml
# or update
conda env update -f environment.yml
```

### Activate the Conda environment

```bash
conda activate yjlhandsome
```
