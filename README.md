# Decision Analytics for Business & Policy

# Final Project

The repository contains the following files:

1) **SIR_final.ipynb** that contains the code for the SIR model
2) **monkeypox_models_app** folder that contains the code for the Neural Network model:
    - monekypox-cnn-78.ipynb
    - model_evaluation.ipynb
    - main.py
4) **Daily Cases USA.csv** that is the data file that is being fed into the SIR model

## Running the model

1) Run **SIR_final.ipynb**, this code stands alone and its independent from the nerual network code. 
2) Run the **monekypox-cnn-78.ipynb** to train the neural network (this took around 20 minutes to run). The result will be stored in the **saved_model** folder. Then run the **model_evaluation.ipynb** file to load the neural network from the **saved_model** folder. This will create the ROC curve and the confusion matrix which are also stored as .jpg files in the repository. Finally, the **main.py** file is to launch the streamlit application.
