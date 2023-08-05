CubeFlow
========

:abstract: CubeFlow is a Python framework to easily build and analyse grid based simulation such as heat transportation
    or fluid dynamics. CubeFlow aims to provide an easy implementation without the need of writing code other than
    the one needed for the actual simulation. CubeFlow is not a super fast simulator but focuses primarily on
    educational purposes.

Code Sample
-----------

The following code generates a simple heat flow simulator of a homogeneous cube.

.. code-block:: python

    from typing import Dict, Sequence
    from cubeflow.cell import MetaCell, Scalar
    from cubeflow.cube import CubeGrid
    from cubeflow.simulator import BaseSimulator, add_derivations, border_handler
    from cubeflow.report.csv import CSVReport
    from cubeflow.predicates.counter import Counter


    class HeatCell(metaclass=MetaCell):
        temperature = Scalar()
        diffusivity = Scalar()
        flow = 0.0

        @add_derivations
        class HeatSimulator(BaseSimulator[HeatCell]):
            Type = HeatCell

        @border_handler(1)
        def no_flow_border(self, cells: Dict[Sequence[int], HeatCell]) -> HeatCell:
            cell = cells[(0, 0)]
            adjacent = self._get_adjacent_inner(cells)
            if adjacent:
                # cell is not a corner
                cell.temperature = self._get_only_cell(adjacent)[1].temperature
                return cell
            else:
                return self._handle_corner(cells)

        def _prepare(self, cells: Dict[Sequence[int], HeatCell]) -> HeatCell:
            cell = cells[(0, 0)]
            cell.flow = cell.diffusivity * self.laplace_temperature(cells)
            return cell

        def _simulate(self, cells: Dict[Sequence[int], HeatCell]) -> HeatCell:
            cell = cells[(0, 0)]
            cell.temperature += self.dt * cell.flow
            return cell


    if __name__ == '__main__':
        from sys import argv
        simulator = HeatSimulator(CubeGrid.from_file(argv[1], HeatCell), [CSVReport('heat')])
        simulator.simulate_while(Counter(1000))

Changes
-------

- 0.17 Added grid specification support via toml like textfile.

Roadmap
-------

- 0.18 Improved examples and documentation. Adding flow based simulation in contrast to the existing "computational"
  approach, meaning defining the simulation in terms of data flows between cells.

- 0.19 Improved output format, browser application to create grids in a graphical and interactive way.

- 0.20 Translation support for CubeFlow projects to either Stackless Python or Rust.

