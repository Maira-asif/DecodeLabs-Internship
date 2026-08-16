"""
DecodeLabs Internship - Project 2
Data Classification Using AI (Supervised Learning)

Goal: Build a basic classification model using the Iris dataset.
Pipeline: Load -> Scale -> Split -> Train (KNN) -> Predict -> Evaluate
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, f1_score


def main():
    # ---------------------------------------------------------
    # 1. INPUT: Load and understand the dataset
    # ---------------------------------------------------------
    iris = load_iris()
    X = iris.data          # features: sepal length, sepal width, petal length, petal width
    y = iris.target        # labels: 0=setosa, 1=versicolor, 2=virginica

    print("Dataset shape:", X.shape)
    print("Classes:", iris.target_names)
    print("Feature names:", iris.feature_names)
    print("-" * 50)

    # ---------------------------------------------------------
    # 2. PROCESS (part A): Train-test split
    # 80% training, 20% testing, shuffled to avoid order bias
    # ---------------------------------------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, shuffle=True
    )

    # ---------------------------------------------------------
    # 2. PROCESS (part B): Feature scaling
    # KNN is distance-based, so features must be on the same scale
    # ---------------------------------------------------------
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # ---------------------------------------------------------
    # 2. PROCESS (part C): Train the KNN classifier
    # ---------------------------------------------------------
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X_train_scaled, y_train)

    # ---------------------------------------------------------
    # 3. OUTPUT: Predict and evaluate
    # ---------------------------------------------------------
    predictions = model.predict(X_test_scaled)

    accuracy = accuracy_score(y_test, predictions)
    f1 = f1_score(y_test, predictions, average="weighted")

    print(f"Accuracy: {accuracy * 100:.2f}%")
    print(f"F1 Score (weighted): {f1:.2f}")
    print("-" * 50)
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, predictions))
    print("-" * 50)
    print("Classification Report:")
    print(classification_report(y_test, predictions, target_names=iris.target_names))

    # ---------------------------------------------------------
    # Bonus: Predict a single new flower sample
    # ---------------------------------------------------------
    sample = [[5.1, 3.5, 1.4, 0.2]]  # example measurements
    sample_scaled = scaler.transform(sample)
    predicted_class = model.predict(sample_scaled)
    print("-" * 50)
    print(f"New sample {sample} predicted as: {iris.target_names[predicted_class[0]]}")


if __name__ == "__main__":
    main()
