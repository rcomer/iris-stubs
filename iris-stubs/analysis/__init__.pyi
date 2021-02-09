from typing import Any, Optional

class _CoordGroup:
    coords: Any = ...
    cubes: Any = ...
    def __init__(self, coords: Any, cubes: Any) -> None: ...
    def __iter__(self) -> Any: ...
    def __getitem__(self, key: Any): ...
    def name(self): ...
    def __hash__(self) -> Any: ...
    def __eq__(self, other: Any) -> Any: ...
    def matches(self, predicate: Any, default_val: bool = ...) -> None: ...
    def matches_all(self, predicate: Any): ...
    def matches_any(self, predicate: Any): ...

class _Aggregator:
    cell_method: Any = ...
    call_func: Any = ...
    units_func: Any = ...
    lazy_func: Any = ...
    def __init__(self, cell_method: Any, call_func: Any, units_func: Optional[Any] = ..., lazy_func: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def lazy_aggregate(self, data: Any, axis: Any, **kwargs: Any): ...
    def aggregate(self, data: Any, axis: Any, **kwargs: Any): ...
    def update_metadata(self, cube: Any, coords: Any, **kwargs: Any) -> None: ...
    def post_process(self, collapsed_cube: Any, data_result: Any, coords: Any, **kwargs: Any): ...
    def aggregate_shape(self, **kwargs: Any): ...
    def name(self): ...

class PercentileAggregator(_Aggregator):
    def __init__(self, units_func: Optional[Any] = ..., lazy_func: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def aggregate(self, data: Any, axis: Any, **kwargs: Any): ...
    def post_process(self, collapsed_cube: Any, data_result: Any, coords: Any, **kwargs: Any): ...
    def aggregate_shape(self, **kwargs: Any): ...
    def name(self): ...

class WeightedPercentileAggregator(PercentileAggregator):
    def __init__(self, units_func: Optional[Any] = ..., lazy_func: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def post_process(self, collapsed_cube: Any, data_result: Any, coords: Any, **kwargs: Any): ...

class Aggregator(_Aggregator):
    def update_metadata(self, cube: Any, coords: Any, **kwargs: Any) -> None: ...

class WeightedAggregator(Aggregator):
    def __init__(self, cell_method: Any, call_func: Any, units_func: Optional[Any] = ..., lazy_func: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def uses_weighting(self, **kwargs: Any): ...
    def post_process(self, collapsed_cube: Any, data_result: Any, coords: Any, **kwargs: Any): ...

COUNT: Any
GMEAN: Any
HMEAN: Any
MEAN: Any
MEDIAN: Any
MIN: Any
MAX: Any
PEAK: Any
PERCENTILE: Any
PROPORTION: Any
RMS: Any
STD_DEV: Any
SUM: Any
VARIANCE: Any
WPERCENTILE: Any

class _Groupby:
    coords: Any = ...
    def __init__(self, groupby_coords: Any, shared_coords: Optional[Any] = ...) -> None: ...
    def group(self) -> None: ...
    def __len__(self): ...

def clear_phenomenon_identity(cube: Any) -> None: ...

class Linear:
    LINEAR_EXTRAPOLATION_MODES: Any = ...
    extrapolation_mode: Any = ...
    def __init__(self, extrapolation_mode: str = ...) -> None: ...
    def interpolator(self, cube: Any, coords: Any): ...
    def regridder(self, src_grid: Any, target_grid: Any): ...

class AreaWeighted:
    mdtol: Any = ...
    def __init__(self, mdtol: int = ...) -> None: ...
    def regridder(self, src_grid_cube: Any, target_grid_cube: Any): ...

class Nearest:
    extrapolation_mode: Any = ...
    def __init__(self, extrapolation_mode: str = ...) -> None: ...
    def interpolator(self, cube: Any, coords: Any): ...
    def regridder(self, src_grid: Any, target_grid: Any): ...

class UnstructuredNearest:
    def __init__(self) -> None: ...
    def regridder(self, src_cube: Any, target_grid: Any): ...

class PointInCell:
    weights: Any = ...
    def __init__(self, weights: Optional[Any] = ...) -> None: ...
    def regridder(self, src_grid: Any, target_grid: Any): ...
