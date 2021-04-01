from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ModelManager(object):
    def bulk_save(self, list_obj):
        try:
            for obj in list_obj:
                db.session.add(obj)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()

    def commit(self):
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()


class AbstractModel(db.Model):
    __abstract__ = True

    objects = ModelManager()

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            db.session.refresh(self)
        except Exception as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()
