import pandas as pd

ds = {
    "student_id": ["ST001", "ST002", "ST003", "ST004",],
    "student_department": ["Cyber Security", "Music", "Accounting", "Computer Science"],
    "student_level": [300, 500, 200, 300],
    "attendance(%)": [85, 92, 78, 88],
    "average_score": [50, 72, 95, 81]
}

df = pd.DataFrame(ds)
print(df)
