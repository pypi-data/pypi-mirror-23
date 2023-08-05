#!/usr/bin/python
# -*- coding: utf-8 -*-


''' Copyright 2013 Smartling, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this work except in compliance with the License.
 * You may obtain a copy of the License in the LICENSE file, or at:
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
'''

class SmartlingDirective:
    """ Smartling directive which is used for file upload """
    sl_prefix = "smartling."

    def __init__(self, name, value):
        if not name:
            raise Exception("name cannot be empty!")
        self.name = self.__remove_sl_prefix(name.lower())

        if value is None:
            self.value = ""
        else:
            self.value = value

    def __remove_sl_prefix(self, name):
        if name.startswith(self.sl_prefix):
            return name[len(self.sl_prefix):]
        return name
