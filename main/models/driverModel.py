from models.connectionpsql import db


class DriverModel(db.Model):
    """
        defines the Model 'driver table'
    """


    __tablename__ = 'driver'

    driver_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    placa = db.Column(db.String())
    
    def __init__(self, name, placa):
        """
            initializes driver columns 
        """
        self.name = name
        self.placa = placa
