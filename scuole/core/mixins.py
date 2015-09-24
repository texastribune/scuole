class GetStatsMixin(object):
    def get_context_data(self, **kwargs):
        context = super(GetStatsMixin, self).get_context_data(**kwargs)
        print(kwargs)
        context['stats'] = 'hi'
        return context
