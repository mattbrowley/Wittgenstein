# -*- coding: utf-8 -*-
"""
Created on Wed May  9 22:50:55 2018

@author: matt
"""
text = """
\\documentclass[12pt, letterpaper]{memoir}
\\usepackage[bookmarks, breaklinks=true]{hyperref}
\\hypersetup{pdftex, colorlinks=true}
\\aliaspagestyle{title}{empty}
\\title{Wittgensteinian Dictionay}
\\author{Matthew Bown Rowley}
\\date{\\today}
\\begin{document}
\\maketitle
\\frontmatter
\\chapter*{Introduction}
This dictionary may only including the 5,000 most common English words, but it
is massive in scope. Other dictionaries (such as the banal Webster's Dictionary
or the tiresome Oxford New English Dictionary) rely on the narrow, prescriptive,
and circular practice of defining elements of a language by using other
elements of the self-same language. This dictionary transcends those others by
providing a complete and rigorous description of each word\'s meaning.

I extend my appreciation to \\hyperref[https://www.wordfrequency.info]{https://www.wordfrequency.info}
 for providing the word list. Now, please enjoy the dictionary.

\\mainmatter
\\chapter*{Words}
\\renewcommand{\\chaptername}{Words}
\\begin{description}
"""
previous_word = ''
with open('words.txt', 'r') as word_file:
    words = word_file.readlines()
    for word in words:
        word = word[6:].replace('\n','').replace(' ','')
        if 'beetle' in word:
            text = text + "\n\\item[{}] A totally awesome bug that I keep in this box. No you can't see it.".format(word)
        elif word not in previous_word:
            text = text + "\n\\item[{}] The meaning of the word \'\'{}\'\' is derived from its usage.".format(word,word)
            previous_word = word
text = text + """
\\end{description}
\\end{document}"""
with open('W_Dictionary.tex', 'w') as tex_file:
    tex_file.write(text)