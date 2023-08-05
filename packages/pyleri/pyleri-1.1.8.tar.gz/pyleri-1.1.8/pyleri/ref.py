'''pyleri.Ref Class.

When a forward reference is used the grammar must contain a final
reference with the same name. The Grammar class is used to validate
a valid grammer and set element.

:copyright: 2015, Jeroen van der Heijden (Transceptor Technology)
'''
from .elements import NamedElement


class Ref(NamedElement):
    '''Ref class.'''

    __slots__ = ('_element', '_get_node_result')

    @property
    def element(self):
        return getattr(self, '_element', None)

    @element.setter
    def element(self, element):
        self._element = self._validate_element(element)
        self._get_node_result = self._element._get_node_result

    def _run_export_js(self, js_identation, ident, classes):
        return 'Ref({})'.format(self._element.__class__.__name__)

    def _run_export_py(self, py_identation, ident, classes):
        return 'Ref()'

    def _run_export_c(self, c_identation, ident, enums):
        return 'cleri_ref()'

    def _run_export_go(self, go_identation, ident, classes):
        return 'goleri.NewRef()'
