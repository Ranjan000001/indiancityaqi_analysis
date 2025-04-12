
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns

    # read all files
    chennai_data = pd.read_csv("C:\\Users\\user\\Downloads\\archive (3)\\chennai_combined.csv")
    delhi_data = pd.read_csv("C:\\Users\\user\\Downloads\\archive (3)\\delhi_combined.csv")
    gwalior_data = pd.read_csv("C:\\Users\\user\\Downloads\\archive (3)\\gwalior_combined.csv" )
    hyderabad_data = pd.read_csv("C:\\Users\\user\\Downloads\\archive (3)\\hyderabad_combined.csv")
    jaipur_data = pd.read_csv("C:\\Users\\user\\Downloads\\archive (3)\\jaipur_combined.csv")
    kolkata_data = pd.read_csv("C:\\Users\\user\\Downloads\\archive (3)\\kolkata_combined.csv")
    lucknow_data = pd.read_csv("C:\\Users\\user\\Downloads\\archive (3)\\lucknow_combined.csv")
    mumbai_data = pd.read_csv("C:\\Users\\user\\Downloads\\archive (3)\\mumbai_combined.csv")
    visakhapatnam_data = pd.read_csv("C:\\Users\\user\\Downloads\\archive (3)\\visakhapatnam_combined.csv")
    bengaluru_data =pd.read_csv("C:\\Users\\user\\Downloads\\archive (3)\\bengaluru_combined.csv")

    # combine files into data
    data = pd.concat(['chennai_data', 'delhi_data', 'gwalior_data', 'hyderabad_data', 'jaipur_data', 'kolkata_data',
                      'lucknow_data', 'mumbai_data', 'visakapatnam_data', 'bengaluru_data'], ignore_index=False)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
