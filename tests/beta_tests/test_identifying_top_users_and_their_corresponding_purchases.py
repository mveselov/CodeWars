import unittest

from katas.beta.identifying_top_users_and_their_corresponding_purchases \
    import id_best_users


class IdBestUsersTestCase(unittest.TestCase):
    def setUp(self):
        self.a1 = ['A042', 'B004', 'A025', 'A042', 'C025']
        self.a2 = ['B009', 'B040', 'B004', 'A042', 'A025', 'A042']

    def test_equal_1(self):
        self.assertEqual(
            id_best_users(self.a1, self.a2, ['A042', 'A025', 'B004']),
            [[5, ['A042']], [3, ['A025', 'B004']]])

    def test_equal_2(self):
        self.assertEqual(id_best_users(
            ['A043', 'B004', 'A025', 'A042', 'C025'],
            ['B009', 'B040', 'B003', 'A042', 'A027', 'A044'],
            ['A041', 'A026', 'B005']), [])

    def test_equal_3(self):
        self.assertEqual(id_best_users(
            self.a1, self.a2,
            ['A042', 'B004', 'A025', 'A042', 'C025', 'B009', 'B040', 'B004',
             'A042', 'A025', 'A042'],
            ['A042', 'A025', 'B004']
        ), [[9, ['A042']], [5, ['A025', 'B004']]])

    def test_equal_4(self):
        self.assertEqual(id_best_users(
            ['A002', 'C004', 'A009', 'C002', 'A006', 'A001', 'A007', 'B002',
             'B005', 'B001', 'A008', 'B002', 'C004', 'C006', 'A004', 'B004',
             'B007', 'B004', 'A007', 'B003', 'C005', 'A001', 'A008', 'A006',
             'C009', 'A002', 'C008', 'B009', 'B007', 'B008', 'B005', 'A005',
             'B002', 'A008', 'B002', 'A004', 'A009', 'C002', 'B008', 'A009'],
            ['A006', 'B003', 'B002', 'A007', 'A007', 'A007', 'B003', 'B007',
             'C002', 'B007', 'A002', 'A009', 'A001', 'A003', 'B005', 'B009',
             'B004', 'A008', 'C004', 'A004', 'B009', 'C004'],
            ['A003', 'A002', 'C008', 'C003', 'C001', 'B007', 'A002', 'A007',
             'B008', 'C006', 'A002', 'C002', 'B005', 'B005', 'A009', 'A005',
             'A008', 'B005', 'A002', 'C008', 'B008', 'C009', 'A005', 'C004',
             'C001', 'B001', 'C005', 'C005', 'A006', 'B002', 'A008', 'C006'],
            ['B004', 'A009', 'B004', 'A006', 'B007', 'B003', 'C008', 'B009',
             'B005', 'C001', 'A002', 'A005', 'B005', 'B001', 'B008', 'C004',
             'A003', 'C009', 'B009', 'B008', 'B004', 'B004', 'B008', 'A002',
             'A009', 'B001', 'C001', 'C007', 'B007', 'B008', 'A007', 'C002',
             'B001', 'B009', 'C001', 'C003', 'A004', 'C006', 'A002'],
            ['A004', 'A004', 'B004', 'C004', 'B004', 'C007', 'B002', 'A005',
             'C004', 'A003', 'B006', 'A006', 'B004', 'A008', 'C009', 'B006',
             'B002', 'A003', 'B009', 'C004', 'A005', 'C006', 'A006', 'B002',
             'C005', 'C007', 'A005', 'C005', 'A002', 'C006', 'C002', 'C009',
             'C004', 'C003', 'A002', 'A006'],
            ['B004', 'B002', 'B002', 'C004', 'C003', 'B005', 'C009', 'A008',
             'B005', 'C006', 'A009', 'B007', 'B006', 'A006', 'B005', 'B009',
             'C003', 'C005', 'C006', 'C003', 'B003', 'B003', 'B004', 'C004',
             'B001', 'A001', 'B006', 'A002', 'A004', 'A002', 'A001', 'B004',
             'A005', 'A009', 'B006']),
            [[14, ['A002']], [12, ['C004']], [9, ['A006']]])
