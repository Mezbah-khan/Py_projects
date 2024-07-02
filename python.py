import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
import sklearn as skn 

class FristCls:
    hello = 'Welcome to this project!'

    def __init__(self, data, nums):
        self.data = data
        self.nums = nums

    @staticmethod
    def warn():
        return 'The system is error!'

    def dataset(self):
        try:
            dataset = {
                'Data': self.data,
                'Nums': self.nums,
            }
            return dataset
        except TypeError:
            print('The system is error!')

    def frist_functions(self):
        data_value = self.data
        if 90 <= data_value <= 100:
            return 'A'
        elif 70 <= data_value <= 89:
            return 'B'
        elif 50 <= data_value <= 69:
            return 'C'
        elif 30 <= data_value <= 49:
            return 'D'
        elif 0 <= data_value <= 29:
            return 'Fail'
        else:
            return self.warn()

# Let's create the second class and functions
class SecendCls(FristCls):
    def __init__(self, data, nums):
        super().__init__(data, nums)

    @classmethod
    def get_user_input(cls):
        try:
            print('1. Enter your data')
            print('2. Enter your nums')
            choice = int(input('Enter your choice: '))
            if choice == 1:
                user_data = int(input('Enter your data: '))
                user_nums = list(map(int, input('Enter your nums (comma separated): ').split(',')))
                return cls(user_data, user_nums)
            else:
                print('Invalid choice')
        except ValueError:
            print('Invalid input')

if __name__ == "__main__":
    user_instance = SecendCls.get_user_input()
    if user_instance:
        print(user_instance.dataset())
        print(user_instance.frist_functions())
