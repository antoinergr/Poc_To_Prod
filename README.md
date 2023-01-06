# End to end Machine Learning Project

# Table of Contents

1. [Description](#description)
2. [Maintainers](#maintainers)
3. [Prerequistes](#prerequistes)
4. [Installation](#Installation)
5. [Run the micro-service application](#run-the-micro-service-application)
6. [Use the application](#use-the-application)
    1. [Example](#example)

## 1. Description

The goal of this project was to create a micro-service to predict programming language associated to Stackoverflow comments.

## 2. Maintainers
- [antoinergr](https://github.com/antoinergr)

## 3. Prerequistes
- conda

## 4. Installation 
``` python
git clone https://github.com/antoinergr/Poc_To_Prod.git

conda env create -n poc_to_prod_capstone -f environment.yml

conda activate poc_to_prod_capstone
```

## 5. Run the micro-service application
```python
python main.py
```

## 6. Use the application

To use the micro-service you have to go the route http://localhost:5000/predict. It is a POST route that needs a JSON body with 2 specific arguments:
- textToPredict : the list of comments.
- top_k : the number of tags you want the micro-service to predict.

### Example

Here, we are going to ask the micro-service to guess the tags associated to three different comments : "how to use matplotlib","my php is not working" and "why c# is the fastest language".

To do so, we need to run a curl request : 
```python
curl -X POST -H "Content-Type: application/json" -d '{"textsToPredict": ["how to use matplotlib python", "my php is not working", "why c# is the fastest language"], "top_k":3}' http://localhost:5000/predict
```
We obtain as a result :
```python
[['iphone', 'c#', 'php'], ['java', 'c#', 'php'], ['java', 'c#', 'php']]
```