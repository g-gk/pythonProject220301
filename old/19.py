from docxtpl import DocxTemplate


def create_training_sheet(class_name, subject_name, tpl_name='tpl.docx', *args):
    nn = list(args)
    nn.sort()
    names = []
    x = 0
    for n in nn:
        x += 1
        d = {}
        d['num'] = str(x)
        d['fio'] = n[0]
        d['mark'] = n[1]
        names.append(d)

    # names.sort()
    doc = DocxTemplate(tpl_name)
    context = {
        'class_name': class_name,
        'subject_name': subject_name,
        'marks': names}
    doc.render(context)
    doc.save('res.docx')


create_training_sheet("3И", "Математика", "tpl.docx",
                      ("Петров Петр", "5"),
                      ("Иванов Иван", "5"),
                      ("Сергеев Сергей", "3"),
                      ("Никитин Никита", "4"))
