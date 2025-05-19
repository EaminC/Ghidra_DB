from __future__ import annotations
import collections.abc
import datetime
import typing
from warnings import deprecated # type: ignore

import jpype # type: ignore
import jpype.protocol # type: ignore

import ghidra.app.plugin.processors.sleigh
import ghidra.pcode.error
import ghidra.pcode.memstate
import ghidra.pcode.pcoderaw
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.mem
import ghidra.program.model.pcode
import ghidra.util.task
import java.lang # type: ignore


class InstructionDecodeException(ghidra.pcode.error.LowlevelError):

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, reason: typing.Union[java.lang.String, str], pc: ghidra.program.model.address.Address):
        ...

    def getProgramCounter(self) -> ghidra.program.model.address.Address:
        ...

    @property
    def programCounter(self) -> ghidra.program.model.address.Address:
        ...


class Emulate(java.lang.Object):

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, lang: ghidra.app.plugin.processors.sleigh.SleighLanguage, s: ghidra.pcode.memstate.MemoryState, b: BreakTable):
        ...

    def dispose(self):
        ...

    def executeBranch(self, op: ghidra.pcode.pcoderaw.PcodeOpRaw):
        ...

    def executeBranchind(self, op: ghidra.pcode.pcoderaw.PcodeOpRaw):
        ...

    def executeCall(self, op: ghidra.pcode.pcoderaw.PcodeOpRaw):
        ...

    def executeCallind(self, op: ghidra.pcode.pcoderaw.PcodeOpRaw):
        ...

    def executeCallother(self, op: ghidra.pcode.pcoderaw.PcodeOpRaw):
        ...

    def executeConditionalBranch(self, op: ghidra.pcode.pcoderaw.PcodeOpRaw):
        ...

    def executeIndirect(self, op: ghidra.pcode.pcoderaw.PcodeOpRaw):
        ...

    def executeInstruction(self, stopAtBreakpoint: typing.Union[jpype.JBoolean, bool], monitor: ghidra.util.task.TaskMonitor):
        ...

    def executeLoad(self, op: ghidra.pcode.pcoderaw.PcodeOpRaw):
        ...

    def executeMultiequal(self, op: ghidra.pcode.pcoderaw.PcodeOpRaw):
        ...

    def executeStore(self, op: ghidra.pcode.pcoderaw.PcodeOpRaw):
        ...

    def fallthruOp(self):
        ...

    def getContextRegisterValue(self) -> ghidra.program.model.lang.RegisterValue:
        """
        Returns the current context register value.  The context value returned reflects
        its state when the previously executed instruction was 
        parsed/executed.  The context value returned will feed into the next 
        instruction to be parsed with its non-flowing bits cleared and
        any future context state merged in.  If no instruction has been executed,
        the explicitly set context will be returned.  A null value is returned
        if no context register is defined by the language or initial context has 
        not been set.
        """

    def getExecuteAddress(self) -> ghidra.program.model.address.Address:
        ...

    def getExecutionState(self) -> EmulateExecutionState:
        """
        
        
        :return: the current emulator execution state
        :rtype: EmulateExecutionState
        """

    def getLanguage(self) -> ghidra.program.model.lang.Language:
        ...

    def getLastExecuteAddress(self) -> ghidra.program.model.address.Address:
        ...

    def getMemoryState(self) -> ghidra.pcode.memstate.MemoryState:
        ...

    def getNewDisassemblerContext(self) -> EmulateDisassemblerContext:
        ...

    def isInstructionStart(self) -> bool:
        ...

    def setContextRegisterValue(self, regValue: ghidra.program.model.lang.RegisterValue):
        """
        Sets the context register value at the current execute address.
        The Emulator should not be running when this method is invoked.
        Only flowing context bits should be set, as non-flowing bits
        will be cleared prior to parsing on instruction.  In addition,
        any future context state set by the pcode emitter will
        take precedence over context set using this method.  This method
        is primarily intended to be used to establish the initial 
        context state.
        
        :param ghidra.program.model.lang.RegisterValue regValue:
        """

    def setExecuteAddress(self, addr: ghidra.program.model.address.Address):
        ...

    @property
    def executeAddress(self) -> ghidra.program.model.address.Address:
        ...

    @executeAddress.setter
    def executeAddress(self, value: ghidra.program.model.address.Address):
        ...

    @property
    def instructionStart(self) -> jpype.JBoolean:
        ...

    @property
    def newDisassemblerContext(self) -> EmulateDisassemblerContext:
        ...

    @property
    def memoryState(self) -> ghidra.pcode.memstate.MemoryState:
        ...

    @property
    def executionState(self) -> EmulateExecutionState:
        ...

    @property
    def language(self) -> ghidra.program.model.lang.Language:
        ...

    @property
    def lastExecuteAddress(self) -> ghidra.program.model.address.Address:
        ...

    @property
    def contextRegisterValue(self) -> ghidra.program.model.lang.RegisterValue:
        ...

    @contextRegisterValue.setter
    def contextRegisterValue(self, value: ghidra.program.model.lang.RegisterValue):
        ...


