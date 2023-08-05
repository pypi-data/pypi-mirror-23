from hwt.hdlObjects.types.array import Array
from hwt.hdlObjects.types.bits import Bits
from hwt.hdlObjects.types.enum import Enum
from hwt.hdlObjects.types.hdlType import HdlType
from hwt.hdlObjects.types.integer import Integer
from hwt.serializer.exceptions import SerializerException
from hwt.synthesizer.param import evalParam
from hwt.hdlObjects.types.integerVal import IntegerVal


class SimModelSerializer_types():
    @classmethod
    def HdlType_bits(cls, typ, declaration=False):
        if typ.signed is None:
            if not (typ.forceVector or typ.bit_length() > 1):
                return 'SIM_BIT'

        w = typ.width
        if isinstance(w, int):
            pass
        else:
            w = evalParam(w)
            assert isinstance(w, IntegerVal)
            assert w._isFullVld()
            w = w.val

        return "simBitsT(%d, %r)" % (w, typ.signed)

    @classmethod
    def HdlType_enum(cls, typ, scope, declaration=False):
        if declaration:
            typ.name = scope.checkedName(typ.name, typ)

            return '%s = Enum( "%s", [%s])' % (typ.name,
                                               typ.name,
                                               ", ".join(map(lambda x: '"%s"' % x,
                                                             typ._allValues)))
        else:
            return typ.name

    @classmethod
    def HdlType_int(cls, typ, scope, declaration=False):
        ma = typ.max
        mi = typ.min
        noMax = ma is None
        noMin = mi is None
        if noMin:
            if noMax:
                return "SIM_INT"
            else:
                raise SerializerException("If max is specified min has to be specified as well")
        else:
            if noMax:
                # [TODO] convert these to sim as well
                if mi == 0:
                    return "UINT"
                elif mi == 1:
                    return "PINT"
                else:
                    raise SerializerException("If max is specified min has to be specified as well")
            else:
                raise NotImplementedError()

    @classmethod
    def HdlType_array(cls, typ, scope, declaration=False):
        assert not declaration
        return "Array(%s, %d)" % (cls.HdlType(typ.elmType), evalParam(typ.size).val)

    @classmethod
    def HdlType(cls, typ, scope=None, declaration=False):
        if isinstance(typ, Bits):
            return cls.HdlType_bits(typ, declaration=declaration)
        elif isinstance(typ, Enum):
            return cls.HdlType_enum(typ, scope, declaration=declaration)
        elif isinstance(typ, Array):
            return cls.HdlType_array(typ, scope, declaration=declaration)
        elif isinstance(typ, Integer):
            return cls.HdlType_int(typ, scope, declaration=declaration)
        else:
            if declaration:
                raise NotImplementedError("type declaration is not implemented for type %s"
                                          % (typ.name))
            else:
                assert isinstance(typ, HdlType)
                return typ.name.upper()
