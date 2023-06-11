#GIT sistema de control de versiones
#Tener CUIDADO donde se lo esta utilizando.
class Persona ():
    def __str__(self):
        return 'Yo soy tu padre'

class Cliente(Persona):
    def __str__(self):
        return super().__str__() + ' y yo tu hijo'

cliente = Cliente()

print(cliente)
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
#