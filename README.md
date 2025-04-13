
# 📝 Product Review Helpfulness Detection System using LSTM and BERT

## 📌 Introduction

In today’s e-commerce landscape, customers rely heavily on product reviews to guide purchasing decisions. However, the sheer volume of reviews makes it difficult to identify helpful and trustworthy feedback. This project presents a **hybrid sentiment analysis system** that leverages **LSTM** and **BERT** models to classify reviews as Positive, Negative, or Neutral, while also **assessing the helpfulness** of each review.

## 💡 Motivation

Traditional machine learning models like Random Forest and Decision Trees often fail to capture deep semantic meaning, long-range dependencies, and nuances like sarcasm. To address these limitations, this system integrates:

- **LSTM (Long Short-Term Memory)** for understanding sequential patterns in text
- **BERT (Bidirectional Encoder Representations from Transformers)** for capturing word context and bidirectional relationships

This hybrid model is deployed as a **Flask web application** for real-time sentiment prediction and helpfulness scoring.

---

## 🎯 Objectives

### General Objective
To develop an advanced sentiment analysis model using LSTM and BERT to improve review classification accuracy and usefulness prediction.

### Specific Objectives
- Improve sentiment classification accuracy using deep learning.
- Enhance contextual understanding with BERT embeddings.
- Capture long-term dependencies using LSTM.
- Provide helpfulness predictions based on class probability scores.
- Deploy a scalable and user-friendly Flask-based web interface.

---

## 🛠️ Technologies Used

- Python
- Flask
- TensorFlow / PyTorch
- BERT (Hugging Face Transformers)
- LSTM (Keras/TensorFlow)
- Scikit-learn
- Amazon Fine Food Reviews Dataset

---

## 🚀 Features

- Real-time classification of product reviews into **Positive, Negative, or Neutral**
- Helpfulness scoring based on **class probability confidence**
- User-friendly web interface for text input and predictions
- Evaluation using **Accuracy**, **Precision**, **Recall**, and **F1-score**

---

## 📁 Dataset

- **Amazon Fine Food Reviews Dataset**
  - Over 500,000 food-related product reviews
  - Includes review text, ratings, and helpfulness votes

---

## 📷 Screenshots (Optional)

<!-- Add screenshots if you have them -->
```
[Insert Image: Web app interface showing sentiment and helpfulness output]
```

---

## ⚙️ Installation & Usage

### Clone the Repository
```bash
git clone https://github.com/yourusername/sentiment-helpfulness-lstm-bert.git
cd sentiment-helpfulness-lstm-bert
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the Flask Application
```bash
python app.py
```

Access the app at: `http://127.0.0.1:5000/`

---

## 📊 Evaluation

The model is evaluated using standard classification metrics:
- **Accuracy**
- **Precision**
- **Recall**
- **F1-score**

It outperforms traditional models like Random Forest and Decision Tree in both sentiment classification and helpfulness estimation.

---

## 📚 Project Structure

```bash
├── app.py                 # Flask backend
├── model/
│   ├── bert_model.py      # BERT integration
│   └── lstm_model.py      # LSTM implementation
├── templates/
│   └── index.html         # Web frontend
├── static/
│   └── style.css          # Optional styling
├── data/
│   └── Reviews.csv        # Preprocessed dataset
└── README.md              # This file
```

---

## 🔮 Future Enhancements

- Multilingual support for non-English reviews
- Integration with real-time review APIs from Amazon, Flipkart, etc.
- Improved visualization of helpfulness scoring

---

## 📄 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgements

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Amazon Fine Food Reviews Dataset](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews)
- [Flask Framework](https://flask.palletsprojects.com/)

---

Let me know if you'd like help with any of these:
- Generating `requirements.txt`
- Adding screenshots
- Writing a basic Flask `app.py`
- Creating the LICENSE file

Would you like me to help format this directly into a `README.md` file you can upload?
