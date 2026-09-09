# 🚀 Job Skill Extraction Using NLP

## 📌 Project Overview

**Job Skill Extraction Using Natural Language Processing (NLP)** is a project that automatically identifies relevant skills from unstructured job descriptions.

Recruiters normally need to manually read job descriptions to identify required skills. When thousands of job postings are involved, this process becomes time-consuming and inconsistent.

This project converts job descriptions into structured information containing extracted and normalized skills.

---

## 🎯 Objectives

* Automatically extract technical and professional skills from job descriptions
* Reduce manual job-description analysis
* Normalize different names and aliases of the same skill
* Identify important skills and skill categories
* Compare different NLP and machine-learning approaches
* Provide analytics through a dashboard
* Provide a user-facing Streamlit application

---

## 📊 Dataset

The project uses a public dataset containing **10,000 job postings**.

### Important Columns

| Column            | Description           |
| ----------------- | --------------------- |
| `job_id`          | Unique job identifier |
| `job_title`       | Job role/title        |
| `company`         | Hiring organization   |
| `location`        | Job location          |
| `job_description` | Full job description  |

The `job_description` column is the main input for skill extraction.

---

## 🔄 Project Workflow

```text
Job Description
       ↓
Data Collection
       ↓
Exploratory Data Analysis
       ↓
Data Cleaning
       ↓
NLP Preprocessing
       ↓
Skill Taxonomy
       ↓
Skill Extraction
       ↓
Skill Normalization
       ↓
Model Evaluation
       ↓
Dashboard
       ↓
Streamlit Application
```

---

## 🧠 NLP Techniques Used

### 1. Tokenization

Splits text into individual words/tokens.

Example:

```text
Python and SQL are required
```

becomes:

```text
Python
SQL
```

### 2. Stopword Removal

Removes common words that usually provide limited information, such as:

```text
the, is, are, and, for, in
```

### 3. Lemmatization

Converts words into their meaningful base form.

### 4. TF-IDF

Used to identify important terms in job descriptions.

### 5. N-Gram Analysis

Used to identify multi-word skills such as:

```text
Power BI
Machine Learning
Database Administration
```

### 6. Semantic Similarity

Used to identify related terms such as:

```text
ML → Machine Learning
```

### 7. Named Entity Recognition

A custom spaCy `EntityRuler` was developed to recognize technical skills using the skill taxonomy.

---

## 🗂️ Skill Taxonomy

A skill taxonomy was created to maintain canonical skill names and aliases.

Examples:

| Canonical Skill  | Aliases              |
| ---------------- | -------------------- |
| Python           | python3, python 3    |
| Power BI         | powerbi, power-bi    |
| PostgreSQL       | postgres, postgre    |
| Machine Learning | ML, machine-learning |
| AWS              | Amazon Web Services  |

This prevents the same skill from being counted multiple times.

---

## 🔍 Skill Extraction

Multiple approaches were implemented and compared:

* Dictionary Matching
* Regex / Phrase Matching
* TF-IDF
* Semantic Similarity
* Custom NER
* Machine Learning
* Transformer-based NER

A word-boundary issue was also identified where `ML` could incorrectly match inside `HTML`.

Regex word boundaries and phrase matching were used to reduce these false positives.

---

## 🤖 Machine Learning

A machine-learning pipeline using:

```text
TF-IDF
   ↓
Logistic Regression
   ↓
Skill Category Prediction
```

was implemented.

The model was trained using examples derived from the skill taxonomy.

---

## 📈 Model Evaluation

The extraction methods were evaluated using:

* Precision
* Recall
* F1 Score

### Results

| Method                  | Precision | Recall |  F1 Score |
| ----------------------- | --------: | -----: | --------: |
| Dictionary Matching     |     0.938 |  0.985 | **0.961** |
| Custom NER              |     0.943 |  0.750 |     0.836 |
| TF-IDF                  |     0.926 |  0.560 |     0.698 |
| Regex / Phrase Matching |     1.000 |  0.385 |     0.556 |
| ML Classifier           |     0.410 |  0.395 |     0.402 |
| Transformer             |     0.000 |  0.000 |     0.000 |

### 🏆 Best Performing Method

**Dictionary Matching achieved the highest F1 score of 0.961.**

This demonstrated that a simple rule-based approach can perform extremely well when the skill vocabulary is well-defined.

---

## 🔄 Skill Normalization

Different job descriptions can use different names for the same skill.

For example:

```text
Python3
python 3
Python programming
PYTHON
```

are normalized to:

```text
Python
```

Similarly:

```text
PowerBI
Power BI
Power-BI
```

are normalized to:

```text
Power BI
```

The normalization engine successfully resolved **62 out of 64 skill variants (96.9%)** in testing.

---

## 📊 Dashboard

The project dashboard provides insights such as:

* Total Jobs: **10,000**
* Unique Skills: **46**
* Top Skill: **SQL**
* Top Job Role: **Machine Learning Engineer**
* Top 20 Skills
* Skill demand by job role
* Skill category distribution

Dashboard tools:

* Power BI
* Tableau
* Matplotlib
* Seaborn

---

## 🌐 Streamlit Application

A Streamlit application was developed as the user interface.

### Application Flow

```text
User Login
    ↓
Enter Job Description
    ↓
Clean Text
    ↓
Extract Skills
    ↓
Normalize Skills
    ↓
Display Results
```

The application returns the extracted skills and role prediction where supported.

---

## 🛠️ Technologies Used

### Programming

* Python

### Data Analysis

* Pandas
* NumPy

### NLP

* NLTK
* spaCy
* sentence-transformers

### Machine Learning

* Scikit-learn
* TF-IDF
* Logistic Regression

### Deep Learning

* Hugging Face Transformers
* BERT

### Visualization

* Matplotlib
* Seaborn
* Power BI
* Tableau

### Application

* Streamlit
* FastAPI

---

## 📁 Project Structure

```text
Job_Skill_Extraction/
│
├── data/
├── notebooks/
├── models/
├── utils/
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project

```bash
cd Job_Skill_Extraction
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Streamlit application

```bash
streamlit run app.py
```

---

## 🔮 Future Scope

The project can be extended with:

* Resume–Job Matching
* Candidate Ranking
* Skill Gap Analysis
* Training/Course Recommendations
* Fine-tuned Transformer-based Skill Extraction
* Expanded Skill Taxonomy
* Integration with Applicant Tracking Systems

---

## 📚 Key Learning Outcomes

Through this project, I gained practical experience in:

* Natural Language Processing
* Text preprocessing
* Skill extraction
* Machine Learning
* Model evaluation
* Error analysis
* Data visualization
* Streamlit application development
* Building an end-to-end NLP pipeline

---

## 👨‍💻 Author

**Abdulsamad Mulla**

GitHub: https://github.com/Abdulsamad-Mulla

---

## ⭐ Acknowledgement

This project was developed as part of an internship project focused on NLP, machine learning and data analytics.
