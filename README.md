# 📖 Bhagavad Gita AI Search Engine

A production-ready semantic search engine for the Bhagavad Gita built using **FastAPI, Docker, AWS, CI/CD, and Streamlit**.

---

## 🚀 Features

- 🔍 Semantic Search over Bhagavad Gita verses
- ⚡ FastAPI backend
- 🐳 Dockerized application
- ☁ Deployed on AWS EC2
- 🔁 CI/CD using GitHub Actions
- 💬 ChatGPT-style Streamlit UI
- 🧠 Config-driven architecture (YAML-based)

---

## 🏗 Architecture

Frontend (Streamlit Cloud)  
⬇  
Backend API (FastAPI on AWS EC2)  
⬇  
Search Pipeline (Embedding + Retrieval)

---


## 📂 Project Structure

```
search_engine_project/
│
├── .github/
│   └── workflows/
│       └── .gitkeep
│
├── artifacts/
│   ├── chunks.json
│   ├── embeddings.pkl
│   ├── inverted_index.json
│   ├── metadata.json
│   ├── tfidf_matrix.pkl
│   └── vectorizer.pkl
│
├── data/
│   ├── processed/
│   └── raw/
│
├── logs/
├── research/
├── senv/
│
├── src/
│   ├── components/
│   │   ├── __init__.py
│   │   ├── document_chunker.py
│   │   ├── embedding_model.py
│   │   ├── evaluator.py
│   │   ├── hybrid_search_engine.py
│   │   ├── index_builder.py
│   │   ├── pdf_loader.py
│   │   ├── preprocessor.py
│   │   ├── search_engine.py
│   │   ├── semantic_search_engine.py
│   │   └── tfidf_vectorizer.py
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   └── configuration.py
│   │
│   ├── logger/
│   │   ├── __init__.py
│   │   └── logger.py
│   │
│   ├── pipeline/
│   │   ├── __init__.py
│   │   ├── embedding_training_pipeline.py
│   │   ├── ingestion_pipeline.py
│   │   ├── search_pipeline.py
│   │   └── training_pipeline.py
│   │
│   ├── schemas/
│   │   ├── response.py
│   │   └── user_query.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── storage.py
│   │   └── exception.py
│   │
│   └── __init__.py
│
├── tests/
│   ├── __init__.py
│   ├── test_chunking.py
│   ├── test_embedding_training.py
│   ├── test_evaluator.py
│   ├── test_hybrid_search_engine.py
│   ├── test_index_builder.py
│   ├── test_ingestion.py
│   ├── test_search_engine.py
│   ├── test_search_pipeline.py
│   ├── test_semantic_search_engine.py
│   └── test_training.py
│
├── .gitignore
├── Dockerfile
├── LICENSE
├── main.py
├── README.md
├── requirements.txt
├── setup.py
├── templates.py
└── test_pdf_pipeline.py
```


---

## ⚙️ Tech Stack

- Python 3.10
- FastAPI
- Uvicorn
- Streamlit
- Docker
- AWS EC2
- GitHub Actions
- YAML Configuration

---

## 🛠 Installation (Local Development)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/bhagavad-gita-api.git
cd bhagavad-gita-api
```

## 2 Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
## 3 Install Dependencies
```
pip install -r requirements.txt
```

## 4 Run server
```aiignore
uvicorn main:app --relaod
```
### API docs 
```aiignore
http://127.0.0.1:8000/docs
```

### Docker Usage
#### Build image
```aiignore
docker build -t bhagavad-gita-api .
```
#### Run container
```aiignore
docker run -p 8000:8000 bhagavad-gita-api
```

---

## 🔁 CI/CD Deployment

On every push to `main` branch:

- GitHub Actions builds Docker image  
- Pushes image to Docker Hub  
- SSH into AWS EC2  
- Pulls latest image  
- Restarts container  

🚀 Fully automated deployment pipeline.

---

## ☁ Deployment

### Backend
- Hosted on AWS EC2  
- Docker containerized  

### Frontend
- Deployed on Streamlit Cloud  
- Connected to AWS backend API  

---

## 📌 API Endpoint

### POST `/search`

### Request

```json
{
  "query": "What is Karma Yoga?"
}
```

### Response

```json
[
  {
    "content": "A true Karma-yogi becomes free from both vice and virtue..."
  }
]
```

---

---

## 📈 Future Improvements

- Add authentication  
- Add Redis caching  
- Add HTTPS with Nginx  
- Use AWS ECR instead of Docker Hub  
- Add vector database (FAISS / Pinecone)  

---

## 👨‍💻 Author

Navneet Kumar  

---

## 📜 License

MIT License  

---

## 🔥 Badges

```markdown
![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![AWS](https://img.shields.io/badge/AWS-Cloud-orange)
```