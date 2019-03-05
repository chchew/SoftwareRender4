#UNIVERSIDAD DEL VALLE DE GUATEMALA
#SR4
#CARLOS CHEW - 17507


def inicio(s, base=10, val=None):
  try:
    return int(s, base)
  except ValueError:
    return val


class Obj(object):
    def __init__(self, filename):
        with open(filename) as f:
            self.lineas = f.read().splitlineas()
        self.vertices = []
        self.vfaces = []
        self.read()

    def read(self):
        for line in self.lineas:
            if line:
                prefix, value = line.split(' ', 1)
                if prefix == 'v':
                    self.vertices.append(list(map(float, value.split(' '))))
                elif prefix == 'f':
                    self.vfaces.append([list(map(inicio, face.split('/'))) for face in value.split(' ')])
