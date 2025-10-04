import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    df = pd.read_csv('electrical_grid.csv')

    print_basic_info(df)

    # ВИЗУАЛИЗАЦИЯ РАСПРЕДЕЛЕНИЙ ПРИЗНАКОВ
    plot_single_histogram(df)
    plot_multiple_histograms(df)
    plot_single_boxplot(df)
    plot_numerical_boxplots(df)

    # АНАЛИЗ КАТЕГОРИАЛЬНЫХ ДАННЫХ
    plot_target_countplot(df)
    plot_bar_chart_elasticity(df)

    # АНАЛИЗ ВЗАИМОСВЯЗЕЙ МЕЖДУ ПРИЗНАКАМИ
    plot_stability_comparison(df)
    plot_pairwise_comparison(df)
    plot_scatter_plot(df)

    # КОРРЕЛЯЦИОННЫЙ АНАЛИЗ
    plot_correlation_heatmap(df)
    plot_top_correlated_features(df)

    # ДОПОЛНИТЕЛЬНЫЕ ВИЗУАЛИЗАЦИИ
    plot_violin_plot(df)
    plot_facet_grid_corrected(df)


def print_basic_info(df):
    """
    ВЫВОД БАЗОВОЙ ИНФОРМАЦИИ О ДАТАСЕТЕ
    """
    print("Первые 10 строк датасета:")
    print(df.head(10))
    print(f"\nРазмер датасета: {df.shape[0]} строк, {df.shape[1]} столбцов")
    print("\nТипы данных:")
    print(df.dtypes)
    print("\nПроверка на пропущенные значения:")
    print(df.isnull().sum())
    print("\nСводная информация:")
    print(df.info())


def plot_single_histogram(df):
    """
    ГИСТОГРАММА РАСПРЕДЕЛЕНИЯ ВРЕМЕНИ РЕАКЦИИ УЗЛА-ПОСТАВЩИКА (TAU1)
    """
    plt.figure(figsize=(10, 6))
    df['tau1'].hist(bins=30, edgecolor='black', alpha=0.7, color='skyblue')
    plt.title('Гистограмма распределения времени реакции узла-поставщика (tau1)')
    plt.xlabel('Время реакции (tau1)')
    plt.ylabel('Частота')
    plt.grid(axis='y', alpha=0.75)
    plt.show()


def plot_multiple_histograms(df):
    """
    ГИСТОГРАММА РАСПРЕДЕЛЕНИЙ ВСЕХ ЧИСЛОВЫХ ПРИЗНАКОВ
    """
    numerical_columns = df.select_dtypes(include=[np.number]).columns
    df[numerical_columns].hist(figsize=(15, 12), bins=20, edgecolor='black', alpha=0.7)
    plt.suptitle('Гистограммы распределений всех числовых признаков', fontsize=16)
    plt.tight_layout()
    plt.show()


def plot_single_boxplot(df):
    """
    ЯЩИК С УСАМИ ДЛЯ ВРЕМЕНИ РЕАКЦИИ УЗЛА-ПОСТАВЩИКА (TAU1)
    """
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, y='tau1', color='lightblue')
    plt.title('Ящик с усами для времени реакции узла-поставщика (tau1)')
    plt.ylabel('Время реакции (tau1)')
    plt.show()


def plot_numerical_boxplots(df):
    """
    ЯЩИКИ С УСАМИ ДЛЯ ВСЕХ ЧИСЛОВЫХ ПРИЗНАКОВ
    """
    plt.figure(figsize=(12, 8))
    numerical_data = df.select_dtypes(include=[np.number])
    sns.boxplot(data=numerical_data)
    plt.title('Ящики с усами для распределения числовых признаков')
    plt.xlabel('Признаки')
    plt.ylabel('Значения')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_target_countplot(df):
    """
    СТОЛБЧАТАЯ ДИАГРАММА РАСПРЕДЕЛЕНИЯ СТАБИЛЬНОСТИ ЭЛЕКТРИЧЕСКОЙ СЕТИ
    """
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, x='stabf', hue='stabf', palette=['red', 'green'], legend=False)
    plt.title('Распределение стабильности электрической сети')
    plt.xlabel('Статус стабильности')
    plt.ylabel('Количество наблюдений')
    plt.show()


