from __future__ import annotations
import collections.abc
import datetime
import typing
from warnings import deprecated # type: ignore

import jpype # type: ignore
import jpype.protocol # type: ignore

import ghidra.app.util.bin
import ghidra.app.util.bin.format.macho
import ghidra.app.util.bin.format.macho.commands
import ghidra.app.util.importer
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.program.model.mem
import ghidra.program.model.symbol
import ghidra.util.task
import java.lang # type: ignore
import java.util # type: ignore


class DyldCacheImageInfoExtra(ghidra.app.util.bin.StructConverter):
    """
    Represents a dyld_cache_image_info_extra structure.
    
    
    .. seealso::
    
        | `dyld_cache_format.h <https://github.com/apple-oss-distributions/dyld/blob/main/cache-builder/dyld_cache_format.h>`_
    """

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, reader: ghidra.app.util.bin.BinaryReader):
        """
        Create a new :obj:`DyldCacheImageInfoExtra`.
        
        :param ghidra.app.util.bin.BinaryReader reader: A :obj:`BinaryReader` positioned at the start of a DYLD image info extra
        :raises IOException: if there was an IO-related problem creating the DYLD image info extra
        """


class DyldCacheImageInfo(DyldCacheImage, ghidra.app.util.bin.StructConverter):
    """
    Represents a dyld_cache_image_info structure.
    
    
    .. seealso::
    
        | `dyld_cache_format.h <https://github.com/apple-oss-distributions/dyld/blob/main/cache-builder/dyld_cache_format.h>`_
    """

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, reader: ghidra.app.util.bin.BinaryReader):
        """
        Create a new :obj:`DyldCacheImageInfo`.
        
        :param ghidra.app.util.bin.BinaryReader reader: A :obj:`BinaryReader` positioned at the start of a DYLD image info
        :raises IOException: if there was an IO-related problem creating the DYLD image info
        """


class DyldCacheAcceleratorDof(ghidra.app.util.bin.StructConverter):
    """
    Represents a dyld_cache_accelerator_dof structure.
    
    
    .. seealso::
    
        | `dyld_cache_format.h <https://github.com/apple-oss-distributions/dyld/blob/main/cache-builder/dyld_cache_format.h>`_
    """

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, reader: ghidra.app.util.bin.BinaryReader):
        """
        Create a new :obj:`DyldCacheAcceleratorDof`.
        
        :param ghidra.app.util.bin.BinaryReader reader: A :obj:`BinaryReader` positioned at the start of a DYLD accelerator DOF
        :raises IOException: if there was an IO-related problem creating the DYLD accelerator DOF
        """


class DyldChainedPtr(java.lang.Object):
    """
    
    
    
    .. seealso::
    
        | `mach-o/fixup-chains.h <https://github.com/apple-oss-distributions/dyld/blob/main/include/mach-o/fixup-chains.h>`_
    """

    class DyldChainType(java.lang.Enum[DyldChainedPtr.DyldChainType]):

        class_: typing.ClassVar[java.lang.Class]
        DYLD_CHAINED_PTR_ARM64E: typing.Final[DyldChainedPtr.DyldChainType]
        DYLD_CHAINED_PTR_64: typing.Final[DyldChainedPtr.DyldChainType]
        DYLD_CHAINED_PTR_32: typing.Final[DyldChainedPtr.DyldChainType]
        DYLD_CHAINED_PTR_32_CACHE: typing.Final[DyldChainedPtr.DyldChainType]
        DYLD_CHAINED_PTR_32_FIRMWARE: typing.Final[DyldChainedPtr.DyldChainType]
        DYLD_CHAINED_PTR_64_OFFSET: typing.Final[DyldChainedPtr.DyldChainType]
        DYLD_CHAINED_PTR_ARM64E_KERNEL: typing.Final[DyldChainedPtr.DyldChainType]
        DYLD_CHAINED_PTR_64_KERNEL_CACHE: typing.Final[DyldChainedPtr.DyldChainType]
        DYLD_CHAINED_PTR_ARM64E_USERLAND: typing.Final[DyldChainedPtr.DyldChainType]
        DYLD_CHAINED_PTR_ARM64E_FIRMWARE: typing.Final[DyldChainedPtr.DyldChainType]
        DYLD_CHAINED_PTR_X86_64_KERNEL_CACHE: typing.Final[DyldChainedPtr.DyldChainType]
        DYLD_CHAINED_PTR_ARM64E_USERLAND24: typing.Final[DyldChainedPtr.DyldChainType]
        DYLD_CHAINED_PTR_ARM64E_SHARED_CACHE: typing.Final[DyldChainedPtr.DyldChainType]
        DYLD_CHAINED_PTR_TYPE_UNKNOWN: typing.Final[DyldChainedPtr.DyldChainType]

        def getName(self) -> str:
            ...

        def getValue(self) -> int:
            ...

        @staticmethod
        def lookupChainPtr(val: typing.Union[jpype.JInt, int]) -> DyldChainedPtr.DyldChainType:
            ...

        @staticmethod
        def valueOf(name: typing.Union[java.lang.String, str]) -> DyldChainedPtr.DyldChainType:
            ...

        @staticmethod
        def values() -> jpype.JArray[DyldChainedPtr.DyldChainType]:
            ...

        @property
        def name(self) -> java.lang.String:
            ...

        @property
        def value(self) -> jpype.JInt:
            ...


    class_: typing.ClassVar[java.lang.Class]
    DYLD_CHAINED_PTR_START_NONE: typing.Final = 65535
    DYLD_CHAINED_PTR_START_MULTI: typing.Final = 32768
    DYLD_CHAINED_PTR_START_LAST: typing.Final = 32768

    def __init__(self):
        ...

    @staticmethod
    def getAddend(ptrFormat: DyldChainedPtr.DyldChainType, chainValue: typing.Union[jpype.JLong, int]) -> int:
        ...

    @staticmethod
    def getChainValue(reader: ghidra.app.util.bin.BinaryReader, chainLoc: typing.Union[jpype.JLong, int], ptrFormat: DyldChainedPtr.DyldChainType) -> int:
        ...

    @staticmethod
    def getNext(ptrFormat: DyldChainedPtr.DyldChainType, chainValue: typing.Union[jpype.JLong, int]) -> int:
        ...

    @staticmethod
    def getOrdinal(ptrFormat: DyldChainedPtr.DyldChainType, chainValue: typing.Union[jpype.JLong, int]) -> int:
        ...

    @staticmethod
    def getSize(ptrFormat: DyldChainedPtr.DyldChainType) -> int:
        ...

    @staticmethod
    def getStride(ptrFormat: DyldChainedPtr.DyldChainType) -> int:
        ...

    @staticmethod
    def getTarget(ptrFormat: DyldChainedPtr.DyldChainType, chainValue: typing.Union[jpype.JLong, int]) -> int:
        ...

    @staticmethod
    def isAuthenticated(ptrFormat: DyldChainedPtr.DyldChainType, chainValue: typing.Union[jpype.JLong, int]) -> bool:
        ...

    @staticmethod
    def isBound(ptrFormat: DyldChainedPtr.DyldChainType, chainValue: typing.Union[jpype.JLong, int]) -> bool:
        ...

    @staticmethod
    def isRelative(ptrFormat: DyldChainedPtr.DyldChainType) -> bool:
        ...