class EmulateDisassemblerContext(ghidra.program.model.lang.DisassemblerContext):

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, language: ghidra.program.model.lang.Language, initialContextValue: ghidra.program.model.lang.RegisterValue):
        ...

    def getCurrentContextRegisterValue(self) -> ghidra.program.model.lang.RegisterValue:
        ...

    def setCurrentAddress(self, addr: ghidra.program.model.address.Address):
        ...

    @property
    def currentContextRegisterValue(self) -> ghidra.program.model.lang.RegisterValue:
        ...


class UnimplementedCallOtherException(ghidra.pcode.error.LowlevelError):

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, op: ghidra.pcode.pcoderaw.PcodeOpRaw, opName: typing.Union[java.lang.String, str]):
        ...

    def getCallOtherOp(self) -> ghidra.pcode.pcoderaw.PcodeOpRaw:
        ...

    def getCallOtherOpName(self) -> str:
        ...

    @property
    def callOtherOpName(self) -> java.lang.String:
        ...

    @property
    def callOtherOp(self) -> ghidra.pcode.pcoderaw.PcodeOpRaw:
        ...


class EmulateMemoryStateBuffer(ghidra.program.model.mem.MemBuffer):
    """
    ``MemoryStateBuffer`` provides a MemBuffer for instruction parsing use
    which wraps an emulator MemoryState.  This implementation wraps all specified 
    memory offsets within the associated address space.
    """

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, memState: ghidra.pcode.memstate.MemoryState, addr: ghidra.program.model.address.Address):
        ...

    def setAddress(self, addr: ghidra.program.model.address.Address):
        ...


class EmulateExecutionState(java.lang.Enum[EmulateExecutionState]):

    class_: typing.ClassVar[java.lang.Class]
    STOPPED: typing.Final[EmulateExecutionState]
    """
    Currently stopped
    """

    BREAKPOINT: typing.Final[EmulateExecutionState]
    """
    Currently stopped at a breakpoint
    """

    INSTRUCTION_DECODE: typing.Final[EmulateExecutionState]
    """
    Currently decoding instruction (i.e., generating pcode ops)
    """

    EXECUTE: typing.Final[EmulateExecutionState]
    """
    Currently executing instruction pcode
    """

    FAULT: typing.Final[EmulateExecutionState]
    """
    Execution stopped due to a fault/error
    """


    @staticmethod
    def valueOf(name: typing.Union[java.lang.String, str]) -> EmulateExecutionState:
        ...

    @staticmethod
    def values() -> jpype.JArray[EmulateExecutionState]:
        ...


class UnimplementedInstructionException(ghidra.pcode.error.LowlevelError):

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, addr: ghidra.program.model.address.Address):
        ...

    def getInstructionAddress(self) -> ghidra.program.model.address.Address:
        ...

    @property
    def instructionAddress(self) -> ghidra.program.model.address.Address:
        ...


