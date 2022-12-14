# Decision Analytics for Business & Policy

# Final Project

The repository contains the following files:
1) **monkeypox_models_app** folder that contains the code for the Neural Network model. The files stand on their own:
    - monekypox-cnn.ipynb <- Trains the neural network model, and stores it in saved_model folder
    - model_evaluation.ipynb <- loads the model from saved_model (the model we trained in our last run is already here) and creates ROC and confusion matrix using test data
    - main.py <- lunches the streamlit application to upload and predict on new images
2) **SIR_final.ipynb** that contains the code for the SIR model
3) **Daily Cases USA.csv** that is the data file that is being fed into the SIR model
4) **our_enviroment.yml** that is the conda environment we used to run the neural network and SIR models (FYI). You can create the same conda enviroment we used with **conda env create -f our_environment.yml ** .Streamlit can be tricky to install depending on the OS of your computer. Please try 'pip3 install streamlit' if conda doesn't work.

## Running the model
1) Run the **monekypox-cnn.ipynb** to train the neural network (this took around 20 minutes to run). The result will be stored in the **saved_model** folder. Then run the **model_evaluation.ipynb** file to load the neural network from the **saved_model** folder. This will create the ROC curve and the confusion matrix which are also stored as .jpg files in the repository. Finally, run the command: **streamlit run monkeypox_models_app/main.py** to launch the streamlit application.
2) Run **SIR_final.ipynb**, this code stands alone and its independent from the neural network code. 