class DyldCacheLocalSymbolsInfo(ghidra.app.util.bin.StructConverter):
    """
    Represents a dyld_cache_local_symbols_info structure.
    
    
    .. seealso::
    
        | `dyld_cache_format.h <https://github.com/apple-oss-distributions/dyld/blob/main/cache-builder/dyld_cache_format.h>`_
    """

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, reader: ghidra.app.util.bin.BinaryReader, architecture: DyldArchitecture, use64bitOffsets: typing.Union[jpype.JBoolean, bool]):
        """
        Create a new :obj:`DyldCacheLocalSymbolsInfo`.
        
        :param ghidra.app.util.bin.BinaryReader reader: A :obj:`BinaryReader` positioned at the start of a DYLD local symbols info
        :param DyldArchitecture architecture: The :obj:`DyldArchitecture`
        :param jpype.JBoolean or bool use64bitOffsets: True if the DYLD local symbol entries use 64-bit dylib offsets; false
        if they use 32-bit
        :raises IOException: if there was an IO-related problem creating the DYLD local symbols info
        """

    def getLocalSymbolsEntries(self) -> java.util.List[DyldCacheLocalSymbolsEntry]:
        """
        Gets the :obj:`List` of :obj:`DyldCacheLocalSymbolsEntry`s.
        
        :return: The :obj:`List` of :obj:`DyldCacheLocalSymbolsEntry`
        :rtype: java.util.List[DyldCacheLocalSymbolsEntry]
        """

    @typing.overload
    def getNList(self) -> java.util.List[ghidra.app.util.bin.format.macho.commands.NList]:
        """
        Gets the :obj:`List` of :obj:`NList`.
        
        :return: The :obj:`List` of :obj:`NList`
        :rtype: java.util.List[ghidra.app.util.bin.format.macho.commands.NList]
        """

    @typing.overload
    def getNList(self, dylibOffset: typing.Union[jpype.JLong, int]) -> java.util.List[ghidra.app.util.bin.format.macho.commands.NList]:
        """
        Gets the :obj:`List` of :obj:`NList` for the given dylib offset.
        
        :param jpype.JLong or int dylibOffset: The offset of dylib in the DYLD Cache
        :return: The :obj:`List` of :obj:`NList` for the given dylib offset
        :rtype: java.util.List[ghidra.app.util.bin.format.macho.commands.NList]
        """

    def markup(self, program: ghidra.program.model.listing.Program, localSymbolsInfoAddr: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor, log: ghidra.app.util.importer.MessageLog):
        """
        Marks up this :obj:`DyldCacheLocalSymbolsInfo` with data structures and comments.
        
        :param ghidra.program.model.listing.Program program: The :obj:`Program` to mark up
        :param ghidra.program.model.address.Address localSymbolsInfoAddr: The :obj:`Address` of the :obj:`DyldCacheLocalSymbolsInfo`
        :param ghidra.util.task.TaskMonitor monitor: A cancellable task monitor
        :param ghidra.app.util.importer.MessageLog log: The log
        :raises CancelledException: if the user cancelled the operation
        """

    def parse(self, log: ghidra.app.util.importer.MessageLog, monitor: ghidra.util.task.TaskMonitor):
        """
        Parses the structures referenced by this :obj:`DyldCacheLocalSymbolsInfo`.
        
        :param ghidra.app.util.importer.MessageLog log: The log
        :param ghidra.util.task.TaskMonitor monitor: A cancellable task monitor
        :raises CancelledException: if the user cancelled the operation
        """

    @property
    def localSymbolsEntries(self) -> java.util.List[DyldCacheLocalSymbolsEntry]:
        ...

    @property
    def nList(self) -> java.util.List[ghidra.app.util.bin.format.macho.commands.NList]:
        ...


class LibObjcDylib(java.lang.Object):
    """
    A class to represent the libobjc DYLIB Mach-O that resides within a DYLD cache
    """

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, libObjcHeader: ghidra.app.util.bin.format.macho.MachHeader, program: ghidra.program.model.listing.Program, space: ghidra.program.model.address.AddressSpace, log: ghidra.app.util.importer.MessageLog, monitor: ghidra.util.task.TaskMonitor):
        """
        Creates a new :obj:`LibObjcDylib`
        
        :param ghidra.app.util.bin.format.macho.MachHeader libObjcHeader: The libobjc DYLIB header
        :param ghidra.program.model.listing.Program program: The :obj:`Program`
        :param ghidra.program.model.address.AddressSpace space: The :obj:`AddressSpace`
        :param ghidra.app.util.importer.MessageLog log: The log
        :param ghidra.util.task.TaskMonitor monitor: A cancelable task monitor
        :raises IOException: if an IO-related error occurred while parsing
        """

    def markup(self):
        """
        Marks up the libobjc DYLIB
        """


class LibObjcOptimization(ghidra.app.util.bin.StructConverter):
    """
    Represents a objc_opt_t structure, which resides in the libobjc DYLIB within a DYLD cache
    
    
    .. seealso::
    
        | `dyld/include/objc-shared-cache.h <https://github.com/apple-oss-distributions/dyld/blob/main/include/objc-shared-cache.h>`_
    """

    class_: typing.ClassVar[java.lang.Class]
    SECTION_NAME: typing.Final = "__objc_opt_ro"
    """
    The name of the section that contains the objc_opt_t_structure
    """


    def __init__(self, program: ghidra.program.model.listing.Program, objcOptRoSectionAddr: ghidra.program.model.address.Address):
        """
        Create a new :obj:`LibObjcOptimization`.
        
        :param ghidra.program.model.listing.Program program: The :obj:`Program`
        :param ghidra.program.model.address.Address objcOptRoSectionAddr: The start address of the __objc_opt_ro section
        :raises IOException: if there was an IO-related problem parsing the structure
        """

    def getAddr(self) -> int:
        """
        Gets the address of the objc_opt_t structure
        
        :return: The address of the objc_opt_t structure
        :rtype: int
        """

    def getRelativeSelectorBaseAddressOffset(self) -> int:
        """
        Gets the relative method selector base address offset.  This will be 0 if the version is less
        than 16.
        
        :return: The relative method selector base address offset
        :rtype: int
        """

    def markup(self, program: ghidra.program.model.listing.Program, space: ghidra.program.model.address.AddressSpace, log: ghidra.app.util.importer.MessageLog, monitor: ghidra.util.task.TaskMonitor):
        """
        Marks up up this structure in memory
        
        :param ghidra.program.model.listing.Program program: The :obj:`Program`
        :param ghidra.program.model.address.AddressSpace space: The :obj:`AddressSpace`
        :param ghidra.app.util.importer.MessageLog log: The log
        :param ghidra.util.task.TaskMonitor monitor: A cancelable task monitor
        """

    @property
    def addr(self) -> jpype.JLong:
        ...

    @property
    def relativeSelectorBaseAddressOffset(self) -> jpype.JLong:
        ...


class DyldCacheMappingInfo(ghidra.app.util.bin.StructConverter):
    """
    Represents a dyld_cache_mapping_info structure.
    
    
    .. seealso::
    
        | `dyld_cache_format.h <https://github.com/apple-oss-distributions/dyld/blob/main/cache-builder/dyld_cache_format.h>`_
    """

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, reader: ghidra.app.util.bin.BinaryReader):
        """
        Create a new :obj:`DyldCacheImageInfo`.
        
        :param ghidra.app.util.bin.BinaryReader reader: A :obj:`BinaryReader` positioned at the start of a DYLD mapping info
        :raises IOException: if there was an IO-related problem creating the DYLD mapping info
        """

    def contains(self, addr: typing.Union[jpype.JLong, int]) -> bool:
        """
        Returns true if the mapping contains the given address
        
        :param jpype.JLong or int addr: The address to check
        :return: True if the mapping contains the given address; otherwise, false
        :rtype: bool
        """

    def getAddress(self) -> int:
        """
        Gets the address of the start of the mapping.
        
        :return: The address of the start of the mapping
        :rtype: int
        """

    def getFileOffset(self) -> int:
        """
        Gets the file offset of the start of the mapping.
        
        :return: The file offset of the start of the mapping
        :rtype: int
        """

    def getSize(self) -> int:
        """
        Gets the size of the mapping.
        
        :return: The size of the mapping
        :rtype: int
        """

    def isExecute(self) -> bool:
        """
        Returns true if the initial protections include EXECUTE.
        
        :return: true if the initial protections include EXECUTE
        :rtype: bool
        """

    def isRead(self) -> bool:
        """
        Returns true if the initial protections include READ.
        
        :return: true if the initial protections include READ
        :rtype: bool
        """

    def isWrite(self) -> bool:
        """
        Returns true if the initial protections include WRITE.
        
        :return: true if the initial protections include WRITE
        :rtype: bool
        """

    @property
    def read(self) -> jpype.JBoolean:
        ...

    @property
    def address(self) -> jpype.JLong:
        ...

    @property
    def size(self) -> jpype.JLong:
        ...

    @property
    def fileOffset(self) -> jpype.JLong:
        ...

    @property
    def write(self) -> jpype.JBoolean:
        ...

    @property
    def execute(self) -> jpype.JBoolean:
        ...


