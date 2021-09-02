from . import helpers

def get_hmm():
    """Get a thought."""
    return 'hmm...'

def hmm(wanted):
    """Contemplation..."""
    if helpers.get_answer(wanted):
        return get_hmm()
    else:
        return None