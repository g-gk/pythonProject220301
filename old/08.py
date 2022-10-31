from docxtpl import DocxTemplate


def create_training_sheet(class_name, subject_name, tpl_name, *students):
    students = list(students)
    students = sorted(students)
    doc = DocxTemplate(tpl_name)
    mark = list()
    for i in range(len(students)):
        d = dict()
        d['num'] = i + 1
        d['fio'] = students[i][0]
        d['mark'] = students[i][1]
        mark.append(d)
    context = {
        'class_name': class_name,
        'subject_name': subject_name,
        'marks': mark
    }
    doc.render(context)
    doc.save("res.docx")


create_training_sheet("3И", "Математика", "tpl.docx",
                      ("Петров Петр", "5"),
                      ("Иванов Иван", "5"),
                      ("Сергеев Сергей", "3"),
                      ("Никитин Никита", "4"))
