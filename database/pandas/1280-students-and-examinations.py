import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    cross = students.merge(subjects, how='cross')

    exam_count = (examinations.groupby(['student_id', 'subject_name'])
                                .size()
                                .reset_index()
                                .rename(columns={0: 'attended_exams'}) # count per student x subject
        )

    return (cross.merge(exam_count,
                        on=["student_id", "subject_name"],
                        how='left'
        ).fillna({'attended_exams': 0}) # missing = never attended
        .sort_values(['student_id', 'subject_name'])
        [['student_id', 'student_name', 'subject_name', 'attended_exams']]
    )
