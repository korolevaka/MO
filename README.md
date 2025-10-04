# Результат выполнения ЛР, вар.8

<img width="912" height="899" alt="image" src="https://github.com/user-attachments/assets/1f18ee63-aed8-4fa9-bc7e-9a3e41a74db4" />


<img width="428" height="433" alt="image" src="https://github.com/user-attachments/assets/e54b9290-4e67-4330-a93d-06c02a1a16b5" />


<img width="530" height="561" alt="image" src="https://github.com/user-attachments/assets/91807bc8-7b75-49bd-8d0f-1eb6480259c9" />


ГИСТОГРАММА РАСПРЕДЕЛЕНИЯ ВРЕМЕНИ РЕАКЦИИ УЗЛА-ПОСТАВЩИКА (TAU1)
Метод: plot_single_histogram(df)

<img width="974" height="587" alt="image" src="https://github.com/user-attachments/assets/8dac2303-ee1b-4e0d-b5f3-71d9ae8b0750" />

ГИСТОГРАММА РАСПРЕДЕЛЕНИЙ ВСЕХ ЧИСЛОВЫХ ПРИЗНАКОВ
Метод: plot_multiple_histograms(df)
Набор гистограмм для всех числовых столбцов в датасете. 
 
<img width="974" height="582" alt="image" src="https://github.com/user-attachments/assets/84388ece-5b49-40fb-b2df-10d8cf50a42d" />


ЯЩИК С УСАМИ ДЛЯ ВРЕМЕНИ РЕАКЦИИ УЗЛА-ПОСТАВЩИКА (TAU1)
Метод: plot_single_boxplot(df)
Выбросы, отображаемые точками, не наблюдаются. 

<img width="974" height="757" alt="image" src="https://github.com/user-attachments/assets/00a2155a-1dd9-4dbe-a8da-4aa4f5fbe293" />


ЯЩИКИ С УСАМИ ДЛЯ ВСЕХ ЧИСЛОВЫХ ПРИЗНАКОВ
Метод: plot_numerical_boxplots(df)
Выбросы, отображаемые точками, наблюдаются для p1 (Номинальная мощность узла-поставщика)

<img width="974" height="584" alt="image" src="https://github.com/user-attachments/assets/cdfd50ab-5bd2-4af4-b22e-780398e085c0" />


СТОЛБЧАТАЯ ДИАГРАММА РАСПРЕДЕЛЕНИЯ СТАБИЛЬНОСТИ ЭЛЕКТРИЧЕСКОЙ СЕТИ
Метод: plot_target_countplot(df)
"stable" (стабильно) и "unstable" (нестабильно). Перевес в сторону нестабильности.

<img width="974" height="753" alt="image" src="https://github.com/user-attachments/assets/0ee2c600-044c-4163-adac-8d4bcc28238f" />


СТОЛБЧАТАЯ ДИАГРАММА СРЕДНИХ ЗНАЧЕНИЙ КОЭФФИЦИЕНТОВ ЭЛАСТИЧНОСТИ
Метод: plot_bar_chart_elasticity(df)
Для четырех узлов сети (g1, g2, g3, g4). Средние значения коэффициентов эластичности для всех узлов одинаковы и равны 0.525.

<img width="974" height="607" alt="image" src="https://github.com/user-attachments/assets/d28d1ca7-cb4b-4893-b046-d906fafe7966" />


СРАВНЕНИЕ РАСПРЕДЕЛЕНИЙ ПРИЗНАКОВ ДЛЯ СТАБИЛЬНЫХ И НЕСТАБИЛЬНЫХ СЕТЕЙ
Метод: plot_stability_comparison(df)
Три ящика с усами, которые сравнивают распределения ключевых признаков (tau1, p1, g1) между стабильными и нестабильными состояниями сети. Выбросы видны только для p1 (Номинальная мощность узла-поставщика)


<img width="974" height="585" alt="image" src="https://github.com/user-attachments/assets/0056b7b5-7ad1-4b73-83c3-f8bbd789164e" />


ПОПАРНОЕ СРАВНЕНИЕ ПРИЗНАКОВ
Метод: plot_pairwise_comparison(df)
Цвет точек указывает на стабильность сети.


<img width="974" height="563" alt="image" src="https://github.com/user-attachments/assets/6bdf7c32-2e1a-437f-a384-a2e3ef357856" />


ТОЧЕЧНАЯ ДИАГРАММА ДЛЯ АНАЛИЗА ВЗАИМОСВЯЗИ МЕЖДУ ПРИЗНАКАМИ
Метод: plot_scatter_plot(df) 

<img width="974" height="745" alt="image" src="https://github.com/user-attachments/assets/e9925df0-5f45-4245-bcda-2faf820c515f" />


ТЕПЛОВАЯ КАРТА МАТРИЦЫ КОРРЕЛЯЦИИ ПРИЗНАКОВ
Метод: plot_correlation_heatmap(df)

<img width="974" height="601" alt="image" src="https://github.com/user-attachments/assets/7ff236d9-3872-4dea-8066-787615a64c68" />


АНАЛИЗ ПРИЗНАКОВ, НАИБОЛЕЕ КОРРЕЛИРУЮЩИХ СО СТАБИЛЬНОСТЬЮ СЕТИ
Метод: plot_top_correlated_features(df)
Показывает топ-6 признаков с наибольшей корреляцией со стабильностью сети.

<img width="974" height="568" alt="image" src="https://github.com/user-attachments/assets/d89b6c8c-a568-4b7f-b733-1afbb68d0b1b" />


ГРАФИК СКРИПКИ ДЛЯ ДЕТАЛЬНОГО АНАЛИЗА РАСПРЕДЕЛЕНИЙ
Метод: plot_violin_plot(df)

<img width="974" height="642" alt="image" src="https://github.com/user-attachments/assets/891138fa-577d-4f13-85d3-50c66b094917" />


ФАСЕТНАЯ СЕТКА ДЛЯ АНАЛИЗА РАСПРЕДЕЛЕНИЙ ПО ГРУППАМ С ИСПРАВЛЕННЫМ ЗАГОЛОВКОМ
Метод: plot_facet_grid_corrected(df)


<img width="974" height="428" alt="image" src="https://github.com/user-attachments/assets/28511799-1433-485d-b775-b62caacb4c6e" />




