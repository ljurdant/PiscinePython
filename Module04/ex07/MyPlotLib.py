import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings


class MyPlotLib:
    def numerical_filter(self, data, features):
        if not isinstance(data, pd.DataFrame) or not isinstance(features, list):
            raise TypeError
        for f in features:
            if f not in data.columns or not isinstance(f, str) :
                raise AttributeError
        df = data[features]._get_numeric_data()
        return df.columns

    def histogram(self, data, features):
        features = self.numerical_filter(data, features)
        fig, axs = plt.subplots(ncols=len(features))
        for index, f in enumerate(features):
            axs[index].hist(data[f], bins=10)
            axs[index].set_title(f)
        fig.tight_layout()
        plt.show()

    def density(self, data, features):
        features = self.numerical_filter(data, features)
        warnings.filterwarnings("ignore")
        sns.displot(data[features], kind="kde")
        plt.show()
    
    def pair_plot(self, data, features):
        features = self.numerical_filter(data, features)
        if len(features) != 2:
            raise AttributeError("Exactly 2 numerical features needed")
        sns.pairplot(data[features],  diag_kws = {'bins':10})
        plt.show()
    
    def box_plot(self, data, features):
        features = self.numerical_filter(data, features)
        warnings.filterwarnings("ignore")
        sns.boxplot(data[features], width=0.2)
        plt.show()