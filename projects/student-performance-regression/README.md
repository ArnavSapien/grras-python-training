# Student Performance Prediction using Multiple Linear Regression

## Project Overview

This project predicts a student's Performance Index using Multiple Linear Regression.

The dataset is taken from Kaggle. It contains student-related information such as hours studied, previous scores, sleep hours, extracurricular activities, and sample question papers practiced.

In this project, Seaborn is used for data visualization, Scikit-learn is used for model training, Joblib is used to save the trained model, and FastAPI is used to create an API. The API is tested using Postman.

## Dataset

Dataset used: Student Performance Dataset from Kaggle

## Input Features

The model uses the following input columns:

* Hours Studied
* Previous Scores
* Extracurricular Activities
* Sleep Hours
* Sample Question Papers Practiced

## Output Column

The model predicts:

* Performance Index

## Technologies Used

* Python
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* FastAPI
* Uvicorn
* Postman

## Project Files

* `graph.py`
  Used to create Seaborn graphs from the dataset.

* `train_model.py`
  Used to train the Multiple Linear Regression model and save it as `model.joblib`.

* `model.joblib`
  Saved trained machine learning model.

* `app.py`
  FastAPI file used to create the prediction API.

* `requirements.txt`
  Contains all required Python libraries.

## Steps Performed

1. Loaded the dataset using Pandas.
2. Removed null values from the dataset.
3. Converted the `Extracurricular Activities` column from Yes/No to 1/0.
4. Created a Seaborn graph to visualize the data.
5. Selected input and output columns.
6. Split the dataset into training and testing data.
7. Trained the model using Multiple Linear Regression.
8. Saved the trained model using Joblib.
9. Created an API using FastAPI.
10. Tested the API using Postman.

## How to Run the Project

### Step 1: Install libraries

```bash
pip install -r requirements.txt
```

### Step 2: Run graph file

```bash
python graph.py
```

### Step 3: Train the model

```bash
python train_model.py
```

This will create:

```text
model.joblib
```

### Step 4: Run the API

```bash
python -m uvicorn app:app --reload
```

The API will run on:

```text
http://127.0.0.1:8000
```

### Step 5: Test in Postman

Use this URL:

```text
http://127.0.0.1:8000/predict
```

Method:

```text
POST
```

Body type:

```text
raw JSON
```

Example input:

```json
{
  "hours_studied": 7,
  "previous_scores": 85,
  "extracurricular_activities": 1,
  "sleep_hours": 8,
  "sample_question_papers_practiced": 5
}
```

Example output:

```json
{
  "predicted_performance_index": 82.45
}
```

## Conclusion

This project shows how Multiple Linear Regression can be used to predict student performance based on multiple input values. The project also demonstrates data visualization using Seaborn and API testing using Postman.