def plot_bar_chart_elasticity(df):
    """
    СТОЛБЧАТАЯ ДИАГРАММА СРЕДНИХ ЗНАЧЕНИЙ КОЭФФИЦИЕНТОВ ЭЛАСТИЧНОСТИ
    """
    elasticity_features = ['g1', 'g2', 'g3', 'g4']
    mean_elasticity = df[elasticity_features].mean()

    plt.figure(figsize=(10, 6))
    bars = plt.bar(elasticity_features, mean_elasticity.values,
                   color=['lightblue', 'lightgreen', 'lightcoral', 'gold'])
    plt.title('Средние значения коэффициентов ценовой эластичности по узлам сети')
    plt.xlabel('Коэффициенты эластичности')
    plt.ylabel('Среднее значение')

    for bar, value in zip(bars, mean_elasticity.values):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.001,
                 f'{value:.3f}', ha='center', va='bottom')

    plt.grid(axis='y', alpha=0.3)
    plt.show()


def plot_stability_comparison(df):
    """
    СРАВНЕНИЕ РАСПРЕДЕЛЕНИЙ ПРИЗНАКОВ ДЛЯ СТАБИЛЬНЫХ И НЕСТАБИЛЬНЫХ СЕТЕЙ
    """
    comparison_features = ['tau1', 'p1', 'g1']

    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    for i, feature in enumerate(comparison_features):
        # ящики для каждого признака по группам стабильности
        sns.boxplot(data=df, x='stabf', y=feature, ax=axes[i],
                    palette={'stable': 'lightgreen', 'unstable': 'lightcoral'})
        if feature.startswith('tau'):
            axes[i].set_ylabel('Время реакции')
        elif feature.startswith('p'):
            axes[i].set_ylabel('Номинальная мощность')
        elif feature.startswith('g'):
            axes[i].set_ylabel('Коэффициент ценовой эластичности')

        axes[i].set_xlabel('Стабильность сети')
        feature_name = get_feature_russian_name(feature)
        axes[i].set_title(f'Распределение {feature}\n({feature_name})')

    plt.tight_layout()
    plt.show()


def plot_pairwise_comparison(df):
    """
    ПОПАРНОЕ СРАВНЕНИЕ ПРИЗНАКОВ
    """
    # подмножество признаков
    selected_features = ['tau1', 'tau2', 'p1', 'p2', 'g1', 'g2', 'stabf']

    sns.pairplot(df[selected_features],
                 hue='stabf',
                 palette={'stable': 'green', 'unstable': 'red'},
                 diag_kind='hist',
                 plot_kws={'alpha': 0.6})

    plt.suptitle('Попарное сравнение ключевых признаков электрической сети', y=1.02)
    plt.show()


def plot_top_correlated_features(df):
    """
    АНАЛИЗ ПРИЗНАКОВ, НАИБОЛЕЕ КОРРЕЛИРУЮЩИХ СО СТАБИЛЬНОСТЬЮ СЕТИ
    """
    df_numeric = df.copy()
    df_numeric['stabf'] = df_numeric['stabf'].map({'stable': 0, 'unstable': 1})

    correlation_with_target = df_numeric.corr()['stabf'].sort_values(ascending=False)

    print("Корреляция признаков со стабильностью сети:")
    for feature, corr in correlation_with_target.items():
        if feature != 'stabf':
            feature_name = get_feature_russian_name(feature)
            print(f"{feature} ({feature_name}): {corr:.3f}")

    top_features = correlation_with_target[1:7].index

    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.ravel()

    for i, feature in enumerate(top_features):
        sns.boxplot(data=df, x='stabf', y=feature, ax=axes[i],
                    palette={'stable': 'lightgreen', 'unstable': 'lightcoral'})

        feature_name = get_feature_russian_name(feature)
        axes[i].set_title(f'{feature} ({feature_name})\nкорр: {correlation_with_target[feature]:.3f}')
        axes[i].set_xlabel('Стабильность сети')
        axes[i].set_ylabel(feature_name)

    plt.tight_layout()
    plt.show()


