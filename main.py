# Importing the dataset

from dataset import func_dataset
dataset=func_dataset()

# Taking the symptoms as input

symptom=input("Enter symptoms (separated by ,): ").split(", ")

# Calculating chances of disease based on input

likely=0
predict=[]
for i in range(len(dataset)):
    diseases=dataset[i][1][0:5]
    for k in symptom:
        if k in diseases:
            likely+=1
    predict.append(likely)
    likely=0

# Selecting and printing the most likely diseases

for a in range(len(symptom),0,-1):
    if a in predict:
        index=-1
        for b in predict:
            index+=1
            if b==a:
                print("You might be having:", dataset[index][0])
        break




# import tkinter as tk
# from dataset import func_dataset as dataset

# def predict_disease():
#     # Get symptoms from input field
#     symptom_str = symptom_entry.get()
#     symptom = symptom_str.split(", ")

#     # Calculate chances of disease based on input
#     likely = 0
#     predict = []
#     for i in range(len(dataset)):
#         diseases = dataset[i][1][0:5]
#         for k in symptom:
#             if k in diseases:
#                 likely += 1
#         predict.append(likely)
#         likely = 0

#     # Select and print the most likely diseases
#     most_likely = max(predict)
#     for i in range(len(predict)):
#         if predict[i] == most_likely:
#             disease_label.config(text="You might be having: " + dataset[i][0])
#             break

# # Create the main window
# root = tk.Tk()
# root.title("Disease Prediction")

# # Create symptom label and input field
# symptom_label = tk.Label(root, text="Enter symptoms (separated by ,): ")
# symptom_label.pack()

# symptom_entry = tk.Entry(root)
# symptom_entry.pack()

# # Create predict button
# predict_button = tk.Button(root, text="Predict", command=predict_disease)
# predict_button.pack()

# # Create disease label
# disease_label = tk.Label(root)
# disease_label.pack()

# # Start the GUI event loop
# root.mainloop()
