import numpy as np
import pandas as pd


def main():
    df = pd.read_csv('beer.tsv', sep=' ')

    print_first_14_rows(df)
    print_shape(df)
    print_info(df)
    set_index_by_name(df)
    print_top5_high_alcohol(df)
    print_top5_low_alcohol(df)
    convert_calories_and_stats(df)
    sort_by_calories(df)
    print_sodium_limits(df)
    split_by_cost_categories(df)
    print_most_caloric_cheap(df)
    analyze_calories_cost_relationship(df)
    analyze_alcohol_calories_relationship(df)


def print_first_14_rows(df):
    print("\n1. Вывод первых 14 строк из файла beer.tsv:")
    print(df.head(14))


def print_shape(df):
    print("\n2. Кол-во строк и столбцов:")
    print(f"Количество строк: {df.shape[0]}")
    print(f"Количество столбцов: {df.shape[1]}")


def print_info(df):
    print("\n3. Сводная информация по датафрейму:")
    print(df.info)


def set_index_by_name(df):
    print("\n4. Проиндексируйте набор данных по полю name:")
    df_indexed = df.set_index('name')
    print(df_indexed.head())


def print_top5_high_alcohol(df):
    print("\n5. TOP-5 продуктов с наибольшим содержанием алкоголя:")
    top5_high_alcohol = df.nlargest(5, 'alcohol')[['name', 'alcohol']]
    print(top5_high_alcohol)


def print_top5_low_alcohol(df):
    print("\n6. TOP-5 продуктов с наименьшим содержанием алкоголя:")
    top5_low_alcohol = df.nsmallest(5, 'alcohol')[['name', 'alcohol']]
    print(top5_low_alcohol)


def convert_calories_and_stats(df):
    print("\n7. Преобразование столбца calories в float и статистика:")
    df['calories'] = df['calories'].astype(float)
    calories_stats = df['calories'].describe()
    print(calories_stats)


def sort_by_calories(df):
    print("\n8. Набор данных, отсортированный по calories (по убыванию):")
    df_sorted_calories = df.sort_values('calories', ascending=False)
    print(df_sorted_calories)


def print_sodium_limits(df):
    print("\n9. Пределы содержания натрия:")
    sodium_min = df['sodium'].min()
    sodium_max = df['sodium'].max()
    print(f"Пределы: от {sodium_min} до {sodium_max}")
    print(f"Среднее содержание натрия: {df['sodium'].mean():.2f}")


def split_by_cost_categories(df):
    print("\n10. Разделение на три категории стоимости:")

    cost_q1 = df['cost'].quantile(0.33)
    cost_q3 = df['cost'].quantile(0.67)

    print(f"\nГраницы категорий по квартилям:")
    print(f"Дешевое: cost < {cost_q1:.3f} (нижние 33%)")
    print(f"Средней стоимости: {cost_q1:.3f} ≤ cost ≤ {cost_q3:.3f} (средние 34%)")
    print(f"Дорогое: cost > {cost_q3:.3f} (верхние 33%)")

    df_cheap = df[df['cost'] < cost_q1]
    df_medium = df[(df['cost'] >= cost_q1) & (df['cost'] <= cost_q3)]
    df_expensive = df[df['cost'] > cost_q3]

    print(f"\nРезультаты разделения:")
    print(f"Дешевое пиво: {len(df_cheap)} шт")
    print(df_cheap[['name', 'cost']].to_string(index=False))

    print(f"\nПиво средней стоимости: {len(df_medium)} шт")
    print(df_medium[['name', 'cost']].to_string(index=False))

    print(f"\nДорогое пиво: {len(df_expensive)} шт")
    print(df_expensive[['name', 'cost']].to_string(index=False))


def print_most_caloric_cheap(df):
    print("\n11. Наиболее калорийное пиво среди дешевых:")
    cost_q1 = df['cost'].quantile(0.33)
    df_cheap = df[df['cost'] < cost_q1]

    most_caloric_cheap = df_cheap.nlargest(1, 'calories')[['name', 'calories']]
    print(most_caloric_cheap.to_string(index=False))


def analyze_calories_cost_relationship(df):
    print("\n12. Существует ли какая-либо связь между калорийностью и стоимостью пива?")

    df_copy = df.copy()
    features_to_drop = ['name', 'sodium', 'alcohol']
    df_copy.drop(features_to_drop, axis=1, inplace=True)
    median_cost = df_copy['cost'].median()
    df_copy['cost_indicator'] = np.where(df_copy['cost'] > median_cost, 1, 0)
    df_copy.drop('cost', axis=1, inplace=True)
    print(f"\nМедианное содержание стоимости: {median_cost:.1f}%")
    print("Датафрейм calories и cost с бинарным индикатором стоимости:")
    print(df_copy.head())

    calories_by_cost = df_copy.groupby('cost_indicator').mean()
    print(f"\nАнализ связи:")
    print(f"Недорогое пиво (cost_indicator = 0): средняя калорийность = {calories_by_cost.loc[0, 'calories']:.1f}")
    print(f"Дорогое пиво (cost_indicator = 1): средняя калорийность = {calories_by_cost.loc[1, 'calories']:.1f}")

    difference = calories_by_cost.loc[1, 'calories'] - calories_by_cost.loc[0, 'calories']
    if difference > 0:
        print(f"Дорогое пиво в среднем на {difference:.1f} калорий калорийнее")
    else:
        print(f"Дорогое пиво в среднем на {abs(difference):.1f} калорий менее калорийное")


def analyze_alcohol_calories_relationship(df):
    print("\n13. Влияет ли содержание алкоголя на калорийность?")

    df_copy = df.copy()
    features_to_drop = ['name', 'sodium', 'cost']
    df_copy.drop(features_to_drop, axis=1, inplace=True)
    median_alcohol = df_copy['alcohol'].median()
    df_copy['alcohol_indicator'] = np.where(df_copy['alcohol'] > median_alcohol, 1, 0)
    df_copy.drop('alcohol', axis=1, inplace=True)

    print(f"\nМедианное содержание алкоголя: {median_alcohol:.1f}%")
    print("Датафрейм alcohol и calories с бинарным индикатором алкоголя:")
    print(df_copy.head())

    calories_by_alcohol = df_copy.groupby('alcohol_indicator').mean()
    print(f"\nАнализ влияния алкоголя на калорийность:")
    print(
        f"Слабоалкогольное пиво (alcohol_indicator = 0): средняя калорийность = {calories_by_alcohol.loc[0, 'calories']:.1f}")
    print(f"Крепкое пиво (alcohol_indicator = 1): средняя калорийность = {calories_by_alcohol.loc[1, 'calories']:.1f}")

    difference = calories_by_alcohol.loc[1, 'calories'] - calories_by_alcohol.loc[0, 'calories']
    if difference > 0:
        print(f"Крепкое пиво в среднем на {difference:.1f} калорий калорийнее")
    else:
        print(f"Крепкое пиво в среднем на {abs(difference):.1f} калорий менее калорийное")


if __name__ == "__main__":
    main()
