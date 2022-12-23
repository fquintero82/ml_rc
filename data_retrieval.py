#from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
""" def get_usgs_rc_from_db():
    contxt = 'postgresql://felipe:@s-iihr51.iihr.uiowa.edu:5432/research_environment'
    engine = create_engine(contxt) """

def _get_all_rc():
    f = 'data/data_rc_usgs.csv'
    df = pd.read_csv(f,
        names=['usgs','stage','discharge'],
        header=0,
        dtype={'usgs':str,'stage':np.float16,'discharge':np.float32},
        index_col=0)
    return df

def get_rc(usgs_code):
    df = _get_all_rc()
    df2 = df[df.index==usgs_code]
    return df2

def test():
    usgs_code = '05387440'
    mydf = get_rc(usgs_code)
    print(mydf)
    plt.scatter(mydf['stage'],mydf['discharge'])
    plt.xlabel('stage, in feet')
    plt.ylabel('discharge, in cfs')
    plt.show()
    plt.close('all')