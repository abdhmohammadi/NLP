file = open('TextVectorization/CBOW.ipynb', mode='r',encoding='utf8')
notebook = file.read()
new_notebook = notebook.replace("mathbf{W}","mathbf{W}_{in}")
new_notebook = new_notebook.replace("mathbf{W'}","mathbf{W}_{out}")
new_notebook = new_notebook.replace("self.W_prime","self.W_out")
file.close()
file = open('TextVectorization/CBOW-updated.ipynb', mode='w',encoding='utf8')

file.write(new_notebook)