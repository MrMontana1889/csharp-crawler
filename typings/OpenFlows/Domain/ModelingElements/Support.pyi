from enum import Enum
from OpenFlows.Units import IUnit
from typing import Generic, List, TypeVar
from Haestad.Support.Support.Interfaces import ILabeled, INamable

TValueType = TypeVar("TValueType")
TFieldType = TypeVar("TFieldType")
TNetworkElementTypeEnum = TypeVar("TNetworkElementTypeEnum", Enum)
TNetworkElementType = TypeVar("TNetworkElementType", Enum)

class UserFieldDataType(Enum):
	Integer = 1
	Real = 2
	LongText = 4
	DateTime = 5
	Boolean = 6

class IFieldInfo(INamable, ILabeled):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetValue(self, id: int) -> TValueType:
		"""No Description

		Args:
			id(int): id

		Returns:
			TValueType: 
		"""
		pass

	def SetValue(self, id: int, value: TValueType) -> None:
		"""No Description

		Args:
			id(int): id
			value(TValueType): value

		Returns:
			None: 
		"""
		pass

	@property
	def Field(self) -> IField:
		"""No Description

		Returns:
			IFieldInfo: 
		"""
		pass

	@property
	def FieldType(self) -> DomainFieldType:
		"""No Description

		Returns:
			IFieldInfo: 
		"""
		pass

	@property
	def FieldDataType(self) -> FieldDataType:
		"""No Description

		Returns:
			IFieldInfo: 
		"""
		pass

	@property
	def StorageUnit(self) -> Unit:
		"""No Description

		Returns:
			IFieldInfo: 
		"""
		pass

	@property
	def Unit(self) -> IUnit:
		"""No Description

		Returns:
			IFieldInfo: 
		"""
		pass

class INetworkFieldInfo(IFieldInfo):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def AlternativeTypeName(self) -> str:
		"""No Description

		Returns:
			INetworkFieldInfo: 
		"""
		pass

	@property
	def DomainElementTypeName(self) -> str:
		"""No Description

		Returns:
			INetworkFieldInfo: 
		"""
		pass

class IUserNetworkfieldInfo(INetworkFieldInfo):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Delete(self) -> None:
		"""No Description

		Returns:
			None: 
		"""
		pass

class IResultFieldInfo(IFieldInfo):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ResultRecordTypeName(self) -> str:
		"""No Description

		Returns:
			IResultFieldInfo: 
		"""
		pass

	@property
	def NumericalEngineTypeName(self) -> str:
		"""No Description

		Returns:
			IResultFieldInfo: 
		"""
		pass

class IComponentElementFieldInfo(IFieldInfo):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def SupportElementTypeName(self) -> str:
		"""No Description

		Returns:
			IComponentElementFieldInfo: 
		"""
		pass

class IFieldManager:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def FieldByName(self, name: str) -> IFieldInfo:
		"""No Description

		Args:
			name(str): name

		Returns:
			IFieldInfo: 
		"""
		pass

	def FieldByLabel(self, label: str) -> IFieldInfo:
		"""No Description

		Args:
			label(str): label

		Returns:
			IFieldInfo: 
		"""
		pass

	@property
	def FieldInfo(self) -> IReadOnlyCollection:
		"""No Description

		Returns:
			IFieldManager: 
		"""
		pass

class IUserFieldOptions(Generic[TFieldType, TNetworkElementTypeEnum]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def FieldType(self) -> UserFieldDataType:
		"""No Description

		Returns:
			IUserFieldOptions: 
		"""
		pass

	@property
	def Name(self) -> str:
		"""No Description

		Returns:
			IUserFieldOptions: 
		"""
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns:
			IUserFieldOptions: 
		"""
		pass

	@property
	def ElementType(self) -> TNetworkElementTypeEnum:
		"""No Description

		Returns:
			IUserFieldOptions: 
		"""
		pass

	@property
	def SharedWith(self) -> List[TNetworkElementTypeEnum]:
		"""No Description

		Returns:
			IUserFieldOptions: 
		"""
		pass

	@property
	def DefaultValue(self) -> TFieldType:
		"""No Description

		Returns:
			IUserFieldOptions: 
		"""
		pass

	@property
	def Category(self) -> str:
		"""No Description

		Returns:
			IUserFieldOptions: 
		"""
		pass

	@property
	def JustLikeField(self) -> IFieldInfo:
		"""No Description

		Returns:
			IUserFieldOptions: 
		"""
		pass

	@Name.setter
	def Name(self, name: str) -> None:
		pass

	@Label.setter
	def Label(self, label: str) -> None:
		pass

	@ElementType.setter
	def ElementType(self, elementtype: TNetworkElementTypeEnum) -> None:
		pass

	@DefaultValue.setter
	def DefaultValue(self, defaultvalue: TFieldType) -> None:
		pass

	@Category.setter
	def Category(self, category: str) -> None:
		pass

	@JustLikeField.setter
	def JustLikeField(self, justlikefield: IFieldInfo) -> None:
		pass

class IUserFieldManager(Generic[TNetworkElementType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def NewFieldOptions(self) -> IUserFieldOptions:
		"""No Description

		Returns:
			IUserFieldOptions: 
		"""
		pass

	def CreateField(self, options: IUserFieldOptions) -> IUserNetworkfieldInfo:
		"""No Description

		Args:
			options(IUserFieldOptions): options

		Returns:
			IUserNetworkfieldInfo: 
		"""
		pass
