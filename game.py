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
	def __init__(self, name: str, power, min_level: int) -> None:
		self.name = name
		self.power = power
		self.min_level = min_level

	def make_unarmed(self):
		pass
		UNARMED_POWER = 20
		self.name = "Unarmed"
		self.power = UNARMED_POWER
		self.min_level = 1


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
		self.name = name
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.weapon = Weapon

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

def deal_damage(attacker, defender):
	# TODO: Calculer dégâts
	damage, crit = attacker.compute_damage(defender)
	defender.max_hp -= damage

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
		if defender.max_hp <= 0:
			print(f"{defender.name } is sleeping with the fishes.")
			break
		# Échanger attaquant/défendeur
		attacker, defender = defender, attacker

	# TODO: Retourner nombre de tours effectués
	return turns
