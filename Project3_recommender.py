"""
DecodeLabs Internship - Project 3
AI Recommendation Logic (Content-Based Filtering)

Capstone: Tech Stack Recommender
Maps a user's raw skills to the closest-matching job roles using
TF-IDF vectorization and Cosine Similarity (content-based filtering).

Pipeline: Input (skills) -> Process (TF-IDF + Cosine Similarity) -> Output (Top-N roles)
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ---------------------------------------------------------
# 1. DATASET: Job roles mapped to their required skills
# (Acts as our "raw_skills.csv" — each role is an "item")
# ---------------------------------------------------------
job_roles = {
    "Data Scientist": "python sql machine learning data analysis statistics pandas",
    "DevOps Engineer": "aws docker kubernetes ci cd automation cloud linux",
    "Backend Developer": "java python sql apis rest databases spring",
    "Frontend Developer": "html css javascript react ui design responsive",
    "Cloud Architect": "aws azure cloud computing automation networking security",
    "AI/ML Engineer": "python machine learning deep learning tensorflow pytorch neural networks",
    "Data Analyst": "sql excel data analysis visualization tableau powerbi statistics",
    "Full Stack Developer": "javascript react node.js python sql apis html css",
}

TOP_N = 3  # how many recommendations to show


def get_user_skills():
    """Ingest step: collect at least 3 skills from the user."""
    print("Enter your skills one by one (minimum 3). Type 'done' when finished.")
    skills = []
    while True:
        skill = input(f"Skill {len(skills) + 1}: ").strip()
        if skill.lower() == "done":
            if len(skills) < 3:
                print("Please enter at least 3 skills before typing 'done'.")
                continue
            break
        if skill:
            skills.append(skill)
    return skills


def recommend_roles(user_skills, roles: dict, top_n: int = TOP_N):
    """
    Process step: Build TF-IDF vectors for the user profile and all job
    roles, then rank roles by cosine similarity (angular alignment).
    """
    role_names = list(roles.keys())
    role_texts = list(roles.values())

    # The user's profile is just their skills joined into one "document"
    user_text = " ".join(user_skills)

    # Combine user profile + all role descriptions into a shared vocabulary space
    documents = [user_text] + role_texts

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    # Compare the user vector (row 0) against every role vector (rows 1+)
    user_vector = tfidf_matrix[0:1]
    role_vectors = tfidf_matrix[1:]

    scores = cosine_similarity(user_vector, role_vectors).flatten()

    # Sort roles by score (descending) and filter to Top-N
    ranked = sorted(zip(role_names, scores), key=lambda x: x[1], reverse=True)
    return ranked[:top_n]


def main():
    print("=" * 55)
    print("  AI Tech Stack Recommender - DecodeLabs Project 3")
    print("=" * 55)

    user_skills = get_user_skills()
    print(f"\nYour skills: {', '.join(user_skills)}")

    results = recommend_roles(user_skills, job_roles)

    print("\nTop recommended career paths for you:")
    print("-" * 55)
    for rank, (role, score) in enumerate(results, start=1):
        match_percent = round(score * 100, 1)
        print(f"{rank}. {role}  —  {match_percent}% match")

    if all(score == 0 for _, score in results):
        print("\nNo strong matches found (Cold Start). "
              "Try adding more common tech skills like 'python' or 'sql'.")


if __name__ == "__main__":
    main()
