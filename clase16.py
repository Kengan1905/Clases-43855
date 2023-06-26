#GIT sistema de control de versiones
#Tener CUIDADO donde se lo esta utilizando.
# class Persona ():
#     def __str__(self):
#         return 'Yo soy tu padre'

# class Cliente(Persona):
#     def __str__(self):
#         return super().__str__() + ' y yo tu hijo'

# cliente = Cliente()

# print(cliente)
#GIT: LOS 3 ESTADOS
#working directory: es cuando git detecta que hay cambios en un archivo y lo manda al working directory
#staging area: una vez q vamos haciendo cambios q nos parece q estan bien, se va guardando en una cajita "stagin area" "git add es el comando"
#una vez q pensamos q los cambios de esta cajita estan bien, queremos que queden fijos y los fijamos como una version estable.
#repository: cuando vemos q ese staging area tiene unos cambios estables que nos parece que esta bien vamos al
# git commit que los fija como una version estable de nuestros proyectos.

#git config --global user.name
#git config --global user.email
#git config --list
#git help config

#ls: todos los archivos que estan aca
#pwd: para asegurarme donde estoy
#start . para visualizar la carpeta donde estoy ubicado

#git init: para que esa ubicacion comience a ser seguida por git
#git status: nos indica el status de los cambios que git esta siguiendo
#todo esto de git statuts esta en el WORKING DIRECTORY
#creamos un nuevo archivo llamado .gitignore y ahi mencionamos las carpetas que queremos que git ignore
#este .gitignore hay que mantenerlo actualizado para que git lo ignore

#Vamos a la Extension de Control de Codigo Fuente y todo lo que esta en Cambios refiere a la parte de working directory
#git add(nombres de los archivos que quiero agregar al staging area)
#Untracked son los que git no esta siguiendo.
#'git add .' me subo todo a staging area
# en staging area le damos el signo - (menos) y nos lo devuelve para atras al working directory
#Antes de pasar las cosas al staging area tenemos q pasar en el 
#.gitignore las cosas que queremos ignorar
#git commit -m 'Mensaje' para identificar que es lo que se hizo en esos cambios que yo estoy agregando en mi version estable
#commit pasa lo de staging area a una version estable
#es como que agarra la cajita le pone un sello y dice esto esta correcto.
#git log
#git log --oneline
#1 hora de clase.
#Entonces GIT ADD para pasar de working directory a staging area
#y GIT COMMIT -m 'mensaje' para pasar de staging area a una version estable

#1 hora 14 min clase GIT - GIT HUB

#git branch es para ver en que rama estamos parados
#Ramas sirve para crear una rama paralela al trabajo pero aparte del programa donde estan usando todos, porque si algo me sale mal, se va a romper el programa donde estan los otros usuarios.
#CREAR RAMA: git branch 'nombre a la rama' . Pero me mantiene en la que estoy.
#Otra forma, git checkout -b 'nombre a la rama' . Crea la nueva rama y me posiciona en la nueva.
#PARA MOVERNOS DE RAMA: git checkout 'nombre a la rama que nos queremos mover'
#PARA BORRAR RAMA: git branch -D 'nombre de la rama'
#PARA TRAER TOD0 A LA RAMA EN LA QUE ESTAMOS: git merge 'nombre de la rama que tiene lo que queremos traer'
#Merge lo que hace es si hay camnbios en algun archivo me trae los cambios, ahora si hay archivos nuevos, me trae esos archivos nuevos y me los agrega
#ahora, si tiene archivos eliminados, que todavia estan en prueba, me va a borrar los arhivos que tengo en prueba
#o sea, lo q hace el merge es traerme todos los commit que hay en un lado que no estan en el otro. y me pisa lo que yo estoy teniendo
#Si yo escribo "git checkout 'copio y pego el codigo amarrillo de un commit' me lleva a en lo que estaba en ese commit
#
#
#
#
#
#
#
#
#
#
#
#
#
#






