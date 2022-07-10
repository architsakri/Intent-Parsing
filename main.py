from intent_capture import Karen_intent as k
import matplotlib.pyplot as plt


icapture = k([['like'], ['notifications']])
index = icapture.search(["like"]) 
print(index)












