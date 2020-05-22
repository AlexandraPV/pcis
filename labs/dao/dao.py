class NotFoundError(Exception):
    def __init__(self, obj):
        self.msg = '{} not found'.format(str(obj))


class BaseDao:
    MODEL_NAME = None

    @classmethod
    def find_one(cls, pk):
        return cls.MODEL_NAME.objects.get(id=pk)

    @classmethod
    def find_all(cls):
        return cls.MODEL_NAME.objects.all()

    @classmethod
    def get_m2m(cls, obj, field_name):
        try:
            m2m_rel = getattr(obj, field_name).all()
            return m2m_rel
        except AttributeError as e:
            raise

    @classmethod
    def delete(cls, obj):
        try:
            obj.delete()
            return True
        except Exception as e:
            raise NotFoundError(obj)
