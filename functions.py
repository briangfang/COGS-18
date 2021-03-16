"""Collection of functions used in my project"""

from datetime import date
import pandas as pd


def create_food(food, quant, exp, categ):
    """Creates dictionary of preset keys paired with input parameters
    as corresponding values.
    
    Parameters
    ----------
    food : string
        String of food name.
    quant : integer or float or string
        Quantity of food in inventory.
    exp : datetime.date
        Expiration date of food. 
        Format is `date(year, month, day)`.
    categ : string
        String of food category.
        
    Returns
    -------
    output_dict : dictionary
        Dictionary of preset keys paired with input parameters 
        as corresponding values.
    """ 
    
    output_dict = {}
    
    # create keys for food information
    output_dict['food'] = food
    output_dict['quant'] = quant
    output_dict['exp'] = exp
    output_dict['categ'] = categ
    
    return output_dict


def init_df(food, quant, exp, categ):
    """Creates a dataframe with labeled columns for corresponding
    input parameters.
    
    Parameters
    ----------
    food : string
        String of food name.
    quant : integer or float or string
        Quantity of food in inventory.
    exp : datetime.date
        Expiration date of food. 
        Format is `date(year, month, day)`.
    categ : string
        String of food category.
        
    Returns
    -------
    df : pandas.core.frame.DataFrame
        Dataframe with labeled columns for corresponding
        input parameters.
    """
    
    # make a df from dict in create_food function
    dict_1 = create_food(food, quant, exp, categ)
    df = pd.DataFrame([dict_1])
    
    return df

 
def add_food(df, food, quant, exp, categ):
    """Adds input parameters as a new row to an existing dataframe.
    
    Parameters
    ----------
    df : pandas.core.frame.DataFrame
        Dataframe to which the input parameters below are added.
    food : string
        String of food name.
    quant : integer or float or string
        Quantity of food in inventory.
    exp : datetime.date
        Expiration date of food. 
        Format is `date(year, month, day)`.
    categ : string
        String of food category.
        
    Returns
    -------
    df : pandas.core.frame.DataFrame
        Input dataframe updated with a new row of other input parameters.
    """
    
    # add to existing df from dict in create_food function
    # ignore_index = True parameter continues numerical row indexing 
    # of input df
    df = df.append(create_food(food, quant, exp, categ), ignore_index = True)
    
    return df


def in_inventory(df, food):
    """Checks if input food is in the 'food' column of input dataframe.
    
    Parameters
    ----------
    df : pandas.core.frame.DataFrame
        Dataframe in which input food will be searched for.
    food : string
        String of food name to be searched.
    
    Returns
    -------
    output : boolean
        Returns False if input food not in 'food' column of input dataframe.
        Returns True if input food is in 'food' column of input dataframe. 
    """
    
    # turns df 'food' column into str and searches for 
    # input str food in 'food' column
    if food not in str(df['food']):
        print('Food not found. Inventory unchanged.')
        output = False
        
    else:
        output = True
        
    return output


def remove_food(df, food):
    """Removes row of input food from input dataframe.
    
    Parameters
    ----------
    df : pandas.core.frame.DataFrame
        Dataframe in which input food is to be removed.
    food : string
        String of food name to be removed.
        
    Returns
    -------
    output : NoneType or pandas.core.frame.DataFrame
        Returns NoneType if input food not in 'food' column of input dataframe.
        Otherwise returns input dataframe with input food row removed.
    """
    
    if in_inventory(df, food) == False:
        
        output = None
        
        return output

    else:
        # turns tuple into list and extracts the 
        # first element of list which is the number 
        # of rows in df and stores in var `rows`
        rows = list(df.shape)[0]
        counter = 0
    
        # loop set to run for the same number of 
        # times as there are rows in the input df. 
        # each row is turned into a str and 
        # searched for a match with input str food.
        # a successful match will drop that row
        # and reset the row indexing to prevent 
        # an error in future usage of this function
        while counter < rows:
            if food in str(df.loc[counter]):
                df = df.drop([counter])
                df = df.reset_index(drop = True)
                
                break
    
            else:
                counter += 1
                
        output = df
        
        return output
        

def edit_quant(df, food, new_quant):
    """Changes corresponding quantity of input food in input dataframe.
    
    Parameters
    ----------
    df : pandas.core.frame.DataFrame
        Dataframe in which input food quantity will be changed.
    food : string
        String of food name to change quantity.
    new_quant : integer or float or string
        New quantity of input food to be changed to.
        
    Returns
    -------
    output : NoneType or pandas.core.frame.DataFrame
        Returns NoneType if either input food is not in 'food' column
        of input dataframe or new_quant is equal to the existing quantity
        stored in the input dataframe. Else returns input dataframe with 
        updated input food quantity.
    """
    
    if in_inventory(df, food) == False:
        
        output = None
        
        return output
    
    else:
        # turns tuple into list and extracts the 
        # first element of list which is the number 
        # of rows in df and stores in var `rows`
        rows = list(df.shape)[0]
        counter = 0
    
        # loop set to run for the same number of 
        # times as there are rows in the input df. 
        # each row is turned into a str and 
        # searched for a match with input str food.
        # a successful match will replace the original
        # food quantity with the input quantity after 
        # the original quantity is stored in a var
        while counter < rows:
            if food in str(df.loc[counter]):
                old_quant = df.at[counter, 'quant']
                df.at[counter, 'quant'] = new_quant
                
                break
            
            else:
                counter += 1
        
        # confirms to user that food quantity has been changed
        if new_quant != old_quant:
            print(str(food) + ' quantity changed from ' + \
                  str(old_quant) + ' to ' + str(new_quant) + '.')
            output = df
        
        # alerts user input quantity == original quantity so
        # the df has not been updated
        else:
            print('The new ' + food + ' quantity is the' + \
                  ' same as the old one. Inventory unchanged.')
            output = None
            
        return output
    
    
def is_expired(df, food):
    """Checks if input food in input dataframe is expired.
    Also prints out how many days the input food has until 
    expiration or has been expired accordingly.
    
    Parameters
    ----------
    df : pandas.core.frame.DataFrame
        Dataframe in which input food will be checked for expiration.
    food : string
        String of food name to be checked for expiration.
        
    Returns
    -------
    output : NoneType or boolean
        Returns NoneType if input food is not in 'food' column
        of input dataframe. Else returns boolean. Boolean will
        be False if input food expires on or after the current 
        date. Boolean will be True if input food expires before
        current date.
    """
    
    if in_inventory(df, food) == False:
        
        output = None
        
        return output
    
    else:
        rows = list(df.shape)[0]
        counter = 0
        
        # loop set to run for the same number of 
        # times as there are rows in the input df. 
        # each row is turned into a str and 
        # searched for a match with input str food.
        # a successful match will then check if the input
        # food has expired and print the appropriate response
        while counter < rows:
            if food in str(df.loc[counter]):
                if df.at[counter, 'exp'] > date.today():
                    output = False
                    days_til_exp = df.at[counter, 'exp'] - date.today()
                    print('This food has not yet expired. It will ' + \
                          'expire in ' + str(days_til_exp.days) + ' days.')
                
                elif df.at[counter, 'exp'] == date.today():
                    output = False
                    print('This food expires today!')
                
                elif df.at[counter, 'exp'] < date.today():
                    output = True
                    days_exp = date.today() - df.at[counter, 'exp']
                    print('This food has expired. It expired ' + \
                          str(days_exp.days) + ' days ago.')
                    
                return output
                
                break
            
            else:
                counter += 1