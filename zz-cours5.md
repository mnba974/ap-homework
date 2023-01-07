# cours #5 du 14 décembre

## devoirs

à publier comme toujours dans votre repo `ap-homework`

* finir le TP commencé en cours, et le publier dans un dossier `students-grades`

* faites l'exercice sur les quaternions qui se trouve ici:
  https://nbhosting.inria.fr/auditor/notebook/exos-mooc:exos/w6/w6-s9-x8-quaternion
  et publiez votre code dans le dossier `quaternion` de votre `ap-homework`

  vous aurez besoin de savoir que, pour définir le comportement de l'addition et de la multiplication,
  vous devez définir les *dundle* méthodes `__add__` et `__mul__`

  par exemple:

  ```python
  In [3]: class Foo:
   ...:     def __init__(self, value):
   ...:         self.value = value
   ...:     def __repr__(self):
   ...:         return f"<Foo ({self.value})>"
   ...:     def __add__(self, other):
   ...:         return Foo(self.value + other.value)
   ...:

  In [4]: Foo(10) + Foo(30)
  Out[4]: <Foo (40)>
  ```

## le cours

### quiz

### retours sur les exercices

### cours

* 5-12 dunder methods
* 5-13 inheritance
* 5-14 class attributes
* 5-15 ERRATUM sur ce que j'ai pu dire la fois passée, concernant la visibilité de la classe à l'intérieur de la définition de la classe

### exos

* Romain ou Polynomial
$$