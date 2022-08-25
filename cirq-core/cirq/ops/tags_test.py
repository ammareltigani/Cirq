# Copyright 2020 The Cirq Developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import cirq
import collections


def test_virtual_tag():
    tag1 = cirq.ops.VirtualTag()
    tag2 = cirq.ops.VirtualTag()

    assert tag1 == tag2
    assert str(tag1) == str(tag2) == '<virtual>'

    cirq.testing.assert_equivalent_repr(tag1)
    cirq.testing.assert_equivalent_repr(tag2)


def test_swap_tag():
    tag1 = cirq.ops._InsertedSwapTag()
    tag2 = cirq.ops._InsertedSwapTag()

    assert tag1 == tag2
    assert str(tag1) == str(tag2) == '<r>'
    assert isinstance(tag1, collections.Hashable)

    cirq.testing.assert_equivalent_repr(tag1)
    cirq.testing.assert_equivalent_repr(tag2)
