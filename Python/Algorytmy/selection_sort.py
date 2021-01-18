#algorytmy sortowania ciągu liczb - przez wybór

def selection_sort(tab):
    for i in range(len(tab)):
        mini = i 
        for j in range(i+1, len(tab)): 
            if tab[mini] > tab[j]: 
                mini = j         
        tab[i], tab[mini] = tab[mini], tab[i]
    return tab

tab = [64, 34, 25, 12, 22, 11, 90] 
    
print(selection_sort(tab))
