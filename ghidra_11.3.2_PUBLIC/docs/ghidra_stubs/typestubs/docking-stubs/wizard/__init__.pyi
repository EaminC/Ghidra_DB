from __future__ import annotations
import collections.abc
import datetime
import typing
from warnings import deprecated # type: ignore

import jpype # type: ignore
import jpype.protocol # type: ignore

import docking
import ghidra.util
import java.awt # type: ignore
import java.lang # type: ignore
import java.util # type: ignore
import javax.swing # type: ignore


T = typing.TypeVar("T")


class AbstractMageJPanel(javax.swing.JPanel, MagePanel[T], typing.Generic[T]):

    class_: typing.ClassVar[java.lang.Class]

    @typing.overload
    def __init__(self):
        ...

    @typing.overload
    def __init__(self, layout: java.awt.LayoutManager):
        ...


class WizardPanel(java.lang.Object):
    """
    Interface to define methods for panels to be shown in the wizard dialog.
    """

    class_: typing.ClassVar[java.lang.Class]

    def addWizardPanelListener(self, l: WizardPanelListener):
        """
        Add a listener to this panel.
        
        :param WizardPanelListener l: listener to add
        """

    def getDefaultFocusComponent(self) -> java.awt.Component:
        """
        Returns the component, if any, that should receive focus when this panel is shown.
        
        :return: the component, if any, that should receive focus when this panel is shown; null
                if no preferred focus component exists.
        :rtype: java.awt.Component
        """

    def getHelpLocation(self) -> ghidra.util.HelpLocation:
        """
        Returns the help content location for this panel.
        
        :return: String help location for this panel; return null if default help
        location should be used.
        :rtype: ghidra.util.HelpLocation
        """

    def getPanel(self) -> javax.swing.JPanel:
        """
        Get the panel object
        
        :return: JPanel panel
        :rtype: javax.swing.JPanel
        """

    def getTitle(self) -> str:
        """
        Get the title for this panel.
        
        :return: String title
        :rtype: str
        """

    def initialize(self):
        """
        Initialize the panel as though this is the first time it is
        being displayed.
        """

    def isValidInformation(self) -> bool:
        """
        Return true if the user entered valid information for this panel.
        
        :return: boolean whether or not the info on the panel valid
        :rtype: bool
        """

    def removeWizardPanelListener(self, l: WizardPanelListener):
        """
        Remove the listener from this panel.
        
        :param WizardPanelListener l: listener to remove
        """

    @property
    def defaultFocusComponent(self) -> java.awt.Component:
        ...

    @property
    def validInformation(self) -> jpype.JBoolean:
        ...

    @property
    def helpLocation(self) -> ghidra.util.HelpLocation:
        ...

    @property
    def title(self) -> java.lang.String:
        ...

    @property
    def panel(self) -> javax.swing.JPanel:
        ...


class IllegalPanelStateException(java.lang.Exception):
    """
    ``IllegalPanelStateException`` allows unexpected IOExceptions and other errors
    to be thrown during Wizard panel transitions
    """

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self, cause: java.lang.Throwable):
        """
        Constructor
        
        :param java.lang.Throwable cause: original cause of exception (required)
        """


class AbstractMagePanelManager(PanelManager, typing.Generic[T]):
    ...
    class_: typing.ClassVar[java.lang.Class]