class DyldCacheAcceleratorInitializer(ghidra.app.util.bin.StructConverter):
    """
    Represents a dyld_cache_accelerator_initializer structure.
    
    
    .. seealso::
    
        | `dyld_cache_format.h <https://github.com/apple-oss-distributions/dyld/blob/main/cache-builder/dyld_cache_format.h>`_
    """

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, reader: ghidra.app.util.bin.BinaryReader):
        """
        Create a new :obj:`DyldCacheAcceleratorInitializer`.
        
        :param ghidra.app.util.bin.BinaryReader reader: A :obj:`BinaryReader` positioned at the start of a DYLD accelerator 
        initializer
        :raises IOException: if there was an IO-related problem creating the DYLD accelerator
        initializer
        """

    def getFunctionsOffset(self) -> int:
        """
        Gets the functions offset, which is an address offset from the start of the cache mapping.
        
        :return: The functions offset,  which is an address offset from the start of the cache 
        mapping
        :rtype: int
        """

    @property
    def functionsOffset(self) -> jpype.JInt:
        ...


class DyldChainedStartsOffsets(ghidra.app.util.bin.StructConverter):
    """
    Represents a dyld_chained_starts_offsets structure.
    
    
    .. seealso::
    
        | `mach-o/fixup-chains.h <https://github.com/apple-oss-distributions/dyld/blob/main/include/mach-o/fixup-chains.h>`_
    """

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, reader: ghidra.app.util.bin.BinaryReader):
        """
        Creates a new :obj:`DyldChainedStartsOffsets`
        
        :param ghidra.app.util.bin.BinaryReader reader: A :obj:`BinaryReader` positioned at the start of the structure
        :raises IOException: if there was an IO-related problem creating the structure
        """

    def getChainStartOffsets(self) -> jpype.JArray[jpype.JInt]:
        """
        Gets the chain start offsets
        
        :return: The chain start offsets
        :rtype: jpype.JArray[jpype.JInt]
        """

    def getPointerFormat(self) -> DyldChainedPtr.DyldChainType:
        """
        Gets the pointer format
        
        :return: The pointer format
        :rtype: DyldChainedPtr.DyldChainType
        """

    def getStartsCount(self) -> int:
        """
        Gets the starts count
        
        :return: The starts count
        :rtype: int
        """

    @property
    def startsCount(self) -> jpype.JInt:
        ...

    @property
    def chainStartOffsets(self) -> jpype.JArray[jpype.JInt]:
        ...

    @property
    def pointerFormat(self) -> DyldChainedPtr.DyldChainType:
        ...


class DyldCacheRangeEntry(ghidra.app.util.bin.StructConverter):
    """
    Represents a dyld_cache_range_entry structure.
    
    
    .. seealso::
    
        | `dyld_cache_format.h <https://github.com/apple-oss-distributions/dyld/blob/main/cache-builder/dyld_cache_format.h>`_
    """

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, reader: ghidra.app.util.bin.BinaryReader):
        """
        Create a new :obj:`DyldCacheRangeEntry`.
        
        :param ghidra.app.util.bin.BinaryReader reader: A :obj:`BinaryReader` positioned at the start of a DYLD range entry
        :raises IOException: if there was an IO-related problem creating the DYLD range entry
        """


class DyldFixup(java.lang.Record):
    """
    Stores information needed to perform a dyld pointer fixup
    """

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, offset: typing.Union[jpype.JLong, int], value: typing.Union[jpype.JLong, int], size: typing.Union[jpype.JInt, int], symbol: ghidra.program.model.symbol.Symbol, libOrdinal: typing.Union[java.lang.Integer, int]):
        ...

    def equals(self, o: java.lang.Object) -> bool:
        ...

    def hashCode(self) -> int:
        ...

    def libOrdinal(self) -> int:
        ...

    def offset(self) -> int:
        ...

    def size(self) -> int:
        ...

    def symbol(self) -> ghidra.program.model.symbol.Symbol:
        ...

    def toString(self) -> str:
        ...

    def value(self) -> int:
        ...


