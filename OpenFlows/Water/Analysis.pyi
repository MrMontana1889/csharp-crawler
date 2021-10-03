from typing import Generic
from OpenFlows.Analysis import IAnalysisCalculator
from OpenFlows.Water.Domain.ModelingElements import IWaterScenario, IWaterScenarios
from OpenFlows.Water.Domain.ModelingElements.CalculationOptions import IWaterScenarioOptions, IWaterScenarioOptionsUnits

class IScenarioEnergyCostCalculator(IAnalysisCalculator[IWaterScenario, IWaterScenarios, IWaterScenarioOptions, IWaterScenarioOptionsUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IAnalysisTools:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ScenarioEnergyCostCalculator(self) -> IScenarioEnergyCostCalculator:
		"""
		Returns:
			IScenarioEnergyCostCalculator: No Description
		"""
		pass
