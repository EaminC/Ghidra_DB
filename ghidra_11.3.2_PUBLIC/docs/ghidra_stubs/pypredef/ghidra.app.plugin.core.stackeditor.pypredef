from __future__ import annotations
import collections.abc
import datetime
import typing
from warnings import deprecated # type: ignore

import jpype # type: ignore
import jpype.protocol # type: ignore

import ghidra.app.context
import ghidra.app.plugin.core.compositeeditor
import ghidra.framework.model
import ghidra.framework.options
import ghidra.framework.plugintool
import ghidra.program.model.data
import ghidra.program.model.listing
import java.lang # type: ignore
import java.util # type: ignore


class EditStackAction(ghidra.app.context.ListingContextAction):
    """
    ``EditStackAction`` allows the user to edit a function's stack frame.
    """

    class_: typing.ClassVar[java.lang.Class]


class StackEditorModel(ghidra.app.plugin.core.compositeeditor.CompositeEditorModel[StackFrameDataType]):

    @typing.type_check_only
    class OffsetPairs(java.lang.Object):
        ...
        class_: typing.ClassVar[java.lang.Class]


    @typing.type_check_only
    class XYPair(java.lang.Object):
        ...
        class_: typing.ClassVar[java.lang.Class]


    class_: typing.ClassVar[java.lang.Class]
    OFFSET: typing.Final = 0
    LENGTH: typing.Final = 1
    DATATYPE: typing.Final = 2
    NAME: typing.Final = 3
    COMMENT: typing.Final = 4

    def add(self, index: typing.Union[jpype.JInt, int], dt: ghidra.program.model.data.DataType) -> ghidra.program.model.data.DataTypeComponent:
        """
        Adds the specified data type at the specified component index. Whether
        an insert or replace occurs depends on whether the indicated index is
        in a selection and whether in locked or unlocked mode.
        
        :param jpype.JInt or int index: the component index of where to add the data type.
        :param ghidra.program.model.data.DataType dt: the data type to add
        :return: true if the component is added, false if it doesn't.
        :rtype: ghidra.program.model.data.DataTypeComponent
        :raises UsrException: if add fails
        """

    def isAddAllowed(self, currentIndex: typing.Union[jpype.JInt, int], dataType: ghidra.program.model.data.DataType) -> bool:
        """
        Returns whether or not addition of the specified component is allowed
        at the specified index. the addition could be an insert or replace as
        determined by the state of the edit model.
        
        :param jpype.JInt or int currentIndex: index of the component in the structure.
        :param ghidra.program.model.data.DataType dataType: the data type to be inserted.
        """

    def replace(self, dataType: ghidra.program.model.data.DataType) -> ghidra.program.model.data.DataTypeComponent:
        ...

    def setComponentOffset(self, rowIndex: typing.Union[jpype.JInt, int], value: typing.Union[java.lang.String, str]):
        ...

    def setValueAt(self, aValue: java.lang.Object, rowIndex: typing.Union[jpype.JInt, int], modelColumnIndex: typing.Union[jpype.JInt, int]):
        """
        This updates one of the values for a component that is a field of
        this data structure.
        
        :param java.lang.Object aValue: the new value for the field
        :param jpype.JInt or int rowIndex: the component index
        :param jpype.JInt or int modelColumnIndex: the model field index within the component
        """


class StackPieceDataType(ghidra.program.model.data.DataTypeImpl):
    ...
    class_: typing.ClassVar[java.lang.Class]


class StackEditorProvider(ghidra.app.plugin.core.compositeeditor.CompositeEditorProvider[StackFrameDataType, StackEditorModel], ghidra.framework.model.DomainObjectListener):
    """
    Editor for a Function Stack.
    """

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, plugin: ghidra.framework.plugintool.Plugin, function: ghidra.program.model.listing.Function):
        ...


