from typing import TypeVar, Generic, List
from OpenFlows.Domain.ModelingElements import IElement, IModelingElementsBase, TElementManagerType, IElementUnits, IModelingElementBase
from enum import Enum

TElementType = TypeVar("TElementType", IElement)
TElementTypeEnum = TypeVar("TElementTypeEnum", Enum)
TUnitsType = TypeVar("TUnitsType", IElementUnits)

class IModelComponents(Generic[TElementType, TElementTypeEnum]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def ElementType(self, id: int) -> TElementTypeEnum:
		"""Method Description

		Args:
			id(int): id

		Returns:
			TElementTypeEnum: 
		"""
		pass

	def Elements(self) -> List[TElementType]:
		"""Method Description

		Returns:
			List[TElementType]: 
		"""
		pass

class IComponentElements(Generic[TElementManagerType, TElementType, TUnitsType, TElementTypeEnum], IModelingElementsBase[TElementManagerType, TElementType, TElementTypeEnum]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IComponentElement(Generic[TElementManagerType, TElementType, TUnitsType, TElementTypeEnum], IModelingElementBase[TElementManagerType, TElementType, TElementTypeEnum]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Units(self) -> TUnitsType:
		"""
		Returns:
			TUnitsType: No Description
		"""
		pass