class PanelManager(java.lang.Object):
    """
    Interface to define methods that control what panel is displayed in a
    wizard.
    """

    class_: typing.ClassVar[java.lang.Class]

    def canFinish(self) -> bool:
        """
        Return true if the "finish" step can be completed.
        
        :return: boolean true if ok to finish
        :rtype: bool
        """

    def cancel(self):
        """
        Method called when the user wants to cancel the process.
        """

    def finish(self):
        """
        Method called when the user wants to finish the process.
        
        :raises IllegalPanelStateException: if an IOException or other unexpected error occurs
        """

    def getInitialPanel(self) -> WizardPanel:
        """
        Get the first panel in the process.
        
        :return: WizardPanel the first panel
        :rtype: WizardPanel
        :raises IllegalPanelStateException: if an IOException or other unexpected error occurs
        """

    def getNextPanel(self) -> WizardPanel:
        """
        Get the next panel in the process.
        
        :return: WizardPanel the next panel
        :rtype: WizardPanel
        :raises IllegalPanelStateException: if an IOException or other unexpected error occurs
        """

    def getPanelSize(self) -> java.awt.Dimension:
        """
        Get the size of the panels.
        
        :return: Dimension size of the panel
        :rtype: java.awt.Dimension
        """

    def getPreviousPanel(self) -> WizardPanel:
        """
        Get the previous panel in the process.
        
        :return: WizardPanel the previous panel
        :rtype: WizardPanel
        :raises IllegalPanelStateException: if an IOException or other unexpected error occurs
        """

    def getStatusMessage(self) -> str:
        """
        Get the status message for the current panel.
        
        :return: String message to display;
                        may be null if there is no message that should be displayed
        :rtype: str
        """

    def getWizardManager(self) -> WizardManager:
        """
        Get the wizard manager.
        
        :return: WizardManager wizard manager for this panel manager
        :rtype: WizardManager
        """

    def hasNextPanel(self) -> bool:
        """
        Return true if there is a "next" panel.
        
        :return: boolean true means there is a next panel to display
        :rtype: bool
        """

    def hasPreviousPanel(self) -> bool:
        """
        Return true if there is a "previous" panel.
        
        :return: boolean true means there is a previous panel to display
        :rtype: bool
        """

    def initialize(self):
        """
        Set up the panel process.   This may also be called to clear the state of an existing panel, 
        such as when the overall wizard is finished.
        """

    def setWizardManager(self, wm: WizardManager):
        """
        Set the wizard manager for this panel manager.
        
        :param WizardManager wm: wizard manager that calls the methods on this panel 
        manager
        """

    @property
    def nextPanel(self) -> WizardPanel:
        ...

    @property
    def wizardManager(self) -> WizardManager:
        ...

    @wizardManager.setter
    def wizardManager(self, value: WizardManager):
        ...

    @property
    def panelSize(self) -> java.awt.Dimension:
        ...

    @property
    def initialPanel(self) -> WizardPanel:
        ...

    @property
    def statusMessage(self) -> java.lang.String:
        ...

    @property
    def previousPanel(self) -> WizardPanel:
        ...


class AbstractWizardJPanel(javax.swing.JPanel, WizardPanel):
    """
    Base class that implements some methods of the WizardPanel, but not
    all. This class handles the notification of the listeners.
    """

    class_: typing.ClassVar[java.lang.Class]

    @typing.overload
    def __init__(self):
        """
        Default constructor.
        """

    @typing.overload
    def __init__(self, isDoubleBuffered: typing.Union[jpype.JBoolean, bool]):
        """
        
        
        
        .. seealso::
        
            | :obj:`javax.swing.JPanel.JPanel(boolean)`
        """

    @typing.overload
    def __init__(self, layout: java.awt.LayoutManager):
        """
        
        
        
        .. seealso::
        
            | :obj:`javax.swing.JPanel.JPanel(LayoutManager)`
        """

    @typing.overload
    def __init__(self, layout: java.awt.LayoutManager, isDoubleBuffered: typing.Union[jpype.JBoolean, bool]):
        """
        
        
        
        .. seealso::
        
            | :obj:`javax.swing.JPanel.JPanel(LayoutManager, boolean)`
        """

    def addWizardPanelListener(self, l: WizardPanelListener):
        """
        
        
        
        .. seealso::
        
            | :obj:`docking.wizard.WizardPanel.addWizardPanelListener(WizardPanelListener)`
        """

    def getDefaultFocusComponent(self) -> java.awt.Component:
        ...

    def getHelpLocation(self) -> ghidra.util.HelpLocation:
        """
        
        
        
        .. seealso::
        
            | :obj:`docking.wizard.WizardPanel.getHelpLocation()`
        """

    def getPanel(self) -> javax.swing.JPanel:
        """
        
        
        
        .. seealso::
        
            | :obj:`docking.wizard.WizardPanel.getPanel()`
        """

    def notifyListenersOfStatusMessage(self, msg: typing.Union[java.lang.String, str]):
        """
        Notification that a message should be displayed on the panel.
        
        :param java.lang.String or str msg: message to display
        """

    def notifyListenersOfValidityChanged(self):
        """
        Notification that something on the panel has changed.
        """

    def removeWizardPanelListener(self, l: WizardPanelListener):
        """
        
        
        
        .. seealso::
        
            | :obj:`docking.wizard.WizardPanel.removeWizardPanelListener(WizardPanelListener)`
        """

    @property
    def defaultFocusComponent(self) -> java.awt.Component:
        ...

    @property
    def helpLocation(self) -> ghidra.util.HelpLocation:
        ...

    @property
    def panel(self) -> javax.swing.JPanel:
        ...


