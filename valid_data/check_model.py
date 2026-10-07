   import pickle

   with open("final_model/model.pkl", "rb") as f:
       model = pickle.load(f)

   print(model)