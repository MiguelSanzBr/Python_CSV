import pandas as pd
from tkinter import Tk
import tkinter.filedialog as filedialog
import os 

def saveTosave(collname,arrayDados) :
    Tk().withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    df = pd.read_csv(file_path)

    newdf = df[df[collname].isin(arrayDados)].index

    idf = df.iloc[newdf]
    mesa_p_str = idf.to_string()
    print(mesa_p_str)


    output = "output.csv"

    if os.path.exists(output):
        mode = "a" 
    else:
        mode = "w" 

    idf.to_csv(output, mode=mode, index=False)
    print("CSV file exported successfully to:", output)

#### NOME DA COLUNA 
###################
collname = 'NOME'
arrayDados = ["chapa", "pedro", "yuri"]
###################
saveTosave(collname,arrayDados)
