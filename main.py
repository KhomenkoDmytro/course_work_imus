import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
from scipy.stats import kstest

class Person:
    def __init__(self, age, education, belief):
        self.age = age
        self.education = education
        self.belief = belief

def generate_people(sample_size, mean, std_dev):
    people = []
    beliefs = np.random.normal(mean, std_dev, sample_size)
    ages = np.random.randint(18, 65, sample_size)
    education_levels = np.random.randint(1, 4, sample_size)

    for i in range(sample_size):
        belief_age = beliefs[i] + 0.005 * (ages[i] - 40)
        belief_education = beliefs[i] - 0.3 * (education_levels[i] - 2)
        combined_belief = belief_age + belief_education - beliefs[i]
        people.append(Person(ages[i], education_levels[i], combined_belief))

    return people

def plot_data(people, attribute, title, subplot_position):
    beliefs = [getattr(person, attribute) for person in people]
    plt.subplot(3, 1, subplot_position)
    sns.histplot(beliefs, kde=True)
    plt.title(title)
    plt.xlabel('Політичні переконання')
    plt.ylabel('Кількість виборців')

mean = 0
std_dev = 1

try:
    sample_size = int(input("Введіть розмір вибірки: "))
    if sample_size <= 0:
        raise ValueError("Розмір вибірки повинен бути більше нуля.")

    start_time = time.time()

    people = generate_people(sample_size, mean, std_dev)

    plt.figure(figsize=(10, 18))

    plot_data(people, 'belief', f'Гістрограма політичних переконань (Вибірка {sample_size})', 1)

    plt.tight_layout()
    plt.show()

    end_time = time.time()
    print(f"Час симуляції: {end_time - start_time:.2f} секунди.")

    beliefs = [person.belief for person in people]
    ks_result = kstest(beliefs, 'norm', args=(mean, std_dev))

    print("\nРезультати KS тесту:")
    print(f"Розподіл: KS статистика = {ks_result[0]:.4f}, P-значення = {ks_result[1]:.4f}")

except ValueError as e:
    print(e)
