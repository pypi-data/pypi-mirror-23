""" run with

python setup.py install; nosetests -v --nocapture tests/cm_basic/test_flatdict.py:Test_flatdict.test_001

nosetests -v --nocapture tests/cm_basic/test_flatdict.py

or

nosetests -v tests/cm_basic/test_flatdict.py

"""

from pprint import pprint

from cloudmesh_client.common.FlatDict import FlatDict, flatten
from cloudmesh_client.common.util import HEADING


# noinspection PyPep8Naming
class Test_pass:
    def setup(self):
        self.d = {
            'cloud': 'india',
            'update': '2015-06-18 22:11:48 UTC',
            'user': 'gregor',
            'extra': {'created': '2015-05-21T20:37:10Z',
                      'metadata': {'base_image_ref': '398746398798372493287',
                                   'description': None,
                                   'image_location': 'snapshot',
                                   'image_state': 'available',
                                   'image_type': 'snapshot',
                                   'instance_type_ephemeral_gb': '0',
                                   'instance_type_flavorid': '3',
                                   'instance_type_id': '1',
                                   'instance_type_memory_mb': '4096',
                                   'instance_type_name': 'm1.medium',
                                   'instance_type_root_gb': '40',
                                   'instance_type_rxtx_factor': '1.0',
                                   'instance_type_swap': '0',
                                   'instance_type_vcpus': '2',
                                   'instance_uuid': '386473678463876387',
                                   'kernel_id': None,
                                   'network_allocated': 'True',
                                   'owner_id': '36487264932876984723649',
                                   'ramdisk_id': None,
                                   'user_id': '762387463827463278649837'},
                      'minDisk': 40,
                      'minRam': 0,
                      'progress': 100,
                      'serverId': 'yiuksajhlkjahl',
                      'status': 'ACTIVE',
                      'updated': '2015-05-27T02:11:48Z'},
            'id': '39276498376478936247832687',
            'name': 'VM with Cloudmesh Configured Completely'
        }

        self.vm = {
            'extra': {'access_ip': '',
                      'availability_zone': 'nova',
                      'config_drive': '',
                      'created': '2015-06-19T00:06:58Z',
                      'disk_config': 'MANUAL',
                      'flavorId': '1',
                      'hostId': '',
                      'imageId': 'abcd',
                      'key_name': None,
                      'metadata': {},
                      'password': '********',
                      'tenantId': '1234',
                      'updated': '2015-06-19T00:06:58Z',
                      'uri': 'http://i5r.idp.iu.futuregrid.org/v2/1234/servers/abcd'},
            'id': '67f6bsf67a6b',
            'image': None,
            'name': 'gregor-cm_test',
            'private_ips': [],
            'public_ips': [],
            'size': None,
            'state': 3
        }
        pass

    # noinspection PyPep8Naming
    def tearDown(self):
        pass

    def test_001(self):
        HEADING("flatten")
        f = flatten(self.d)
        pprint(f)
        assert f['extra__minDisk'] == 40

    def test_002(self):
        HEADING("FlatDict")

        f = FlatDict(self.d)
        pprint(f.dict)
        pprint(f.__dict__)
        print(f['user'])
        print(f['extra__created'])
        print(f.user)
        print(f.extra__created)

        f.user = 'GREGOR'
        assert f.user == 'GREGOR'
        assert f['extra__minDisk'] == 40
