# Decision Analytics for Business & Policy

# Final Project

The repository contains the following files:
1) **monkeypox_models_app** folder that contains the code for the Neural Network model:
    - monekypox-cnn.ipynb
    - model_evaluation.ipynb
    - main.py
2) **SIR_final.ipynb** that contains the code for the SIR model
3) **Daily Cases USA.csv** that is the data file that is being fed into the SIR model
4) **our_enviroment.yml** that is the conda environment we used to run the neural network and SIR models (FYI)

## Running the model
1) Run the **monekypox-cnn.ipynb** to train the neural network (this took around 20 minutes to run). The result will be stored in the **saved_model** folder. Then run the **model_evaluation.ipynb** file to load the neural network from the **saved_model** folder. This will create the ROC curve and the confusion matrix which are also stored as .jpg files in the repository. Finally, run the command: **streamlit run monkeypox_models_app/main.py** to launch the streamlit application.
2) Run **SIR_final.ipynb**, this code stands alone and its independent from the neural network code. 