class WizardStateDependencyValidator(java.lang.Object, typing.Generic[T]):

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self):
        ...

    def addDependency(self, dependent: T, predecessor: T):
        """
        Registers a dependency from one property state to another.  If the predecessor is null, then
        the dependent is registered such that a call to :meth:`findAffectedDependants(WizardState) <.findAffectedDependants>`
        will include that property key only if its cached value is null.  (i.e. the first time it 
        is called.)
        
        :param T dependent: the property key that depends on a previous property being set.
        :param T predecessor: the property key of the property that affects the dependent property.
        """

    def findAffectedDependants(self, globalState: WizardState[T]) -> java.util.Set[T]:
        """
        Returns a set of all property keys that need to have their values set because a predecessor 
        property has been changed that may affect the valid values for this property.  Also, any
        property keys that don't have a value in the local cache will be returned.
        
        :param WizardState[T] globalState: the global WizardState that is passed from one wizard panel to the next.
        :return: the set of property keys whose values should be (re)computed.
        :rtype: java.util.Set[T]
        """

    def updatePropertyValues(self, globalState: WizardState[T]):
        """
        Updates the local cache values for all the relevant properties.  This method should be
        called from a wizard panel when the "next" action is invoked (i.e. the user values have been
        accepted).
        
        :param WizardState[T] globalState: The WizardState containing all the property values.
        """


class WizardContext(java.lang.Object):

    class_: typing.ClassVar[java.lang.Class]

    def checkpoint(self):
        ...

    def deepCopy(self) -> WizardContext:
        ...

    def depth(self) -> int:
        ...

    def uncheckpoint(self):
        ...


class WizardState(java.lang.Cloneable, typing.Generic[T]):

    class_: typing.ClassVar[java.lang.Class]

    def __init__(self):
        ...

    def addDependency(self, dependent: T, predecessor: T):
        """
        Defines a dependency from one property to another.  A property dependency has the effect of
        clear the dependent's property value whenever the predecessor property is changed or cleared.
        
        :param T dependent: the property whose value is to be cleared when the predecessor property is
        changed or cleared.
        :param T predecessor: the property that, when changed or cleared, will cause the dependent property
        to be cleared.
        """

    def clear(self, key: T):
        """
        Removes the property key,value pair from this wizard state.
        
        :param T key: the property key of the property to be cleared.
        """

    def get(self, key: T) -> java.lang.Object:
        """
        Gets the value for a property key.
        
        :param T key: the identifier for the property.  Typically, it would be a string or enum.
        :return: the value associated with the given property key or null if the property has no
        value.
        :rtype: java.lang.Object
        """

    def put(self, key: T, value: java.lang.Object):
        """
        Sets the property value for a given property key.  Also clears out the property values for
        any properties that depend on this property.
        
        :param T key: the propertyKey whose value is to be set or changed with the new value.
        :param java.lang.Object value: the new value for the property.
        """


class MagePanel(WizardPanel, typing.Generic[T]):

    class_: typing.ClassVar[java.lang.Class]

    def addDependencies(self, state: WizardState[T]):
        ...

    def dispose(self):
        """
        Called when the wizard is cancelled or otherwise finished being shown
        """

    def enterPanel(self, state: WizardState[T]):
        """
        Enter panel for real; take your state from the state object and then
        populate your external state accordingly.
        
        :param WizardState[T] state: the state object
        :raises IllegalPanelStateException: indicates that something bad has happened and we should
        return to the very first panel - unless we are the first panel in which case we
        should abort the wizard.
        """

    def getPanelDisplayabilityAndUpdateState(self, state: WizardState[T]) -> WizardPanelDisplayability:
        """
        Enter and leave panel for pretend; take your state from the state object and then add
        whatever state you need into it to pretend finish the wizard (if possible).  Return
        whether you must, can, or should not be displayed.
        
        :param WizardState[T] state: the state object
        :return: displayability
        :rtype: WizardPanelDisplayability
        """

    def leavePanel(self, state: WizardState[T]):
        """
        Leave panel for real; inject your external state into the state object.
        
        :param WizardState[T] state: the state object
        """

    def updateStateObjectWithPanelInfo(self, state: WizardState[T]):
        """
        Updates the state object, being passed as a parameter, with the current state information 
        from this panel. Only state information that the panel is intended to set should be modified 
        within the state object by this method. For example, a summary panel might display state 
        information, but doesn't set it and therefore wouldn't change it in the state object.
        
        :param WizardState[T] state: the state object to update
        """

    @property
    def panelDisplayabilityAndUpdateState(self) -> WizardPanelDisplayability:
        ...


class WizardPanelListener(java.lang.Object):
    """
    Listener that is called when something on the WizardPanel has
    changed.
    """

    class_: typing.ClassVar[java.lang.Class]

    def setStatusMessage(self, msg: typing.Union[java.lang.String, str]):
        """
        Notification to set a status message.
        
        :param java.lang.String or str msg: message
        """

    def validityChanged(self):
        """
        Notification that something on the panel changed.
        """


