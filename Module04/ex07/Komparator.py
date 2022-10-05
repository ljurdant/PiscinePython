from enum import unique

from click import argument
from MyPlotLib import MyPlotLib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import warnings


class Komparator:
    def __init__(self, df):
        self.df = df
    
    @property
    def df(self):
        return self._df

    @df.setter
    def df(self, value):
        if not isinstance(value, pd.DataFrame):
            raise TypeError
        self._df = value
    
    def argument_check(self, categorical_var, numerical_var):
        if not isinstance(categorical_var, str) or not isinstance(numerical_var, str):
            raise TypeError
        df = self.df._get_numeric_data()
        if categorical_var not in self.df.columns or numerical_var not in df.columns:
            raise AttributeError

    def compare_box_plots(self, categorical_var, numerical_var):
        self.argument_check(categorical_var, numerical_var)
        ax = sns.boxplot(data=self.df, x=categorical_var, y=numerical_var)
        plt.title(numerical_var+" per "+categorical_var)
        plt.show()
    
    def density(self, categorical_var, numerical_var):
        self.argument_check(categorical_var, numerical_var)
        df = self.df.pivot(columns=categorical_var, values=numerical_var)
        warnings.filterwarnings("ignore")
        sns.displot(df, kind="kde")
        plt.title(numerical_var+" per "+categorical_var)
        plt.show()

    def compare_histograms(self, categorical_var, numerical_var):
        self.argument_check(categorical_var, numerical_var)
        df = self.df.pivot(columns=categorical_var, values=numerical_var)
        for col in df.columns:
            plt.hist(df[col], alpha=0.5, label=col)
        plt.legend(df.columns)
        plt.title(numerical_var+" per "+categorical_var)
        plt.show()