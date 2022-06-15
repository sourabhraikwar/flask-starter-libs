from main.settings import db


class Site(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    domain_name = db.Column(db.String(100), unique=True, nullable=True)
    domain_host = db.Column(db.String(200), unique=False, nullable=False)

    def __repr__(self):
        return "<Site %r>" % self.domain_name
