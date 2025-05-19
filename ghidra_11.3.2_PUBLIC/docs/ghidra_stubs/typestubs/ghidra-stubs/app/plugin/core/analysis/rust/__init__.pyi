from __future__ import annotations
import collections.abc
import datetime
import typing
from warnings import deprecated # type: ignore

import jpype # type: ignore
import jpype.protocol # type: ignore

import ghidra.app.plugin.core.analysis
import ghidra.app.services
import ghidra.framework.options
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.program.model.mem
import ghidra.util.task
import java.beans # type: ignore
import java.lang # type: ignore


class RustConstants(java.lang.Object):

    class_: typing.ClassVar[java.lang.Class]
    RUST_CATEGORYPATH: typing.Final[ghidra.program.model.data.CategoryPath]
    RUST_SIGNATURE_1: typing.Final[jpype.JArray[jpype.JByte]]
    RUST_SIGNATURE_2: typing.Final[jpype.JArray[jpype.JByte]]
    RUST_EXTENSIONS_PATH: typing.Final = "extensions/rust/"
    RUST_EXTENSIONS_UNIX: typing.Final = "unix"
    RUST_EXTENSIONS_WINDOWS: typing.Final = "windows"
    RUST_COMPILER: typing.Final = "rustc"

    def __init__(self):
        ...


class RustUtilities(java.lang.Object):
    """
    Rust utility functions
    """

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self):
        ...

    @staticmethod
    def addExtensions(program: ghidra.program.model.listing.Program, monitor: ghidra.util.task.TaskMonitor, subPath: typing.Union[java.lang.String, str]) -> int:
        ...

    @staticmethod
    def isRust(block: ghidra.program.model.mem.MemoryBlock) -> bool:
        """
        Checks if a given :obj:`MemoryBlock` contains a Rust signature
        
        :param ghidra.program.model.mem.MemoryBlock block: The :obj:`MemoryBlock` to scan for Rust signatures
        :return: True if the given :obj:`MemoryBlock` is not null and contains a Rust signature; 
        otherwise, false
        :rtype: bool
        :raises IOException: if there was an IO-related error
        """

    @staticmethod
    def isRustProgram(program: ghidra.program.model.listing.Program) -> bool:
        """
        Returns true if the given program has earlier been tagged as having a Rust compiler by
        the loader.
        
        :param ghidra.program.model.listing.Program program: :obj:`Program`
        :return: boolean true if program's compiler property includes rust
        :rtype: bool
        """


class RustDemanglerAnalyzer(ghidra.app.plugin.core.analysis.AbstractDemanglerAnalyzer):
    """
    A version of the demangler analyzer to handle Rust symbols
    """

    @typing.type_check_only
    class RustOptionsEditor(java.lang.Object):
        ...
        class_: typing.ClassVar[java.lang.Class]


    @typing.type_check_only
    class FormatEditor(ghidra.framework.options.EnumEditor, java.beans.PropertyChangeListener):
        ...
        class_: typing.ClassVar[java.lang.Class]


    @typing.type_check_only
    class FormatSelector(ghidra.framework.options.PropertySelector):

        class_: typing.ClassVar[java.lang.Class]

        def __init__(self, fe: RustDemanglerAnalyzer.FormatEditor):
            ...


    class_: typing.ClassVar[java.lang.Class]

    def __init__(self):
        ...


class RustStringAnalyzer(ghidra.app.services.AbstractAnalyzer):
    """
    Splits non-terminated strings into separate strings
    """

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self):
        ...



__all__ = ["RustConstants", "RustUtilities", "RustDemanglerAnalyzer", "RustStringAnalyzer"]
