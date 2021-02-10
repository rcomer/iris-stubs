from ctypes import Union
from typing import Any, Mapping, Optional

from cf_units import Unit



# class LimitedAttributeDict(dict): ...
#     # def __init__(self, *args: Any, **kwargs: Any) -> None: ...
#     # def __eq__(self, other: Any) -> Any: ...
#     # def __ne__(self, other: Any) -> Any: ...
#     # def __setitem__(self, key: Any, value: Any) -> None: ...
#     #def update(self, other: Mapping[str, Any], **kwargs: Any) -> None: ...  # mypy doesn't like this

class CFVariableMixin:
    def name(self, default: Optional[str] = ..., token: bool = ...) -> str: ...
    def rename(self, name: str) -> None: ...
    @property
    def standard_name(self) -> str: ...
    @standard_name.setter
    def standard_name(self, name: str) -> None: ...
    @property
    def long_name(self) -> str: ...
    @long_name.setter
    def long_name(self, name: str) -> None: ...
    @property
    def var_name(self) -> str: ...
    @var_name.setter
    def var_name(self, name: str) -> None: ...
    @property
    def units(self) -> Unit: ...
    @units.setter
    def units(self, unit: Union[str, Unit]) -> None: ...  # type: ignore
    @property
    def attributes(self): ...
    @attributes.setter
    def attributes(self, attributes: Mapping[str, Any]) -> None: ...
    @property
    def metadata(self): ...
    @metadata.setter
    def metadata(self, metadata: Any): ...