class DyldCacheHeader(ghidra.app.util.bin.StructConverter):
    """
    Represents a dyld_cache_header structure.
    
    
    .. seealso::
    
        | `dyld_cache_format.h <https://github.com/apple-oss-distributions/dyld/blob/main/cache-builder/dyld_cache_format.h>`_
    """

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, reader: ghidra.app.util.bin.BinaryReader):
        """
        Create a new :obj:`DyldCacheHeader`.
        
        :param ghidra.app.util.bin.BinaryReader reader: A :obj:`BinaryReader` positioned at the start of a DYLD cache header
        :raises IOException: if there was an IO-related problem creating the DYLD cache header
        """

    def getArchitecture(self) -> DyldArchitecture:
        """
        Gets architecture information.
        
        :return: architecture information
        :rtype: DyldArchitecture
        """

    def getBaseAddress(self) -> int:
        """
        Gets the base address of the DYLD cache.  This is where the cache should be loaded in
        memory.
        
        :return: The base address of the DYLD cache
        :rtype: int
        """

    def getBranchPoolAddresses(self) -> java.util.List[java.lang.Long]:
        """
        Gets the :obj:`List` of branch pool address.  Requires header to have been parsed.
        
        :return: The :obj:`List` of branch pool address
        :rtype: java.util.List[java.lang.Long]
        """

    def getCacheMappingAndSlideInfos(self) -> java.util.List[DyldCacheMappingAndSlideInfo]:
        """
        Gets the :obj:`List` of :obj:`DyldCacheMappingAndSlideInfo`s.  Requires header to have been parsed.
        
        :return: The :obj:`List` of :obj:`DyldCacheMappingAndSlideInfo`s
        :rtype: java.util.List[DyldCacheMappingAndSlideInfo]
        """

    def getEntryPoint(self) -> int:
        """
        Gets the DYLD entry point address (if known)
        
        :return: The DYLD entry point address, or null if it is not known
        :rtype: int
        """

    def getImagesCount(self) -> int:
        """
        Gets the number of :obj:`DyldCacheImageInfo`s.
        
        :return: The number of :obj:`DyldCacheImageInfo`s
        :rtype: int
        """

    def getImagesOffset(self) -> int:
        """
        Gets the file offset to first :obj:`DyldCacheImageInfo`.
        
        :return: The file offset to first :obj:`DyldCacheImageInfo`
        :rtype: int
        """

    def getLocalSymbolsInfo(self) -> DyldCacheLocalSymbolsInfo:
        """
        Gets the :obj:`DyldCacheLocalSymbolsInfo`.
        
        :return: The :obj:`DyldCacheLocalSymbolsInfo`.  Could be be null if it didn't parse.
        :rtype: DyldCacheLocalSymbolsInfo
        """

    def getMagic(self) -> jpype.JArray[jpype.JByte]:
        """
        Gets the magic bytes, which contain version information.
        
        :return: The magic bytes
        :rtype: jpype.JArray[jpype.JByte]
        """

    def getMappedImages(self) -> java.util.List[DyldCacheImage]:
        """
        Generates a :obj:`List` of :obj:`DyldCacheImage`s that are mapped in by this 
        :obj:`DyldCacheHeader`.  Requires header to have been parsed.
         
        
        NOTE: A DYLD subcache header may declare an image, but that image may get loaded at an
        address defined by the memory map of a different subcache header.  This method will only 
        return the images that are mapped by "this" header's memory map.
        
        :return: A :obj:`List` of :obj:`DyldCacheImage`s mapped by this :obj:`DyldCacheHeader`
        :rtype: java.util.List[DyldCacheImage]
        """

    def getMappingInfos(self) -> java.util.List[DyldCacheMappingInfo]:
        """
        Gets the :obj:`List` of :obj:`DyldCacheMappingInfo`s.  Requires header to have been parsed.
        
        :return: The :obj:`List` of :obj:`DyldCacheMappingInfo`s
        :rtype: java.util.List[DyldCacheMappingInfo]
        """

    def getSlideInfos(self) -> java.util.List[DyldCacheSlideInfoCommon]:
        """
        Gets the :obj:`List` of :obj:`DyldCacheSlideInfoCommon`s.
        
        :return: the :obj:`List` of :obj:`DyldCacheSlideInfoCommon`s.
        :rtype: java.util.List[DyldCacheSlideInfoCommon]
        """

    def getSubcacheEntries(self) -> java.util.List[DyldSubcacheEntry]:
        """
        Gets the :obj:`List` of :obj:`DyldSubcacheEntry`s.  Requires header to have been parsed.
        
        :return: The :obj:`List` of :obj:`DyldSubcacheEntry`s
        :rtype: java.util.List[DyldSubcacheEntry]
        """

    def getSymbolFileUUID(self) -> str:
        """
        Gets the symbol file UUID in :obj:`String` form
        
        :return: The symbol file UUID in :obj:`String` form, or null if a symbol file UUID is not 
            defined or is all zeros
        :rtype: str
        """

    def getUUID(self) -> str:
        """
        Gets the UUID in :obj:`String` form
        
        :return: The UUID in :obj:`String` form, or null if a UUID is not defined
        :rtype: str
        """

    def hasAccelerateInfo(self) -> bool:
        """
        Checks to see whether or not the old accelerate info fields are being used
        
        :return: True if the old accelerate info fields are being used; otherwise, false if the new
        dyldInCache fields are being used
        :rtype: bool
        """

    def hasSlideInfo(self) -> bool:
        """
        Checks to see if any slide info exists
        
        :return: True if any slide info exists; otherwise, false
        :rtype: bool
        """

    def isSubcache(self) -> bool:
        """
        Checks to see whether or not this is a subcache
        
        :return: True if this is a subcache; otherwise, false if it's a base cache
        :rtype: bool
        """

    def markup(self, program: ghidra.program.model.listing.Program, markupLocalSymbols: typing.Union[jpype.JBoolean, bool], space: ghidra.program.model.address.AddressSpace, monitor: ghidra.util.task.TaskMonitor, log: ghidra.app.util.importer.MessageLog):
        """
        Marks up this :obj:`DyldCacheHeader` with data structures and comments.
        
        :param ghidra.program.model.listing.Program program: The :obj:`Program` to mark up
        :param jpype.JBoolean or bool markupLocalSymbols: True if the local symbols should be marked up; otherwise, false
        :param ghidra.program.model.address.AddressSpace space: The :obj:`Program`'s :obj:`AddressSpace`
        :param ghidra.util.task.TaskMonitor monitor: A cancellable task monitor
        :param ghidra.app.util.importer.MessageLog log: The log
        :raises CancelledException: if the user cancelled the operation
        """

    def parseFromFile(self, parseLocalSymbols: typing.Union[jpype.JBoolean, bool], log: ghidra.app.util.importer.MessageLog, monitor: ghidra.util.task.TaskMonitor):
        """
        Parses the structures referenced by this :obj:`DyldCacheHeader` from a file.
        
        :param jpype.JBoolean or bool parseLocalSymbols: True if local symbols should be parsed; otherwise, false
        :param ghidra.app.util.importer.MessageLog log: The log
        :param ghidra.util.task.TaskMonitor monitor: A cancellable task monitor
        :raises CancelledException: if the user cancelled the operation
        """

    def parseFromMemory(self, program: ghidra.program.model.listing.Program, space: ghidra.program.model.address.AddressSpace, log: ghidra.app.util.importer.MessageLog, monitor: ghidra.util.task.TaskMonitor):
        """
        Parses the structures referenced by this :obj:`DyldCacheHeader` from memory.
        
        :param ghidra.program.model.listing.Program program: The :obj:`Program` whose memory to parse
        :param ghidra.program.model.address.AddressSpace space: The :obj:`Program`'s :obj:`AddressSpace`
        :param ghidra.app.util.importer.MessageLog log: The log
        :param ghidra.util.task.TaskMonitor monitor: A cancellable task monitor
        :raises CancelledException: if the user cancelled the operation
        """

    def parseLocalSymbolsInfo(self, shouldParse: typing.Union[jpype.JBoolean, bool], log: ghidra.app.util.importer.MessageLog, monitor: ghidra.util.task.TaskMonitor):
        ...

    def setFileBlock(self, block: ghidra.program.model.mem.MemoryBlock):
        """
        Sets the :obj:`MemoryBlock` associated with this header's FILE block.
        
        :param ghidra.program.model.mem.MemoryBlock block: The :obj:`MemoryBlock` associated with this header's FILE block
        """

    def unslidLoadAddress(self) -> int:
        """
        Get the original unslid load address.  This is found in the first mapping infos.
        
        :return: the original unslid load address
        :rtype: int
        """

    @property
    def magic(self) -> jpype.JArray[jpype.JByte]:
        ...

    @property
    def baseAddress(self) -> jpype.JLong:
        ...

    @property
    def imagesCount(self) -> jpype.JInt:
        ...

    @property
    def mappedImages(self) -> java.util.List[DyldCacheImage]:
        ...

    @property
    def slideInfos(self) -> java.util.List[DyldCacheSlideInfoCommon]:
        ...

    @property
    def localSymbolsInfo(self) -> DyldCacheLocalSymbolsInfo:
        ...

    @property
    def uUID(self) -> java.lang.String:
        ...

    @property
    def cacheMappingAndSlideInfos(self) -> java.util.List[DyldCacheMappingAndSlideInfo]:
        ...

    @property
    def imagesOffset(self) -> jpype.JInt:
        ...

    @property
    def symbolFileUUID(self) -> java.lang.String:
        ...

    @property
    def mappingInfos(self) -> java.util.List[DyldCacheMappingInfo]:
        ...

    @property
    def subcacheEntries(self) -> java.util.List[DyldSubcacheEntry]:
        ...

    @property
    def subcache(self) -> jpype.JBoolean:
        ...

    @property
    def entryPoint(self) -> jpype.JLong:
        ...

    @property
    def branchPoolAddresses(self) -> java.util.List[java.lang.Long]:
        ...

    @property
    def architecture(self) -> DyldArchitecture:
        ...


