def notas(*nota, sit=False):
    """
    -> Fuction to analyse the scores and situations of several students.
    :param nota: One or more students' scores.
    :param sit: Option to return a situation or not
    :return:Dictionary with information about the students and their respective scores.
    """
    resumo = dict()
    resumo['total'] = len(nota)
    resumo['maior'] = max(nota)
    resumo['menor'] = min(nota)
    resumo['media'] = sum(nota) / len(nota)
    if sit:
        if resumo['media'] >= 7:
            resumo['situacao'] = 'Aprovado'
        elif 5 < resumo['media'] < 7:
            resumo['situacao'] = 'Recuperação'
        else:
            resumo['situacao'] = 'Reprovado'
    return resumo

#Main Program
print(notas(5,7,4,6, sit=True))
help(notas)




