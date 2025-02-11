# Text-Summarization
This repository for summarization task using a pre-trained model from Hugging Face. The process involves fine-tuning the model on a custom dataset to improve its accuracy and relevance for specific summarization tasks. After fine-tuning, the model is deployed as an interactive web application using Streamlit, providing an easy-to-use interface.



### Install python using Miniconda

1) Download and install Miniconda 

2) Create a new environment using the following command:
```bash
$ conda create -n Text-Summarization python=3.9
```
3) Activate the environment:
```bash
$ conda activate Text-Summarization
```

### Install the required packages

```bash
$ cd src
```

```bash
$ pip install -r requirements.txt
```

### Run the app 
```bash
$ streamlit run app.py
```
