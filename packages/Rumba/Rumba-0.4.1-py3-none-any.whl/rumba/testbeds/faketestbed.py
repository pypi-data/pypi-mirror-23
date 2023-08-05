#
# Fake testbed for Rumba testing
#
#    Vincenzo Maffione  <v.maffione@nextworks.it>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA  02110-1301  USA

import rumba.model as mod
import rumba.log as log


logger = log.get_logger(__name__)


# Fake testbed, useful for testing
class Testbed(mod.Testbed):

    def __init__(self, exp_name, username, proj_name="ARCFIRE", password=""):
        mod.Testbed.__init__(self, exp_name, username, password, proj_name)

    def swap_in(self, experiment):
        logger.info("[Fake testbed] experiment swapped in")
