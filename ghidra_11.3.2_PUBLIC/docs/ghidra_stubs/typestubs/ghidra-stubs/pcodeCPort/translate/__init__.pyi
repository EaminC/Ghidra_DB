from __future__ import annotations
import collections.abc
import datetime
import typing
from warnings import deprecated # type: ignore

import jpype # type: ignore
import jpype.protocol # type: ignore

import generic.stl
import ghidra.pcodeCPort.address
import ghidra.pcodeCPort.error
import ghidra.pcodeCPort.pcoderaw
import ghidra.pcodeCPort.space
import java.io # type: ignore
import java.lang # type: ignore


class BasicSpaceProvider(java.lang.Object):

    class_: typing.ClassVar[java.lang.Class]

    def getConstantSpace(self) -> ghidra.pcodeCPort.space.AddrSpace:
        ...

    def getDefaultSpace(self) -> ghidra.pcodeCPort.space.AddrSpace:
        ...

    @property
    def defaultSpace(self) -> ghidra.pcodeCPort.space.AddrSpace:
        ...

    @property
    def constantSpace(self) -> ghidra.pcodeCPort.space.AddrSpace:
        ...


class BadDataError(ghidra.pcodeCPort.error.LowlevelError):

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, string: typing.Union[java.lang.String, str]):
        ...


class UnimplError(ghidra.pcodeCPort.error.LowlevelError):

    class_: typing.ClassVar[java.lang.Class]
    instruction_length: jpype.JInt

    def __init__(self, string: typing.Union[java.lang.String, str], instruction_length: typing.Union[jpype.JInt, int]):
        ...


class Translate(BasicSpaceProvider):

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self):
        ...

    def addSpacebase(self, basespace: ghidra.pcodeCPort.space.AddrSpace, spc: ghidra.pcodeCPort.space.AddrSpace, offset: typing.Union[jpype.JLong, int], size: typing.Union[jpype.JInt, int]):
        ...

    def assignShortcut(self, tp: ghidra.pcodeCPort.space.spacetype) -> str:
        ...

    def createConstFromSpace(self, spc: ghidra.pcodeCPort.space.AddrSpace) -> ghidra.pcodeCPort.address.Address:
        ...

    def dispose(self):
        ...

    def getAddrSize(self) -> int:
        ...

    def getConstant(self, val: typing.Union[jpype.JLong, int]) -> ghidra.pcodeCPort.address.Address:
        ...

    def getDefaultSize(self) -> int:
        ...

    def getFspecSpace(self) -> ghidra.pcodeCPort.space.AddrSpace:
        ...

    def getIopSpace(self) -> ghidra.pcodeCPort.space.AddrSpace:
        ...

    def getNextSpaceInOrder(self, spc: ghidra.pcodeCPort.space.AddrSpace) -> ghidra.pcodeCPort.space.AddrSpace:
        ...

    def getRegister(self, nm: typing.Union[java.lang.String, str]) -> ghidra.pcodeCPort.pcoderaw.VarnodeData:
        ...

    def getRegisterName(self, base: ghidra.pcodeCPort.space.AddrSpace, off: typing.Union[jpype.JLong, int], size: typing.Union[jpype.JInt, int]) -> str:
        ...

    def getSpace(self, i: typing.Union[jpype.JInt, int]) -> ghidra.pcodeCPort.space.AddrSpace:
        ...

    def getSpaceByName(self, nm: typing.Union[java.lang.String, str]) -> ghidra.pcodeCPort.space.AddrSpace:
        ...

    def getSpaceByShortcut(self, sc: typing.Union[jpype.JChar, int, str]) -> ghidra.pcodeCPort.space.AddrSpace:
        ...

    def getSpaceBySpacebase(self, loc: ghidra.pcodeCPort.address.Address, size: typing.Union[jpype.JInt, int]) -> ghidra.pcodeCPort.space.AddrSpace:
        ...

    def getSpacebase(self, basespace: ghidra.pcodeCPort.space.AddrSpace, i: typing.Union[jpype.JInt, int]) -> ghidra.pcodeCPort.pcoderaw.VarnodeData:
        ...

    def getStackSpace(self) -> ghidra.pcodeCPort.space.AddrSpace:
        ...

    def getUniqueBase(self) -> int:
        ...

    def getUniqueSpace(self) -> ghidra.pcodeCPort.space.AddrSpace:
        ...

    def getUserOpNames(self, res: generic.stl.VectorSTL[java.lang.String]):
        ...

    def highPtrPossible(self, loc: ghidra.pcodeCPort.address.Address, size: typing.Union[jpype.JInt, int]) -> bool:
        ...

    def insertSpace(self, spc: ghidra.pcodeCPort.space.AddrSpace):
        ...

    def instructionLength(self, baseaddr: ghidra.pcodeCPort.address.Address) -> int:
        ...

    def isBigEndian(self) -> bool:
        ...

    def numSpacebase(self, basespace: ghidra.pcodeCPort.space.AddrSpace) -> int:
        ...

    def numSpaces(self) -> int:
        ...

    def printAssembly(self, s: java.io.PrintStream, size: typing.Union[jpype.JInt, int], baseaddr: ghidra.pcodeCPort.address.Address) -> int:
        ...

    def setDefaultSpace(self, index: typing.Union[jpype.JInt, int]):
        ...

    def setLanguage(self, processorFile: typing.Union[java.lang.String, str]):
        ...

    @property
    def spaceByShortcut(self) -> ghidra.pcodeCPort.space.AddrSpace:
        ...

    @property
    def addrSize(self) -> jpype.JInt:
        ...

    @property
    def constant(self) -> ghidra.pcodeCPort.address.Address:
        ...

    @property
    def stackSpace(self) -> ghidra.pcodeCPort.space.AddrSpace:
        ...

    @property
    def fspecSpace(self) -> ghidra.pcodeCPort.space.AddrSpace:
        ...

    @property
    def uniqueBase(self) -> jpype.JLong:
        ...

    @property
    def spaceByName(self) -> ghidra.pcodeCPort.space.AddrSpace:
        ...

    @property
    def space(self) -> ghidra.pcodeCPort.space.AddrSpace:
        ...

    @property
    def iopSpace(self) -> ghidra.pcodeCPort.space.AddrSpace:
        ...

    @property
    def bigEndian(self) -> jpype.JBoolean:
        ...

    @property
    def nextSpaceInOrder(self) -> ghidra.pcodeCPort.space.AddrSpace:
        ...

    @property
    def uniqueSpace(self) -> ghidra.pcodeCPort.space.AddrSpace:
        ...

    @property
    def defaultSize(self) -> jpype.JInt:
        ...

    @property
    def register(self) -> ghidra.pcodeCPort.pcoderaw.VarnodeData:
        ...



__all__ = ["BasicSpaceProvider", "BadDataError", "UnimplError", "Translate"]
