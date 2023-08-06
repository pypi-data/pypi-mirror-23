#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslotest import base as test_base

from oslo_utils import specs_matcher


class SpecsMatcherTestCase(test_base.BaseTestCase):
    def _do_specs_matcher_test(self, value, req, matches):
        assertion = self.assertTrue if matches else self.assertFalse
        assertion(specs_matcher.match(value, req))

    def test_specs_matches_simple(self):
        self._do_specs_matcher_test(
            value='1',
            req='1',
            matches=True)

    def test_specs_fails_simple(self):
        self._do_specs_matcher_test(
            value='',
            req='1',
            matches=False)

    def test_specs_fails_simple2(self):
        self._do_specs_matcher_test(
            value='3',
            req='1',
            matches=False)

    def test_specs_fails_simple3(self):
        self._do_specs_matcher_test(
            value='222',
            req='2',
            matches=False)

    def test_specs_fails_with_bogus_ops(self):
        self._do_specs_matcher_test(
            value='4',
            req='> 2',
            matches=False)

    def test_specs_matches_with_op_eq(self):
        self._do_specs_matcher_test(
            value='123',
            req='= 123',
            matches=True)

    def test_specs_matches_with_op_eq2(self):
        self._do_specs_matcher_test(
            value='124',
            req='= 123',
            matches=True)

    def test_specs_fails_with_op_eq(self):
        self._do_specs_matcher_test(
            value='34',
            req='= 234',
            matches=False)

    def test_specs_fails_with_op_eq3(self):
        self._do_specs_matcher_test(
            value='34',
            req='=',
            matches=False)

    def test_specs_matches_with_op_seq(self):
        self._do_specs_matcher_test(
            value='123',
            req='s== 123',
            matches=True)

    def test_specs_fails_with_op_seq(self):
        self._do_specs_matcher_test(
            value='1234',
            req='s== 123',
            matches=False)

    def test_specs_matches_with_op_sneq(self):
        self._do_specs_matcher_test(
            value='1234',
            req='s!= 123',
            matches=True)

    def test_specs_fails_with_op_sneq(self):
        self._do_specs_matcher_test(
            value='123',
            req='s!= 123',
            matches=False)

    def test_specs_matches_with_op_sge(self):
        self._do_specs_matcher_test(
            value='234',
            req='s>= 1000',
            matches=True)

    def test_specs_matches_with_op_sge2(self):
        self._do_specs_matcher_test(
            value='234',
            req='s>= 234',
            matches=True)

    def test_specs_fails_with_op_sge(self):
        self._do_specs_matcher_test(
            value='1000',
            req='s>= 234',
            matches=False)

    def test_specs_matches_with_op_sle(self):
        self._do_specs_matcher_test(
            value='1000',
            req='s<= 1234',
            matches=True)

    def test_specs_matches_with_op_sle2(self):
        self._do_specs_matcher_test(
            value='1234',
            req='s<= 1234',
            matches=True)

    def test_specs_fails_with_op_sle(self):
        self._do_specs_matcher_test(
            value='1234',
            req='s<= 1000',
            matches=False)

    def test_specs_matches_with_op_sl(self):
        self._do_specs_matcher_test(
            value='12',
            req='s< 2',
            matches=True)

    def test_specs_fails_with_op_sl(self):
        self._do_specs_matcher_test(
            value='2',
            req='s< 12',
            matches=False)

    def test_specs_fails_with_op_sl2(self):
        self._do_specs_matcher_test(
            value='12',
            req='s< 12',
            matches=False)

    def test_specs_matches_with_op_sg(self):
        self._do_specs_matcher_test(
            value='2',
            req='s> 12',
            matches=True)

    def test_specs_fails_with_op_sg(self):
        self._do_specs_matcher_test(
            value='12',
            req='s> 2',
            matches=False)

    def test_specs_fails_with_op_sg2(self):
        self._do_specs_matcher_test(
            value='12',
            req='s> 12',
            matches=False)

    def test_specs_matches_with_op_in(self):
        self._do_specs_matcher_test(
            value='12311321',
            req='<in> 11',
            matches=True)

    def test_specs_matches_with_op_in2(self):
        self._do_specs_matcher_test(
            value='12311321',
            req='<in> 12311321',
            matches=True)

    def test_specs_matches_with_op_in3(self):
        self._do_specs_matcher_test(
            value='12311321',
            req='<in> 12311321 <in>',
            matches=True)

    def test_specs_fails_with_op_in(self):
        self._do_specs_matcher_test(
            value='12310321',
            req='<in> 11',
            matches=False)

    def test_specs_fails_with_op_in2(self):
        self._do_specs_matcher_test(
            value='12310321',
            req='<in> 11 <in>',
            matches=False)

    def test_specs_matches_with_op_or(self):
        self._do_specs_matcher_test(
            value='12',
            req='<or> 11 <or> 12',
            matches=True)

    def test_specs_matches_with_op_or2(self):
        self._do_specs_matcher_test(
            value='12',
            req='<or> 11 <or> 12 <or>',
            matches=True)

    def test_specs_matches_with_op_or3(self):
        self._do_specs_matcher_test(
            value='12',
            req='<or> 12',
            matches=True)

    def test_specs_fails_with_op_or(self):
        self._do_specs_matcher_test(
            value='13',
            req='<or> 11 <or> 12',
            matches=False)

    def test_specs_fails_with_op_or2(self):
        self._do_specs_matcher_test(
            value='13',
            req='<or> 11 <or> 12 <or>',
            matches=False)

    def test_specs_fails_with_op_or3(self):
        self._do_specs_matcher_test(
            value='13',
            req='<or> 11',
            matches=False)

    def test_specs_matches_with_op_le(self):
        self._do_specs_matcher_test(
            value='2',
            req='<= 10',
            matches=True)

    def test_specs_matches_with_op_le2(self):
        self._do_specs_matcher_test(
            value='10',
            req='<= 10',
            matches=True)

    def test_specs_fails_with_op_le(self):
        self._do_specs_matcher_test(
            value='3',
            req='<= 2',
            matches=False)

    def test_specs_matches_with_op_ge(self):
        self._do_specs_matcher_test(
            value='3',
            req='>= 1',
            matches=True)

    def test_specs_matches_with_op_ge2(self):
        self._do_specs_matcher_test(
            value='3.0',
            req='>= 3',
            matches=True)

    def test_specs_fails_with_op_ge(self):
        self._do_specs_matcher_test(
            value='2',
            req='>= 3',
            matches=False)

    def test_specs_matches_with_op_ne(self):
        self._do_specs_matcher_test(
            value='3.2',
            req='!= 3.1',
            matches=True)

    def test_specs_fails_with_op_ne(self):
        self._do_specs_matcher_test(
            value='3.2',
            req='!= 3.2',
            matches=False)

    def test_specs_matches_with_op_eqeq(self):
        self._do_specs_matcher_test(
            value='3',
            req='== 3',
            matches=True)

    def test_specs_matches_with_op_eqeq2(self):
        self._do_specs_matcher_test(
            value='3.0',
            req='== 3',
            matches=True)

    def test_specs_fails_with_op_eqeq(self):
        self._do_specs_matcher_test(
            value='3.0',
            req='== 3.1',
            matches=False)
