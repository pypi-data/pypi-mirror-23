'''Element and NamedElement Class.

These are the base classes used for all other elements.

:copyright: 2015, Jeroen van der Heijden (Transceptor Technology)
'''


def camel_case(s):
    return ''.join(
        p[0].upper() + p[1:] if n else p
        for n, p in enumerate(s.split('_')))


def cap_case(s):
    return ''.join(p[0].upper() + p[1:] for p in s.split('_') if p)


def c_export(func):

    def wrapper(self, c_identation, ident, enums):
        gid = getattr(self, 'name', getattr(self, '_name', 'CLERI_NONE'))
        if gid != 'CLERI_NONE':
            gid = 'CLERI_GID_{}'.format(gid.upper())
            enums.add(gid)
        return func(self, c_identation, ident, enums, gid)

    return wrapper


def go_export(func):

    def wrapper(self, go_identation, ident, enums):
        gid = getattr(self, 'name', getattr(self, '_name', 'NoGid'))
        if gid != 'NoGid':
            gid = 'Gid{}'.format(cap_case(gid))
            enums.add(gid)
        return func(self, go_identation, ident, enums, gid)

    return wrapper


class Element:

    __slots__ = tuple()

    @staticmethod
    def _validate_element(element):
        if isinstance(element, str):
            return Token(element)
        if isinstance(element, Element):
            return element
        raise TypeError(
            'Expecting an element or string but received type: {}'.format(
                type(element)))

    @classmethod
    def _validate_elements(cls, elements):
        return [cls._validate_element(elem) for elem in elements]


class NamedElement(Element):

    __slots__ = ('name',)

    def _export_js(self, js_identation, ident, classes):
        classes.add(self.__class__.__name__.lstrip('_'))
        if hasattr(self, 'name') and ident:
            return self.name
        return self._run_export_js(js_identation, ident or 1, classes)

    def _export_js_elements(self, js_identation, ident, classes):
        new_ident = ident + 1
        value = ',\n'.join(['{ident}{elem}'.format(
            ident=js_identation * new_ident,
            elem=elem._export_js(
                js_identation,
                new_ident, classes)) for elem in self._elements])
        return '{class_name}(\n{value}\n{ident})'.format(
            class_name=self.__class__.__name__.lstrip('_'),
            value=value,
            ident=js_identation * ident)

    def _run_export_js(self, js_identation, ident, classes):
        return 'not_implemented'

    def _export_py(self, py_identation, ident, classes):
        classes.add(self.__class__.__name__.lstrip('_'))
        if hasattr(self, 'name') and ident:
            return self.name
        return self._run_export_py(py_identation, ident or 1, classes)

    def _export_py_elements(self, py_identation, ident, classes):
        new_ident = ident + 1
        value = ',\n'.join(['{ident}{elem}'.format(
            ident=py_identation * new_ident,
            elem=elem._export_py(
                py_identation,
                new_ident, classes)) for elem in self._elements])
        return '{class_name}(\n{value}\n{ident})'.format(
            class_name=self.__class__.__name__.lstrip('_'),
            value=value,
            ident=py_identation * ident)

    def _run_export_py(self, py_identation, ident, classes):
        return 'not_implemented'

    @c_export
    def _export_c(self, c_identation, ident, enums, gid):
        if hasattr(self, 'name') and ident:
            return self.name
        return self._run_export_c(c_identation, ident or 1, enums)

    @c_export
    def _export_c_elements(self, c_identation, ident, enums, gid):
        new_ident = ident + 1
        value = ',\n'.join(['{ident}{elem}'.format(
            ident=c_identation * new_ident,
            elem=elem._export_c(
                c_identation,
                new_ident,
                enums)) for elem in self._elements])
        return 'cleri_{class_name}(\n{gid},\n{num},\n{value}\n{ident})'.format(
            class_name=self.__class__.__name__.lstrip('_').lower(),
            gid='{ident}{gid}'.format(
                ident=c_identation * (ident + 1),
                gid=gid),
            num='{ident}{num}'.format(
                ident=c_identation * (ident + 1),
                num=len(self._elements)),
            value=value,
            ident=c_identation * ident)

    def _run_export_c(self, c_identation, ident, enums):
        return 'not_implemented'

    @go_export
    def _export_go(self, go_identation, ident, enums, gid):
        if hasattr(self, 'name') and ident:
            return camel_case(self.name)
        return self._run_export_go(go_identation, ident or 1, enums)

    @go_export
    def _export_go_elements(self, go_identation, ident, enums, gid):
        new_ident = ident + 1
        value = ',\n'.join(['{ident}{elem}'.format(
            ident=go_identation * new_ident,
            elem=elem._export_go(
                go_identation,
                new_ident,
                enums)) for elem in self._elements])
        return '{class_name}(\n{gid},\n{value},\n{ident})'.format(
            class_name='goleri.New' + self.__class__.__name__.lstrip('_'),
            gid='{ident}{gid}'.format(
                ident=go_identation * (ident + 1),
                gid=gid),
            value=value,
            ident=go_identation * ident)

    def _run_export_go(self, go_identation, ident, enums):
        return 'not_implemented'

# Added this import to the bottom to prevent circular import cycle.
# Note: usually this is bad design but in this case we do want class
#       inheritance which allows us to create a new class Token which
#       is sub-classed from the 'NamedElement' class.
from .token import Token  # nopep8
