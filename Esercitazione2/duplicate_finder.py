import hashlib
from collections import defaultdict
import os

def is_image(path, extensions):
    """
    Check whether the path ends with one of the extensions
    
    path: string file path
    extensions: list of extensions
    
    >>> is_image('photo.jpg', ['jpg', 'jpeg'])
    True
    >>> is_image('PHOTO.JPG', ['jpg', 'jpeg'])
    True
    >>> is_image('notes.txt', ['jpg', 'jpeg'])
    False
    """
    # lower() restituisce una copia della stringa in cui tutti i caratteri sono in minuscolo
    # endswith() restituisce True se la stringa termina con il suffisso specificato
    for extension in extensions:
        if path.lower().endswith(extension):
            return True
    return False

def md5_digest(filename):
    data = open(filename, 'rb').read()
    md5_hash = hashlib.md5()
    md5_hash.update(data)
    digest = md5_hash.hexdigest()
    return digest

def add_path(path, d):
    """
    Compute the digest of path, add the digest to d as key and append path to a list as value

    path : path to a file
    d : defaultdict of lists # "C:/Users/Home/OneDrive/Desktop/ES_PYTHON/Esercitazione2/photos/feb-2023/photo1.jpg"

    >>> add_path("C:/Users/Home/OneDrive/Desktop/ES_PYTHON/Esercitazione2/photos/feb-2023/photo1.jpg", defaultdict(list))
    defaultdict(<class 'list'>, {'dace5bcdd614b5a23e465b1edc406bc3': ['C:/Users/Home/OneDrive/Desktop/ES_PYTHON/Esercitazione2/photos/feb-2023/photo1.jpg']})
    """
    # Nota che se due file contengono gli stessi dati, avranno lo stesso digest. Se due file sono diversi,
    # avranno quasi sempre digest diversi. Un digest è l'output di una funzione hash. 
    # Usa md5 per questo scopo: una funzione che restituisce il digest di un percorso.
    # il digest è la rappresentazione unica e compatta delle informazioni originali contenute
    # nel documento firmato, nonché del documento stesso. 
    # È la cosiddetta impronta digitale del documento informatico
    digest = md5_digest(path)
    # append() aggiunge un elemento alla fine della lista
    d[digest].append(path) 
    return d

def walk_images(dirname, d):
    """
    Walk the directory tree and return a defaultdict of lists where
    - the key is the digest of the image
    - the value is a list of paths to the images with the same digest

    dirname : path to a directory
    d : defaultdict of lists
    """
    # walk_image prende una directory e scorre i file in questa directory e nelle sue sottodirectory. 
    # Per ogni file, dovrebbe usare  is_image per controllare se è un file immagine e  
    # add_path per aggiungerlo a defaultdict
    # os.listdir() restituisce un elenco di voci in un percorso specificato
    # os.path.join() unisce uno o più componenti di percorso in un percorso
    # os.path.isfile() restituisce True se il percorso specificato è un file
    # os.path.isdir() restituisce True se il percorso specificato è una directory
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path) and is_image(path, ['jpg', 'jpeg']):
            add_path(path, d)
        elif os.path.isdir(path):
            walk_images(path,d)
        
def main():
    d = defaultdict(list)
    walk_images(".", d)
    for digest, paths in d.items(): # items() restituisce una vista(tupla   ) di oggetti chiave-valore
        if len(paths) > 1:
            for path in paths:
                print(path)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    main()