class WizardPanelDisplayability(java.lang.Enum[WizardPanelDisplayability]):

    class_: typing.ClassVar[java.lang.Class]
    MUST_BE_DISPLAYED: typing.Final[WizardPanelDisplayability]
    CAN_BE_DISPLAYED: typing.Final[WizardPanelDisplayability]
    DO_NOT_DISPLAY: typing.Final[WizardPanelDisplayability]

    @staticmethod
    def valueOf(name: typing.Union[java.lang.String, str]) -> WizardPanelDisplayability:
        ...

    @staticmethod
    def values() -> jpype.JArray[WizardPanelDisplayability]:
        ...


class WizardManager(docking.ReusableDialogComponentProvider, WizardPanelListener):
    """
    A dialog that controls the panels for going to "Next" and "Previous" in some
    process that the user is being led through.
    """

    class_: typing.ClassVar[java.lang.Class]
    FINISH: typing.Final = "Finish"
    """
    Default text for the 'finish' button
    """

    NEXT: typing.Final = "Next >>"
    """
    Default text for the 'next' button
    """

    BACK: typing.Final = "<< Back"
    """
    Default text for the 'back' button
    """


    @typing.overload
    def __init__(self, title: typing.Union[java.lang.String, str], modal: typing.Union[jpype.JBoolean, bool], pmgr: PanelManager):
        """
        Constructor
        
        :param java.lang.String or str title: title of the dialog
        :param jpype.JBoolean or bool modal: true if the wizard should be modal
        :param PanelManager pmgr: object that knows about the next and previous panels
        """

    @typing.overload
    def __init__(self, title: typing.Union[java.lang.String, str], modal: typing.Union[jpype.JBoolean, bool], pmgr: PanelManager, wizardIcon: javax.swing.Icon):
        """
        Constructor
        
        :param java.lang.String or str title: title of the dialog
        :param jpype.JBoolean or bool modal: true if the wizard should be modal
        :param PanelManager pmgr: object that knows about the next and previous panels
        :param javax.swing.Icon wizardIcon: icon to use for this dialog
        """

    def back(self) -> bool:
        """
        Programmatically move the wizard back one panel.
        Simulates the user clicking on the 'back' button.
        Returns true if not on the first panel.
        
        :return: true if not on the first panel
        :rtype: bool
        """

    def completed(self, success: typing.Union[jpype.JBoolean, bool]):
        """
        Notification that the wizard process is complete.
        
        :param jpype.JBoolean or bool success: status of the process
        """

    def disableNavigation(self):
        """
        Disable the back, next, finish, and cancel buttons.
        """

    def enableNavigation(self):
        """
        Enable the next, previous, and finish buttons according to the
        panel manager for this dialog. The panel manager is the object that
        knows the steps in the process and what buttons should be
        enabled.
        """

    def finish(self) -> bool:
        """
        Programmatically finished the wizard task.
        Returns true if the wizard can finish.
        
        :return: true if the wizard can finish
        :rtype: bool
        """

    def focusFinish(self):
        """
        Places focus on the 'finish' button.
        """

    def focusNext(self):
        """
        Places focus on the 'next' button.
        """

    def getCurrentWizardPanel(self) -> WizardPanel:
        """
        Returns the current wizard panel.
        
        :return: the current wizard panel
        :rtype: WizardPanel
        """

    def getStatusMessage(self) -> str:
        """
        Returns the current status message being displayed in this dialog.
        
        :return: the current status message being displayed in this dialog
        :rtype: str
        """

    def next(self) -> bool:
        """
        Programmatically move the wizard forward one panel.
        Simulates the user clicking on the 'next' button.
        Returns true if not on the last panel.
        
        :return: true if not on the last panel
        :rtype: bool
        """

    @typing.overload
    def showWizard(self):
        """
        Display this dialog.
        """

    @typing.overload
    def showWizard(self, parent: java.awt.Component):
        """
        Display this dialog and parent it to the given component.
        
        :param java.awt.Component parent: parent
        """

    @property
    def currentWizardPanel(self) -> WizardPanel:
        ...

    @property
    def statusMessage(self) -> java.lang.String:
        ...



__all__ = ["AbstractMageJPanel", "WizardPanel", "IllegalPanelStateException", "AbstractMagePanelManager", "PanelManager", "AbstractWizardJPanel", "WizardStateDependencyValidator", "WizardContext", "WizardState", "MagePanel", "WizardPanelListener", "WizardPanelDisplayability", "WizardManager"]
