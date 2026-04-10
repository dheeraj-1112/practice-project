# Simple Resume Matching Logic

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

resume = "Python developer with knowledge of data analysis and machine learning"
job_description = "Looking for a Python developer with data analysis skills"

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform([resume, job_description])

similarity = cosine_similarity(vectors[0], vectors[1])

print("Match Score:", similarity[0][0])
