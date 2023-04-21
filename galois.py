# Dans ce fichier, nous allons implémenter les opérations mathématiques
# dans les corps finis, aussi appelés corps de Galois.


class CorpsGalois(object):

    def __init__(self, p):
        # Initialisation des champs.
        self.degre_max = (2 ** degre(p)) - 1
        self.exps = [0] * self.degre_max
        self.logs = [0] * (self.degre_max + 1)


        self.polynome_primitve = 285
        # À compléter.
        # Remplir les listes self.exps et self.logs

        p_x = 1
        for i in range(self.degre_max):
            self.exps[i] = p_x
            self.logs[p_x] = i
            p_x <<= 1
            p_x = modulo(p_x, self.polynome_primitve)

    def plus(self, a, b):                                                           
        return a ^ b
       
    def moins(self, a, b):
        return a ^ b     

    def fois(self, a, b):
            if a == 0 or b == 0:
                return 0

            log_a = self.logs[a]
            log_b = self.logs[b]
            log = (log_a + log_b) % self.degre_max
            result = self.exps[log]

            return result

    def division(self, a, b):
            if b == 0:
                raise ZeroDivisionError()
            if a == 0:
                return 0
            log_a = self.logs[a]
            log_b = self.logs[b]
            log = (log_a - log_b) % self.degre_max
            result = self.exps[log]

            return result

    def puissance(self, a, b):
            if a == 0:
                return 0
            log_a = self.logs[a]
            log = (log_a * b) % self.degre_max
            result = self.exps[log]

            return result



class AnneauPolynome(object):

    def __init__(self, corps):
        self.corps = corps


    def fois(self, p, q):
            r = [0] * (len(p) + len(q) - 1)
            for i in range(len(p)):
                for j in range (len(q)):   
                    k = r[i+j]
                    m = self.corps.fois(p[i], q[j])
                    r[i+j] = self.corps.plus(k, m)
            return r

    def reste_division(self, p, q):

        while len(p) >= len(q):
            p_max = p[0]
            q_max = q[0]
            for i in range(len(q)):
                q_m = self.corps.fois(q[i], p_max)
                q_m = self.corps.division(q_m, q_max)
                p[i] = self.corps.moins(p[i], q_m)
            p.pop(0)

        return p

    def generateur(self, n):
        r = [1]
        for i in range(n):
            r = self.fois(r, [1, self.corps.puissance(2, i)])
        return r


class Correcteur(object):

    def __init__(self, n_extra, p):
        self.anneau = AnneauPolynome(CorpsGalois(p))
        self.generateur = self.anneau.generateur(n_extra)

    def encode(self, donnees):
        avec_extra = donnees + [0] * (len(self.generateur) - 1)
        return self.anneau.reste_division(avec_extra, self.generateur)      


def degre(n):
    d = -1
    while n > 0:
        n = n >> 1
        d += 1
    return d


def bit(n, i):
    return (n >> i) & 1


def modulo(dividende, diviseur):
    while degre(dividende)>=degre(diviseur):
        dividende = dividende^(diviseur << (degre(dividende)-degre(diviseur)))


    return dividende


def encode_format(mode, masque):
    mode <<= 3
    result = mode^masque
    result <<= 10

    rest = modulo(result, 0b10100110111)
    result ^= rest

    result = result^0b101010000010010

    return result


