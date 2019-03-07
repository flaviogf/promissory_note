class ErrorArrayMixin:
    @property
    def errors(self):
        errors = super().errors
        return [i for a in errors.values() for i in a]