class DyldCacheAccelerateInfo(ghidra.app.util.bin.StructConverter):
    """
    Represents a dyld_cache_accelerator_info structure.
    
    
    .. seealso::
    
        | `dyld_cache_format.h <https://github.com/apple-oss-distributions/dyld/blob/main/cache-builder/dyld_cache_format.h>`_
    """

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, reader: ghidra.app.util.bin.BinaryReader):
        """
        Create a new :obj:`DyldCacheAccelerateInfo`.
        
        :param ghidra.app.util.bin.BinaryReader reader: A :obj:`BinaryReader` positioned at the start of a DYLD accelerate info
        :raises IOException: if there was an IO-related problem creating the DYLD accelerate info
        """

    def markup(self, program: ghidra.program.model.listing.Program, accelerateInfoAddr: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor, log: ghidra.app.util.importer.MessageLog):
        """
        Marks up this :obj:`DyldCacheAccelerateInfo` with data structures and comments.
        
        :param ghidra.program.model.listing.Program program: The :obj:`Program` to mark up
        :param ghidra.program.model.address.Address accelerateInfoAddr: The :obj:`Address` of the :obj:`DyldCacheAccelerateInfo`
        :param ghidra.util.task.TaskMonitor monitor: A cancellable task monitor
        :param ghidra.app.util.importer.MessageLog log: The log
        :raises CancelledException: if the user cancelled the operation
        """

    def parse(self, program: ghidra.program.model.listing.Program, accelerateInfoAddr: ghidra.program.model.address.Address, log: ghidra.app.util.importer.MessageLog, monitor: ghidra.util.task.TaskMonitor):
        """
        Parses the structures referenced by this :obj:`DyldCacheAccelerateInfo`.
        
        :param ghidra.program.model.listing.Program program: The :obj:`Program` to parse.
        :param ghidra.program.model.address.Address accelerateInfoAddr: The :obj:`Address` of the :obj:`DyldCacheAccelerateInfo`
        :param ghidra.app.util.importer.MessageLog log: The log
        :param ghidra.util.task.TaskMonitor monitor: A cancellable task monitor
        :raises CancelledException: if the user cancelled the operation
        """


class DyldArchitecture(java.lang.Object):

    class_: typing.ClassVar[java.lang.Class]
    DYLD_V1_SIGNATURE_PREFIX: typing.Final = "dyld_v1"
    """
    Magic value prefix
    """

    DYLD_V1_SIGNATURE_LEN: typing.Final = 16
    """
    Maximum length of any signature
    """

    X86: typing.Final[DyldArchitecture]
    X86_64: typing.Final[DyldArchitecture]
    X86_64h: typing.Final[DyldArchitecture]
    POWERPC: typing.Final[DyldArchitecture]
    ARMV6: typing.Final[DyldArchitecture]
    ARMV7: typing.Final[DyldArchitecture]
    ARMV7F: typing.Final[DyldArchitecture]
    ARMV7S: typing.Final[DyldArchitecture]
    ARMV7K: typing.Final[DyldArchitecture]
    ARMV8A: typing.Final[DyldArchitecture]
    ARMV8Ae: typing.Final[DyldArchitecture]
    ARM64_32: typing.Final[DyldArchitecture]
    ARCHITECTURES: typing.Final[jpype.JArray[DyldArchitecture]]

    @staticmethod
    @typing.overload
    def getArchitecture(signature: typing.Union[java.lang.String, str]) -> DyldArchitecture:
        """
        Returns the architecture object with the given signature.
        Returns NULL if one does not exist.
        
        :param java.lang.String or str signature: the signature string
        :return: the architecture object with the given signature or NULL
        :rtype: DyldArchitecture
        """

    @staticmethod
    @typing.overload
    def getArchitecture(provider: ghidra.app.util.bin.ByteProvider) -> DyldArchitecture:
        ...

    def getCpuSubType(self) -> int:
        ...

    def getCpuType(self) -> int:
        ...

    def getEndianness(self) -> ghidra.program.model.lang.Endian:
        ...

    def getLanguageCompilerSpecPair(self, languageService: ghidra.program.model.lang.LanguageService) -> ghidra.program.model.lang.LanguageCompilerSpecPair:
        ...

    def getProcessor(self) -> str:
        ...

    def getSignature(self) -> str:
        ...

    def is64bit(self) -> bool:
        ...

    @property
    def cpuType(self) -> jpype.JInt:
        ...

    @property
    def signature(self) -> java.lang.String:
        ...

    @property
    def languageCompilerSpecPair(self) -> ghidra.program.model.lang.LanguageCompilerSpecPair:
        ...

    @property
    def cpuSubType(self) -> jpype.JInt:
        ...

    @property
    def processor(self) -> java.lang.String:
        ...

    @property
    def endianness(self) -> ghidra.program.model.lang.Endian:
        ...


class DyldCacheSlideInfo5(DyldCacheSlideInfoCommon):
    """
    Represents a dyld_cache_slide_info5 structure.
     
    
    Seen in macOS 14.4 and later.
    """

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, reader: ghidra.app.util.bin.BinaryReader, mappingAddress: typing.Union[jpype.JLong, int], mappingSize: typing.Union[jpype.JLong, int], mappingFileOffset: typing.Union[jpype.JLong, int]):
        """
        Create a new :obj:`DyldCacheSlideInfo5`.
        
        :param ghidra.app.util.bin.BinaryReader reader: A :obj:`BinaryReader` positioned at the start of a DYLD slide info 5
        :param jpype.JLong or int mappingAddress: The base address of where the slide fixups will take place
        :param jpype.JLong or int mappingSize: The size of the slide fixups block
        :param jpype.JLong or int mappingFileOffset: The base file offset of where the slide fixups will take place
        :raises IOException: if there was an IO-related problem creating the DYLD slide info 5
        """

    def getPageSize(self) -> int:
        """
        :return: The page size
        :rtype: int
        """

    def getPageStarts(self) -> jpype.JArray[jpype.JShort]:
        """
        :return: The page starts array
        :rtype: jpype.JArray[jpype.JShort]
        """

    def getPageStartsCount(self) -> int:
        """
        :return: The page starts count
        :rtype: int
        """

    def getValueAdd(self) -> int:
        """
        :return: The "value add"
        :rtype: int
        """

    @property
    def pageStarts(self) -> jpype.JArray[jpype.JShort]:
        ...

    @property
    def valueAdd(self) -> jpype.JLong:
        ...

    @property
    def pageStartsCount(self) -> jpype.JInt:
        ...

    @property
    def pageSize(self) -> jpype.JInt:
        ...


class DyldCacheSlideInfo3(DyldCacheSlideInfoCommon):
    """
    Represents a dyld_cache_slide_info3 structure.
     
    
    Seen in iOS 12 and later.
    """

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, reader: ghidra.app.util.bin.BinaryReader, mappingAddress: typing.Union[jpype.JLong, int], mappingSize: typing.Union[jpype.JLong, int], mappingFileOffset: typing.Union[jpype.JLong, int]):
        """
        Create a new :obj:`DyldCacheSlideInfo3`.
        
        :param ghidra.app.util.bin.BinaryReader reader: A :obj:`BinaryReader` positioned at the start of a DYLD slide info 3
        :param jpype.JLong or int mappingAddress: The base address of where the slide fixups will take place
        :param jpype.JLong or int mappingSize: The size of the slide fixups block
        :param jpype.JLong or int mappingFileOffset: The base file offset of where the slide fixups will take place
        :raises IOException: if there was an IO-related problem creating the DYLD slide info 3
        """

    def getAuthValueAdd(self) -> int:
        """
        :return: The "auth value add"
        :rtype: int
        """

    def getPageSize(self) -> int:
        """
        :return: The page size
        :rtype: int
        """

    def getPageStarts(self) -> jpype.JArray[jpype.JShort]:
        """
        :return: The page starts array
        :rtype: jpype.JArray[jpype.JShort]
        """

    def getPageStartsCount(self) -> int:
        """
        :return: The page starts count
        :rtype: int
        """

    @property
    def pageStarts(self) -> jpype.JArray[jpype.JShort]:
        ...

    @property
    def pageStartsCount(self) -> jpype.JInt:
        ...

    @property
    def pageSize(self) -> jpype.JInt:
        ...

    @property
    def authValueAdd(self) -> jpype.JLong:
        ...


