from database import db

def registrar_verso(verso, poema, verso_posicion):
    db.versos.insert_one({'verso': verso, 'poema': poema, 'verso_posicion': verso_posicion})
    return True

def listar_versos():
    return db.versos.find()

def listar_versos_poema(poema):
    return db.versos.find({'poema': poema}).sort('verso_posicion', 1)