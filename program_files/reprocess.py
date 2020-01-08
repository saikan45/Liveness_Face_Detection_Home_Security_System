import pickle
import os
import pandas as pd

def again(text1,text2):
    df = pd.read_pickle(r"encodings.pickle")
    #print(df['names'])
    n = len(df['names'])
    for i in range(0,n):
        if(df['names'][i]==text1):
            df['names'][i]=text2
    print(df['names'])
    if os.path.isfile("encodings.pickle"):
        print ("File exist")
        os.remove("encodings.pickle")
        print("File Removed!")
    else:
       print ("File not exist")
    f = open("encodings.pickle", "wb")
    f.write(pickle.dumps(df))
    ovi = pd.read_pickle(r"encodings.pickle")
    print(ovi['names'])
    f.close()
