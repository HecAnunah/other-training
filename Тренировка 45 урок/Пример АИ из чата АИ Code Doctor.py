

import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Загружаем набор данных Ирисов
iris = datasets.load_iris()
X = iris.data  # Признаки (длина и ширина чашелистика и лепестка)
Y = iris.target  # Метки классов (виды ирисов). Делим данные на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
# Создаем классификатор KNN

knn = KNeighborsClassifier(n_neighbors=3)  # Обучаем модель
knn.fit(X_train, y_train)  # Делаем предсказания
y_pred = knn.predict(X_test)# Вычисляем точность
accuracy = accuracy_score(y_test, y_pred)# Выводим результаты
print("Предсказанные метки:", y_pred)
print("Фактические метки:", y_test)
print("Точность модели:", accuracy)
