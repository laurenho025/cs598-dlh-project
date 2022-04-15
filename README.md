# CS 598 DLH Project - Patient Phenotyping

albertc4, laurenh4

Group ID: 20

Paper ID: 116

Code re-used from the original paper author: https://github.com/sebastianGehrmann/phenotyping

## Data

Due to patient confidentiality requirements, we are not including the annotated dataset in this repository. The `data/annotations.csv` file is available in the linked google drive folder in our written report. This file contains patient and hospital admission IDs, and the annotations done by the original paper authors.

## Running The Code

### Preprocessing

The word2vec results were provided by the original paper authors, and are included in the google drive folder as `w2v.txt`. The preprocessed data files `data.h5` and `data-nobatch.h5` are also included in the google drive folder. To generate these files on your own, you can run the following command with python 3:

```
python preprocess.py data/annotations.csv w2v.txt --batchsize=5
```

This will create `data.h5` and `data-nobatch.h5` in the root folder.

### Baseline Methods

To run the baseline methods:

```
python basic_models.py --data data-nobatch.h5 --ngram 5
```

### Convolutional Neural Net (CNN)

TODO: Update CNN instructions

We recommend that you have a GPU with a cuda installation. Otherwise, training might take
a very long time! This code is based off of the following repository:
https://github.com/harvardnlp/sent-conv-torch
You can find more information there!

#### Install Torch

From http://torch.ch/docs/getting-started.html :

```
git clone https://github.com/torch/distro.git
cd distro; bash install-deps;
./install.sh
```

#### Install Torch packages

    luarocks install hdf5

#### Running the code

Please run the code with the following command:

```
th main.lua [OPTIONS]
```

You can find all options documented in the file itself.
Important ones are "-gpuid" to set your GPU as well as "-label_index" to define
which phenotype you want to detect. Here is the list that explains the indices:

1: cohort (is the patient frequent flier)
2: Obesity
3: Non Adherence
4: Developmental Delay Retardation
5: Advanced Heart Disease
6: Advanced Lung Disease
7: Schizophrenia and other Psychiatric Disorders
8: Alcohol Abuse
9: Other Substance Abuse
10: Chronic Pain Fibromyalgia
11: Chronic Neurological Dystrophies
12: Advanced Cancer
13: Depression
14: Dementia