def plot_violin_plot(df):
    """
    ГРАФИК СКРИПКИ ДЛЯ ДЕТАЛЬНОГО АНАЛИЗА РАСПРЕДЕЛЕНИЙ
    """
    plt.figure(figsize=(12, 8))
    sns.violinplot(data=df, x='stabf', y='p1',
                   palette={'stable': 'lightgreen', 'unstable': 'lightcoral'})
    plt.title('График скрипки для распределения номинальной мощности узла-поставщика (p1)')
    plt.xlabel('Стабильность сети')
    plt.ylabel('Номинальная мощность (p1)')
    plt.show()


def plot_scatter_plot(df):
    """
    ТОЧЕЧНАЯ ДИАГРАММА ДЛЯ АНАЛИЗА ВЗАИМОСВЯЗИ МЕЖДУ ПРИЗНАКАМИ
    """
    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=df, x='p1', y='g1', hue='stabf',
                    palette={'stable': 'green', 'unstable': 'red'}, alpha=0.6)
    plt.title('Взаимосвязь между мощностью и ценовой эластичностью узла-поставщика')
    plt.xlabel('Номинальная мощность (p1)')
    plt.ylabel('Коэффициент ценовой эластичности (g1)')
    plt.legend(title='Стабильность сети')
    plt.show()


def plot_facet_grid_corrected(df):
    """
    ФАСЕТНАЯ СЕТКА ДЛЯ АНАЛИЗА РАСПРЕДЕЛЕНИЙ ПО ГРУППАМ С ИСПРАВЛЕННЫМ ЗАГОЛОВКОМ
    """
    g = sns.FacetGrid(df, col='stabf', height=5, aspect=1.2)
    g.map(sns.histplot, 'tau1', kde=True, color='skyblue', edgecolor='black')
    g.set_titles('Стабильность: {col_name}')
    g.set_axis_labels('Время реакции узла-поставщика (tau1)', 'Частота')

    plt.subplots_adjust(top=0.85)
    g.fig.suptitle('Распределение времени реакции для разных состояний стабильности')
    plt.show()


def plot_correlation_heatmap(df):
    """
    ТЕПЛОВАЯ КАРТА МАТРИЦЫ КОРРЕЛЯЦИИ ПРИЗНАКОВ
    """
    df_numeric = df.copy()
    df_numeric['stabf'] = df_numeric['stabf'].map({'stable': 0, 'unstable': 1})

    plt.figure(figsize=(12, 10))
    correlation_matrix = df_numeric.corr()

    sns.heatmap(correlation_matrix,
                annot=True,
                cmap='coolwarm',
                center=0,
                fmt='.2f',
                linewidths=0.5,
                cbar_kws={'shrink': 0.8})

    plt.title('Тепловая карта матрицы корреляции признаков электрической сети', fontsize=16)
    plt.tight_layout()
    plt.show()


def get_feature_russian_name(feature):
    """
    ВОЗВРАЩАЕТ РУССКОЕ ОПИСАНИЕ ПРИЗНАКА ДЛЯ ПОДПИСЕЙ НА ГРАФИКАХ
    """
    feature_descriptions = {
        'tau1': 'Время реакции узла-поставщика',
        'tau2': 'Время реакции узла-потребителя 1',
        'tau3': 'Время реакции узла-потребителя 2',
        'tau4': 'Время реакции узла-потребителя 3',
        'p1': 'Номинальная мощность узла-поставщика',
        'p2': 'Номинальная мощность узла-потребителя 1',
        'p3': 'Номинальная мощность узла-потребителя 2',
        'p4': 'Номинальная мощность узла-потребителя 3',
        'g1': 'Коэффициент ценовой эластичности узла-поставщика',
        'g2': 'Коэффициент ценовой эластичности узла-потребителя 1',
        'g3': 'Коэффициент ценовой эластичности узла-потребителя 2',
        'g4': 'Коэффициент ценовой эластичности узла-потребителя 3',
        'stabf': 'Стабильность сети'
    }
    return feature_descriptions.get(feature, feature)


if __name__ == "__main__":
    main()
