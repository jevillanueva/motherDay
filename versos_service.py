from database import db


def registrar_verso(verso, poema, verso_posicion):
    db.versos.insert_one({'verso': verso, 'poema': poema,
                          'verso_posicion': verso_posicion})
    return True


def listar_versos():
    return db.versos.find()


def listar_versos_poema(poema: str):
    return list(db.versos.find({'poema': poema}).sort('verso_posicion', 1))


def random_poema(poema: str = None):
    if poema is None:
        versos = db.versos.aggregate(
            [{"$match": {}}, {"$sample": {"size": 1}}])
    else:
        versos = db.versos.aggregate([
            {"$match":
             {'poema':
              {"$regex": poema, "$options":'i'}
              }
             },
            {"$sample": {"size": 1}}
        ])
    verso_actual = {}
    for verso in versos:
        verso_actual = verso
    return verso_actual

def generator_random_versos(versos: int = 2):
    versos = list(db.versos.aggregate([
        {"$match": {}},
        {"$sample": {"size": versos}}
    ]))
    verso_actual = []
    versos_full = ""
    if versos != []:
        title = versos[0]['poema']
    else:
        title = 'No hay poemas'
    for verso in versos:
        verso['verso_posicion'] = versos.index(verso) + 1
        del(verso['_id'])
        del(verso['poema'])
        verso_actual.append(verso)
        verso['verso'] = verso['verso'].replace('\n', ' ').replace('\r', '').replace('\t', '')
        versos_full = versos_full +" "+ verso['verso']
    if  verso_actual != []:
        return verso_actual, title, versos_full.strip()
    else:
        return [], "", versos_full


def generator_poema(poema):
    verso = random_poema(poema)
    versos = ""
    if verso != {}:
        poema_full = listar_versos_poema(verso['poema'])
        for verso_poema_full in poema_full:
            del(verso_poema_full['_id'])
            del(verso_poema_full['poema'])
            verso_poema_full['verso'] = verso_poema_full['verso'].replace('\n', ' ').replace('\r', '').replace('\t', '')
            versos = versos + verso_poema_full['verso'] +" "
        return poema_full, verso['poema'], versos.strip()
    else:
        return [], poema, versos

def generator_random_poema(numero_versos: int = 2):
    # for i in range(numero_versos):
    #     verso = random_poema()
    #     new_poema.append(verso)
    new_poema, title, versos = generator_random_versos(numero_versos)
    return new_poema, title, versos

