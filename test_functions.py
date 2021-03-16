"""Test for my functions used in my project."""

from datetime import date
import pandas as pd
from functions import (create_food, 
                       init_df, 
                       add_food, 
                       in_inventory, 
                       remove_food, 
                       edit_quant, 
                       is_expired)


def test_remove_food():
    
    # create sample dataframe
    df = init_df('banana', 2, date(2021, 3, 10), 'fruit')
    df = add_food(df, 'pasta', 1, date(2021, 3, 15), 'grains')
    df = add_food(df, 'mango', 7, date(2021, 3, 23), 'fruit')
    
    # check sample dataframe has been created with 3 rows
    rows = list(df.shape)[0]
    
    assert rows == 3
    
    # run remove_food function and check that 
    # resulting dataframe has 2 rows
    df_1 = remove_food(df, 'banana')
    rows_1 = list(df_1.shape)[0]
    
    assert rows_1 == 2
    
    # verify if input food is not in input dataframe,
    # remove_food function will return NoneType variable
    df_2 = remove_food(df, 'pineapple')
    
    assert df_2 == None

    
def test_edit_quant():
    
    # create sample dataframe
    df = init_df('banana', 2, date(2021, 3, 10), 'fruit')
    df = add_food(df, 'pasta', 1, date(2021, 3, 15), 'grains')
    df = add_food(df, 'mango', 7, date(2021, 3, 23), 'fruit')
    
    # verify 'banana' quantity is 2
    assert df.at[0, 'quant'] == 2
    
        # test scenario when input food is not in input df
    # or when input new_quant is same as current quantity
    # 'banana' quantity should return NoneType variable for
    # both scenarios
    df_2 = df
    df_3 = df
    df_2 = edit_quant(df_2, 'pineapple', 7)
    df_3 = edit_quant(df_3, 'banana', 2)
    
    assert df_2 == None
    assert df_3 == None
    
    # test scenario when input new_quant is 7
    df_1 = df
    df_1 = edit_quant(df_1, 'banana', 7)
    
    assert df.at[0, 'quant'] == 7


def test_is_expired():
    
    # create sample dataframe
    df = init_df('banana', 2, date(2021, 3, 10), 'fruit')
    df = add_food(df, 'pasta', 1, date.today(), 'grains')
    df = add_food(df, 'mango', 7, date(9999, 12, 31), 'fruit')
    
    # test when input food has not expired
    assert is_expired(df, 'mango') == False
    
    # test when input food expires on current day
    assert is_expired(df, 'pasta') == False
    
    # test when input food has expired
    assert is_expired(df, 'banana') == True
    
    #test when input food is not in input dataframe
    assert is_expired(df, 'pineapple') == None             
    
    
def test_tests():
    
    assert test_remove_food() == None 
    assert test_edit_quant() == None
    assert test_is_expired() == None