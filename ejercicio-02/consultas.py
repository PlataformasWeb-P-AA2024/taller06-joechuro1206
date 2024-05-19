from sqlalchemy import create_engine, Column, Integer, String, or_
from sqlalchemy.orm import sessionmaker
from genera_base import Pais

engine = create_engine('sqlite:///dbpaises.db')
Session = sessionmaker(bind=engine)
session = Session()

# Presentar todos los países del continente americano
print(f'\tCONSULTA 1:')
c1 = session.query(Pais).filter(Pais.continente.in_(['SA', 'NA'])).order_by(Pais.nombre).all()
print("Países del continente americano:")
for pais in c1:
    print(f"{pais.nombre}")

print('-----------------------------------------------')

# Presentar los países de Asía, ordenados por el atributo Dial.
print(f'\tCONSULTA 2:')

c2 = session.query(Pais).filter(Pais.continente == 'AS').order_by(Pais.dial).all()
print("Países de Asia ordenados por Dial:")
for pais in c2:
    print(f"{pais.nombre} | Dial: {pais.dial}")

print('-----------------------------------------------')

# Presentar los lenguajes de cada país.
print(f'\tCONSULTA 3:')

c3 = session.query(Pais).order_by(Pais.lenguajes).all()
print("Lenguajes de cada país:")
for pais in c3:
    print(f"{pais.nombre} | Lenguajes: {pais.lenguajes}")

print('-----------------------------------------------')

# Presentar los países ordenados por la capital, siempre que el país pertenezca a Europa
print(f'\tCONSULTA 4:')

c4 = session.query(Pais).filter(Pais.continente == 'EU').order_by(Pais.capital).all()
print("Países de Europa ordenados por capital:")
for pais in c4:
    print(f"{pais.nombre} | Capital: {pais.capital}")

print('-----------------------------------------------')

print(f'\tCONSULTA 5:')
# Presentar todos los países que tengan en su cadena de nombre de país "uador" o en su cadena de capital "ito".
c5 = session.query(Pais).filter(or_(Pais.nombre.like('%uador%'), Pais.capital.like('%ito%'))).all()
print("Países con 'uador' en el nombre o 'ito' en la capital:")
for pais in c5:
    print(f"País: {pais.nombre}, Capital: {pais.capital}")
