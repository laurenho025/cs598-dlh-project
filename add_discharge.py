import pandas as pd


def main():
    annotations = pd.read_csv('data/annotations.csv')
    discharges = pd.read_csv('data/NOTEEVENTS.csv')[['SUBJECT_ID', 'HADM_ID', 'TEXT']]
    annotations_text = pd.merge(annotations, discharges, how='left', left_on=['Hospital.Admission.ID', 'subject.id'], right_on=['HADM_ID', 'SUBJECT_ID'])
    annotations_text.drop(['SUBJECT_ID', 'HADM_ID'], axis=1, inplace=True)
    annotations_text.rename(columns={'TEXT': 'text'}, inplace=True)
    annotations_text = annotations_text.drop_duplicates(
        subset=['Hospital.Admission.ID', 'subject.id'],
        keep='first')
    print(annotations.shape)
    print(annotations_text.shape)
    print(annotations_text.head())
    annotations_text.to_csv('data/annotations_text.csv', index=False)

if __name__ == "__main__":
    main()