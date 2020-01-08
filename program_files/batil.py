import pickle
import os
import pandas as pd

def cancel(text):
    df = pd.read_pickle(r"encodings.pickle")
    #print(df['names'])
    n = len(df['names'])
    #for i in range(0,n):
    i=0
    while(i<n):
        if(df['names'][i]==text):
            print(df['names'].pop(i))
            df['encodings'].pop(i)
            #print()
            n=n-1
            #i=i-1
            print(i,n)
        else:
            i = i + 1

            
    print(df['names'])
    if os.path.isfile("encodings.pickle"):
        print ("File exist")
        os.remove("encodings.pickle")
        print("File Removed!")
    else:
       print ("File not exist")
    f = open("encodings.pickle", "wb")
    f.write(pickle.dumps(df))
    sourav = pd.read_pickle(r"encodings.pickle")
    print(sourav['names'])
    f.close()