class DyldCacheSlideInfo1(DyldCacheSlideInfoCommon):
    """
    Represents a dyld_cache_slide_info structure.
     
    
    Seen in iOS 8 and earlier.
    """

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, reader: ghidra.app.util.bin.BinaryReader, mappingAddress: typing.Union[jpype.JLong, int], mappingSize: typing.Union[jpype.JLong, int], mappingFileOffset: typing.Union[jpype.JLong, int]):
        """
        Create a new :obj:`DyldCacheSlideInfo1`.
        
        :param ghidra.app.util.bin.BinaryReader reader: A :obj:`BinaryReader` positioned at the start of a DYLD slide info 1
        :param jpype.JLong or int mappingAddress: The base address of where the slide fixups will take place
        :param jpype.JLong or int mappingSize: The size of the slide fixups block
        :param jpype.JLong or int mappingFileOffset: The base file offset of where the slide fixups will take place
        :raises IOException: if there was an IO-related problem creating the DYLD slide info 1
        """

    def getEntries(self) -> jpype.JArray[jpype.JArray[jpype.JByte]]:
        """
        :return: The entries
        :rtype: jpype.JArray[jpype.JArray[jpype.JByte]]
        """

    def getEntriesCount(self) -> int:
        """
        :return: The entries count
        :rtype: int
        """

    def getEntriesOffset(self) -> int:
        """
        :return: The entries offset
        :rtype: int
        """

    def getEntriesSize(self) -> int:
        """
        :return: The entries size
        :rtype: int
        """

    def getToc(self) -> jpype.JArray[jpype.JShort]:
        """
        :return: The TOC
        :rtype: jpype.JArray[jpype.JShort]
        """

    def getTocCount(self) -> int:
        """
        :return: The TOC count
        :rtype: int
        """

    def getTocOffset(self) -> int:
        """
        :return: The TOC offset
        :rtype: int
        """

    @property
    def entriesCount(self) -> jpype.JInt:
        ...

    @property
    def tocOffset(self) -> jpype.JInt:
        ...

    @property
    def entries(self) -> jpype.JArray[jpype.JArray[jpype.JByte]]:
        ...

    @property
    def entriesSize(self) -> jpype.JInt:
        ...

    @property
    def tocCount(self) -> jpype.JInt:
        ...

    @property
    def toc(self) -> jpype.JArray[jpype.JShort]:
        ...

    @property
    def entriesOffset(self) -> jpype.JInt:
        ...


class DyldCacheMappingAndSlideInfo(ghidra.app.util.bin.StructConverter):
    """
    Represents a dyld_cache_mapping_and_slide_info structure.
    
    
    .. seealso::
    
        | `dyld_cache_format.h <https://github.com/apple-oss-distributions/dyld/blob/main/cache-builder/dyld_cache_format.h>`_
    """

    class_: typing.ClassVar[java.lang.Class]
    DYLD_CACHE_MAPPING_AUTH_DATA: typing.ClassVar[jpype.JLong]
    DYLD_CACHE_MAPPING_DIRTY_DATA: typing.ClassVar[jpype.JLong]
    DYLD_CACHE_MAPPING_CONST_DATA: typing.ClassVar[jpype.JLong]
    DYLD_CACHE_MAPPING_TEXT_STUBS: typing.ClassVar[jpype.JLong]
    DYLD_CACHE_DYNAMIC_CONFIG_DATA: typing.ClassVar[jpype.JLong]

    def __init__(self, reader: ghidra.app.util.bin.BinaryReader):
        """
        Create a new :obj:`DyldCacheImageInfo`.
        
        :param ghidra.app.util.bin.BinaryReader reader: A :obj:`BinaryReader` positioned at the start of a DYLD mapping info
        :raises IOException: if there was an IO-related problem creating the DYLD mapping info
        """

    def contains(self, addr: typing.Union[jpype.JLong, int]) -> bool:
        """
        Returns true if the mapping contains the given address
        
        :param jpype.JLong or int addr: The address to check
        :return: True if the mapping contains the given address; otherwise, false
        :rtype: bool
        """

    def getAddress(self) -> int:
        """
        Gets the address of the start of the mapping.
        
        :return: The address of the start of the mapping
        :rtype: int
        """

    def getFileOffset(self) -> int:
        """
        Gets the file offset of the start of the mapping.
        
        :return: The file offset of the start of the mapping
        :rtype: int
        """

    def getFlags(self) -> int:
        """
        Get slide info flags
        
        :return: slide info flags
        :rtype: int
        """

    def getInitialProtection(self) -> int:
        ...

    def getMaxProtection(self) -> int:
        ...

    def getSize(self) -> int:
        """
        Gets the size of the mapping.
        
        :return: The size of the mapping
        :rtype: int
        """

    def getSlideInfoFileOffset(self) -> int:
        """
        Get slide info file offset
        
        :return: slide info file offset
        :rtype: int
        """

    def getSlideInfoFileSize(self) -> int:
        """
        Get slide info file size
        
        :return: slide info file size
        :rtype: int
        """

    def isAuthData(self) -> bool:
        ...

    def isConfigData(self) -> bool:
        ...

    def isConstData(self) -> bool:
        ...

    def isDirtyData(self) -> bool:
        ...

    def isExecute(self) -> bool:
        """
        Returns true if the initial protections include EXECUTE.
        
        :return: true if the initial protections include EXECUTE
        :rtype: bool
        """

    def isRead(self) -> bool:
        """
        Returns true if the initial protections include READ.
        
        :return: true if the initial protections include READ
        :rtype: bool
        """

    def isTextStubs(self) -> bool:
        ...

    def isWrite(self) -> bool:
        """
        Returns true if the initial protections include WRITE.
        
        :return: true if the initial protections include WRITE
        :rtype: bool
        """

    @property
    def read(self) -> jpype.JBoolean:
        ...

    @property
    def address(self) -> jpype.JLong:
        ...

    @property
    def dirtyData(self) -> jpype.JBoolean:
        ...

    @property
    def configData(self) -> jpype.JBoolean:
        ...

    @property
    def authData(self) -> jpype.JBoolean:
        ...

    @property
    def textStubs(self) -> jpype.JBoolean:
        ...

    @property
    def flags(self) -> jpype.JLong:
        ...

    @property
    def constData(self) -> jpype.JBoolean:
        ...

    @property
    def fileOffset(self) -> jpype.JLong:
        ...

    @property
    def execute(self) -> jpype.JBoolean:
        ...

    @property
    def slideInfoFileOffset(self) -> jpype.JLong:
        ...

    @property
    def maxProtection(self) -> jpype.JInt:
        ...

    @property
    def size(self) -> jpype.JLong:
        ...

    @property
    def slideInfoFileSize(self) -> jpype.JLong:
        ...

    @property
    def initialProtection(self) -> jpype.JInt:
        ...

    @property
    def write(self) -> jpype.JBoolean:
        ...


