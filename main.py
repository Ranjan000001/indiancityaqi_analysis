# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns

    # read all files
    chennai_data = pd.read_csv("C:\\Users\\user\\Downloads\\archive (3)\\chennai_combined.csv")
    delhi_data = pd.read_csv("C:\\Users\\user\\Downloads\\archive (3)\\delhi_combined.csv")
    gwalior_data = pd.read_csv("C:\\Users\\user\\Downloads\\archive (3)\\gwalior_combined.csv")
    hyderabad_data = pd.read_csv("C:\\Users\\user\\Downloads\\archive (3)\\hyderabad_combined.csv")
    jaipur_data = pd.read_csv("C:\\Users\\user\\Downloads\\archive (3)\\jaipur_combined.csv")
    kolkata_data = pd.read_csv("C:\\Users\\user\\Downloads\\archive (3)\\kolkata_combined.csv")
    lucknow_data = pd.read_csv("C:\\Users\\user\\Downloads\\archive (3)\\lucknow_combined.csv")
    mumbai_data = pd.read_csv("C:\\Users\\user\\Downloads\\archive (3)\\mumbai_combined.csv")
    visakhapatnam_data = pd.read_csv("C:\\Users\\user\\Downloads\\archive (3)\\visakhapatnam_combined.csv")
    bengaluru_data = pd.read_csv("C:\\Users\\user\\Downloads\\archive (3)\\bengaluru_combined.csv")

    # combine files into data
    data = pd.concat([chennai_data, delhi_data, gwalior_data, hyderabad_data, jaipur_data, kolkata_data,
                      lucknow_data, mumbai_data, visakhapatnam_data, bengaluru_data], ignore_index=False)
    # info and head and describe
    print(data.info())
    print(data.head())
    print(data.describe())

    # Data Cleaning
    # null and duplicated values
    print(data.isnull().sum())
    print(data.duplicated().sum())

    # fill empty cells with mean of that column
    table = ['PM2.5', 'PM10', 'NO2', 'NH3', 'SO2', 'CO', 'O3']
    # for loop for columns to fill values
    for col in table:
        data[col] = data[col].fillna(data[col].mean(), inplace=False)  # fill na with mean value
    # check values
    print(data.isnull().sum())

    # outliers
    # using tabel list from 35 line

    # check data
    print(data.info())
    print(data.tail())
    print(data.describe())
    # new columns
    bins = [0, 30, 60, 90, 120, 400]  # range
    label = ['good', 'moderate', 'poor', 'very poor', 'danger']  # range labels
    data['pm2.5_range'] = pd.cut(x=data['PM2.5'], bins=bins, labels=label)  # created range column of pm2.5
    bins = [0, 1, 2, 10, 17, 400]  # range
    labels = ['Good', 'moderate', 'poor', 'very poor', 'Danger']
    data['co_range'] = pd.cut(x=data['CO'], bins=bins, labels=labels)  # new column range of co
    bins = [0, 40, 80, 180, 280, 2000]  # range
    labels = ['good', 'moderate', 'Poor', 'Very poor', 'danger']
    data['no2_range'] = pd.cut(x=data['NO2'], bins=bins, labels=labels)  # column range of no2
    bins = [0, 200, 400, 800, 1200, 3000]  # range
    labels = ['good', 'Moderate', 'poor', 'Very poor', 'danger']
    data['nh3_range'] = pd.cut(x=data['NH3'], bins=bins, labels=labels)  # column range of nh3
    bins = [0, 40, 80, 380, 800, 3000]  # range
    label = ['good', 'moderate', 'poor', 'very poor', 'dangers']
    data['so2_range'] = pd.cut(x=data['SO2'], bins=bins, labels=label)  # column range of so2
    two_col = ['PM10', 'O3']  # two columns list
    for col in two_col:
        bins = [0, 50, 100, 169, 208, 2000]  # range
        labels = ['Good', 'Moderate', 'Poor', 'Very Poor', 'Danger']
        data[f'{col}_range'] = pd.cut(x=data[f'{col}'], bins=bins, labels=labels)  # new column range of col


    data = data.reset_index(drop=True)
    print(data.info())
    print(data.describe())
    # Data Visualization



    # list of columns
    col_list = ['pm2.5_range', 'PM10_range', 'co_range', 'no2_range', 'O3_range', 'nh3_range', 'so2_range']
    for col in col_list:
        plt.figure(figsize=(14, 7))  # size
        sns.countplot(data=data, x=col)  # count graph of columns
        plt.xlabel(f'{col}')  # x axis label
        plt.ylabel('count')  # y axis label
        plt.yscale('log')  # y axis in log
        plt.title(f'graph of {col}')  # title
        plt.show()  # show
    arr = np.array([1, 2, 3, 4])

    # locations
    plt.figure(figsize=(12, 7))  # figure size
    list_column = ['PM2.5', 'PM10', 'CO', 'NO2', 'O3', 'NH3', 'SO2']
    df = data.groupby('Location')[list_column].mean().reset_index()  # location basis on another columns mean
    # melt the data of group
    df_melt = df.melt(id_vars='Location', value_vars=list_column, var_name='pollution', value_name='mean_value')
    # line graph of location basis on another columns  mean
    sns.lineplot(data=df_melt, x='Location', y='mean_value', hue='pollution', marker='o')
    plt.title('Graph of location vs PM2.5, PM10, NO2, NH3, SO2, CO, O3')  # title
    plt.xlabel('Location')  # x axis label
    plt.ylabel('Pollutions Elements')  # y axis label
    plt.xticks(rotation=90)  # rotation x index by 90
    plt.tight_layout()  # all parts come inside graph
    plt.show()  # show
    # years basis data
    year_2020 = data.loc['01-01-2020':'31-12-2020']  # year 2020
    year_2021 = data.loc['01-01-2021':'31-12-2021']  # year 2021
    year_2022 = data.loc['01-01-2022':'31-12-2022']  # year 2022
    year_2023 = data.loc['01-01-2023':'31-12-2023']  # year 2023
    year_2024 = data.loc['01-01-2024':'31-12-2024']  # year 2024

    year_col = [year_2020, year_2021, year_2022, year_2023, year_2024]  # list of year column
    list_range = ['pm2.5_range', 'PM10_range', 'no2_range', 'O3_range', 'nh3_range', 'so2_range', 'co_range']
    for col in year_col:
        df1 = col.groupby('Timestamp')[list_column].mean().reset_index()  # groping year_col with list_column
        df1_melt = col.melt(id_vars='Timestamp', value_vars=list_column, var_name='pollution', value_name='mean_value')
        # bar graph of years vs pollutions
        sns.lineplot(data=col, x='Timestamp', y='mean_value', hue='pollution', marker='o')
        #col['year'].plot()
        plt.xlabel(f'{col}')  # x axis label
        plt.ylabel('count')  # y axis label
        plt.title(f'Graph {col} vs Pollution')  # title
        plt.show()  # show