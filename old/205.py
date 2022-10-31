from docxtpl import DocxTemplate


def create_training_sheet(class_name, subject_name, name, *marks):
    d = DocxTemplate(name)
    marks = sorted(marks, key=lambda x: x[0])
    context = {'class_name': class_name,
               'subject_name': subject_name,
               'marks': [{'num': i + 1, 'fio': marks[i][0], 'mark': marks[i][1]}
                         for i in range(len(marks))]}
    d.render(context)
    d.save("res.docx")