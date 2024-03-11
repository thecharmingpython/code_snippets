##### Charmingpython.com #####

algorythm = ['Large Lang Model', 'Linear Regression', 'Gradient Descent', 'Support Vector Machine' ]
uses = ['Tokenise language for generative reuse', 
        'Linear prediction from scattered data',
        'Locate local minimum for back propogation', 
        'Parametric classification for separating label classes'
        ]


for index, algo in enumerate(algorythm):
    print(algo,' - ', uses[index])    

for algo, use in zip(algorythm, uses):
    print(algo, ' - ', use)
    


