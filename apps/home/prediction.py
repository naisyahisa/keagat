import pandas as pd
import numpy as np
from .models import Vaksinasi

df = pd.DataFrame(list(Vaksinasi.objects.all().values()))

# data = pd.read_csv('E:\OneDrive\1-Documents\6-Other\3-Aisyah\fyp\keagat\data.csv\data.csv',sep=',')
print(df)