class StackEditorManagerPlugin(ghidra.framework.plugintool.Plugin, ghidra.framework.options.OptionsChangeListener, StackEditorOptionManager):
    """
    Plugin to popup edit sessions for function stack frames.
    """

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, tool: ghidra.framework.plugintool.PluginTool):
        """
        Constructor
        """

    def dispose(self):
        """
        Tells a plugin that it is no longer needed.  The plugin should remove itself
        from anything that it is registered to and release any resources.
        """

    def edit(self, function: ghidra.program.model.listing.Function):
        ...

    def optionsChanged(self, options: ghidra.framework.options.ToolOptions, optionName: typing.Union[java.lang.String, str], oldValue: java.lang.Object, newValue: java.lang.Object):
        ...

    def showStackNumbersInHex(self) -> bool:
        ...

    def updateOptions(self):
        ...


class StackEditorPanel(ghidra.app.plugin.core.compositeeditor.CompositeEditorPanel[StackFrameDataType, StackEditorModel]):
    """
    Panel for editing a function stack.
    """

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, program: ghidra.program.model.listing.Program, model: StackEditorModel, provider: StackEditorProvider):
        ...


class StackEditorOptionManager(java.lang.Object):

    class_: typing.ClassVar[java.lang.Class]

    def showStackNumbersInHex(self) -> bool:
        ...


