from msilib.text import UIText
import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

def summarizer():

    url = Utext.get('1.0','end').strip()    
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    
    title.config(state='normal')
    author.config(state='normal')
    pdate.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')
    
    title.delete("1.0",'end')
    title.insert("1.0",article.title)
    
    author.delete("1.0",'end')
    author.insert("1.0",article.authors)
    
    pdate.delete("1.0",'end')
    pdate.insert("1.0",article.publish_date or 'none')
    
    summary.delete("1.0",'end')
    summary.insert("1.0",article.summary)
   
    analysis = TextBlob(article.text)
    sentiment.delete("1.0","end")
    sentiment.insert("1.0",f'Polarity:{analysis.polarity}, Sentiment: {"Positive" if analysis.polarity > 0 else "Negative" if analysis.polarity < 0 else "Neutral"}')

    title.config(state='disabled')
    author.config(state='disabled')
    pdate.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')
    
root = tk.Tk()
root.title("News Summarizer")
root.geometry('500x600')

tlabel1 = tk.Label(root,text="Title")
tlabel1.pack()
title = tk.Text(root,height=1,width=140)
title.config(state='disabled',bg='#dddddd')
title.pack()

alabel = tk.Label(root,text="Author")
alabel.pack()
author = tk.Text(root,height=1,width=140)
author.config(state='disabled',bg='#dddddd')
author.pack()

plabel = tk.Label(root,text="Publishing date")
plabel.pack()
pdate = tk.Text(root,height=1,width=140)
pdate.config(state='disabled',bg='#dddddd')
pdate.pack()

slabel = tk.Label(root,text="Summary")
slabel.pack()
summary = tk.Text(root,height=20,width=140)
summary.config(state='disabled',bg='#dddddd')
summary.pack()

selabel = tk.Label(root,text="Sentiment")
selabel.pack()
sentiment = tk.Text(root,height=1,width=140)
sentiment.config(state='disabled',bg='#dddddd')
sentiment.pack()

ulabel = tk.Label(root,text="URL")
ulabel.pack()
Utext = tk.Text(root,height=1,width=140)
Utext.pack()

btn = tk.Button(root,text="Summarize",command=summarizer)
btn.pack()
root.mainloop()