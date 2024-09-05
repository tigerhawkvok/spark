#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import (
    ClassVar as _ClassVar,
    Mapping as _Mapping,
    Optional as _Optional,
    Union as _Union,
)

DESCRIPTOR: _descriptor.FileDescriptor

class HandleState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CREATED: _ClassVar[HandleState]
    INITIALIZED: _ClassVar[HandleState]
    DATA_PROCESSED: _ClassVar[HandleState]
    CLOSED: _ClassVar[HandleState]

CREATED: HandleState
INITIALIZED: HandleState
DATA_PROCESSED: HandleState
CLOSED: HandleState

class StateRequest(_message.Message):
    __slots__ = (
        "version",
        "statefulProcessorCall",
        "stateVariableRequest",
        "implicitGroupingKeyRequest",
    )
    VERSION_FIELD_NUMBER: _ClassVar[int]
    STATEFULPROCESSORCALL_FIELD_NUMBER: _ClassVar[int]
    STATEVARIABLEREQUEST_FIELD_NUMBER: _ClassVar[int]
    IMPLICITGROUPINGKEYREQUEST_FIELD_NUMBER: _ClassVar[int]
    version: int
    statefulProcessorCall: StatefulProcessorCall
    stateVariableRequest: StateVariableRequest
    implicitGroupingKeyRequest: ImplicitGroupingKeyRequest
    def __init__(
        self,
        version: _Optional[int] = ...,
        statefulProcessorCall: _Optional[_Union[StatefulProcessorCall, _Mapping]] = ...,
        stateVariableRequest: _Optional[_Union[StateVariableRequest, _Mapping]] = ...,
        implicitGroupingKeyRequest: _Optional[_Union[ImplicitGroupingKeyRequest, _Mapping]] = ...,
    ) -> None: ...

class StateResponse(_message.Message):
    __slots__ = ("statusCode", "errorMessage", "value")
    STATUSCODE_FIELD_NUMBER: _ClassVar[int]
    ERRORMESSAGE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    statusCode: int
    errorMessage: str
    value: bytes
    def __init__(
        self, statusCode: _Optional[int] = ..., errorMessage: _Optional[str] = ...
    ) -> None: ...

class StatefulProcessorCall(_message.Message):
    __slots__ = ("setHandleState", "getValueState", "getListState", "getMapState")
    SETHANDLESTATE_FIELD_NUMBER: _ClassVar[int]
    GETVALUESTATE_FIELD_NUMBER: _ClassVar[int]
    GETLISTSTATE_FIELD_NUMBER: _ClassVar[int]
    GETMAPSTATE_FIELD_NUMBER: _ClassVar[int]
    setHandleState: SetHandleState
    getValueState: StateCallCommand
    getListState: StateCallCommand
    getMapState: StateCallCommand
    def __init__(
        self,
        setHandleState: _Optional[_Union[SetHandleState, _Mapping]] = ...,
        getValueState: _Optional[_Union[StateCallCommand, _Mapping]] = ...,
        getListState: _Optional[_Union[StateCallCommand, _Mapping]] = ...,
        getMapState: _Optional[_Union[StateCallCommand, _Mapping]] = ...,
    ) -> None: ...

class StateVariableRequest(_message.Message):
    __slots__ = ("valueStateCall",)
    VALUESTATECALL_FIELD_NUMBER: _ClassVar[int]
    valueStateCall: ValueStateCall
    def __init__(
        self, valueStateCall: _Optional[_Union[ValueStateCall, _Mapping]] = ...
    ) -> None: ...

class ImplicitGroupingKeyRequest(_message.Message):
    __slots__ = ("setImplicitKey", "removeImplicitKey")
    SETIMPLICITKEY_FIELD_NUMBER: _ClassVar[int]
    REMOVEIMPLICITKEY_FIELD_NUMBER: _ClassVar[int]
    setImplicitKey: SetImplicitKey
    removeImplicitKey: RemoveImplicitKey
    def __init__(
        self,
        setImplicitKey: _Optional[_Union[SetImplicitKey, _Mapping]] = ...,
        removeImplicitKey: _Optional[_Union[RemoveImplicitKey, _Mapping]] = ...,
    ) -> None: ...

class StateCallCommand(_message.Message):
    __slots__ = ("stateName", "schema")
    STATENAME_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    stateName: str
    schema: str
    def __init__(self, stateName: _Optional[str] = ..., schema: _Optional[str] = ...) -> None: ...

class ValueStateCall(_message.Message):
    __slots__ = ("stateName", "exists", "get", "valueStateUpdate", "clear")
    STATENAME_FIELD_NUMBER: _ClassVar[int]
    EXISTS_FIELD_NUMBER: _ClassVar[int]
    GET_FIELD_NUMBER: _ClassVar[int]
    VALUESTATEUPDATE_FIELD_NUMBER: _ClassVar[int]
    CLEAR_FIELD_NUMBER: _ClassVar[int]
    stateName: str
    exists: Exists
    get: Get
    valueStateUpdate: ValueStateUpdate
    clear: Clear
    def __init__(
        self,
        stateName: _Optional[str] = ...,
        exists: _Optional[_Union[Exists, _Mapping]] = ...,
        get: _Optional[_Union[Get, _Mapping]] = ...,
        valueStateUpdate: _Optional[_Union[ValueStateUpdate, _Mapping]] = ...,
        clear: _Optional[_Union[Clear, _Mapping]] = ...,
    ) -> None: ...

class SetImplicitKey(_message.Message):
    __slots__ = ("key",)
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: bytes
    def __init__(self, key: _Optional[bytes] = ...) -> None: ...

class RemoveImplicitKey(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Exists(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Get(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ValueStateUpdate(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bytes
    def __init__(self, value: _Optional[bytes] = ...) -> None: ...

class Clear(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetHandleState(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: HandleState
    def __init__(self, state: _Optional[_Union[HandleState, str]] = ...) -> None: ...