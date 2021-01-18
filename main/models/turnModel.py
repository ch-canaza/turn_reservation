from models.connectionpsql import db


class TurnModel(db.Model):
    """
        defines the Model 'Turn table'
    """


    __tablename__ = 'user_driver'

    driver_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, primary_key=False)
    date = db.Column(db.DateTime)
    
    def __init__(self, driver_id, user_id, date):
        """
            initializes user_driver turn columns 
        """
        self.driver_id = driver_id
        self.user_id = user_id 
        self.date = date
