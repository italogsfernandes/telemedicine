from app import db

# Table representing a relationship *.* between Clinic and User
joinClinicUser = db.Table(
    'joinClinicUser',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('clinic_id', db.Integer, db.ForeignKey('clinic.id'))
)

# Table representing a relationship *.* between Specialty and User
joinsSpecialtyUser = db.Table(
    'joinsSpecialtyUser',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('specialty_id', db.Integer, db.ForeignKey('specialty.id'))
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    image_file = db.Column(db.String(100))
    # format crm: 0000000000000/MG
    crm = db.Column(db.String(13), unique=True, nullable=False)
    fullname = db.Column(db.String(256), nullable=False)
    birthdate = db.Column(db.DateTime)
    birthcity = db.Column(db.String(256))
    rg = db.Column(db.String(12), unique=True, nullable=False)
    cpf = db.Column(db.String(12), unique=True, nullable=False)
    cep = db.Column(db.Integer)
    place = db.Column(db.String(64))
    address = db.Column(db.String(256))
    neighborhood = db.Column(db.String(128))
    city = db.Column(db.String(128))
    state = db.Column(db.String(2))
    phone_1 = db.Column(db.String(16), nullable=False)
    phone_2 = db.Column(db.String(16))
    # FKs
    clinics = db.relationship('Clinic', secondary=joinClinicUser, backref=db.backref('employees', lazy='dynamic'))
    # appointments = db.relationship('Appointment', backref='specialist', lazy=True)
    specialties = db.relationship('Specialty', secondary=joinsSpecialtyUser, backref=db.backref('doctors', lazy='dynamic'))

    def __repr__(self):
        return f"User('{self.id}','{self.crm}','{self.fullname}')"


class Clinic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # format crm: 0000000000000/MG
    business_name = db.Column(db.String(256), nullable=False)
    company_name = db.Column(db.String(256), unique=True, nullable=False)
    cep = db.Column(db.Integer)
    place = db.Column(db.String(64))
    address = db.Column(db.String(256))
    neighborhood = db.Column(db.String(120))
    city = db.Column(db.String(120))
    state = db.Column(db.String(2))
    phone_1 = db.Column(db.String(16), nullable=False)
    phone_2 = db.Column(db.String(16))
    email = db.Column(db.String(120), unique=True, nullable=False)
    cnpj = db.Column(db.String(16))
    state_inscription = db.Column(db.String(32), unique=True)

    def __repr__(self):
        return f"Clinic('{self.id}','{self.business_name}')"


class Specialty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    specialty = db.Column(db.String(64), unique=True, nullable=False)

    def __repr__(self):
        return f"Specialty('{self.id}','{self.specialty}')"



class Appointment(db.Model):
    pass



    def __repr__(self):
        return f"Specialty('{self.id}','{self.specialty}')"