class StackFrameDataType(BiDirectionDataType):
    """
    StackFrameDataType provides an editable copy of a function stack frame.
    """

    class_: typing.ClassVar[java.lang.Class]

    @typing.overload
    def __init__(self, stack: ghidra.program.model.listing.StackFrame, dtm: ghidra.program.model.data.DataTypeManager):
        """
        Constructor for an editable stack frame for use with the editor.
        The specified stack will be copied into this new instance.
        
        :param ghidra.program.model.listing.StackFrame stack: the function stack frame to be replicated.
        :param ghidra.program.model.data.DataTypeManager dtm: datatype manager (required)
        """

    @typing.overload
    def __init__(self, stackDt: StackFrameDataType, dtm: ghidra.program.model.data.DataTypeManager):
        """
        Constructor for an editable stack frame for use with the editor.
        The specified stackDt will be copied into this new instance.
        
        :param StackFrameDataType stackDt: the function stack frame to be replicated.
        :param ghidra.program.model.data.DataTypeManager dtm: datatype manager (required)
        """

    def clearComponentAt(self, offset: typing.Union[jpype.JInt, int]):
        ...

    def getDefaultName(self, element: ghidra.program.model.data.DataTypeComponent) -> str:
        """
        Returns the default name for the indicated stack offset.
        
        :param offset: :return: the default stack variable name.
        :rtype: str
        """

    def getDefinedComponentAtOffset(self, offset: typing.Union[jpype.JInt, int]) -> ghidra.program.model.data.DataTypeComponent:
        """
        If a stack variable is defined in the editor at the specified offset, this retrieves the
        editor element containing that stack variable 
        
        Note: if a stack variable isn't defined at the indicated offset then null is returned.
        
        :param jpype.JInt or int offset: the offset
        :return: the stack editor's element at the offset. Otherwise, null.
        :rtype: ghidra.program.model.data.DataTypeComponent
        """

    def getDefinedComponentAtOrdinal(self, ordinal: typing.Union[jpype.JInt, int]) -> ghidra.program.model.data.DataTypeComponent:
        """
        If a stack variable is defined in the editor at the specified ordinal, this retrieves the
        editor element containing that stack variable. 
        
        Note: if a stack variable isn't defined for the indicated ordinal then null is returned.
        
        :param jpype.JInt or int ordinal: the ordinal
        :return: the stack editor's element at the ordinal. Otherwise, null.
        :rtype: ghidra.program.model.data.DataTypeComponent
        """

    def getFrameSize(self) -> int:
        ...

    def getFunction(self) -> ghidra.program.model.listing.Function:
        ...

    @staticmethod
    def getHexString(offset: typing.Union[jpype.JInt, int], showPrefix: typing.Union[jpype.JBoolean, bool]) -> str:
        ...

    def getLocalSize(self) -> int:
        ...

    def getMaxLength(self, offset: typing.Union[jpype.JInt, int]) -> int:
        """
        Get the maximum variable size that will fit at the indicated offset if a replace is done.
        
        :param jpype.JInt or int offset: 
        :return: the maximum size
        :rtype: int
        """

    def getParameterOffset(self) -> int:
        ...

    def getParameterSize(self) -> int:
        ...

    def getReturnAddressOffset(self) -> int:
        ...

    def getStackVariables(self) -> jpype.JArray[ghidra.program.model.listing.Variable]:
        ...

    def growsNegative(self) -> bool:
        ...

    def isStackVariable(self, ordinal: typing.Union[jpype.JInt, int]) -> bool:
        """
        Returns true if a stack variable is defined at the specified ordinal.
        
        :param jpype.JInt or int ordinal: 
        :return: true if variable is defined at ordinal or false if undefined.
        :rtype: bool
        """

    def setComment(self, ordinal: typing.Union[jpype.JInt, int], comment: typing.Union[java.lang.String, str]) -> bool:
        """
        Sets the comment at the specified ordinal.
        
        :param jpype.JInt or int ordinal: the ordinal
        :param java.lang.String or str comment: the new comment.
        """

    def setDataType(self, ordinal: typing.Union[jpype.JInt, int], type: ghidra.program.model.data.DataType, length: typing.Union[jpype.JInt, int]) -> ghidra.program.model.data.DataTypeComponent:
        """
        Sets a component representing the defined stack variable at the indicated ordinal to have the
        specified data type and length.
        
        :param jpype.JInt or int ordinal: the ordinal
        :param ghidra.program.model.data.DataType type: the data type
        :param jpype.JInt or int length: the length or size of this variable.
        :return: the component representing this stack variable.
        :rtype: ghidra.program.model.data.DataTypeComponent
        """

    def setLocalSize(self, size: typing.Union[jpype.JInt, int]) -> bool:
        ...

    def setName(self, ordinal: typing.Union[jpype.JInt, int], name: typing.Union[java.lang.String, str]) -> bool:
        """
        Sets the name of the component at the specified ordinal.
        
        :param jpype.JInt or int ordinal: the ordinal
        :param java.lang.String or str name: the new name. Null indicates the default name.
        :return: true if name change was successful, else false
        :rtype: bool
        """

    def setOffset(self, ordinal: typing.Union[jpype.JInt, int], newOffset: typing.Union[jpype.JInt, int]) -> ghidra.program.model.data.DataTypeComponent:
        """
        Effectively moves a component for a defined stack variable if it will fit where it is being
        moved to in the stack frame.
        
        :param jpype.JInt or int ordinal: the ordinal of the component to move by changing its offset.
        :param jpype.JInt or int newOffset: the offset to move the variable to.
        :return: the component representing the stack variable at the new offset.
        :rtype: ghidra.program.model.data.DataTypeComponent
        :raises InvalidInputException: if it can't be moved.
        """

    def setParameterSize(self, newParamSize: typing.Union[jpype.JInt, int]) -> bool:
        ...

    @property
    def returnAddressOffset(self) -> jpype.JInt:
        ...

    @property
    def frameSize(self) -> jpype.JInt:
        ...

    @property
    def stackVariables(self) -> jpype.JArray[ghidra.program.model.listing.Variable]:
        ...

    @property
    def localSize(self) -> jpype.JInt:
        ...

    @property
    def stackVariable(self) -> jpype.JBoolean:
        ...

    @property
    def function(self) -> ghidra.program.model.listing.Function:
        ...

    @property
    def parameterSize(self) -> jpype.JInt:
        ...

    @property
    def definedComponentAtOrdinal(self) -> ghidra.program.model.data.DataTypeComponent:
        ...

    @property
    def parameterOffset(self) -> jpype.JInt:
        ...

    @property
    def defaultName(self) -> java.lang.String:
        ...

    @property
    def maxLength(self) -> jpype.JInt:
        ...

    @property
    def definedComponentAtOffset(self) -> ghidra.program.model.data.DataTypeComponent:
        ...