class BreakTable(java.lang.Object):

    class_: typing.ClassVar[java.lang.Class]

    def doAddressBreak(self, addr: ghidra.program.model.address.Address) -> bool:
        ...

    def doPcodeOpBreak(self, curop: ghidra.pcode.pcoderaw.PcodeOpRaw) -> bool:
        ...

    def setEmulate(self, emu: Emulate):
        ...


class BreakTableCallBack(BreakTable):

    class_: typing.ClassVar[java.lang.Class]
    DEFAULT_NAME: typing.Final = "*"

    def __init__(self, language: ghidra.app.plugin.processors.sleigh.SleighLanguage):
        ...

    def registerAddressCallback(self, addr: ghidra.program.model.address.Address, func: BreakCallBack):
        ...

    def registerPcodeCallback(self, name: typing.Union[java.lang.String, str], func: BreakCallBack):
        ...

    def unregisterAddressCallback(self, addr: ghidra.program.model.address.Address):
        ...

    def unregisterPcodeCallback(self, name: typing.Union[java.lang.String, str]):
        ...


class EmulateInstructionStateModifier(java.lang.Object):
    """
    ``EmulateInstructionStateModifier`` defines a language specific 
    handler to assist emulation with adjusting the current execution state,
    providing support for custom pcodeop's (i.e., CALLOTHER).
    The implementation of this interface must provide a public constructor which 
    takes a single Emulate argument.
    """

    class_: typing.ClassVar[java.lang.Class]

    def executeCallOther(self, op: ghidra.program.model.pcode.PcodeOp) -> bool:
        """
        Execute a CALLOTHER op
        
        :param ghidra.program.model.pcode.PcodeOp op: 
        :return: true if corresponding pcodeop was registered and emulation support is
        performed, or false if corresponding pcodeop is not supported by this class.
        :rtype: bool
        :raises LowlevelError:
        """

    def initialExecuteCallback(self, emulate: Emulate, current_address: ghidra.program.model.address.Address, contextRegisterValue: ghidra.program.model.lang.RegisterValue):
        """
        Emulation callback immediately before the first instruction is executed.
        This callback permits any language specific initializations to be performed.
        
        :param Emulate emulate: 
        :param ghidra.program.model.address.Address current_address: intial execute address
        :param ghidra.program.model.lang.RegisterValue contextRegisterValue: initial context value or null if not applicable or unknown
        :raises LowlevelError:
        """

    def postExecuteCallback(self, emulate: Emulate, lastExecuteAddress: ghidra.program.model.address.Address, lastExecutePcode: jpype.JArray[ghidra.program.model.pcode.PcodeOp], lastPcodeIndex: typing.Union[jpype.JInt, int], currentAddress: ghidra.program.model.address.Address):
        """
        Emulation callback immediately following execution of the lastExecuteAddress.
        One use of this callback is to modify the flowing/future context state.
        
        :param Emulate emulate: 
        :param ghidra.program.model.address.Address lastExecuteAddress: 
        :param jpype.JArray[ghidra.program.model.pcode.PcodeOp] lastExecutePcode: 
        :param jpype.JInt or int lastPcodeIndex: pcode index of last op or -1 if no pcode or fall-through occurred.
        :param ghidra.program.model.address.Address currentAddress: 
        :raises LowlevelError:
        """


class BreakCallBack(java.lang.Object):

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self):
        ...

    def addressCallback(self, addr: ghidra.program.model.address.Address) -> bool:
        ...

    def pcodeCallback(self, op: ghidra.pcode.pcoderaw.PcodeOpRaw) -> bool:
        ...

    def setEmulate(self, emu: Emulate):
        ...



__all__ = ["InstructionDecodeException", "Emulate", "EmulateDisassemblerContext", "UnimplementedCallOtherException", "EmulateMemoryStateBuffer", "EmulateExecutionState", "UnimplementedInstructionException", "BreakTable", "BreakTableCallBack", "EmulateInstructionStateModifier", "BreakCallBack"]
