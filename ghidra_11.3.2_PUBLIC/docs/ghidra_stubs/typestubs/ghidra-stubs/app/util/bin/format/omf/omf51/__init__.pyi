from __future__ import annotations
import collections.abc
import datetime
import typing
from warnings import deprecated # type: ignore

import jpype # type: ignore
import jpype.protocol # type: ignore

import ghidra.app.util.bin
import ghidra.app.util.bin.format.omf
import java.lang # type: ignore


class Omf51ModuleEnd(ghidra.app.util.bin.format.omf.OmfRecord):

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, reader: ghidra.app.util.bin.BinaryReader):
        """
        Creates a new :obj:`Omf51ModuleEnd` record
        
        :param ghidra.app.util.bin.BinaryReader reader: A :obj:`BinaryReader` positioned at the start of the record
        :raises IOException: if an IO-related error occurred
        """

    def getRegisterMask(self) -> int:
        """
        :return: the register mask
        :rtype: int
        """

    @property
    def registerMask(self) -> jpype.JByte:
        ...


class Omf51RecordTypes(java.lang.Object):
    """
    OMF-51 record types
    
    
    .. seealso::
    
        | `OMF-51 Object Module Format <https://turbo51.com/documentation/omf-51-object-module-format>`_
    """

    class_: typing.ClassVar[java.lang.Class]
    ModuleHDR: typing.Final = 2
    ModuleEND: typing.Final = 4
    Content: typing.Final = 6
    Fixup: typing.Final = 8
    SegmentDEF: typing.Final = 14
    ScopeDEF: typing.Final = 16
    DebugItem: typing.Final = 18
    PublicDEF: typing.Final = 22
    ExternalDEF: typing.Final = 24
    LibModLocs: typing.Final = 38
    LibModName: typing.Final = 40
    LibDictionary: typing.Final = 42
    LibHeader: typing.Final = 44
    SegmentDEFKeil: typing.Final = 15
    ScopeDEFKeil: typing.Final = 17
    DebugItemKeil: typing.Final = 19
    PublicDEFKeil: typing.Final = 23
    DebugData62Keil: typing.Final = 98
    DebugData63Keil: typing.Final = 99
    DebugData64Keil: typing.Final = 100

    def __init__(self):
        ...

    @staticmethod
    def getName(type: typing.Union[jpype.JInt, int]) -> str:
        """
        Gets the name of the given record type
        
        :param jpype.JInt or int type: The record type
        :return: The name of the given record type
        :rtype: str
        """


class Omf51RecordFactory(ghidra.app.util.bin.format.omf.AbstractOmfRecordFactory):
    """
    A class for reading/creating OMF-51 records
    """

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, provider: ghidra.app.util.bin.ByteProvider):
        """
        Creates a new :obj:`Omf51RecordFactory`
        
        :param ghidra.app.util.bin.ByteProvider provider: The :obj:`ByteProvider` that contains the records
        """


class Omf51ModuleHeader(ghidra.app.util.bin.format.omf.OmfRecord):

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, reader: ghidra.app.util.bin.BinaryReader):
        """
        Creates a new :obj:`Omf51ModuleHeader` record
        
        :param ghidra.app.util.bin.BinaryReader reader: A :obj:`BinaryReader` positioned at the start of the record
        :raises IOException: if an IO-related error occurred
        """

    def getTrnId(self) -> int:
        """
        :return: the TRN ID
        :rtype: int
        """

    @property
    def trnId(self) -> jpype.JByte:
        ...



__all__ = ["Omf51ModuleEnd", "Omf51RecordTypes", "Omf51RecordFactory", "Omf51ModuleHeader"]
