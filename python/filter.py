import pandas as pd
import pandasql as psql
from tkinter import *
from tkinter import ttk
df = pd.read_csv("movies_clean.csv")
rename = {
    "Comdy": "Comedy",
    "Romence": "Romance",
    "romance": "Romance",
    "comedy": "Comedy"
}
df["Genre"] = df["Genre"].replace(rename)

query = "SELECT DISTINCT Genre FROM df;"
df_sorted = psql.sqldf(query, locals())

df.to_csv("movies_clean.csv", index=False)

print(df_sorted)

DistGenre = df_sorted["Genre"].tolist()
root = Tk()
root.geometry("500x500")

def show():
    lbl.config(text=cb.get())

Genre = [DistGenre]

cb = ttk.Combobox(root, values=Genre)
cb.set("Select a genre")
cb.pack()
entry = ttk.Entry(root, font=("Arial", 12))
entry.pack(pady=10)
Button(root, text="Show Selection", command=show).pack()



lbl = Label(root, text=" ")
lbl.pack()

root.mainloop()