class DyldCacheSlideInfo4(DyldCacheSlideInfoCommon):
    """
    Represents a dyld_cache_slide_info4 structure. 
     
    
    Not seen yet.
    """

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, reader: ghidra.app.util.bin.BinaryReader, mappingAddress: typing.Union[jpype.JLong, int], mappingSize: typing.Union[jpype.JLong, int], mappingFileOffset: typing.Union[jpype.JLong, int]):
        """
        Create a new :obj:`DyldCacheSlideInfo4`.
        
        :param ghidra.app.util.bin.BinaryReader reader: A :obj:`BinaryReader` positioned at the start of a DYLD slide info 3
        :param jpype.JLong or int mappingAddress: The base address of where the slide fixups will take place
        :param jpype.JLong or int mappingSize: The size of the slide fixups block
        :param jpype.JLong or int mappingFileOffset: The base file offset of where the slide fixups will take place
        :raises IOException: if there was an IO-related problem creating the DYLD slide info 3
        """

    def getDeltaMask(self) -> int:
        """
        :return: The delta mask
        :rtype: int
        """

    def getPageExtras(self) -> jpype.JArray[jpype.JShort]:
        """
        :return: The page extras array
        :rtype: jpype.JArray[jpype.JShort]
        """

    def getPageExtrasCount(self) -> int:
        """
        :return: The page extras count
        :rtype: int
        """

    def getPageExtrasOffset(self) -> int:
        """
        :return: The page extras offset
        :rtype: int
        """

    def getPageSize(self) -> int:
        """
        :return: The page size
        :rtype: int
        """

    def getPageStarts(self) -> jpype.JArray[jpype.JShort]:
        """
        :return: The page starts array
        :rtype: jpype.JArray[jpype.JShort]
        """

    def getPageStartsCount(self) -> int:
        """
        :return: The page starts count
        :rtype: int
        """

    def getPageStartsOffset(self) -> int:
        """
        :return: The page starts offset
        :rtype: int
        """

    def getValueAdd(self) -> int:
        """
        :return: The "value add"
        :rtype: int
        """

    @property
    def pageStarts(self) -> jpype.JArray[jpype.JShort]:
        ...

    @property
    def pageExtrasCount(self) -> jpype.JInt:
        ...

    @property
    def valueAdd(self) -> jpype.JLong:
        ...

    @property
    def pageStartsCount(self) -> jpype.JInt:
        ...

    @property
    def deltaMask(self) -> jpype.JLong:
        ...

    @property
    def pageExtrasOffset(self) -> jpype.JInt:
        ...

    @property
    def pageStartsOffset(self) -> jpype.JInt:
        ...

    @property
    def pageSize(self) -> jpype.JInt:
        ...

    @property
    def pageExtras(self) -> jpype.JArray[jpype.JShort]:
        ...


class DyldCacheImageTextInfo(DyldCacheImage, ghidra.app.util.bin.StructConverter):
    """
    Represents a dyld_cache_image_text_info structure.
    
    
    .. seealso::
    
        | `dyld_cache_format.h <https://github.com/apple-oss-distributions/dyld/blob/main/cache-builder/dyld_cache_format.h>`_
    """

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, reader: ghidra.app.util.bin.BinaryReader):
        """
        Create a new :obj:`DyldCacheImageTextInfo`.
        
        :param ghidra.app.util.bin.BinaryReader reader: A :obj:`BinaryReader` positioned at the start of a DYLD image text info
        :raises IOException: if there was an IO-related problem creating the DYLD image text info
        """


class DyldCacheImage(java.lang.Object):
    """
    A convenience interface for getting the address and path of a DYLD Cache image
    """

    class_: typing.ClassVar[java.lang.Class]

    def getAddress(self) -> int:
        """
        Gets the address the start of the image
        
        :return: The address of the start of the image
        :rtype: int
        """

    def getPath(self) -> str:
        """
        Gets the path of the image
        
        :return: The path of the image
        :rtype: str
        """

    @property
    def path(self) -> java.lang.String:
        ...

    @property
    def address(self) -> jpype.JLong:
        ...


class DyldSubcacheEntry(ghidra.app.util.bin.StructConverter):
    """
    Represents a dyld_subcache_entry structure.
    
    
    .. seealso::
    
        | `dyld_cache_format.h <https://github.com/apple-oss-distributions/dyld/blob/main/cache-builder/dyld_cache_format.h>`_
    """

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, reader: ghidra.app.util.bin.BinaryReader):
        """
        Create a new :obj:`DyldSubcacheEntry`.
        
        :param ghidra.app.util.bin.BinaryReader reader: A :obj:`BinaryReader` positioned at the start of a DYLD subCache entry
        :raises IOException: if there was an IO-related problem creating the DYLD subCache entry
        """

    def getCacheExtension(self) -> str:
        """
        Gets the extension of this subCache, if it is known
        
        :return: The extension of this subCache, or null if it is not known
        :rtype: str
        """

    def getCacheVMOffset(self) -> int:
        """
        Gets the offset of this subCache from the main cache base address
        
        :return: The offset of this subCache from the main cache base address
        :rtype: int
        """

    def getUuid(self) -> str:
        """
        Gets the UUID of the subCache file
        
        :return: The UUID of the subCache file
        :rtype: str
        """

    @property
    def cacheExtension(self) -> java.lang.String:
        ...

    @property
    def uuid(self) -> java.lang.String:
        ...

    @property
    def cacheVMOffset(self) -> jpype.JLong:
        ...


class DyldCacheSlideInfoCommon(ghidra.app.util.bin.StructConverter):
    """
    Class for representing the common components of the various dyld_cache_slide_info structures.
    The intent is for the full dyld_cache_slide_info structures to extend this and add their
    specific parts.
    
    
    .. seealso::
    
        | `dyld_cache_format.h <https://github.com/apple-oss-distributions/dyld/blob/main/cache-builder/dyld_cache_format.h>`_
    """

    class_: typing.ClassVar[java.lang.Class]
    DATA_PAGE_MAP_ENTRY: typing.Final = 1
    BYTES_PER_CHAIN_OFFSET: typing.Final = 4
    CHAIN_OFFSET_MASK: typing.Final = 16383

    def __init__(self, reader: ghidra.app.util.bin.BinaryReader, mappingAddress: typing.Union[jpype.JLong, int], mappingSize: typing.Union[jpype.JLong, int], mappingFileOffset: typing.Union[jpype.JLong, int]):
        """
        Create a new :obj:`DyldCacheSlideInfoCommon`.
        
        :param ghidra.app.util.bin.BinaryReader reader: A :obj:`BinaryReader` positioned at the start of a DYLD slide info
        :param jpype.JLong or int mappingAddress: The base address of where the slide fixups will take place
        :param jpype.JLong or int mappingSize: The size of the slide fixups block
        :param jpype.JLong or int mappingFileOffset: The base file offset of where the slide fixups will take place
        :raises IOException: if there was an IO-related problem creating the DYLD slide info
        """

    def fixupSlidePointers(self, program: ghidra.program.model.listing.Program, markup: typing.Union[jpype.JBoolean, bool], addRelocations: typing.Union[jpype.JBoolean, bool], log: ghidra.app.util.importer.MessageLog, monitor: ghidra.util.task.TaskMonitor):
        """
        Fixes up the program's slide pointers
        
        :param ghidra.program.model.listing.Program program: The :obj:`Program`
        :param jpype.JBoolean or bool markup: True if the slide pointers should be marked up; otherwise, false
        :param jpype.JBoolean or bool addRelocations: True if slide pointer locations should be added to the relocation
        table; otherwise, false
        :param ghidra.app.util.importer.MessageLog log: The log
        :param ghidra.util.task.TaskMonitor monitor: A cancellable monitor
        :raises MemoryAccessException: If there was a problem accessing memory
        :raises CancelledException: If the user cancelled the operation
        """

    def getMappingAddress(self) -> int:
        """
        :return: The base address of where the slide fixups will take place
        :rtype: int
        """

    def getMappingFileOffset(self) -> int:
        """
        :return: The base file offset of where the slide fixups will take place
        :rtype: int
        """

    def getMappingSize(self) -> int:
        """
        :return: The size of the slide fixups block
        :rtype: int
        """

    def getSlideFixups(self, reader: ghidra.app.util.bin.BinaryReader, pointerSize: typing.Union[jpype.JInt, int], log: ghidra.app.util.importer.MessageLog, monitor: ghidra.util.task.TaskMonitor) -> java.util.List[DyldFixup]:
        """
        Walks the slide fixup information and collects a :obj:`List` of :obj:`DyldFixup`s that will
        need to be applied to the image
        
        :param ghidra.app.util.bin.BinaryReader reader: A :obj:`BinaryReader` positioned at the start of the segment to fix up
        :param jpype.JInt or int pointerSize: The size of a pointer in bytes
        :param ghidra.app.util.importer.MessageLog log: The log
        :param ghidra.util.task.TaskMonitor monitor: A cancellable monitor
        :return: A :obj:`List` of :obj:`DyldFixup`s
        :rtype: java.util.List[DyldFixup]
        :raises IOException: If there was an IO-related issue
        :raises CancelledException: If the user cancelled the operation
        """

    def getSlideInfoOffset(self) -> int:
        """
        :return: The original slide info offset
        :rtype: int
        """

    def getVersion(self) -> int:
        """
        :return: The version of the DYLD slide info
        :rtype: int
        """

    @staticmethod
    def parseSlideInfo(reader: ghidra.app.util.bin.BinaryReader, slideInfoOffset: typing.Union[jpype.JLong, int], mappingAddress: typing.Union[jpype.JLong, int], mappingSize: typing.Union[jpype.JLong, int], mappingFileOffset: typing.Union[jpype.JLong, int], log: ghidra.app.util.importer.MessageLog, monitor: ghidra.util.task.TaskMonitor) -> DyldCacheSlideInfoCommon:
        """
        Parses the slide info
        
        :param ghidra.app.util.bin.BinaryReader reader: A :obj:`BinaryReader` positioned at the start of a DYLD slide info
        :param jpype.JLong or int slideInfoOffset: The offset of the slide info to parse
        :param jpype.JLong or int mappingAddress: The base address of where the slide fixups will take place
        :param jpype.JLong or int mappingSize: The size of the slide fixups block
        :param jpype.JLong or int mappingFileOffset: The base file offset of where the slide fixups will take place
        :param ghidra.app.util.importer.MessageLog log: The log
        :param ghidra.util.task.TaskMonitor monitor: A cancelable task monitor
        :return: The slide info object
        :rtype: DyldCacheSlideInfoCommon
        """

    @property
    def mappingFileOffset(self) -> jpype.JLong:
        ...

    @property
    def mappingSize(self) -> jpype.JLong:
        ...

    @property
    def version(self) -> jpype.JInt:
        ...

    @property
    def slideInfoOffset(self) -> jpype.JLong:
        ...

    @property
    def mappingAddress(self) -> jpype.JLong:
        ...


