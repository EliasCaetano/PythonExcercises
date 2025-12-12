import math
ang = int(input('Informe o ângulo: '))
rad = math.radians(ang)
cos = math.cos(rad)
sen = math.sin(rad)
tan = math.tan(rad)

print('Ângulo informado: {:.2f}\nCosseno: {:.2f}\nSeno: {:.2f}\nTangente: {:.2f}'.format(ang,cos,sen,tan))
