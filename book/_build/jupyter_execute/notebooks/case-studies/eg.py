#!/usr/bin/env python
# coding: utf-8

# # Jupyter Notebook files
# 
# You can create content with Jupyter notebooks.
# For example, the content for the current page is contained in {download}`this notebook file <./notebooks.ipynb>`.
# 
# ```{margin}
# If you'd like to write in plain-text files, but still keep a notebook structure, you can write
# Jupyter notebooks with MyST Markdown, which are then automatically converted to notebooks.
# See [](./myst-notebooks.md) for more details.
# ```
# 
# Jupyter Book supports all Markdown that is supported by Jupyter Notebook.
# This is mostly a flavour of Markdown called [CommonMark Markdown](https://commonmark.org/) with minor modifications.
# For more information about writing Jupyter-flavoured Markdown in Jupyter Book, see [](./markdown.md).
# 
# ## Code blocks and image outputs
# 
# Jupyter Book will also embed your code blocks and output in your book.
# For example, here's some sample Matplotlib code:

# In[1]:


print(1+1)


# ## Another section 2.3
# some text goes here
# ### Section 2.3.1
# another thing goes here

# In[2]:


print('x2=2')


# In[3]:


#%inline matplotlib
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2*np.pi*t)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
plt.savefig("test.png")
plt.show()


# In[ ]:




