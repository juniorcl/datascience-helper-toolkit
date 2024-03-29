import numpy as np


def agg_num(df, groupby, variables, quantiles=[0.25, 0.50, 0.75]):

    """
    Function to calculate a list of mathematical functions

    Parameters
    ----------
    df : DataFrame
        Initial DataFrame

    groupby : List
        List of variables to be groupped.

    variables : List
        List of variables to apply the functions.

    quantiles : List
        List of numbers of quantiles to calculate.
    
    Returns
    -------
    df_agg : DataFrame
        Result DataFrame. 
    """

    list_funcs = [
        'sum', 'mean', 'median', 'min', 'max', 'std', 'var', ('range', lambda i: np.max(i) - np.min(i))]
    
    list_quantiles = [
        (f'quantile_{q}', lambda i, q=q: np.quantile(i, q=q)) for q in quantiles]
    
    list_funcs.extend(list_quantiles)

    dict_funcs = {var: list_funcs for var in variables}

    df_agg = df.groupby(groupby).agg(dict_funcs)

    df_agg.columns = [f'{col[0]}_{col[1]}' for col in df_agg.columns]

    df_agg = df_agg.reset_index()

    return df_agg