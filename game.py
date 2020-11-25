"""
Chapitre 11.1

Classes pour représenter un personnage.
"""


import random

import utils


class Weapon:
	"""
	Une arme dans le jeu.

	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""
	UNARMED_POWER = 20

	def __init__(self, name: str, power, min_level: int) -> None:
		self.__name = name		# Attribut privé
		self.power = power
		self.min_level = min_level

	'''Pour modifier l'attributs name, il faut passer par le setter. Contrôle sur accès des variables privés.'''

	@property
	def name(self):
		return self.__name


	# Méthode de classe
	''' On passe une instance de la classe Weapon en cls. Cls représente le template de weapon'''
	@classmethod
	def make_unarmed(cls):
		return cls("Unarmed", cls.UNARMED_POWER, 1)
		# return Weapon(Weapon.UNARMED_POWER, "Unarmed") # Autre méthode


class Character:
	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""
	def __init__(self, name: str, max_hp: float, attack, defense, level: int) -> None:
		self.__name = name	# Attribut privé, peut pas le changer
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.weapon = None
		self.__hp = max_hp

	# Accesseur. Pour aller lire la valeur de l'attribut privé
	@property
	def name(self):
		return self.__name

	# Accesseur
	@property
	def weapon(self):
		return self.__weapon

	# Affecter ce qui est passé comme valeur, Si la valeur est Non, je lui ..
	# Setter : Pour aller écrire dans la variable privée.
	@weapon.setter
	def weapon(self, val):
		if val is None:
			val = Weapon.make_unarmed()
		if val.min_level > self.level:
			raise ValueError(Weapon)
		self.__weapon = val

	# Définir getter/Setter pour 'hp', qui doit être borné entre 0 et max_ho ...
	@property
	def hp(self):
		return self.__hp

	@hp.setter
	def hp(self, val):
		self.__hp = utils.clamp(val, 0, self.max_hp)

	def compute_damage(self, other):
		level_factor = (2 * self.level) / 5 + 2
		weapon_factor = self.weapon.power
		atk_def_factor = self.attack / other.defense
		critical = random.random() <= 1/16
		modifier = (2 if critical else 1) * random.uniform(0.85, 1.0)
		damage = ((level_factor * weapon_factor + atk_def_factor)/ 50) * modifier
		return int(round(damage)), critical

	'''
	# Ma fonction
	def compute_damage(self, defender: "Character") -> float:
		# a = self, notre personnage attaque
		# 6.25% du temps, crit = 2. Sinon crit = 1
		number_random = random.random()
		if number_random < 0.0625:
			crit = 2
		else:
			crit = 1
		# Ajoute un facteur aléatoire au nombre de dommages faits
		modifier = crit * random.randrange(85, 100)/100
		damage = ((((2 * self.level) / 5 + 2) * self.weapon.power * self.attack / defender.defense) / 50 + 2) * modifier
		return int(damage), crit
	'''
def deal_damage(attacker, defender):
	# TODO: Calculer dégâts
	damage, crit = attacker.compute_damage(defender)
	defender.hp -= damage

	print(f"{attacker.name} used {attacker.weapon.name}")
	if crit == 2:
		print("  Critical hit!")
	print(f"  {defender.name} took {damage} dmg")

def run_battle(c1, c2):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	turns = 0
	attacker = c1
	defender = c2

	print(f"{attacker.name} starts a battle with {defender.name}!")

	while True:
		# TODO: Appliquer l'attaque
		turns += 1
		deal_damage(attacker, defender)

		# TODO: Si le défendeur est mort
		if defender.hp <= 0:
			print(f"{defender.name } is sleeping with the fishes.")
			break
		# Échanger attaquant/défendeur
		attacker, defender = defender, attacker	# Swap les variables

	# TODO: Retourner nombre de tours effectués
	return turns
