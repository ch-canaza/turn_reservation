from models.connectionpsql import db


class UserModel(db.Model):
    """
        defines the Model 'user table'
    """


    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    
    def __init__(self, name):
        """
            initializes user columns 
        """
        self.name = name