class BiDirectionDataType(ghidra.program.model.data.StructureDataType, BiDirectionStructure):
    """
    :obj:`BiDirectionDataType` is a special structure data type that allows both positive and 
    negative offset values.
     
    
    NOTE: This special purpose datatype does not support resolving with a :obj:`DataTypeManager`
    """

    class_: typing.ClassVar[java.lang.Class]

    def growStructure(self, amount: typing.Union[jpype.JInt, int]):
        """
        Increases the size of the bidirectional data type If amount is positive then the positive
        offset side will grow by the indicated amount. If amount is negative, the data type grows on
        the negative offsets side.
        
        :param jpype.JInt or int amount: Positive value indicates number of bytes to add to positive side. Negative
                    value indicates number of bytes to add to negative side.
        """

    def replaceWith(self, struct: ghidra.program.model.data.Structure):
        ...


class StackEditorManager(ghidra.app.plugin.core.compositeeditor.EditorListener):
    """
    Manages edit sessions of function stack frames for multiple open programs.
    """

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, plugin: StackEditorManagerPlugin):
        """
        Constructor
        
        :param StackEditorManagerPlugin plugin: the plugin that owns this manager.
        """

    def dispose(self):
        """
        Tells a plugin that it is no longer needed.  The plugin should remove itself
        from anything that it is registered to and release any resources.
        """

    def edit(self, function: ghidra.program.model.listing.Function):
        """
        Pop up the editor dialog for the given stack frame.
        
        :param ghidra.program.model.listing.Function function: function whose stack frame is to be edited
        """


@typing.type_check_only
class OrdinalComparator(java.util.Comparator[java.lang.Object]):
    ...
    class_: typing.ClassVar[java.lang.Class]


class BiDirectionStructure(ghidra.program.model.data.Structure):

    class_: typing.ClassVar[java.lang.Class]

    def addNegative(self, dataType: ghidra.program.model.data.DataType, length: typing.Union[jpype.JInt, int], name: typing.Union[java.lang.String, str], comment: typing.Union[java.lang.String, str]) -> ghidra.program.model.data.DataTypeComponent:
        ...

    def addPositive(self, dataType: ghidra.program.model.data.DataType, length: typing.Union[jpype.JInt, int], name: typing.Union[java.lang.String, str], comment: typing.Union[java.lang.String, str]) -> ghidra.program.model.data.DataTypeComponent:
        ...

    def getNegativeLength(self) -> int:
        """
        Get the length of this DataType in the negative direction.
        
        :return: the length of this DataType in the negative direction.
        :rtype: int
        """

    def getPositiveLength(self) -> int:
        """
        Get the length of this DataType in the positive direction.
        
        :return: the length of this DataType in the positive direction.
        :rtype: int
        """

    def getSplitOffset(self) -> int:
        """
        Get the component offset which represents the division point
        between the positive and negative halves of the structure.
        
        :return: split offset
        :rtype: int
        """

    @property
    def negativeLength(self) -> jpype.JInt:
        ...

    @property
    def positiveLength(self) -> jpype.JInt:
        ...

    @property
    def splitOffset(self) -> jpype.JInt:
        ...


@typing.type_check_only
class OffsetComparator(java.util.Comparator[java.lang.Object]):
    ...
    class_: typing.ClassVar[java.lang.Class]



__all__ = ["EditStackAction", "StackEditorModel", "StackPieceDataType", "StackEditorProvider", "StackEditorManagerPlugin", "StackEditorPanel", "StackEditorOptionManager", "StackFrameDataType", "BiDirectionDataType", "StackEditorManager", "OrdinalComparator", "BiDirectionStructure", "OffsetComparator"]
