import pickle

with open('persistants/marks.pickle', 'rb') as f:
    marks = pickle.load(f)

with open('persistants/modelss.pickle', 'rb') as f:
    models = pickle.load(f)


with open('persistants/citys.pickle', 'rb') as f:
    citys = pickle.load(f)

with open('persistants/citys_map.pickle', 'rb') as f:
    citys_map = pickle.load(f)

marks_revers: dict = {v: k for k, v in marks.items()}

models_revers: dict = {v: k for k, v in models.items()}

