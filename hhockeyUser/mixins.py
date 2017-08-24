

class PageTitleMixin(object):
    """
    Allows for tabbing content.  So much for using react..
    """
    active_tab = None

    def get_context_data(self, **kwargs):
        ctx = super(PageTitleMixin, self).get_context_data(**kwargs)
        ctx.setdefault('active_tab', self.active_tab)
        return ctx