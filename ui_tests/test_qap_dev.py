def test_carlos_is_on_leadership(py):
    py.visit('https://qap.dev')
    py.get('a[href="/about"]').hover()
    py.get('a[href="/leadership"][class^="Header-nav"]').click()
    assert py.contains('Carlos Kidman')