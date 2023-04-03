import hashlib

from player import Player
class Game:

    def __init__(self, player1 : Player, player2 : Player):
        self.player1 = player1
        self.player2 = player2


    def calculate_hash(self, chaine):
        """Méthode pour calculer la chaine concaténer"""
        sha = hashlib.sha256()
        sha.update(chaine.encode('utf-8'))
        return sha.hexdigest()

    def is_valid(self, choice):
        return choice in ['pierre', 'feuille', 'ciseaux']

    def play_a_turn(self):
        #verifier si les choix sont valides
        if not self.is_valid(self.player1.getChoix()) or not self.is_valid(self.player2.getChoix()):
            raise ValueError('Choix invalide')

        #concatener les choix et les nonces des deux joueurs
        chaine = self.player1.getChoix() + str(self.player1.generateNonce()) + self.player2.getChoix() + str(self.player2.generateNonce())

        hash_chaine = self.calculate_hash(chaine)

        return hash_chaine

    def determinate_winner(self):
        pass


