from pyramid.security import Allow, Deny, Everyone, Authenticated, authenticated_userid
from pyramid.events import subscriber, BeforeRender

class RootFactory(object):
    __acl__ = [(Allow, Authenticated, 'view')]

    def __init__(self, request):
        pass

@subscriber(BeforeRender)
def before_render(event):
    pass
