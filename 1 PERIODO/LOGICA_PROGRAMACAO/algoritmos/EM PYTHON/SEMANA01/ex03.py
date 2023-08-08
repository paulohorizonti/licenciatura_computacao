# Ler 4 notas e verificar aprovação
n1 = eval(input('Digite a primeira nota: '))
n2 = eval(input('Digite a segunda nota: '))
n3 = eval(input('Digite a terceira nota: '))
n4 = eval(input('Digite a quarta nota: '))

media = (n1 + n2 + n3 + n4) / 4

if media >= 7:
    print('Com a média {} o aluno está APROVADO'.format(media))
if media <= 4:
    print('Com a média {} o aluno está REPROVADO'.format(media))
else:
    print('O aluno fez exame, pois sua media ficou entre 4 e 7, digite agora a nota do exame: ')
    exame = eval(input('Digite a nota de exame do moleque : '))
    media_final = (media + exame) / 2
    if media_final >= 5:
        print('O aluno obteve media final apos o exame de {}, com essa media final ele está APROVADO COM EXAME'.format(
            media_final))
    else:
        print('O aluno obteve media final apos o exame de {}, com essa media final ele está REPROVADO COM EXAME'.format(
            media_final))