class DyldCacheLocalSymbolsEntry(ghidra.app.util.bin.StructConverter):
    """
    Represents a dyld_cache_local_symbols_entry structure.
    
    
    .. seealso::
    
        | `dyld_cache_format.h <https://github.com/apple-oss-distributions/dyld/blob/main/cache-builder/dyld_cache_format.h>`_
    """

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, reader: ghidra.app.util.bin.BinaryReader, use64bitOffsets: typing.Union[jpype.JBoolean, bool]):
        """
        Create a new :obj:`DyldCacheLocalSymbolsEntry`.
        
        :param ghidra.app.util.bin.BinaryReader reader: A :obj:`BinaryReader` positioned at the start of a DYLD local symbols entry
        :param jpype.JBoolean or bool use64bitOffsets: True if the DYLD local symbol entries use 64-bit dylib offsets; false
        if they use 32-bit
        :raises IOException: if there was an IO-related problem creating the DYLD local symbols entry
        """

    def getDylibOffset(self) -> int:
        """
        :return: The dylib offset
        :rtype: int
        """

    def getNListCount(self) -> int:
        """
        :return: The nlist count
        :rtype: int
        """

    def getNListStartIndex(self) -> int:
        """
        :return: The nlist start index
        :rtype: int
        """

    @property
    def dylibOffset(self) -> jpype.JLong:
        ...

    @property
    def nListStartIndex(self) -> jpype.JInt:
        ...

    @property
    def nListCount(self) -> jpype.JInt:
        ...


class DyldCacheSlideInfo2(DyldCacheSlideInfoCommon):
    """
    Represents a dyld_cache_slide_info2 structure.
     
    
    Seen in iOS 10 and 11.
    """

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, reader: ghidra.app.util.bin.BinaryReader, mappingAddress: typing.Union[jpype.JLong, int], mappingSize: typing.Union[jpype.JLong, int], mappingFileOffset: typing.Union[jpype.JLong, int]):
        """
        Create a new :obj:`DyldCacheSlideInfo2`.
        
        :param ghidra.app.util.bin.BinaryReader reader: A :obj:`BinaryReader` positioned at the start of a DYLD slide info 2
        :param jpype.JLong or int mappingAddress: The base address of where the slide fixups will take place
        :param jpype.JLong or int mappingSize: The size of the slide fixups block
        :param jpype.JLong or int mappingFileOffset: The base file offset of where the slide fixups will take place
        :raises IOException: if there was an IO-related problem creating the DYLD slide info 2
        """

    def getDeltaMask(self) -> int:
        """
        :return: The delta mask
        :rtype: int
        """

    def getPageExtras(self) -> jpype.JArray[jpype.JShort]:
        """
        :return: The page extras array
        :rtype: jpype.JArray[jpype.JShort]
        """

    def getPageExtrasCount(self) -> int:
        """
        :return: The page extras count
        :rtype: int
        """

    def getPageExtrasOffset(self) -> int:
        """
        :return: The page extras offset
        :rtype: int
        """

    def getPageSize(self) -> int:
        """
        :return: The page size
        :rtype: int
        """

    def getPageStarts(self) -> jpype.JArray[jpype.JShort]:
        """
        :return: The page starts array
        :rtype: jpype.JArray[jpype.JShort]
        """

    def getPageStartsCount(self) -> int:
        """
        :return: The page starts count
        :rtype: int
        """

    def getPageStartsOffset(self) -> int:
        """
        :return: The page starts offset
        :rtype: int
        """

    def getValueAdd(self) -> int:
        """
        :return: The "value add"
        :rtype: int
        """

    @property
    def pageStarts(self) -> jpype.JArray[jpype.JShort]:
        ...

    @property
    def pageExtrasCount(self) -> jpype.JLong:
        ...

    @property
    def valueAdd(self) -> jpype.JLong:
        ...

    @property
    def pageStartsCount(self) -> jpype.JLong:
        ...

    @property
    def deltaMask(self) -> jpype.JLong:
        ...

    @property
    def pageExtrasOffset(self) -> jpype.JLong:
        ...

    @property
    def pageStartsOffset(self) -> jpype.JLong:
        ...

    @property
    def pageSize(self) -> jpype.JLong:
        ...

    @property
    def pageExtras(self) -> jpype.JArray[jpype.JShort]:
        ...



__all__ = ["DyldCacheImageInfoExtra", "DyldCacheImageInfo", "DyldCacheAcceleratorDof", "DyldChainedPtr", "DyldCacheLocalSymbolsInfo", "LibObjcDylib", "LibObjcOptimization", "DyldCacheMappingInfo", "DyldCacheAcceleratorInitializer", "DyldChainedStartsOffsets", "DyldCacheRangeEntry", "DyldFixup", "DyldCacheHeader", "DyldCacheAccelerateInfo", "DyldArchitecture", "DyldCacheSlideInfo5", "DyldCacheSlideInfo3", "DyldCacheSlideInfo1", "DyldCacheMappingAndSlideInfo", "DyldCacheSlideInfo4", "DyldCacheImageTextInfo", "DyldCacheImage", "DyldSubcacheEntry", "DyldCacheSlideInfoCommon", "DyldCacheLocalSymbolsEntry", "DyldCacheSlideInfo2"]
