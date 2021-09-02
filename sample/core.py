from . import helpers
from . import submod

def get_hmm():
    """Get a thought."""
    return 'hmm...'

def hmm(wanted):
    """Contemplation..."""
    if helpers.get_answer(wanted):
        return get_hmm()
    else:
        return None

def pretty_sum(a,b):
    return (str(a)+' + '+str(b)+' = '+str(submod.extras.sum(a,b)))

def pretty_multiply(a,b):
    return (str(a)+' X '+str(b)+' = '+str(submod.extras.multiply(a,b)))