# CS 598 DLH Project - Patient Phenotyping

albertc4, laurenh4

Group ID: 20

Paper ID: 116

Code re-used from the original paper author: https://github.com/sebastianGehrmann/phenotyping

## Data

Due to patient confidentiality requirements, we are not including the annotated dataset in this repository. The `data/annotations.csv` file is available in the original paper's code implementation [here](https://github.com/sebastianGehrmann/phenotyping). This file contains patient and hospital admission IDs, and the annotations done by the original paper authors. This file is missing the discharge summary text column, which can be obtained from MIMIC-III via physionet and should be saved as `data/NOTEEVENTS.csv`. To append the necessary column and get the full dataset, run the following command with python 3:

```
python add_discharge.py
```

## Running The Code

### Preprocessing

The word2vec results were provided by the original paper authors, and are included in the original paper's implementation [repository](https://github.com/sebastianGehrmann/phenotyping). This file should be saved to the root directory as `w2v.txt`. The preprocessed data files `data.h5` and `data-nobatch.h5` can be generated by running the following command with python 3:

```
python preprocess.py data/annotations.csv w2v.txt --batchsize=5
```

This will create `data.h5` and `data-nobatch.h5` in the root folder.

### Baseline Methods

Create a directory named `converted` in the root directory, if you have not run the baseline methods script previously. To run the baseline methods:

```
python basic_models.py --data data-nobatch.h5 --ngram 5
```

ngram value should be set to 1 to run bag of words logistic regression

### Convolutional Neural Net (CNN)

Create a directory named `results` in the root directory, if you have not run the CNN script previously. First, run the following to install torch:

```
git clone https://github.com/torch/distro.git
cd distro
bash install-deps
./install.sh
```

If you are using a Mac, first run:

```
brew install hdf5@1.8
```

Then run the following to install the correct version of hdf5:

```
git clone https://github.com/anibali/torch-hdf5.git
cd torch-hdf5
git checkout hdf5-1.10 
luarocks make hdf5-0-0.rockspec
```

If you are using a Mac, edit the file `distro/install/share/lua/5.1/hdf5/config.lua` to point to the brew installed version of hdf5:

```
hdf5._config = {
      HDF5_INCLUDE_PATH = "/usr/local/Cellar/hdf5@1.8/1.8.22_3/include",
      HDF5_LIBRARIES = "/usr/local/Cellar/hdf5@1.8/1.8.22_3/lib/libhdf5.dylib"
}
```

Finally, run the CNN script using:

```
th main.lua -label_index i
```

i should be replaced with the label that you wish to train and evaluate the CNN for: Advanced Cancer (12), Advanced Heart Disease (5), Advanced Lung Disease (6), Chronic Neurological Dystrophies (11), Chronic Pain Fibromyalgia (10), Alcohol Abuse (8), Other Substance Abuse (9), Obesity (2), Schizophrenia and other Psychiatric Disorders (7), Depression (13)

## Results
Below is a table of our results, showing precision, recall, and f1-score for the CNN and two baseline methods.

|                       | CNN                  | BoW                 | n-gram              |
| --------------------- | -------------------- | ------------------- | ------------------- |
| Adv. Cancer           | P:96, R:98, F1: 97   | P:83, R:72, F1: 76  | P:81, R:63, F1: 68  |
| Adv. Heart Disease    | P:94, R:94, F1: 94   | P:66, R:65, F1: 66  | P:69, R:62, F1: 64  |
| Adv. Lung Disease     | P:93, R:99, F1: 96   | P:80, R:70, F1: 74  | P:81, R:61, F1: 65  |
| Chronic Neuro         | P:86, R:91, F1: 89   | P:66, R:62, F1: 64  | P:62, R:59, F1: 60  |
| Chronic Pain          | P:83, R:95, F1: 88   | P:68, R:63, F1: 64  | P:71, R:61, F1: 63  |
| Alcohol Abuse         | P:96, R:97, F1: 97   | P:77, R:72, F1: 74  | P:83, R:70, F1: 74  |
| Substance Abuse       | P:95, R:97, F1: 96   | P:79, R:68, F1: 72  | P:78, R:60, F1: 63  |
| Obesity               | P:99, R:99, F1: 99   | P:64, R:57, F1: 59  | P:67, R:55, F1: 56  |
| Psychiatric Disorders | P:95, R:99, F1: 97   | P:64, R:63, F1: 63  | P:64, R:61, F1: 62  |
| Depression            | P:89, R:95, F1: 92   | P:58, R:57, F1: 57  | P:57, R:56, F1: 56  |
